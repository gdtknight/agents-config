# Agents Config Repository Guidelines

Claude Code, Gemini CLI / Antigravity, Codex CLI 통합 설정·스킬·에이전트·훅 단일 진실 공급원(SSoT) 저장소 지침.

---

## 1. 핵심 작업 원칙

1. **Single Source of Truth (SSoT)**:
   - 대상 시스템 경로(`~/.claude`, `~/.gemini`, `~/.codex`, `~/.claude.json`) 직접 편집 금지.
   - 모든 변경은 `agents-config/` 내부 파일에서 수행하고 `./install.sh`로 반영.
   - 호스트 환경은 심볼릭 링크로 연결되므로 저장소 수정 즉시 반영.

2. **민감 정보 및 동적 상태 격리**:
   - 인증 토큰(`oauth_creds.json`, `auth.json`, `credentials.json`), 세션 히스토리(`history.jsonl`, `*.sqlite*`), 머신별 호스트명·로컬 절대 경로 커밋 금지.
   - 선언적 설정(`settings.json`, `config.json`, `config.toml`, `rules/`, `agents/`, `skills/`, `hooks/`, `mcp.json`)만 Git 추적.

---

## 2. 디렉터리 구조 및 동기화 규칙

```
agents-config/
├── shared/           # 3사 공용 SSoT (INSTRUCTIONS.md, rules/, agents/, skills/, hooks/, mcp.json, sync_mcp.py)
├── claude/           # Claude Code 설정 (settings.json)
├── gemini/           # Gemini CLI / Antigravity 설정 (settings.json, config.json, hooks.json, mcp_config.json)
├── codex/            # Codex CLI 설정 (config.toml, agents/*.toml)
├── docker/formatter/ # PostToolUse 공용 포매터 컨테이너 (agents-config-formatter:latest)
├── raw/              # LLM Wiki 불변 원본 (raw/assets/ 포함)
├── wiki/             # 저장소 운영 지식 위키 (index.md, log.md, overview.md, concepts/, visuals/*.excalidraw.md)
├── WIKI_SCHEMA.md    # 저장소 위키 스키마 규약
└── install.sh        # Bash 3.2+ 멱등적 심볼릭 링크·MCP 설치 스크립트
```

1. **3사 공용 에이전트·스킬 관리 (`shared/`)**:
   - 전역 지침([INSTRUCTIONS.md](shared/INSTRUCTIONS.md)), 세부 규칙(`shared/rules/`), 전문 에이전트(`shared/agents/*.md`), 공용 스킬(`shared/skills/<name>/`: `graphify`, `llm-wiki`), 라이프사이클 훅(`shared/hooks/hook.py`), 공용 MCP(`shared/mcp.json`)는 `shared/`에서 단일 관리.
   - 전문 에이전트 추가 시 `shared/agents/<name>.md`와 `codex/agents/<name>.toml` 동시 작성.
   - 다중 파일 스킬 추가 시 `shared/skills/<name>/` 하위에 배치하여 `./install.sh agents` 실행 시 Claude(`~/.claude/skills`), Gemini(`~/.gemini/config/skills`), Codex(`~/.codex/skills`) 자동 동기화 유지.
   - `.excalidraw.md` 다이어그램은 `shared/skills/llm-wiki/scripts/excalidraw_gen.py`로 생성·검증하며 `shared/hooks/hook.py`가 Prettier 포매팅에서 자동 제외.

2. **공용 MCP 동기화 (`shared/mcp.json`, `shared/sync_mcp.py`)**:
   - MCP 서버 추가·비활성화 변경은 `shared/mcp.json`만 수정(시크릿 포함 금지).
   - `./install.sh mcp` 또는 `./install.sh agents` 실행 시 `shared/sync_mcp.py`가 `gemini/mcp_config.json`, `codex/config.toml`(`[mcp_servers.*]`), `~/.claude.json`(`mcpServers`) 자동 갱신.

3. **설치 스크립트 호환성 (`install.sh`)**:
   - macOS 기본 Bash 3.2+ 호환 유지(연관 배열 등 Bash 4+ 전용 문법 금지).
   - `--dry-run` 시 파일·디렉터리 생성 및 변경 차단, 충돌 시 `~/.agents-config_backups/` 타임스탬프 백업 보장.
   - `AGENTS.md -> CLAUDE.md` 심볼릭 링크 유지.

---

## 3. 검증 및 커밋 표준

1. **사전 드라이런 검증**:
   - 수정 후 `./install.sh --dry-run --skip-cli`로 구문 및 링크 대상 검증.
   - 문법·정적 검증: `bash -n install.sh docker/formatter/build.sh`, `python3 -m py_compile shared/sync_mcp.py shared/hooks/hook.py`.
2. **격리 홈 디렉터리 검증**:
   - 실환경(`$HOME`) 적용 전 임시 `HOME` 경로에서 `./install.sh --skip-cli` 실행 및 깨진 심볼릭 링크 부재 확인.
3. **커밋 규칙**:
   - Conventional Commits(`feat:`, `fix:`, `refactor:`, `docs:`, `chore:`) 및 Chris Beams 7원칙(영문 명령문, 첫 글자 대문자, 50자 이하 제목, 마침표 생략) 준수.
