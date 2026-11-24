---
id: llm-wiki-and-excalidraw-workflow
type: excalidraw
excalidraw-plugin: parsed
tags:
  - excalidraw
  - llm-wiki
  - obsidian
created: 2026-11-24
updated: 2026-11-24
sources:
  - "[[llm-wiki-workflow]]"
  - "[[overview]]"
---
==⚠ Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠==

# Excalidraw Data
## Text Elements
Layer 1: Raw (불변) ^grp-title-layer-raw

LLM Operations ^grp-title-layer-ops

Layer 2: Wiki & Visuals ^grp-title-layer-wiki

Obsidian IDE ^grp-title-layer-obs

raw/
원본 문서·노트 ^raw-docs-text

raw/assets/
로컬 첨부 이미지 ^raw-assets-text

Ingest
요약·통합·모순 감지 ^op-ingest-text

Query
색인 탐색·질의 응답 ^op-query-text

Lint
링크·고아·모순 점검 ^op-lint-text

wiki/
sources · entities · concepts ^wiki-pages-text

wiki/visuals/
*.excalidraw.md ^wiki-exc-text

index.md & log.md
카탈로그 · 연대기 로그 ^wiki-meta-text

Obsidian
Graph · Excalidraw · Dataview ^obsidian-text

read ^edge-0-raw-docs-to-op-ingest-label

vision ^edge-1-raw-assets-to-op-ingest-label

write/update ^edge-2-op-ingest-to-wiki-pages-label

excalidraw_gen.py ^edge-3-op-ingest-to-wiki-exc-label

read ^edge-4-wiki-pages-to-op-query-label

file-back ^edge-5-op-query-to-wiki-pages-label

wiki_tool.py lint ^edge-6-wiki-pages-to-op-lint-label

catalog ^edge-7-wiki-pages-to-wiki-meta-label

render ^edge-8-wiki-exc-to-obsidian-label

browse ^edge-9-wiki-meta-to-obsidian-label

## Element Links
^raw-docs: [[llm-wiki-workflow]]
^raw-assets: [[llm-wiki-workflow]]
^op-ingest: [[llm-wiki-workflow]]
^op-query: [[llm-wiki-workflow]]
^op-lint: [[llm-wiki-workflow]]
^wiki-pages: [[overview]]
^wiki-exc: [[agents-config-architecture.excalidraw]]
^wiki-meta: [[index]]
^obsidian: [[overview]]

%%
## Drawing
```json
{
  "type": "excalidraw",
  "version": 2,
  "source": "https://excalidraw.com",
  "elements": [
    {
      "id": "grp-layer-raw",
      "type": "rectangle",
      "x": 56.0,
      "y": 232.4,
      "width": 214.7,
      "height": 248.0,
      "angle": 0,
      "strokeColor": "#1971c2",
      "backgroundColor": "#f8f9fa",
      "fillStyle": "solid",
      "strokeWidth": 1,
      "strokeStyle": "dashed",
      "roughness": 1,
      "opacity": 60,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 3
      },
      "seed": 1130578164,
      "version": 1,
      "versionNonce": 1130578165,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "id": "grp-title-layer-raw",
      "type": "text",
      "x": 68.0,
      "y": 242.4,
      "width": 151.8,
      "height": 17.5,
      "angle": 0,
      "strokeColor": "#1971c2",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 473859373,
      "version": 1,
      "versionNonce": 473859374,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1,
      "link": null,
      "locked": false,
      "text": "Layer 1: Raw (불변)",
      "originalText": "Layer 1: Raw (불변)",
      "fontSize": 14,
      "fontFamily": 1,
      "textAlign": "left",
      "verticalAlign": "top",
      "containerId": null,
      "lineHeight": 1.25,
      "autoResize": true
    },
    {
      "id": "grp-layer-ops",
      "type": "rectangle",
      "x": 332.7,
      "y": 36.0,
      "width": 975.0,
      "height": 397.6,
      "angle": 0,
      "strokeColor": "#c2255c",
      "backgroundColor": "#f8f9fa",
      "fillStyle": "solid",
      "strokeWidth": 1,
      "strokeStyle": "dashed",
      "roughness": 1,
      "opacity": 60,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 3
      },
      "seed": 53057498,
      "version": 1,
      "versionNonce": 53057499,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "id": "grp-title-layer-ops",
      "type": "text",
      "x": 344.7,
      "y": 46.0,
      "width": 113.7,
      "height": 17.5,
      "angle": 0,
      "strokeColor": "#c2255c",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 1551127047,
      "version": 1,
      "versionNonce": 1551127048,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1,
      "link": null,
      "locked": false,
      "text": "LLM Operations",
      "originalText": "LLM Operations",
      "fontSize": 14,
      "fontFamily": 1,
      "textAlign": "left",
      "verticalAlign": "top",
      "containerId": null,
      "lineHeight": 1.25,
      "autoResize": true
    },
    {
      "id": "grp-layer-wiki",
      "type": "rectangle",
      "x": 703.5,
      "y": 290.4,
      "width": 622.3,
      "height": 270.4,
      "angle": 0,
      "strokeColor": "#2f9e44",
      "backgroundColor": "#f8f9fa",
      "fillStyle": "solid",
      "strokeWidth": 1,
      "strokeStyle": "dashed",
      "roughness": 1,
      "opacity": 60,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 3
      },
      "seed": 488704577,
      "version": 1,
      "versionNonce": 488704578,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "id": "grp-title-layer-wiki",
      "type": "text",
      "x": 715.5,
      "y": 300.4,
      "width": 186.8,
      "height": 17.5,
      "angle": 0,
      "strokeColor": "#2f9e44",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 194156737,
      "version": 1,
      "versionNonce": 194156738,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1,
      "link": null,
      "locked": false,
      "text": "Layer 2: Wiki & Visuals",
      "originalText": "Layer 2: Wiki & Visuals",
      "fontSize": 14,
      "fontFamily": 1,
      "textAlign": "left",
      "verticalAlign": "top",
      "containerId": null,
      "lineHeight": 1.25,
      "autoResize": true
    },
    {
      "id": "grp-layer-obs",
      "type": "rectangle",
      "x": 980.7,
      "y": 544.8,
      "width": 345.1,
      "height": 132.0,
      "angle": 0,
      "strokeColor": "#6741d9",
      "backgroundColor": "#f8f9fa",
      "fillStyle": "solid",
      "strokeWidth": 1,
      "strokeStyle": "dashed",
      "roughness": 1,
      "opacity": 60,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 3
      },
      "seed": 2078140171,
      "version": 1,
      "versionNonce": 2078140172,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "id": "grp-title-layer-obs",
      "type": "text",
      "x": 992.7,
      "y": 554.8,
      "width": 97.4,
      "height": 17.5,
      "angle": 0,
      "strokeColor": "#6741d9",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 612377302,
      "version": 1,
      "versionNonce": 612377303,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1,
      "link": null,
      "locked": false,
      "text": "Obsidian IDE",
      "originalText": "Obsidian IDE",
      "fontSize": 14,
      "fontFamily": 1,
      "textAlign": "left",
      "verticalAlign": "top",
      "containerId": null,
      "lineHeight": 1.25,
      "autoResize": true
    },
    {
      "id": "raw-docs",
      "type": "rectangle",
      "x": 83.3,
      "y": 276.4,
      "width": 160.0,
      "height": 64.0,
      "angle": 0,
      "strokeColor": "#1971c2",
      "backgroundColor": "#d0ebff",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 3
      },
      "seed": 2045979827,
      "version": 1,
      "versionNonce": 2045979828,
      "isDeleted": false,
      "boundElements": [
        {
          "id": "raw-docs-text",
          "type": "text"
        },
        {
          "id": "edge-0-raw-docs-to-op-ingest",
          "type": "arrow"
        }
      ],
      "updated": 1,
      "link": "[[llm-wiki-workflow]]",
      "locked": false
    },
    {
      "id": "raw-docs-text",
      "type": "text",
      "x": 102.5,
      "y": 288.4,
      "width": 121.6,
      "height": 40.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 396605693,
      "version": 1,
      "versionNonce": 396605694,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1,
      "link": null,
      "locked": false,
      "text": "raw/\n원본 문서·노트",
      "originalText": "raw/\n원본 문서·노트",
      "fontSize": 16,
      "fontFamily": 1,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "raw-docs",
      "lineHeight": 1.25,
      "autoResize": true
    },
    {
      "id": "raw-assets",
      "type": "rectangle",
      "x": 80.0,
      "y": 392.4,
      "width": 166.7,
      "height": 64.0,
      "angle": 0,
      "strokeColor": "#1971c2",
      "backgroundColor": "#d0ebff",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 3
      },
      "seed": 448967885,
      "version": 1,
      "versionNonce": 448967886,
      "isDeleted": false,
      "boundElements": [
        {
          "id": "raw-assets-text",
          "type": "text"
        },
        {
          "id": "edge-1-raw-assets-to-op-ingest",
          "type": "arrow"
        }
      ],
      "updated": 1,
      "link": "[[llm-wiki-workflow]]",
      "locked": false
    },
    {
      "id": "raw-assets-text",
      "type": "text",
      "x": 94.0,
      "y": 404.4,
      "width": 138.7,
      "height": 40.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 1120704731,
      "version": 1,
      "versionNonce": 1120704732,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1,
      "link": null,
      "locked": false,
      "text": "raw/assets/\n로컬 첨부 이미지",
      "originalText": "raw/assets/\n로컬 첨부 이미지",
      "fontSize": 16,
      "fontFamily": 1,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "raw-assets",
      "lineHeight": 1.25,
      "autoResize": true
    },
    {
      "id": "op-ingest",
      "type": "diamond",
      "x": 356.7,
      "y": 323.2,
      "width": 260.8,
      "height": 86.4,
      "angle": 0,
      "strokeColor": "#c2255c",
      "backgroundColor": "#ffdeeb",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 1434934729,
      "version": 1,
      "versionNonce": 1434934730,
      "isDeleted": false,
      "boundElements": [
        {
          "id": "op-ingest-text",
          "type": "text"
        },
        {
          "id": "edge-0-raw-docs-to-op-ingest",
          "type": "arrow"
        },
        {
          "id": "edge-1-raw-assets-to-op-ingest",
          "type": "arrow"
        },
        {
          "id": "edge-2-op-ingest-to-wiki-pages",
          "type": "arrow"
        },
        {
          "id": "edge-3-op-ingest-to-wiki-exc",
          "type": "arrow"
        }
      ],
      "updated": 1,
      "link": "[[llm-wiki-workflow]]",
      "locked": false
    },
    {
      "id": "op-ingest-text",
      "type": "text",
      "x": 404.5,
      "y": 346.4,
      "width": 165.2,
      "height": 40.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 495660106,
      "version": 1,
      "versionNonce": 495660107,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1,
      "link": null,
      "locked": false,
      "text": "Ingest\n요약·통합·모순 감지",
      "originalText": "Ingest\n요약·통합·모순 감지",
      "fontSize": 16,
      "fontFamily": 1,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "op-ingest",
      "lineHeight": 1.25,
      "autoResize": true
    },
    {
      "id": "op-query",
      "type": "diamond",
      "x": 1022.9,
      "y": 80.0,
      "width": 260.8,
      "height": 86.4,
      "angle": 0,
      "strokeColor": "#c2255c",
      "backgroundColor": "#ffdeeb",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 1496115532,
      "version": 1,
      "versionNonce": 1496115533,
      "isDeleted": false,
      "boundElements": [
        {
          "id": "op-query-text",
          "type": "text"
        },
        {
          "id": "edge-4-wiki-pages-to-op-query",
          "type": "arrow"
        },
        {
          "id": "edge-5-op-query-to-wiki-pages",
          "type": "arrow"
        }
      ],
      "updated": 1,
      "link": "[[llm-wiki-workflow]]",
      "locked": false
    },
    {
      "id": "op-query-text",
      "type": "text",
      "x": 1070.7,
      "y": 103.2,
      "width": 165.2,
      "height": 40.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 4571724,
      "version": 1,
      "versionNonce": 4571725,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1,
      "link": null,
      "locked": false,
      "text": "Query\n색인 탐색·질의 응답",
      "originalText": "Query\n색인 탐색·질의 응답",
      "fontSize": 16,
      "fontFamily": 1,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "op-query",
      "lineHeight": 1.25,
      "autoResize": true
    },
    {
      "id": "op-lint",
      "type": "diamond",
      "x": 1022.9,
      "y": 218.4,
      "width": 260.8,
      "height": 86.4,
      "angle": 0,
      "strokeColor": "#c2255c",
      "backgroundColor": "#ffdeeb",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 1208045087,
      "version": 1,
      "versionNonce": 1208045088,
      "isDeleted": false,
      "boundElements": [
        {
          "id": "op-lint-text",
          "type": "text"
        },
        {
          "id": "edge-6-wiki-pages-to-op-lint",
          "type": "arrow"
        }
      ],
      "updated": 1,
      "link": "[[llm-wiki-workflow]]",
      "locked": false
    },
    {
      "id": "op-lint-text",
      "type": "text",
      "x": 1070.7,
      "y": 241.6,
      "width": 165.2,
      "height": 40.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 2026229157,
      "version": 1,
      "versionNonce": 2026229158,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1,
      "link": null,
      "locked": false,
      "text": "Lint\n링크·고아·모순 점검",
      "originalText": "Lint\n링크·고아·모순 점검",
      "fontSize": 16,
      "fontFamily": 1,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "op-lint",
      "lineHeight": 1.25,
      "autoResize": true
    },
    {
      "id": "wiki-pages",
      "type": "rectangle",
      "x": 1004.7,
      "y": 356.8,
      "width": 297.1,
      "height": 64.0,
      "angle": 0,
      "strokeColor": "#2f9e44",
      "backgroundColor": "#d3f9d8",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 3
      },
      "seed": 1226076212,
      "version": 1,
      "versionNonce": 1226076213,
      "isDeleted": false,
      "boundElements": [
        {
          "id": "wiki-pages-text",
          "type": "text"
        },
        {
          "id": "edge-2-op-ingest-to-wiki-pages",
          "type": "arrow"
        },
        {
          "id": "edge-4-wiki-pages-to-op-query",
          "type": "arrow"
        },
        {
          "id": "edge-5-op-query-to-wiki-pages",
          "type": "arrow"
        },
        {
          "id": "edge-6-wiki-pages-to-op-lint",
          "type": "arrow"
        },
        {
          "id": "edge-7-wiki-pages-to-wiki-meta",
          "type": "arrow"
        }
      ],
      "updated": 1,
      "link": "[[overview]]",
      "locked": false
    },
    {
      "id": "wiki-pages-text",
      "type": "text",
      "x": 1018.7,
      "y": 368.8,
      "width": 269.1,
      "height": 40.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 1763008787,
      "version": 1,
      "versionNonce": 1763008788,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1,
      "link": null,
      "locked": false,
      "text": "wiki/\nsources · entities · concepts",
      "originalText": "wiki/\nsources · entities · concepts",
      "fontSize": 16,
      "fontFamily": 1,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "wiki-pages",
      "lineHeight": 1.25,
      "autoResize": true
    },
    {
      "id": "wiki-exc",
      "type": "rectangle",
      "x": 727.5,
      "y": 334.4,
      "width": 167.2,
      "height": 64.0,
      "angle": 0,
      "strokeColor": "#e8590c",
      "backgroundColor": "#ffe8cc",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 3
      },
      "seed": 76618056,
      "version": 1,
      "versionNonce": 76618057,
      "isDeleted": false,
      "boundElements": [
        {
          "id": "wiki-exc-text",
          "type": "text"
        },
        {
          "id": "edge-3-op-ingest-to-wiki-exc",
          "type": "arrow"
        },
        {
          "id": "edge-8-wiki-exc-to-obsidian",
          "type": "arrow"
        }
      ],
      "updated": 1,
      "link": "[[agents-config-architecture.excalidraw]]",
      "locked": false
    },
    {
      "id": "wiki-exc-text",
      "type": "text",
      "x": 741.5,
      "y": 346.4,
      "width": 139.2,
      "height": 40.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 985919485,
      "version": 1,
      "versionNonce": 985919486,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1,
      "link": null,
      "locked": false,
      "text": "wiki/visuals/\n*.excalidraw.md",
      "originalText": "wiki/visuals/\n*.excalidraw.md",
      "fontSize": 16,
      "fontFamily": 1,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "wiki-exc",
      "lineHeight": 1.25,
      "autoResize": true
    },
    {
      "id": "wiki-meta",
      "type": "rectangle",
      "x": 1043.5,
      "y": 472.8,
      "width": 219.6,
      "height": 64.0,
      "angle": 0,
      "strokeColor": "#6741d9",
      "backgroundColor": "#e5dbff",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 3
      },
      "seed": 1422026548,
      "version": 1,
      "versionNonce": 1422026549,
      "isDeleted": false,
      "boundElements": [
        {
          "id": "wiki-meta-text",
          "type": "text"
        },
        {
          "id": "edge-7-wiki-pages-to-wiki-meta",
          "type": "arrow"
        },
        {
          "id": "edge-9-wiki-meta-to-obsidian",
          "type": "arrow"
        }
      ],
      "updated": 1,
      "link": "[[index]]",
      "locked": false
    },
    {
      "id": "wiki-meta-text",
      "type": "text",
      "x": 1057.5,
      "y": 484.8,
      "width": 191.6,
      "height": 40.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 1387473835,
      "version": 1,
      "versionNonce": 1387473836,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1,
      "link": null,
      "locked": false,
      "text": "index.md & log.md\n카탈로그 · 연대기 로그",
      "originalText": "index.md & log.md\n카탈로그 · 연대기 로그",
      "fontSize": 16,
      "fontFamily": 1,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "wiki-meta",
      "lineHeight": 1.25,
      "autoResize": true
    },
    {
      "id": "obsidian",
      "type": "rectangle",
      "x": 1004.7,
      "y": 588.8,
      "width": 297.1,
      "height": 64.0,
      "angle": 0,
      "strokeColor": "#0c8599",
      "backgroundColor": "#c5f6fa",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 3
      },
      "seed": 1291508900,
      "version": 1,
      "versionNonce": 1291508901,
      "isDeleted": false,
      "boundElements": [
        {
          "id": "obsidian-text",
          "type": "text"
        },
        {
          "id": "edge-8-wiki-exc-to-obsidian",
          "type": "arrow"
        },
        {
          "id": "edge-9-wiki-meta-to-obsidian",
          "type": "arrow"
        }
      ],
      "updated": 1,
      "link": "[[overview]]",
      "locked": false
    },
    {
      "id": "obsidian-text",
      "type": "text",
      "x": 1018.7,
      "y": 600.8,
      "width": 269.1,
      "height": 40.0,
      "angle": 0,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 1512468764,
      "version": 1,
      "versionNonce": 1512468765,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1,
      "link": null,
      "locked": false,
      "text": "Obsidian\nGraph · Excalidraw · Dataview",
      "originalText": "Obsidian\nGraph · Excalidraw · Dataview",
      "fontSize": 16,
      "fontFamily": 1,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "obsidian",
      "lineHeight": 1.25,
      "autoResize": true
    },
    {
      "id": "edge-0-raw-docs-to-op-ingest",
      "type": "arrow",
      "x": 243.3,
      "y": 308.4,
      "width": 113.3,
      "height": 58.0,
      "angle": 0,
      "strokeColor": "#495057",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 695837521,
      "version": 1,
      "versionNonce": 695837522,
      "isDeleted": false,
      "boundElements": [
        {
          "id": "edge-0-raw-docs-to-op-ingest-label",
          "type": "text"
        }
      ],
      "updated": 1,
      "link": null,
      "locked": false,
      "points": [
        [
          0,
          0
        ],
        [
          113.3,
          58.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "raw-docs",
        "focus": 0,
        "gap": 4
      },
      "endBinding": {
        "elementId": "op-ingest",
        "focus": 0,
        "gap": 4
      },
      "startArrowhead": null,
      "endArrowhead": "arrow",
      "elbowed": false
    },
    {
      "id": "edge-0-raw-docs-to-op-ingest-label",
      "type": "text",
      "x": 280.0,
      "y": 328.6,
      "width": 40.0,
      "height": 17.5,
      "angle": 0,
      "strokeColor": "#343a40",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 1490513783,
      "version": 1,
      "versionNonce": 1490513784,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1,
      "link": null,
      "locked": false,
      "text": "read",
      "originalText": "read",
      "fontSize": 14,
      "fontFamily": 1,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "edge-0-raw-docs-to-op-ingest",
      "lineHeight": 1.25,
      "autoResize": true
    },
    {
      "id": "edge-1-raw-assets-to-op-ingest",
      "type": "arrow",
      "x": 246.7,
      "y": 424.4,
      "width": 110.0,
      "height": 58.0,
      "angle": 0,
      "strokeColor": "#495057",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 679664291,
      "version": 1,
      "versionNonce": 679664292,
      "isDeleted": false,
      "boundElements": [
        {
          "id": "edge-1-raw-assets-to-op-ingest-label",
          "type": "text"
        }
      ],
      "updated": 1,
      "link": null,
      "locked": false,
      "points": [
        [
          0,
          0
        ],
        [
          110.0,
          -58.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "raw-assets",
        "focus": 0,
        "gap": 4
      },
      "endBinding": {
        "elementId": "op-ingest",
        "focus": 0,
        "gap": 4
      },
      "startArrowhead": null,
      "endArrowhead": "arrow",
      "elbowed": false
    },
    {
      "id": "edge-1-raw-assets-to-op-ingest-label",
      "type": "text",
      "x": 277.3,
      "y": 386.6,
      "width": 48.7,
      "height": 17.5,
      "angle": 0,
      "strokeColor": "#343a40",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 619359820,
      "version": 1,
      "versionNonce": 619359821,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1,
      "link": null,
      "locked": false,
      "text": "vision",
      "originalText": "vision",
      "fontSize": 14,
      "fontFamily": 1,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "edge-1-raw-assets-to-op-ingest",
      "lineHeight": 1.25,
      "autoResize": true
    },
    {
      "id": "edge-2-op-ingest-to-wiki-pages",
      "type": "arrow",
      "x": 617.5,
      "y": 366.4,
      "width": 387.2,
      "height": 22.4,
      "angle": 0,
      "strokeColor": "#495057",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 1839671233,
      "version": 1,
      "versionNonce": 1839671234,
      "isDeleted": false,
      "boundElements": [
        {
          "id": "edge-2-op-ingest-to-wiki-pages-label",
          "type": "text"
        }
      ],
      "updated": 1,
      "link": null,
      "locked": false,
      "points": [
        [
          0,
          0
        ],
        [
          387.2,
          22.4
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "op-ingest",
        "focus": 0,
        "gap": 4
      },
      "endBinding": {
        "elementId": "wiki-pages",
        "focus": 0,
        "gap": 4
      },
      "startArrowhead": null,
      "endArrowhead": "arrow",
      "elbowed": false
    },
    {
      "id": "edge-2-op-ingest-to-wiki-pages-label",
      "type": "text",
      "x": 762.4,
      "y": 368.8,
      "width": 97.4,
      "height": 17.5,
      "angle": 0,
      "strokeColor": "#343a40",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 818906322,
      "version": 1,
      "versionNonce": 818906323,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1,
      "link": null,
      "locked": false,
      "text": "write/update",
      "originalText": "write/update",
      "fontSize": 14,
      "fontFamily": 1,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "edge-2-op-ingest-to-wiki-pages",
      "lineHeight": 1.25,
      "autoResize": true
    },
    {
      "id": "edge-3-op-ingest-to-wiki-exc",
      "type": "arrow",
      "x": 617.5,
      "y": 366.4,
      "width": 110.0,
      "height": 0.0,
      "angle": 0,
      "strokeColor": "#495057",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 1365330640,
      "version": 1,
      "versionNonce": 1365330641,
      "isDeleted": false,
      "boundElements": [
        {
          "id": "edge-3-op-ingest-to-wiki-exc-label",
          "type": "text"
        }
      ],
      "updated": 1,
      "link": null,
      "locked": false,
      "points": [
        [
          0,
          0
        ],
        [
          110.0,
          0.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "op-ingest",
        "focus": 0,
        "gap": 4
      },
      "endBinding": {
        "elementId": "wiki-exc",
        "focus": 0,
        "gap": 4
      },
      "startArrowhead": null,
      "endArrowhead": "arrow",
      "elbowed": false
    },
    {
      "id": "edge-3-op-ingest-to-wiki-exc-label",
      "type": "text",
      "x": 603.5,
      "y": 357.6,
      "width": 138.0,
      "height": 17.5,
      "angle": 0,
      "strokeColor": "#343a40",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 1062810455,
      "version": 1,
      "versionNonce": 1062810456,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1,
      "link": null,
      "locked": false,
      "text": "excalidraw_gen.py",
      "originalText": "excalidraw_gen.py",
      "fontSize": 14,
      "fontFamily": 1,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "edge-3-op-ingest-to-wiki-exc",
      "lineHeight": 1.25,
      "autoResize": true
    },
    {
      "id": "edge-4-wiki-pages-to-op-query",
      "type": "arrow",
      "x": 1153.2,
      "y": 356.8,
      "width": 0.0,
      "height": 190.4,
      "angle": 0,
      "strokeColor": "#495057",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 1757982212,
      "version": 1,
      "versionNonce": 1757982213,
      "isDeleted": false,
      "boundElements": [
        {
          "id": "edge-4-wiki-pages-to-op-query-label",
          "type": "text"
        }
      ],
      "updated": 1,
      "link": null,
      "locked": false,
      "points": [
        [
          0,
          0
        ],
        [
          0.0,
          -190.4
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "wiki-pages",
        "focus": 0,
        "gap": 4
      },
      "endBinding": {
        "elementId": "op-query",
        "focus": 0,
        "gap": 4
      },
      "startArrowhead": null,
      "endArrowhead": "arrow",
      "elbowed": false
    },
    {
      "id": "edge-4-wiki-pages-to-op-query-label",
      "type": "text",
      "x": 1133.2,
      "y": 252.9,
      "width": 40.0,
      "height": 17.5,
      "angle": 0,
      "strokeColor": "#343a40",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 2127241111,
      "version": 1,
      "versionNonce": 2127241112,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1,
      "link": null,
      "locked": false,
      "text": "read",
      "originalText": "read",
      "fontSize": 14,
      "fontFamily": 1,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "edge-4-wiki-pages-to-op-query",
      "lineHeight": 1.25,
      "autoResize": true
    },
    {
      "id": "edge-5-op-query-to-wiki-pages",
      "type": "arrow",
      "x": 1153.2,
      "y": 166.4,
      "width": 0.0,
      "height": 190.4,
      "angle": 0,
      "strokeColor": "#495057",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "dashed",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 808054722,
      "version": 1,
      "versionNonce": 808054723,
      "isDeleted": false,
      "boundElements": [
        {
          "id": "edge-5-op-query-to-wiki-pages-label",
          "type": "text"
        }
      ],
      "updated": 1,
      "link": null,
      "locked": false,
      "points": [
        [
          0,
          0
        ],
        [
          0.0,
          190.4
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "op-query",
        "focus": 0,
        "gap": 4
      },
      "endBinding": {
        "elementId": "wiki-pages",
        "focus": 0,
        "gap": 4
      },
      "startArrowhead": null,
      "endArrowhead": "arrow",
      "elbowed": false
    },
    {
      "id": "edge-5-op-query-to-wiki-pages-label",
      "type": "text",
      "x": 1116.7,
      "y": 252.9,
      "width": 73.1,
      "height": 17.5,
      "angle": 0,
      "strokeColor": "#343a40",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 706843398,
      "version": 1,
      "versionNonce": 706843399,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1,
      "link": null,
      "locked": false,
      "text": "file-back",
      "originalText": "file-back",
      "fontSize": 14,
      "fontFamily": 1,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "edge-5-op-query-to-wiki-pages",
      "lineHeight": 1.25,
      "autoResize": true
    },
    {
      "id": "edge-6-wiki-pages-to-op-lint",
      "type": "arrow",
      "x": 1153.2,
      "y": 356.8,
      "width": 0.0,
      "height": 52.0,
      "angle": 0,
      "strokeColor": "#495057",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 1245311437,
      "version": 1,
      "versionNonce": 1245311438,
      "isDeleted": false,
      "boundElements": [
        {
          "id": "edge-6-wiki-pages-to-op-lint-label",
          "type": "text"
        }
      ],
      "updated": 1,
      "link": null,
      "locked": false,
      "points": [
        [
          0,
          0
        ],
        [
          0.0,
          -52.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "wiki-pages",
        "focus": 0,
        "gap": 4
      },
      "endBinding": {
        "elementId": "op-lint",
        "focus": 0,
        "gap": 4
      },
      "startArrowhead": null,
      "endArrowhead": "arrow",
      "elbowed": false
    },
    {
      "id": "edge-6-wiki-pages-to-op-lint-label",
      "type": "text",
      "x": 1084.2,
      "y": 322.1,
      "width": 138.0,
      "height": 17.5,
      "angle": 0,
      "strokeColor": "#343a40",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 556075170,
      "version": 1,
      "versionNonce": 556075171,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1,
      "link": null,
      "locked": false,
      "text": "wiki_tool.py lint",
      "originalText": "wiki_tool.py lint",
      "fontSize": 14,
      "fontFamily": 1,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "edge-6-wiki-pages-to-op-lint",
      "lineHeight": 1.25,
      "autoResize": true
    },
    {
      "id": "edge-7-wiki-pages-to-wiki-meta",
      "type": "arrow",
      "x": 1153.2,
      "y": 420.8,
      "width": 0.0,
      "height": 52.0,
      "angle": 0,
      "strokeColor": "#495057",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 429522054,
      "version": 1,
      "versionNonce": 429522055,
      "isDeleted": false,
      "boundElements": [
        {
          "id": "edge-7-wiki-pages-to-wiki-meta-label",
          "type": "text"
        }
      ],
      "updated": 1,
      "link": null,
      "locked": false,
      "points": [
        [
          0,
          0
        ],
        [
          0.0,
          52.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "wiki-pages",
        "focus": 0,
        "gap": 4
      },
      "endBinding": {
        "elementId": "wiki-meta",
        "focus": 0,
        "gap": 4
      },
      "startArrowhead": null,
      "endArrowhead": "arrow",
      "elbowed": false
    },
    {
      "id": "edge-7-wiki-pages-to-wiki-meta-label",
      "type": "text",
      "x": 1124.8,
      "y": 438.1,
      "width": 56.8,
      "height": 17.5,
      "angle": 0,
      "strokeColor": "#343a40",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 860227033,
      "version": 1,
      "versionNonce": 860227034,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1,
      "link": null,
      "locked": false,
      "text": "catalog",
      "originalText": "catalog",
      "fontSize": 14,
      "fontFamily": 1,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "edge-7-wiki-pages-to-wiki-meta",
      "lineHeight": 1.25,
      "autoResize": true
    },
    {
      "id": "edge-8-wiki-exc-to-obsidian",
      "type": "arrow",
      "x": 894.7,
      "y": 366.4,
      "width": 110.0,
      "height": 254.4,
      "angle": 0,
      "strokeColor": "#495057",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 91721763,
      "version": 1,
      "versionNonce": 91721764,
      "isDeleted": false,
      "boundElements": [
        {
          "id": "edge-8-wiki-exc-to-obsidian-label",
          "type": "text"
        }
      ],
      "updated": 1,
      "link": null,
      "locked": false,
      "points": [
        [
          0,
          0
        ],
        [
          110.0,
          254.4
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "wiki-exc",
        "focus": 0,
        "gap": 4
      },
      "endBinding": {
        "elementId": "obsidian",
        "focus": 0,
        "gap": 4
      },
      "startArrowhead": null,
      "endArrowhead": "arrow",
      "elbowed": false
    },
    {
      "id": "edge-8-wiki-exc-to-obsidian-label",
      "type": "text",
      "x": 925.4,
      "y": 484.8,
      "width": 48.7,
      "height": 17.5,
      "angle": 0,
      "strokeColor": "#343a40",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 1208079070,
      "version": 1,
      "versionNonce": 1208079071,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1,
      "link": null,
      "locked": false,
      "text": "render",
      "originalText": "render",
      "fontSize": 14,
      "fontFamily": 1,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "edge-8-wiki-exc-to-obsidian",
      "lineHeight": 1.25,
      "autoResize": true
    },
    {
      "id": "edge-9-wiki-meta-to-obsidian",
      "type": "arrow",
      "x": 1153.2,
      "y": 536.8,
      "width": 0.0,
      "height": 52.0,
      "angle": 0,
      "strokeColor": "#495057",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": {
        "type": 2
      },
      "seed": 1679269570,
      "version": 1,
      "versionNonce": 1679269571,
      "isDeleted": false,
      "boundElements": [
        {
          "id": "edge-9-wiki-meta-to-obsidian-label",
          "type": "text"
        }
      ],
      "updated": 1,
      "link": null,
      "locked": false,
      "points": [
        [
          0,
          0
        ],
        [
          0.0,
          52.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "wiki-meta",
        "focus": 0,
        "gap": 4
      },
      "endBinding": {
        "elementId": "obsidian",
        "focus": 0,
        "gap": 4
      },
      "startArrowhead": null,
      "endArrowhead": "arrow",
      "elbowed": false
    },
    {
      "id": "edge-9-wiki-meta-to-obsidian-label",
      "type": "text",
      "x": 1128.9,
      "y": 554.0,
      "width": 48.7,
      "height": 17.5,
      "angle": 0,
      "strokeColor": "#343a40",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 366105477,
      "version": 1,
      "versionNonce": 366105478,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1,
      "link": null,
      "locked": false,
      "text": "browse",
      "originalText": "browse",
      "fontSize": 14,
      "fontFamily": 1,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "edge-9-wiki-meta-to-obsidian",
      "lineHeight": 1.25,
      "autoResize": true
    }
  ],
  "appState": {
    "gridSize": 20,
    "viewBackgroundColor": "#ffffff"
  },
  "files": {}
}
```
%%
