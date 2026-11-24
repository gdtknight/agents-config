---
id: lifecycle-hooks
type: concept
aliases:
  - "통합 라이프사이클 훅"
  - "hook.py"
tags:
  - concept
  - security
  - formatter
  - hooks
created: 2026-11-24
updated: 2026-11-24
sources: []
status: active
---

# 통합 라이프사이클 훅 (`shared/hooks/hook.py`)

Claude Code(`PreToolUse`/`PostToolUse`/`Stop`), Gemini/AGY(`BeforeTool`/`AfterTool`/`AfterAgent`, `gemini/hooks.json`), Codex(`hooks/`) 페이로드를 `extract_tool_info()`로 정규화해 단일 보안·포매팅·알림 파이프라인으로 처리.

---

## 단계별 동작

1. **`PreToolUse` (보안 가드)**:
   - 위험 Git·디스크 명령(`git push --force`, `git reset --hard`, `git clean -f`, `git checkout .`/`-f`, `mkfs`, `dd`) 차단
   - `is_dangerous_rm()` 및 `is_dangerous_chmod()`로 루트(`/`)·홈(`~`)·시스템 핵심 디렉터리 대상 파괴적 명령만 정밀 차단
   - `SENSITIVE_FILE_PATTERN`(`.env`, SSH 키, 인증 토큰 파일) 및 `SECRET_PATTERNS`(GitHub/OpenAI/Google/AWS/Slack 토큰) 노출 차단 (`decision: "deny"`, exit 1)
2. **`PostToolUse` (단발성 Docker 포매터 + 예외 보호)**:
   - 파일 쓰기·수정 도구(`write_file`, `edit_file`, `Write`, `Edit`, `str_replace_editor`) 실행 후 확장자별 포매터(`prettier`, `ruff`, `clang-format`, `stylua`, `google-java-format`)를 `agents-config-formatter:latest` 컨테이너에서 실행 (Docker 미가용 시 로컬 바이너리 폴백)
   - **Excalidraw 보호**: `.excalidraw.md` 및 `.excalidraw` 파일은 `%%...%%` 주석·JSON 블록 손상 방지를 위해 포매팅 단계에서 즉시 반환
3. **`Stop` (완료 알림)**:
   - macOS 환경에서 `terminal-notifier` 우선 실행 후 미설치 시 `osascript`로 활성 앱(`Antigravity IDE`, `WezTerm`, `Alacritty`, `iTerm2`, `Terminal`) 대상 완료 알림 전송

---

## 연관 개념

- 전체 허브: [[overview]]
- 훅 배포·링크 구조: [[three-vendor-ssot]]
- Excalidraw 보호 대상 워크플로우: [[llm-wiki-workflow]]
