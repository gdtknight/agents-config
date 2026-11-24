# Agents Config

Claude Code, Gemini CLI / Antigravity, Codex CLI 설정·규칙·전문 에이전트·스킬·라이프사이클 훅을 단일 진실 공급원(SSoT)으로 통합 관리하는 독립 저장소.

---

## 디렉터리 구조

| 경로 | 역할 | 비고 |
| :--- | :--- | :--- |
| `shared/` | 3사 공용 지침·규칙·에이전트·스킬·훅·MCP | 단일 원본(SSoT) |
| `shared/INSTRUCTIONS.md` | 전역 엔지니어링 지침 | Claude/Gemini/Codex 공통 진입점 |
| `shared/rules/` | 세부 규칙 (`accuracy.md`, `engineering.md`, `c-cpp.md`) | — |
| `shared/agents/` | 13개 전문 에이전트 프롬프트 (`*.md`) | Codex용 `SKILL.md`로도 연결 |
| `shared/skills/` | 다중 파일 공용 스킬 (`graphify/`, `llm-wiki/`) | 3사 `skills/` 경로 자동 동기화 |
| `shared/hooks/hook.py` | `PreToolUse` / `PostToolUse` / `Stop` 통합 훅 | 보안 가드 · 자동 포맷 · 완료 알림 |
| `shared/mcp.json` | 공용 MCP 선언 | `sync_mcp.py`로 3사 포맷 생성 |
| `claude/` | Claude Code 전용 `settings.json` | — |
| `gemini/` | Gemini / Antigravity 설정 (`settings.json`, `config.json`, `hooks.json`, `mcp_config.json`) | — |
| `codex/` | Codex CLI 설정 (`config.toml`, `agents/*.toml`) | 13개 서브에이전트 TOML 매핑 |
| `docker/formatter/` | `PostToolUse` 포매터 이미지 (`agents-config-formatter:latest`) | Prettier, Ruff, Black, Clang-format, StyLua, Google-Java-Format |
| `raw/`, `wiki/`, `WIKI_SCHEMA.md` | Obsidian + Excalidraw 호환 저장소 위키 | `wiki/visuals/*.excalidraw.md` 시각화 포함 |
| `install.sh` | Bash 3.2+ 심볼릭 링크·MCP·CLI 설치 스크립트 | `--dry-run`, 타임스탬프 백업 지원 |

---

## 설치 및 사용법

```bash
# 1. 변경 내역 사전 점검 (디스크 변경 없음)
./install.sh --dry-run

# 2. 전체 연동 (MCP 동기화 + 3사 심볼릭 링크 + CLI 설치 확인)
./install.sh

# 3. CLI 설치 확인 제외하고 링크/MCP만 반영
./install.sh --skip-cli

# 4. 특정 모듈만 선택 적용
./install.sh claude gemini
./install.sh mcp

# 5. PostToolUse Docker 포매터 이미지 빌드 (선택)
./install.sh formatter
```

- 기존 파일 충돌 시 `~/.agents-config_backups/backup_YYYYMMDD_HHMMSS/`로 자동 백업 후 심볼릭 링크 생성.
- `--force`(`-f`) 옵션으로 기존 동일 대상 심볼릭 링크 강제 재연결 가능.

---

## 3사 심볼릭 링크 및 MCP 매핑

| 구성 요소 | Claude (`~/.claude`) | Gemini / AGY (`~/.gemini`) | Codex (`~/.codex`) |
| :--- | :--- | :--- | :--- |
| 전역 지침 | `CLAUDE.md` | `GEMINI.md` | `AGENTS.md` |
| 세부 규칙 | `rules/` | `config/rules/` | `rules/` |
| 전문 에이전트 | `agents/` | `agents/`, `config/skills/<name>/SKILL.md` | `agents/`, `skills/<name>/SKILL.md` |
| 공용 스킬 | `skills/<skill>/` | `config/skills/<skill>/` | `skills/<skill>/` |
| 라이프사이클 훅 | `hooks/`, `settings.json` | `config/hooks/`, `settings.json`, `config/hooks.json` | `hooks/` |
| MCP 서버 | `~/.claude.json` (`mcpServers` 병합) | `config/mcp_config.json` | `config.toml` (`[mcp_servers.*]`) |

---

## 주요 내장 구성

- **전문 에이전트 (13종)**: `code-reviewer`, `security-reviewer`, `quality-reviewer`, `test-agent`, `unit-test-agent`, `integration-test-agent`, `debug-agent`, `refactor-agent`, `commit-agent`, `github-agent`, `docs-agent`, `guide-writer`, `human-writer`
- **공용 스킬 (2종)**:
  - `graphify`: 코드·문서 지식 그래프 구축 및 탐색
  - `llm-wiki`: Obsidian + Excalidraw 연동 3계층 위키(`raw/` · `wiki/` · `WIKI_SCHEMA.md`) 구축·유지보수 (`wiki_tool.py`, `excalidraw_gen.py`)
- **통합 훅 (`shared/hooks/hook.py`)**:
  - `PreToolUse`: 파괴적 명령(`git push --force`, `git reset --hard`, 루트/홈 `rm`/`chmod`), `.env`·키 파일 접근, API 토큰 패턴 차단
  - `PostToolUse`: `agents-config-formatter:latest` 단발성 컨테이너 또는 로컬 포매터 폴백 실행 (`.excalidraw.md`, `.excalidraw` 자동 제외)
  - `Stop`: macOS 완료 알림 (`terminal-notifier` 우선, AppleScript 폴백)

---

## 개인 Obsidian 볼트 위키 초기화

```bash
# 새 Obsidian 볼트 또는 기존 볼트에 LLM Wiki 구조 초기화
python3 shared/skills/llm-wiki/scripts/wiki_tool.py init \
  "${HOME}/Library/Mobile Documents/iCloud~md~obsidian/Documents/<VaultName>" \
  --name "<Wiki Title>" \
  --domain "<Domain>"

# 위키 링크·프론트매터·Excalidraw 무결성 검증
python3 shared/skills/llm-wiki/scripts/wiki_tool.py lint \
  "${HOME}/Library/Mobile Documents/iCloud~md~obsidian/Documents/<VaultName>"
```
