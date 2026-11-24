import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SYNC_MCP_PATH = REPO_ROOT / "shared" / "sync_mcp.py"


def _load_sync_mcp():
    spec = importlib.util.spec_from_file_location("agents_config_sync_mcp", SYNC_MCP_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


sync_mcp = _load_sync_mcp()


class TestSyncMcp(unittest.TestCase):
    def test_validate_servers_normalizes_http_and_stdio(self):
        payload = {
            "mcpServers": {
                "graphify": {"url": "https://api.graphify.com/mcp"},
                "local-tool": {
                    "command": "npx",
                    "args": ["-y", "demo-mcp"],
                    "env": {"MODE": "prod"},
                    "disabled": True,
                },
            }
        }
        servers = sync_mcp.validate_servers(payload)
        self.assertEqual(servers["graphify"]["type"], "http")
        self.assertFalse(servers["graphify"]["disabled"])
        self.assertEqual(servers["local-tool"]["type"], "stdio")
        self.assertTrue(servers["local-tool"]["disabled"])
        self.assertEqual(servers["local-tool"]["env"], {"MODE": "prod"})

    def test_validate_servers_rejects_invalid_entries(self):
        invalid_payloads = [
            {},
            {"mcpServers": {"bad": {"url": "https://x", "command": "cmd"}}},
            {"mcpServers": {"bad": {}}},
            {"mcpServers": {"bad": {"url": "https://x", "disabled": "no"}}},
            {"mcpServers": {"bad": {"command": "cmd", "args": "not-a-list"}}},
            {"mcpServers": {"bad": {"command": "cmd", "env": {"K": 123}}}},
        ]
        for payload in invalid_payloads:
            with self.subTest(payload=payload):
                with self.assertRaises(ValueError):
                    sync_mcp.validate_servers(payload)

    def test_render_gemini_and_codex_outputs(self):
        servers = sync_mcp.validate_servers(
            {
                "mcpServers": {
                    "graphify": {"type": "http", "url": "https://api.graphify.com/mcp"},
                    "qmd": {
                        "type": "stdio",
                        "command": "qmd",
                        "args": ["mcp"],
                        "disabled": True,
                    },
                }
            }
        )
        gemini_data = json.loads(sync_mcp.render_gemini_json(servers))
        self.assertEqual(
            gemini_data["mcpServers"]["graphify"],
            {"disabled": False, "serverUrl": "https://api.graphify.com/mcp"},
        )
        self.assertEqual(gemini_data["mcpServers"]["qmd"]["command"], "qmd")

        existing_toml = 'model = "gpt-6-luna"\n\n[tui]\nscreen_reader_detection_done = true\n'
        merged = sync_mcp.merge_codex_toml(
            existing_toml, sync_mcp.render_codex_block(servers)
        )
        self.assertIn(sync_mcp.MANAGED_BEGIN, merged)
        self.assertIn('[mcp_servers.graphify]', merged)
        self.assertIn('enabled = false', merged)
        # Re-merging is idempotent and preserves top keys
        remerged = sync_mcp.merge_codex_toml(merged, sync_mcp.render_codex_block(servers))
        self.assertEqual(merged, remerged)
        self.assertIn('model = "gpt-6-luna"', remerged)

    def test_sync_claude_config_preserves_custom_state_and_honors_dry_run(self):
        servers = sync_mcp.validate_servers(
            {
                "mcpServers": {
                    "graphify": {"type": "http", "url": "https://api.graphify.com/mcp"},
                    "disabled-srv": {
                        "type": "http",
                        "url": "https://old.example/mcp",
                        "disabled": True,
                    },
                }
            }
        )
        with tempfile.TemporaryDirectory() as tmp:
            claude_json = Path(tmp) / ".claude.json"
            claude_json.write_text(
                json.dumps(
                    {
                        "numStartups": 12,
                        "mcpServers": {
                            "custom-local": {"type": "stdio", "command": "echo"},
                            "disabled-srv": {"type": "http", "url": "https://old.example/mcp"},
                        },
                    }
                ),
                encoding="utf-8",
            )
            before = claude_json.read_text(encoding="utf-8")
            sync_mcp.sync_claude_config(str(claude_json), servers, dry_run=True)
            self.assertEqual(claude_json.read_text(encoding="utf-8"), before)

            sync_mcp.sync_claude_config(str(claude_json), servers, dry_run=False)
            updated = json.loads(claude_json.read_text(encoding="utf-8"))
            self.assertEqual(updated["numStartups"], 12)
            self.assertIn("custom-local", updated["mcpServers"])
            self.assertIn("graphify", updated["mcpServers"])
            self.assertNotIn("disabled-srv", updated["mcpServers"])


if __name__ == "__main__":
    unittest.main()
