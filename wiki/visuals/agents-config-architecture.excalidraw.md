---
id: agents-config-architecture
type: excalidraw
excalidraw-plugin: parsed
tags:
  - excalidraw
  - architecture
  - ssot
  - agents-config
created: 2026-11-24
updated: 2026-11-24
sources:
  - "[[overview]]"
  - "[[three-vendor-ssot]]"
  - "[[lifecycle-hooks]]"
---
==⚠ Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠==

# Excalidraw Data
## Text Elements
Single Source of Truth (shared/) ^grp-title-ssot

Sync & Deploy ^grp-title-deploy

Vendor Targets ^grp-title-vendors

Runtime Guards & Formatters ^grp-title-runtime

INSTRUCTIONS.md
rules/ · agents/ (13) ^shared-core-text

skills/
graphify · llm-wiki ^shared-skills-text

shared/mcp.json ^shared-mcp-text

shared/hooks/hook.py ^shared-hook-text

sync_mcp.py ^sync-mcp-text

install.sh
(Bash 3.2+) ^install-sh-text

Claude Code
~/.claude + ~/.claude.json ^claude-text

Gemini / AGY
~/.gemini ^gemini-text

Codex CLI
~/.codex ^codex-text

PreToolUse
보안 가드 · 시크릿 차단 ^pre-tool-text

PostToolUse
agents-config-formatter
(.excalidraw.md 제외) ^post-tool-text

symlink ^edge-0-shared-core-to-install-sh-label

sync ^edge-1-shared-skills-to-install-sh-label

canonical ^edge-2-shared-mcp-to-sync-mcp-label

invoke ^edge-3-sync-mcp-to-install-sh-label

link ^edge-4-install-sh-to-claude-label

link ^edge-5-install-sh-to-gemini-label

link ^edge-6-install-sh-to-codex-label

guard ^edge-7-shared-hook-to-pre-tool-label

format ^edge-8-shared-hook-to-post-tool-label

## Element Links
^shared-core: [[three-vendor-ssot]]
^shared-skills: [[llm-wiki-workflow]]
^shared-mcp: [[three-vendor-ssot]]
^shared-hook: [[lifecycle-hooks]]
^sync-mcp: [[three-vendor-ssot]]
^install-sh: [[three-vendor-ssot]]
^claude: [[three-vendor-ssot]]
^gemini: [[three-vendor-ssot]]
^codex: [[three-vendor-ssot]]
^pre-tool: [[lifecycle-hooks]]
^post-tool: [[lifecycle-hooks]]

%%
## Drawing
```json
{
  "type": "excalidraw",
  "version": 2,
  "source": "https://excalidraw.com",
  "elements": [
    {
      "id": "grp-ssot",
      "type": "rectangle",
      "x": 56.0,
      "y": 36.0,
      "width": 270.9,
      "height": 480.0,
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
      "seed": 1824017036,
      "version": 1,
      "versionNonce": 1824017037,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "id": "grp-title-ssot",
      "type": "text",
      "x": 68.0,
      "y": 46.0,
      "width": 259.8,
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
      "seed": 460788554,
      "version": 1,
      "versionNonce": 460788555,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1,
      "link": null,
      "locked": false,
      "text": "Single Source of Truth (shared/)",
      "originalText": "Single Source of Truth (shared/)",
      "fontSize": 14,
      "fontFamily": 1,
      "textAlign": "left",
      "verticalAlign": "top",
      "containerId": null,
      "lineHeight": 1.25,
      "autoResize": true
    },
    {
      "id": "grp-deploy",
      "type": "rectangle",
      "x": 429.6,
      "y": 86.0,
      "width": 518.7,
      "height": 256.0,
      "angle": 0,
      "strokeColor": "#0c8599",
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
      "seed": 791137466,
      "version": 1,
      "versionNonce": 791137467,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "id": "grp-title-deploy",
      "type": "text",
      "x": 441.6,
      "y": 96.0,
      "width": 105.6,
      "height": 17.5,
      "angle": 0,
      "strokeColor": "#0c8599",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 1146939371,
      "version": 1,
      "versionNonce": 1146939372,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1,
      "link": null,
      "locked": false,
      "text": "Sync & Deploy",
      "originalText": "Sync & Deploy",
      "fontSize": 14,
      "fontFamily": 1,
      "textAlign": "left",
      "verticalAlign": "top",
      "containerId": null,
      "lineHeight": 1.25,
      "autoResize": true
    },
    {
      "id": "grp-vendors",
      "type": "rectangle",
      "x": 1010.3,
      "y": 94.0,
      "width": 317.3,
      "height": 364.0,
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
      "seed": 541963984,
      "version": 1,
      "versionNonce": 541963985,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "id": "grp-title-vendors",
      "type": "text",
      "x": 1022.3,
      "y": 104.0,
      "width": 113.7,
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
      "seed": 1388629419,
      "version": 1,
      "versionNonce": 1388629420,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1,
      "link": null,
      "locked": false,
      "text": "Vendor Targets",
      "originalText": "Vendor Targets",
      "fontSize": 14,
      "fontFamily": 1,
      "textAlign": "left",
      "verticalAlign": "top",
      "containerId": null,
      "lineHeight": 1.25,
      "autoResize": true
    },
    {
      "id": "grp-runtime",
      "type": "rectangle",
      "x": 388.9,
      "y": 202.0,
      "width": 289.4,
      "height": 264.0,
      "angle": 0,
      "strokeColor": "#c92a2a",
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
      "seed": 986579110,
      "version": 1,
      "versionNonce": 986579111,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1,
      "link": null,
      "locked": false
    },
    {
      "id": "grp-title-runtime",
      "type": "text",
      "x": 400.9,
      "y": 212.0,
      "width": 219.2,
      "height": 17.5,
      "angle": 0,
      "strokeColor": "#c92a2a",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "groupIds": [],
      "frameId": null,
      "roundness": null,
      "seed": 1212644289,
      "version": 1,
      "versionNonce": 1212644290,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1,
      "link": null,
      "locked": false,
      "text": "Runtime Guards & Formatters",
      "originalText": "Runtime Guards & Formatters",
      "fontSize": 14,
      "fontFamily": 1,
      "textAlign": "left",
      "verticalAlign": "top",
      "containerId": null,
      "lineHeight": 1.25,
      "autoResize": true
    },
    {
      "id": "shared-core",
      "type": "rectangle",
      "x": 80.0,
      "y": 80.0,
      "width": 222.9,
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
      "seed": 1382636921,
      "version": 1,
      "versionNonce": 1382636922,
      "isDeleted": false,
      "boundElements": [
        {
          "id": "shared-core-text",
          "type": "text"
        },
        {
          "id": "edge-0-shared-core-to-install-sh",
          "type": "arrow"
        }
      ],
      "updated": 1,
      "link": "[[three-vendor-ssot]]",
      "locked": false
    },
    {
      "id": "shared-core-text",
      "type": "text",
      "x": 94.0,
      "y": 92.0,
      "width": 194.9,
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
      "seed": 1525864316,
      "version": 1,
      "versionNonce": 1525864317,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1,
      "link": null,
      "locked": false,
      "text": "INSTRUCTIONS.md\nrules/ · agents/ (13)",
      "originalText": "INSTRUCTIONS.md\nrules/ · agents/ (13)",
      "fontSize": 16,
      "fontFamily": 1,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "shared-core",
      "lineHeight": 1.25,
      "autoResize": true
    },
    {
      "id": "shared-skills",
      "type": "rectangle",
      "x": 89.3,
      "y": 196.0,
      "width": 204.3,
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
      "seed": 1295963463,
      "version": 1,
      "versionNonce": 1295963464,
      "isDeleted": false,
      "boundElements": [
        {
          "id": "shared-skills-text",
          "type": "text"
        },
        {
          "id": "edge-1-shared-skills-to-install-sh",
          "type": "arrow"
        }
      ],
      "updated": 1,
      "link": "[[llm-wiki-workflow]]",
      "locked": false
    },
    {
      "id": "shared-skills-text",
      "type": "text",
      "x": 103.3,
      "y": 208.0,
      "width": 176.3,
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
      "seed": 1931796905,
      "version": 1,
      "versionNonce": 1931796906,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1,
      "link": null,
      "locked": false,
      "text": "skills/\ngraphify · llm-wiki",
      "originalText": "skills/\ngraphify · llm-wiki",
      "fontSize": 16,
      "fontFamily": 1,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "shared-skills",
      "lineHeight": 1.25,
      "autoResize": true
    },
    {
      "id": "shared-mcp",
      "type": "rectangle",
      "x": 107.9,
      "y": 312.0,
      "width": 167.2,
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
      "seed": 1190149595,
      "version": 1,
      "versionNonce": 1190149596,
      "isDeleted": false,
      "boundElements": [
        {
          "id": "shared-mcp-text",
          "type": "text"
        },
        {
          "id": "edge-2-shared-mcp-to-sync-mcp",
          "type": "arrow"
        }
      ],
      "updated": 1,
      "link": "[[three-vendor-ssot]]",
      "locked": false
    },
    {
      "id": "shared-mcp-text",
      "type": "text",
      "x": 121.9,
      "y": 334.0,
      "width": 139.2,
      "height": 20.0,
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
      "seed": 929020069,
      "version": 1,
      "versionNonce": 929020070,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1,
      "link": null,
      "locked": false,
      "text": "shared/mcp.json",
      "originalText": "shared/mcp.json",
      "fontSize": 16,
      "fontFamily": 1,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "shared-mcp",
      "lineHeight": 1.25,
      "autoResize": true
    },
    {
      "id": "shared-hook",
      "type": "rectangle",
      "x": 84.7,
      "y": 428.0,
      "width": 213.6,
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
      "seed": 498899811,
      "version": 1,
      "versionNonce": 498899812,
      "isDeleted": false,
      "boundElements": [
        {
          "id": "shared-hook-text",
          "type": "text"
        },
        {
          "id": "edge-7-shared-hook-to-pre-tool",
          "type": "arrow"
        },
        {
          "id": "edge-8-shared-hook-to-post-tool",
          "type": "arrow"
        }
      ],
      "updated": 1,
      "link": "[[lifecycle-hooks]]",
      "locked": false
    },
    {
      "id": "shared-hook-text",
      "type": "text",
      "x": 98.7,
      "y": 450.0,
      "width": 185.6,
      "height": 20.0,
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
      "seed": 1688524249,
      "version": 1,
      "versionNonce": 1688524250,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1,
      "link": null,
      "locked": false,
      "text": "shared/hooks/hook.py",
      "originalText": "shared/hooks/hook.py",
      "fontSize": 16,
      "fontFamily": 1,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "shared-hook",
      "lineHeight": 1.25,
      "autoResize": true
    },
    {
      "id": "sync-mcp",
      "type": "rectangle",
      "x": 453.6,
      "y": 130.0,
      "width": 160.0,
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
      "seed": 1591990686,
      "version": 1,
      "versionNonce": 1591990687,
      "isDeleted": false,
      "boundElements": [
        {
          "id": "sync-mcp-text",
          "type": "text"
        },
        {
          "id": "edge-2-shared-mcp-to-sync-mcp",
          "type": "arrow"
        },
        {
          "id": "edge-3-sync-mcp-to-install-sh",
          "type": "arrow"
        }
      ],
      "updated": 1,
      "link": "[[three-vendor-ssot]]",
      "locked": false
    },
    {
      "id": "sync-mcp-text",
      "type": "text",
      "x": 482.5,
      "y": 152.0,
      "width": 102.1,
      "height": 20.0,
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
      "seed": 594147242,
      "version": 1,
      "versionNonce": 594147243,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1,
      "link": null,
      "locked": false,
      "text": "sync_mcp.py",
      "originalText": "sync_mcp.py",
      "fontSize": 16,
      "fontFamily": 1,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "sync-mcp",
      "lineHeight": 1.25,
      "autoResize": true
    },
    {
      "id": "install-sh",
      "type": "rectangle",
      "x": 764.3,
      "y": 254.0,
      "width": 160.0,
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
      "seed": 2035640150,
      "version": 1,
      "versionNonce": 2035640151,
      "isDeleted": false,
      "boundElements": [
        {
          "id": "install-sh-text",
          "type": "text"
        },
        {
          "id": "edge-0-shared-core-to-install-sh",
          "type": "arrow"
        },
        {
          "id": "edge-1-shared-skills-to-install-sh",
          "type": "arrow"
        },
        {
          "id": "edge-3-sync-mcp-to-install-sh",
          "type": "arrow"
        },
        {
          "id": "edge-4-install-sh-to-claude",
          "type": "arrow"
        },
        {
          "id": "edge-5-install-sh-to-gemini",
          "type": "arrow"
        },
        {
          "id": "edge-6-install-sh-to-codex",
          "type": "arrow"
        }
      ],
      "updated": 1,
      "link": "[[three-vendor-ssot]]",
      "locked": false
    },
    {
      "id": "install-sh-text",
      "type": "text",
      "x": 793.2,
      "y": 266.0,
      "width": 102.1,
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
      "seed": 481779166,
      "version": 1,
      "versionNonce": 481779167,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1,
      "link": null,
      "locked": false,
      "text": "install.sh\n(Bash 3.2+)",
      "originalText": "install.sh\n(Bash 3.2+)",
      "fontSize": 16,
      "fontFamily": 1,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "install-sh",
      "lineHeight": 1.25,
      "autoResize": true
    },
    {
      "id": "claude",
      "type": "rectangle",
      "x": 1034.3,
      "y": 138.0,
      "width": 269.3,
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
      "seed": 243877811,
      "version": 1,
      "versionNonce": 243877812,
      "isDeleted": false,
      "boundElements": [
        {
          "id": "claude-text",
          "type": "text"
        },
        {
          "id": "edge-4-install-sh-to-claude",
          "type": "arrow"
        }
      ],
      "updated": 1,
      "link": "[[three-vendor-ssot]]",
      "locked": false
    },
    {
      "id": "claude-text",
      "type": "text",
      "x": 1048.3,
      "y": 150.0,
      "width": 241.3,
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
      "seed": 1117571658,
      "version": 1,
      "versionNonce": 1117571659,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1,
      "link": null,
      "locked": false,
      "text": "Claude Code\n~/.claude + ~/.claude.json",
      "originalText": "Claude Code\n~/.claude + ~/.claude.json",
      "fontSize": 16,
      "fontFamily": 1,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "claude",
      "lineHeight": 1.25,
      "autoResize": true
    },
    {
      "id": "gemini",
      "type": "rectangle",
      "x": 1089.0,
      "y": 254.0,
      "width": 160.0,
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
      "seed": 884680409,
      "version": 1,
      "versionNonce": 884680410,
      "isDeleted": false,
      "boundElements": [
        {
          "id": "gemini-text",
          "type": "text"
        },
        {
          "id": "edge-5-install-sh-to-gemini",
          "type": "arrow"
        }
      ],
      "updated": 1,
      "link": "[[three-vendor-ssot]]",
      "locked": false
    },
    {
      "id": "gemini-text",
      "type": "text",
      "x": 1113.2,
      "y": 266.0,
      "width": 111.4,
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
      "seed": 281205317,
      "version": 1,
      "versionNonce": 281205318,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1,
      "link": null,
      "locked": false,
      "text": "Gemini / AGY\n~/.gemini",
      "originalText": "Gemini / AGY\n~/.gemini",
      "fontSize": 16,
      "fontFamily": 1,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "gemini",
      "lineHeight": 1.25,
      "autoResize": true
    },
    {
      "id": "codex",
      "type": "rectangle",
      "x": 1089.0,
      "y": 370.0,
      "width": 160.0,
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
      "seed": 1920932038,
      "version": 1,
      "versionNonce": 1920932039,
      "isDeleted": false,
      "boundElements": [
        {
          "id": "codex-text",
          "type": "text"
        },
        {
          "id": "edge-6-install-sh-to-codex",
          "type": "arrow"
        }
      ],
      "updated": 1,
      "link": "[[three-vendor-ssot]]",
      "locked": false
    },
    {
      "id": "codex-text",
      "type": "text",
      "x": 1127.2,
      "y": 382.0,
      "width": 83.5,
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
      "seed": 322980018,
      "version": 1,
      "versionNonce": 322980019,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1,
      "link": null,
      "locked": false,
      "text": "Codex CLI\n~/.codex",
      "originalText": "Codex CLI\n~/.codex",
      "fontSize": 16,
      "fontFamily": 1,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "codex",
      "lineHeight": 1.25,
      "autoResize": true
    },
    {
      "id": "pre-tool",
      "type": "rectangle",
      "x": 419.1,
      "y": 246.0,
      "width": 228.9,
      "height": 64.0,
      "angle": 0,
      "strokeColor": "#c92a2a",
      "backgroundColor": "#ffe3e3",
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
      "seed": 1381636971,
      "version": 1,
      "versionNonce": 1381636972,
      "isDeleted": false,
      "boundElements": [
        {
          "id": "pre-tool-text",
          "type": "text"
        },
        {
          "id": "edge-7-shared-hook-to-pre-tool",
          "type": "arrow"
        }
      ],
      "updated": 1,
      "link": "[[lifecycle-hooks]]",
      "locked": false
    },
    {
      "id": "pre-tool-text",
      "type": "text",
      "x": 433.1,
      "y": 258.0,
      "width": 200.9,
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
      "seed": 1661196283,
      "version": 1,
      "versionNonce": 1661196284,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1,
      "link": null,
      "locked": false,
      "text": "PreToolUse\n보안 가드 · 시크릿 차단",
      "originalText": "PreToolUse\n보안 가드 · 시크릿 차단",
      "fontSize": 16,
      "fontFamily": 1,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "pre-tool",
      "lineHeight": 1.25,
      "autoResize": true
    },
    {
      "id": "post-tool",
      "type": "rectangle",
      "x": 412.9,
      "y": 362.0,
      "width": 241.4,
      "height": 80.0,
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
      "seed": 1790241398,
      "version": 1,
      "versionNonce": 1790241399,
      "isDeleted": false,
      "boundElements": [
        {
          "id": "post-tool-text",
          "type": "text"
        },
        {
          "id": "edge-8-shared-hook-to-post-tool",
          "type": "arrow"
        }
      ],
      "updated": 1,
      "link": "[[lifecycle-hooks]]",
      "locked": false
    },
    {
      "id": "post-tool-text",
      "type": "text",
      "x": 426.9,
      "y": 372.0,
      "width": 213.4,
      "height": 60.0,
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
      "seed": 805928818,
      "version": 1,
      "versionNonce": 805928819,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1,
      "link": null,
      "locked": false,
      "text": "PostToolUse\nagents-config-formatter\n(.excalidraw.md 제외)",
      "originalText": "PostToolUse\nagents-config-formatter\n(.excalidraw.md 제외)",
      "fontSize": 16,
      "fontFamily": 1,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "post-tool",
      "lineHeight": 1.25,
      "autoResize": true
    },
    {
      "id": "edge-0-shared-core-to-install-sh",
      "type": "arrow",
      "x": 302.9,
      "y": 112.0,
      "width": 461.4,
      "height": 174.0,
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
      "seed": 1125161066,
      "version": 1,
      "versionNonce": 1125161067,
      "isDeleted": false,
      "boundElements": [
        {
          "id": "edge-0-shared-core-to-install-sh-label",
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
          461.4,
          174.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "shared-core",
        "focus": 0,
        "gap": 4
      },
      "endBinding": {
        "elementId": "install-sh",
        "focus": 0,
        "gap": 4
      },
      "startArrowhead": null,
      "endArrowhead": "arrow",
      "elbowed": false
    },
    {
      "id": "edge-0-shared-core-to-install-sh-label",
      "type": "text",
      "x": 505.2,
      "y": 190.2,
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
      "seed": 1325948284,
      "version": 1,
      "versionNonce": 1325948285,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1,
      "link": null,
      "locked": false,
      "text": "symlink",
      "originalText": "symlink",
      "fontSize": 14,
      "fontFamily": 1,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "edge-0-shared-core-to-install-sh",
      "lineHeight": 1.25,
      "autoResize": true
    },
    {
      "id": "edge-1-shared-skills-to-install-sh",
      "type": "arrow",
      "x": 293.6,
      "y": 228.0,
      "width": 470.7,
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
      "seed": 1166140975,
      "version": 1,
      "versionNonce": 1166140976,
      "isDeleted": false,
      "boundElements": [
        {
          "id": "edge-1-shared-skills-to-install-sh-label",
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
          470.7,
          58.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "shared-skills",
        "focus": 0,
        "gap": 4
      },
      "endBinding": {
        "elementId": "install-sh",
        "focus": 0,
        "gap": 4
      },
      "startArrowhead": null,
      "endArrowhead": "arrow",
      "elbowed": false
    },
    {
      "id": "edge-1-shared-skills-to-install-sh-label",
      "type": "text",
      "x": 509.0,
      "y": 248.2,
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
      "seed": 449233779,
      "version": 1,
      "versionNonce": 449233780,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1,
      "link": null,
      "locked": false,
      "text": "sync",
      "originalText": "sync",
      "fontSize": 14,
      "fontFamily": 1,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "edge-1-shared-skills-to-install-sh",
      "lineHeight": 1.25,
      "autoResize": true
    },
    {
      "id": "edge-2-shared-mcp-to-sync-mcp",
      "type": "arrow",
      "x": 275.1,
      "y": 344.0,
      "width": 178.5,
      "height": 182.0,
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
      "seed": 272614274,
      "version": 1,
      "versionNonce": 272614275,
      "isDeleted": false,
      "boundElements": [
        {
          "id": "edge-2-shared-mcp-to-sync-mcp-label",
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
          178.5,
          -182.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "shared-mcp",
        "focus": 0,
        "gap": 4
      },
      "endBinding": {
        "elementId": "sync-mcp",
        "focus": 0,
        "gap": 4
      },
      "startArrowhead": null,
      "endArrowhead": "arrow",
      "elbowed": false
    },
    {
      "id": "edge-2-shared-mcp-to-sync-mcp-label",
      "type": "text",
      "x": 327.8,
      "y": 244.2,
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
      "seed": 1819743696,
      "version": 1,
      "versionNonce": 1819743697,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1,
      "link": null,
      "locked": false,
      "text": "canonical",
      "originalText": "canonical",
      "fontSize": 14,
      "fontFamily": 1,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "edge-2-shared-mcp-to-sync-mcp",
      "lineHeight": 1.25,
      "autoResize": true
    },
    {
      "id": "edge-3-sync-mcp-to-install-sh",
      "type": "arrow",
      "x": 613.6,
      "y": 162.0,
      "width": 150.7,
      "height": 124.0,
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
      "seed": 1620933364,
      "version": 1,
      "versionNonce": 1620933365,
      "isDeleted": false,
      "boundElements": [
        {
          "id": "edge-3-sync-mcp-to-install-sh-label",
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
          150.7,
          124.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "sync-mcp",
        "focus": 0,
        "gap": 4
      },
      "endBinding": {
        "elementId": "install-sh",
        "focus": 0,
        "gap": 4
      },
      "startArrowhead": null,
      "endArrowhead": "arrow",
      "elbowed": false
    },
    {
      "id": "edge-3-sync-mcp-to-install-sh-label",
      "type": "text",
      "x": 664.6,
      "y": 215.2,
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
      "seed": 1709994303,
      "version": 1,
      "versionNonce": 1709994304,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1,
      "link": null,
      "locked": false,
      "text": "invoke",
      "originalText": "invoke",
      "fontSize": 14,
      "fontFamily": 1,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "edge-3-sync-mcp-to-install-sh",
      "lineHeight": 1.25,
      "autoResize": true
    },
    {
      "id": "edge-4-install-sh-to-claude",
      "type": "arrow",
      "x": 924.3,
      "y": 286.0,
      "width": 110.0,
      "height": 116.0,
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
      "seed": 754543200,
      "version": 1,
      "versionNonce": 754543201,
      "isDeleted": false,
      "boundElements": [
        {
          "id": "edge-4-install-sh-to-claude-label",
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
          -116.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "install-sh",
        "focus": 0,
        "gap": 4
      },
      "endBinding": {
        "elementId": "claude",
        "focus": 0,
        "gap": 4
      },
      "startArrowhead": null,
      "endArrowhead": "arrow",
      "elbowed": false
    },
    {
      "id": "edge-4-install-sh-to-claude-label",
      "type": "text",
      "x": 959.3,
      "y": 219.2,
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
      "seed": 1193490522,
      "version": 1,
      "versionNonce": 1193490523,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1,
      "link": null,
      "locked": false,
      "text": "link",
      "originalText": "link",
      "fontSize": 14,
      "fontFamily": 1,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "edge-4-install-sh-to-claude",
      "lineHeight": 1.25,
      "autoResize": true
    },
    {
      "id": "edge-5-install-sh-to-gemini",
      "type": "arrow",
      "x": 924.3,
      "y": 286.0,
      "width": 164.7,
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
      "seed": 31682550,
      "version": 1,
      "versionNonce": 31682551,
      "isDeleted": false,
      "boundElements": [
        {
          "id": "edge-5-install-sh-to-gemini-label",
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
          164.7,
          0.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "install-sh",
        "focus": 0,
        "gap": 4
      },
      "endBinding": {
        "elementId": "gemini",
        "focus": 0,
        "gap": 4
      },
      "startArrowhead": null,
      "endArrowhead": "arrow",
      "elbowed": false
    },
    {
      "id": "edge-5-install-sh-to-gemini-label",
      "type": "text",
      "x": 986.6,
      "y": 277.2,
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
      "seed": 947251178,
      "version": 1,
      "versionNonce": 947251179,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1,
      "link": null,
      "locked": false,
      "text": "link",
      "originalText": "link",
      "fontSize": 14,
      "fontFamily": 1,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "edge-5-install-sh-to-gemini",
      "lineHeight": 1.25,
      "autoResize": true
    },
    {
      "id": "edge-6-install-sh-to-codex",
      "type": "arrow",
      "x": 924.3,
      "y": 286.0,
      "width": 164.7,
      "height": 116.0,
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
      "seed": 1686129935,
      "version": 1,
      "versionNonce": 1686129936,
      "isDeleted": false,
      "boundElements": [
        {
          "id": "edge-6-install-sh-to-codex-label",
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
          164.7,
          116.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "install-sh",
        "focus": 0,
        "gap": 4
      },
      "endBinding": {
        "elementId": "codex",
        "focus": 0,
        "gap": 4
      },
      "startArrowhead": null,
      "endArrowhead": "arrow",
      "elbowed": false
    },
    {
      "id": "edge-6-install-sh-to-codex-label",
      "type": "text",
      "x": 986.6,
      "y": 335.2,
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
      "seed": 464397170,
      "version": 1,
      "versionNonce": 464397171,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1,
      "link": null,
      "locked": false,
      "text": "link",
      "originalText": "link",
      "fontSize": 14,
      "fontFamily": 1,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "edge-6-install-sh-to-codex",
      "lineHeight": 1.25,
      "autoResize": true
    },
    {
      "id": "edge-7-shared-hook-to-pre-tool",
      "type": "arrow",
      "x": 298.2,
      "y": 460.0,
      "width": 120.9,
      "height": 182.0,
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
      "seed": 1277077865,
      "version": 1,
      "versionNonce": 1277077866,
      "isDeleted": false,
      "boundElements": [
        {
          "id": "edge-7-shared-hook-to-pre-tool-label",
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
          120.9,
          -182.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "shared-hook",
        "focus": 0,
        "gap": 4
      },
      "endBinding": {
        "elementId": "pre-tool",
        "focus": 0,
        "gap": 4
      },
      "startArrowhead": null,
      "endArrowhead": "arrow",
      "elbowed": false
    },
    {
      "id": "edge-7-shared-hook-to-pre-tool-label",
      "type": "text",
      "x": 338.4,
      "y": 360.2,
      "width": 40.6,
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
      "seed": 1939222503,
      "version": 1,
      "versionNonce": 1939222504,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1,
      "link": null,
      "locked": false,
      "text": "guard",
      "originalText": "guard",
      "fontSize": 14,
      "fontFamily": 1,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "edge-7-shared-hook-to-pre-tool",
      "lineHeight": 1.25,
      "autoResize": true
    },
    {
      "id": "edge-8-shared-hook-to-post-tool",
      "type": "arrow",
      "x": 298.2,
      "y": 460.0,
      "width": 114.6,
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
      "seed": 156146034,
      "version": 1,
      "versionNonce": 156146035,
      "isDeleted": false,
      "boundElements": [
        {
          "id": "edge-8-shared-hook-to-post-tool-label",
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
          114.6,
          -58.0
        ]
      ],
      "lastCommittedPoint": null,
      "startBinding": {
        "elementId": "shared-hook",
        "focus": 0,
        "gap": 4
      },
      "endBinding": {
        "elementId": "post-tool",
        "focus": 0,
        "gap": 4
      },
      "startArrowhead": null,
      "endArrowhead": "arrow",
      "elbowed": false
    },
    {
      "id": "edge-8-shared-hook-to-post-tool-label",
      "type": "text",
      "x": 331.2,
      "y": 422.2,
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
      "seed": 705142587,
      "version": 1,
      "versionNonce": 705142588,
      "isDeleted": false,
      "boundElements": null,
      "updated": 1,
      "link": null,
      "locked": false,
      "text": "format",
      "originalText": "format",
      "fontSize": 14,
      "fontFamily": 1,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "edge-8-shared-hook-to-post-tool",
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
