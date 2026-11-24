# Agents Config Wiki Index

도메인: Claude, Gemini/AGY, Codex 통합 설정·스킬·훅 운영 지식  
최종 갱신: 2026-11-24  

> 질의 시 `index.md`에서 관련 페이지를 먼저 선별한 뒤 본문을 정독.  
> 인제스트·시각화·역축적 완료 시 이 카탈로그를 즉시 갱신.

---

## Overview

- [[overview|Agents Config Wiki Overview]] — `agents-config` 지식 베이스 전체 구조 및 핵심 진입 허브

---

## Visuals (Excalidraw)

- [[visuals/agents-config-architecture.excalidraw|Agents Config Architecture]] — `shared/` SSoT, `install.sh` 배포, `sync_mcp.py`, `hook.py` 런타임 계층도
- [[visuals/llm-wiki-workflow.excalidraw|LLM Wiki and Excalidraw Workflow]] — `raw/` → `Ingest/Query/Lint` → `wiki/` · `.excalidraw.md` → Obsidian 순환 흐름도

---

## Sources

<!-- raw/ 원본별 요약 페이지 (wiki/sources/) -->

---

## Concepts

- [[concepts/three-vendor-ssot|3사 통합 SSoT 및 동기화 구조]] — `shared/` 단일 원본 기반 Claude/Gemini/Codex 심볼릭 링크·MCP 동기화 메커니즘
- [[concepts/lifecycle-hooks|통합 라이프사이클 훅 (hook.py)]] — `PreToolUse` 보안 가드, `PostToolUse` Docker 포매터(`.excalidraw.md` 제외), `Stop` 알림
- [[concepts/llm-wiki-workflow|Obsidian + Excalidraw LLM Wiki 워크플로우]] — `excalidraw_gen.py`·`wiki_tool.py` 기반 지식 축적 및 시각화 파이프라인

---

## Entities

<!-- 도구·시스템·에이전트별 상세 페이지 (wiki/entities/) -->

---

## Syntheses

<!-- 질의 결과 역축적·비교 분석 (wiki/syntheses/) -->
