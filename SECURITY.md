# Security Policy

## 1. 민감 정보 및 동적 상태 격리 원칙 (Secret Isolation)

`agents-config`는 순수 선언적 설정만 추적하며, 아래 항목은 `.gitignore` 및 `PreToolUse` 가드로 저장소 포함·노출을 차단한다.

- **인증·토큰 파일**: `.env`, `.env.*` (`.env.example` 제외), `oauth_creds.json`, `auth.json`, `credentials.json`, SSH 개인키(`id_rsa*`, `id_ed25519*`, `*.pem`, `*.key`)
- **동적 상태·로컬 오버라이드**: `*.local`, `*.local.*`, `*.sqlite*`, `history.jsonl`, `.obsidian/workspace*.json`
- **시크릿 토큰 패턴 (`shared/hooks/hook.py`)**: GitHub PAT(`ghp_`, `github_pat_`), OpenAI(`sk-`), Google(`AIzaSy`), AWS(`AKIA`), Slack(`xox*`) 패턴이 명령어에 포함되면 `PreToolUse` 단계에서 차단

---

## 2. 런타임 및 자동화 안전 통제

1. **파괴적 명령 선별 차단 (`shared/hooks/hook.py`)**:
   - `git push --force`, `git reset --hard`, `git clean -f`, `git checkout .`/`-f`, `mkfs`, `dd` 차단
   - 루트(`/`)·홈(`~`)·시스템 핵심 디렉터리 대상 재귀 삭제(`rm -r`) 및 `chmod -R 777` 차단
2. **`gh` CLI 명령 인젝션·변수 오염 방지 (`shared/agents/github-agent.md`)**:
   - 마크다운 본문 등록·수정(`create`/`edit`) 시 셸 백틱 치환을 막기 위해 `--body-file - <<'EOF'` 또는 `subprocess.run([...], shell=False)` + `--body-file` 옵션만 허용
3. **최소 권한 CI (`ci.yml`)**:
   - GitHub Actions 워크플로에 `permissions: contents: read` 적용

---

## 3. 취약점 제보 (Reporting a Vulnerability)

- 민감 정보 노출이나 보안 취약점 발견 시 공개 이슈 대신 저장소 소유자(`@gdtknight`)의 GitHub Security Advisories 또는 비공개 연락 채널을 통해 제보한다.
- 토큰·키 유출이 의심되는 경우 즉시 해당 자격 증명을 폐기·재발급한 뒤 커밋 히스토리를 점검한다.
