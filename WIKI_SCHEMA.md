# Agents Config Wiki Schema

**도메인**: Claude Code, Gemini CLI / Antigravity, Codex CLI 통합 설정·스킬·훅 운영 지식  
**생성일**: 2026-11-24  

---

## 1. 3계층 구조 및 소유권

1. **`raw/` (불변 원본)**: 외부 레퍼런스, 클리핑 노트, 이미지(`raw/assets/`) 저장. LLM 수정 금지.
2. **`wiki/` (지속 누적 위키)**: `overview.md`, `index.md`, `log.md`, `sources/`, `entities/`, `concepts/`, `syntheses/`, `visuals/*.excalidraw.md`. LLM이 유지보수.
3. **`WIKI_SCHEMA.md` (스키마)**: `agents-config` 저장소의 위키 구조·문체·시각화 규약 정의.

---

## 2. 작성·시각화·검증 규칙

- **근거 검증 (`shared/rules/accuracy.md`)**: 모든 설정 경로, 심볼, 스크립트 동작은 실제 저장소 파일을 직접 확인한 사실만 기술.
- **기술 문서 문체**: 서술형 종결어미와 1인칭을 배제한 간결한 명사형·개조식 문장 유지.
- **YAML Frontmatter**: 모든 콘텐츠 페이지 상단에 `id`, `type`, `aliases`, `tags`, `created`, `updated`, `sources`, `status` 기재.
- **Excalidraw 시각화**: 아키텍처·워크플로우 다이어그램은 `shared/skills/llm-wiki/scripts/excalidraw_gen.py`로 `wiki/visuals/*.excalidraw.md` 생성 후 `![[<name>.excalidraw]]`로 임베드.
- **포매팅 보호**: `.excalidraw.md`는 `shared/hooks/hook.py`가 Prettier 자동 포매팅에서 제외.

---

## 3. 유지보수 명령

```bash
# 위키 정적·링크·Excalidraw 무결성 점검
python3 shared/skills/llm-wiki/scripts/wiki_tool.py lint .

# 로그 추가
python3 shared/skills/llm-wiki/scripts/wiki_tool.py log . <op> "<Title>"
```
