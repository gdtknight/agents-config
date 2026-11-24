# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.0] - 2026-11-25

### Added
- Standalone cross-vendor SSoT layout (`shared/`, `claude/`, `gemini/`, `codex/`, `docker/formatter/`) separated from `dotconfig`.
- Dependency-free Bash 3.2+ installer (`install.sh`) with `--dry-run`, `--force`, `--skip-cli`, timestamped backups (`~/.agents-config_backups/`), and `curl` remote bootstrapper (SDKMAN pipe and Homebrew `-c` modes).
- Cross-vendor MCP synchronizer (`shared/sync_mcp.py`) translating `shared/mcp.json` into Gemini `mcp_config.json`, Codex `config.toml`, and Claude `~/.claude.json`.
- Unified lifecycle hook (`shared/hooks/hook.py`) with `PreToolUse` destructive/secret guards, `PostToolUse` ephemeral Docker formatter (`agents-config-formatter:latest`), and macOS `Stop` notifications.
- `llm-wiki` shared skill (`shared/skills/llm-wiki/`) with zero-dependency `excalidraw_gen.py` (CJK-aware sizing, deterministic `zlib.crc32` seeds, `LR`/`TB` layout, bidirectional bindings, `## Element Links`) and `wiki_tool.py` (`init`, `lint`, `log`), plus repository wiki (`wiki/`, `raw/`, `WIKI_SCHEMA.md`).
- Python stdlib unit/integration test suite (`tests/` — 17 test cases across `test_hook.py`, `test_sync_mcp.py`, `test_excalidraw_gen.py`, `test_wiki_tool.py`).
- GitHub Actions CI workflow (`.github/workflows/ci.yml`) running `shellcheck`, `bash -n`, `py_compile`, JSON/TOML validation, `unittest`, `wiki_tool.py lint .`, `excalidraw_gen.py validate`, and `ubuntu-latest`/`macos-latest` installer matrix, alongside `.github/` PR and Issue templates ([#4](https://github.com/gdtknight/agents-config/pull/4)).
- Bilingual architecture documentation (`docs/ARCHITECTURE.ko.md`, `docs/ARCHITECTURE.md` with C4 Model & ADR-01~05) and portfolio READMEs (`README.md`, `README.en.md`) ([#6](https://github.com/gdtknight/agents-config/pull/6)).

### Changed
- Enforced GitHub Flow branch protection, issue-linked commit titles (`[#N]` default and `- #N` for strict parsers), Milestone/GitHub Project checks, `--body-file`/`shell=False` body safety, and CI-gated merge & issue checkbox synchronization in `@commit-agent`, `@github-agent`, Codex TOMLs, and `shared/INSTRUCTIONS.md` ([#2](https://github.com/gdtknight/agents-config/pull/2)).
- Excluded `.excalidraw.md` and `.excalidraw` files from `PostToolUse` Prettier auto-formatting in `shared/hooks/hook.py`.

### Fixed
- Replaced non-existent `gh milestone list` with `gh api repos/{owner}/{repo}/milestones` in `shared/agents/github-agent.md` ([#2](https://github.com/gdtknight/agents-config/pull/2)).
- Quoted `"$HOME"` inside backup path stripping in `install.sh` to resolve ShellCheck `SC2295` ([#4](https://github.com/gdtknight/agents-config/pull/4)).

[Unreleased]: https://github.com/gdtknight/agents-config/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/gdtknight/agents-config/releases/tag/v1.0.0
