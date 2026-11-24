---
id: llm-wiki-workflow
type: concept
aliases:
  - "LLM Wiki 워크플로우"
  - "Obsidian Excalidraw Wiki"
tags:
  - concept
  - llm-wiki
  - obsidian
  - excalidraw
created: 2026-11-24
updated: 2026-11-24
sources: []
status: active
---

# Obsidian + Excalidraw LLM Wiki 워크플로우

질의마다 원문을 재검색하는 기존 RAG 대신, LLM이 마크다운 위키와 Excalidraw 다이어그램을 점진적으로 유지보수하는 지식 축적 패턴.

---

## 시각화

![[llm-wiki-workflow.excalidraw]]

---

## 핵심 구성 요소 (`shared/skills/llm-wiki/`)

1. **스킬 지침 (`SKILL.md`, `references/`)**:
   - `init`, `ingest`, `query`(역축적 포함), `visualize`, `lint` 5개 표준 워크플로우 정의
   - Obsidian Frontmatter, Dataview 쿼리, Web Clipper + `raw/assets/` 로컬 첨부 이미지 워크플로우, `qmd` 연동 규약 수록
2. **Excalidraw 생성·검증기 (`scripts/excalidraw_gen.py`)**:
   - 경량 JSON 스펙(노드 `kind` 시맨틱 팔레트, 그룹 프레임, `LR`/`TB` 자동 배치)을 Obsidian `excalidraw-plugin: parsed` 포맷(`.excalidraw.md`)으로 변환
   - CJK 문자 폭 자동 계산, 결정적 시드(`zlib.crc32`), 도형-텍스트(`containerId`) 및 화살표(`startBinding`/`endBinding`) 양방향 바인딩과 `## Element Links`(`^id: [[wikilink]]`) 자동 생성
3. **위키 초기화·린트·로그 도구 (`scripts/wiki_tool.py`)**:
   - `init`: 개인 Obsidian 볼트 또는 저장소 위키 골격 생성 (`--no-templates` 지원)
   - `lint`: YAML Frontmatter, 깨진 `[[wikilink]]`/`![[embed]]`, 고아 페이지, `index.md` 누락, `.excalidraw.md` 바인딩 무결성 일괄 검증
   - `log`: `## [YYYY-MM-DD] <op> | <Title>` 형식으로 append-only 로그 기록

---

## 연관 개념

- 전체 허브: [[overview]]
- 3사 스킬 배포 구조: [[three-vendor-ssot]]
- `.excalidraw.md` 포매팅 보호: [[lifecycle-hooks]]
