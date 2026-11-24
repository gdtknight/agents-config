**English** | [한국어](./ARCHITECTURE.ko.md)

# Agents Config Architecture Guide

System architecture, runtime workflows, module design, and Architecture Decision Records (ADRs) for managing Claude Code, Gemini CLI / Antigravity, and Codex CLI from a single source of truth.

---

## 1. System Context & Container Architecture (C4 Model)

### Level 1–2: System Context & Container Architecture

`agents-config` centralizes prompts, rules, 13 specialized subagents, cross-vendor skills, lifecycle hooks, and MCP declarations under `shared/`, projecting them into each vendor's home directory via a Bash 3.2+ orchestrator ([install.sh](../install.sh)).

```mermaid
flowchart TD
    Dev["Developer (macOS / Linux)"]
    Repo["agents-config Repository (Single Source of Truth)"]
    Inst["install.sh (Bash 3.2+ Orchestrator)"]
    McpSync["sync_mcp.py (Cross-Vendor MCP Renderer)"]
    Backup["Backup Store (~/.agents-config_backups)"]

    Dev -->|"curl one-liner / local CLI"| Inst
    Repo -->|"shared/ & vendor/ assets"| Inst
    Inst -->|"Normalize & merge MCP"| McpSync
    Inst -. "Snapshot backup on conflict" .-> Backup

    Inst --> Claude["Claude Code (~/.claude & ~/.claude.json)"]
    Inst --> Gemini["Gemini CLI / Antigravity (~/.gemini)"]
    Inst --> Codex["Codex CLI (~/.codex)"]

    Claude -->|"PreToolUse / PostToolUse / Stop"| Hook["Unified Hook (shared/hooks/hook.py)"]
    Gemini -->|"BeforeTool / AfterTool / AfterAgent"| Hook
    Codex -->|"hooks/"| Hook

    Hook -->|"docker run --rm (or local fallback)"| FmtDocker["agents-config-formatter:latest"]
    Repo -->|"llm-wiki skill + Excalidraw"| Wiki["Obsidian Knowledge Base (raw/ · wiki/)"]
```

### Level 3: Internal `shared/` Component Layout

```mermaid
flowchart LR
    subgraph Shared["shared/ (Single Source of Truth)"]
        InstMD["INSTRUCTIONS.md"]
        Rules["rules/ (accuracy, engineering, c-cpp)"]
        Agents["agents/*.md (13 Subagents)"]
        Skills["skills/ (graphify, llm-wiki)"]
        Hooks["hooks/hook.py"]
        McpJson["mcp.json"]
    end

    subgraph VendorAdapters["Vendor Adapters"]
        ClaudeCfg["claude/settings.json"]
        GeminiCfg["gemini/ (settings, config, hooks, mcp_config)"]
        CodexCfg["codex/ (config.toml, agents/*.toml)"]
    end

    McpJson -->|"sync_mcp.py"| GeminiCfg
    McpJson -->|"sync_mcp.py"| CodexCfg
    Agents -->|"1:1 role mapping"| CodexCfg
    Agents -->|"SKILL.md symlinks"| GeminiCfg
```

---

## 2. Core Runtime Workflows

### 2.1 Remote Bootstrap & Idempotent Deployment (`install.sh`)

```mermaid
sequenceDiagram
    actor User as Developer
    participant Boot as install.sh (Remote / Local)
    participant Sync as sync_mcp.py
    participant FS as Target Filesystem
    participant BK as ~/.agents-config_backups

    User->>Boot: curl | bash or ./install.sh [--dry-run] [--skip-cli]
    alt Piped or -c remote execution
        Boot->>FS: Clone or fast-forward ~/.agents-config
        Boot->>Boot: TTY-safe exec handoff
    end
    Boot->>Sync: Validate shared/mcp.json and render vendor configs
    Sync->>FS: Update gemini/mcp_config.json, codex/config.toml, ~/.claude.json
    loop Claude / Gemini / Codex targets
        Boot->>FS: Inspect target symlink state
        alt Already linked to repo source
            Boot-->>User: Skip (Idempotent No-Op)
        else Existing regular file or directory
            Boot->>BK: Move existing target to backup_YYYYMMDD_HHMMSS/
            Boot->>FS: ln -sfn <repo_src> <target>
        else Target missing
            Boot->>FS: ln -sfn <repo_src> <target>
        end
    end
```

### 2.2 Unified Lifecycle Hook Pipeline ([hook.py](../shared/hooks/hook.py))

```mermaid
sequenceDiagram
    actor Agent as AI Agent (Claude / Gemini / Codex)
    participant Hook as shared/hooks/hook.py
    participant Guard as Security Guard (PreToolUse)
    participant Fmt as agents-config-formatter:latest

    Agent->>Hook: stdin JSON (toolCall or tool_name/tool_input)
    Hook->>Hook: Normalize via extract_tool_info(payload)

    alt Event == PreToolUse
        Hook->>Guard: Check DANGEROUS_COMMAND_PATTERNS, is_dangerous_rm(), is_dangerous_chmod()
        Hook->>Guard: Check SENSITIVE_FILE_PATTERN & SECRET_PATTERNS
        alt Policy violation
            Guard-->>Agent: Exit 1 + JSON decision "deny"
        else Safe operation
            Guard-->>Agent: Exit 0 + JSON decision "allow"
        end
    else Event == PostToolUse (write/edit tools)
        alt *.excalidraw.md or *.excalidraw
            Hook-->>Agent: Early return (protect Obsidian JSON/comment blocks)
        else Standard code or markdown file
            Hook->>Fmt: docker run --rm (or local formatter fallback)
            Hook-->>Agent: Exit 0
        end
    end
```

### 2.3 Obsidian + Excalidraw LLM Wiki Pipeline

```mermaid
flowchart LR
    Raw["raw/ (Immutable sources + raw/assets/)"] -->|"Read-only ingestion"| Ops["LLM Operations (Ingest / Query / Lint)"]
    Ops -->|"Summaries, entities, concepts, syntheses"| Wiki["wiki/ (*.md + index.md + log.md)"]
    Ops -->|"JSON spec → excalidraw_gen.py"| Visuals["wiki/visuals/*.excalidraw.md"]
    Wiki -->|"![[diagram.excalidraw]] embeds"| Obsidian["Obsidian (Graph · Excalidraw · Dataview)"]
    Visuals -->|"^id: [[wikilink]] navigation"| Obsidian
    Wiki -->|"wiki_tool.py lint"| Gate["Link, frontmatter & Excalidraw validation"]
```

---

## 3. Module Breakdown

### 3.1 Installer & Remote Bootstrapper (`install.sh`)
- **Bash 3.2+ compatibility**: Avoids Bash 4+ features (associative arrays, `mapfile`) and passes `${1+"$@"}` to remain safe under `set -u` with zero arguments on stock macOS `/bin/bash`.
- **Safe remote execution**: Wraps execution in `main()`, handles `--help`/`-h` before cloning, validates non-git target directory collisions, and recovers interactive TTY via `/dev/tty`.
- **Pure `--dry-run`**: Guards directory creation (`mkdir -p`) under `DRY_RUN=false` so preview runs leave the filesystem untouched.

### 3.2 Cross-Vendor SSoT (`shared/`)
- **13 Specialized Subagents & Model Tiering**:
  - Deep reasoning tier (`opus` / `high` / `pro`, 8 agents): `code-reviewer`, `security-reviewer`, `quality-reviewer`, `test-agent`, `debug-agent`, `refactor-agent`, `guide-writer`, `human-writer`.
  - Fast execution tier (`sonnet` / `medium` / `flash`, 5 agents): `unit-test-agent`, `integration-test-agent`, `commit-agent`, `github-agent`, `docs-agent`.
- **Built-in GitHub Flow (`commit-agent`, `github-agent`)**: `main`/`master` branch protection, issue-linked commits (`[#N]` default, `- #N` for strict Conventional Commit parsers), Milestone/Project existence checks, `--body-file` + `shell=False` body safety, and `gh pr checks` + issue checkbox synchronization on merge.
- **Cross-Vendor MCP Sync ([sync_mcp.py](../shared/sync_mcp.py))**: Translates `shared/mcp.json` into Gemini `mcp_config.json` (`serverUrl`), Codex `config.toml` (`[mcp_servers.*]`), and Claude `~/.claude.json` (`mcpServers` merge preserving dynamic state).

### 3.3 Security Guard & Containerized Formatter (`hook.py`, `docker/formatter/`)
- **Selective blocking (`PreToolUse`)**: `is_dangerous_rm()` and `is_dangerous_chmod()` permit safe subpath cleanups (`/tmp/...`, `./dist`) while blocking destructive operations on `/`, `~`, and critical system directories.
- **Isolated formatter (`PostToolUse`)**: `debian:bookworm-slim` image (`agents-config-formatter:latest`) bundling Prettier, Ruff, Black, Clang-format, `google-java-format` v1.24.0, and StyLua v2.0.2, with local binary fallback and explicit exclusion for `.excalidraw.md`/`.excalidraw`.

### 3.4 LLM Wiki & Excalidraw Toolchain (`shared/skills/llm-wiki/`)
- **`excalidraw_gen.py`**: Zero-dependency generator computing CJK character widths via `unicodedata.east_asian_width`, deterministic `zlib.crc32` seeds, `LR`/`TB` layouts, semantic `KIND_STYLES`, bidirectional `containerId`/`startBinding`/`endBinding` bindings, `## Element Links`, and schema validation.
- **`wiki_tool.py`**: `init` (personal Obsidian vaults or `--no-templates` repo wikis), `lint` (frontmatter, wikilinks/embeds, orphan detection, `index.md` coverage, Excalidraw schema), and `log` (chronological append-only entries).

### 3.5 Automated Testing & CI (`tests/`, `.github/workflows/ci.yml`)
- **Stdlib test suite (`tests/`)**: 17 unit/integration tests executable via `python3 -m unittest discover -s tests` with zero third-party dependencies.
- **Dual-OS CI matrix**: `ubuntu-latest` lint/schema/unit job plus `ubuntu-latest` and `macos-latest` isolated-`HOME` installer verification matrix.

---

## 4. Architecture Decision Records (ADRs)

### ADR-01: Bash 3.2+ Single Orchestrator (`install.sh`) Over Stow / Chezmoi
- **Context**: Clean macOS workstations and minimal Linux environments lack third-party dotfile managers before bootstrap.
- **Decision**: Implement symlinking, timestamped backups, `--dry-run`, and remote `curl` bootstrap in dependency-free Bash 3.2+.
- **Consequences**: Zero-dependency one-line installation across macOS and Linux, verified on every PR via GitHub Actions.

### ADR-02: `shared/` SSoT + Unified Hook Payload Normalization
- **Context**: Claude Code, Gemini CLI, and Codex CLI differ in skill directory layouts, MCP schemas, and hook JSON payloads (`toolCall` vs `tool_name`/`tool_input`).
- **Decision**: Keep `shared/` as the sole canonical source, render vendor configs via `sync_mcp.py`, and normalize hook payloads inside `hook.py`'s `extract_tool_info()`.
- **Consequences**: Rules, security policies, skills, and MCP definitions stay synchronized across all three vendors without duplication.

### ADR-03: Ephemeral Docker Formatter + Excalidraw Exclusion Guard
- **Context**: Host-installed formatters drift across versions, and running Prettier on `.excalidraw.md` breaks Obsidian's `%%...%%` drawing blocks and `^id` anchors.
- **Decision**: Package multi-language formatters in `agents-config-formatter:latest` (with local fallback) and short-circuit `.excalidraw.md`/`.excalidraw` inside `format_file()`.
- **Consequences**: Consistent formatting across languages without corrupting Excalidraw diagrams.

### ADR-04: Deterministic JSON-Spec Excalidraw Generator (`excalidraw_gen.py`)
- **Context**: Hand-authoring raw Excalidraw v2 JSON in LLM output frequently causes dangling `boundElements` IDs and CJK text-box clipping.
- **Decision**: Have agents author compact semantic JSON specs and let `excalidraw_gen.py` compute CJK sizing, layout, deterministic seeds, bidirectional bindings, and `## Element Links`.
- **Consequences**: Zero schema errors and minimal, noise-free Git diffs on regeneration.

### ADR-05: Clear Separation Between `graphify` and `llm-wiki`
- **Context**: AST code-structure extraction and narrative personal/operational knowledge curation require different representations.
- **Decision**: Use `graphify` for structural AST/community knowledge graphs and `llm-wiki` for curated `raw/`/`wiki/` synthesis, contradiction tracking, and Excalidraw visuals.
- **Consequences**: Fast structural code queries paired with persistent, Obsidian-browsable knowledge accumulation.

---

- Overview: [README.en.md](../README.en.md)
- Repository Wiki: [wiki/overview.md](../wiki/overview.md)
