---
id: three-vendor-ssot
type: concept
aliases:
  - "3사 통합 SSoT"
  - "Three-Vendor SSoT"
tags:
  - concept
  - architecture
  - mcp
  - install
created: 2026-11-24
updated: 2026-11-24
sources: []
status: active
---

# 3사 통합 SSoT 및 동기화 구조

`shared/` 디렉터리를 단일 진실 공급원(SSoT)으로 두고 `install.sh`와 `shared/sync_mcp.py`가 Claude Code, Gemini/Antigravity, Codex CLI 환경에 투영하는 구조.

---

## 핵심 메커니즘

1. **공용 지침·규칙·에이전트·스킬 (`shared/`)**:
   - `shared/INSTRUCTIONS.md` → `~/.claude/CLAUDE.md`, `~/.gemini/GEMINI.md`, `~/.codex/AGENTS.md`
   - `shared/rules/` → 3사 `rules/` 경로 심볼릭 링크
   - `shared/agents/*.md` (13개 전문 에이전트) → Claude `agents/`, Gemini/Codex `skills/<name>/SKILL.md`로 연결 (`codex/agents/*.toml` 1:1 대응)
   - `shared/skills/<name>/` (`graphify`, `llm-wiki`) → 3사 `skills/<name>/`로 자동 동기화
2. **Bash 3.2+ 멱등적 설치 (`install.sh`)**:
   - macOS 기본 Bash 3.2 환경 호환 (`--dry-run` 시 디렉터리·파일 미생성, 충돌 시 `~/.agents-config_backups/` 타임스탬프 백업)
   - `--skip-cli`로 CLI(`agy`, `claude`, `codex`) 설치 확인 생략 가능
3. **공용 MCP 동기화 (`shared/sync_mcp.py`)**:
   - `shared/mcp.json`을 검증·정규화한 뒤 벤더별 포맷으로 변환
   - Gemini/AGY: `gemini/mcp_config.json` (`serverUrl` 스키마)
   - Codex: `codex/config.toml`의 `# BEGIN/END AGENTS-CONFIG MANAGED MCP` 블록
   - Claude Code: `~/.claude.json`의 기존 동적 상태를 유지하며 `mcpServers` 병합

---

## 시각화

![[agents-config-architecture.excalidraw]]

---

## 연관 개념

- 전체 허브: [[overview]]
- 런타임 훅 연동: [[lifecycle-hooks]]
- 공용 스킬 구조: [[llm-wiki-workflow]]
