import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parent.parent
HOOK_PATH = REPO_ROOT / "shared" / "hooks" / "hook.py"


def _load_hook():
    spec = importlib.util.spec_from_file_location("agents_config_hook", HOOK_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


hook = _load_hook()


class TestHookModule(unittest.TestCase):
    def test_extract_tool_info_normalizes_vendors(self):
        name, args = hook.extract_tool_info(
            {"toolCall": {"name": "run_command", "args": {"CommandLine": "ls"}}}
        )
        self.assertEqual(name, "run_command")
        self.assertEqual(args, {"CommandLine": "ls"})

        name2, args2 = hook.extract_tool_info(
            {"tool_name": "Bash", "tool_input": {"command": "pwd"}}
        )
        self.assertEqual(name2, "Bash")
        self.assertEqual(args2, {"command": "pwd"})

    def test_is_dangerous_rm_boundaries(self):
        for bad in (
            "rm -rf /",
            "rm -rf /*",
            "rm -rf ~",
            "rm -rf $HOME/",
            "sudo rm -rf /usr",
            "rm --recursive -f /System",
        ):
            with self.subTest(bad=bad):
                self.assertTrue(hook.is_dangerous_rm(bad))

        for safe in (
            "rm -rf /tmp/agents-config-test",
            "rm -rf ./dist",
            "rm -f /",
            "rm foo.txt",
        ):
            with self.subTest(safe=safe):
                self.assertFalse(hook.is_dangerous_rm(safe))

    def test_is_dangerous_chmod_boundaries(self):
        self.assertTrue(hook.is_dangerous_chmod("chmod -R 777 /"))
        self.assertTrue(hook.is_dangerous_chmod("sudo chmod -R 777 ~"))
        self.assertFalse(hook.is_dangerous_chmod("chmod +x install.sh"))
        self.assertFalse(hook.is_dangerous_chmod("chmod -R 755 ./scripts"))

    def _run_pre_tool(self, payload: dict) -> subprocess.CompletedProcess:
        return subprocess.run(
            [sys.executable, str(HOOK_PATH), "pre-tool"],
            input=json.dumps(payload),
            text=True,
            capture_output=True,
            check=False,
        )

    def test_pre_tool_denies_dangerous_commands_and_secrets(self):
        force_push = "git " + "push --" + "force origin main"
        fake_ghp = "ghp_" + ("A" * 36)
        fake_aws = "AKIA" + ("0" * 16)
        cases = [
            {"tool_name": "Bash", "tool_input": {"command": force_push}},
            {"tool_name": "Bash", "tool_input": {"command": "git reset --hard HEAD~1"}},
            {"tool_name": "Bash", "tool_input": {"command": "git clean -fd"}},
            {"tool_name": "Bash", "tool_input": {"command": "cat .env"}},
            {"tool_name": "Bash", "tool_input": {"command": f"echo {fake_ghp}"}},
            {"tool_name": "Bash", "tool_input": {"command": f"export KEY={fake_aws}"}},
            {"tool_name": "read_file", "tool_input": {"Path": "/tmp/app/.env"}},
            {"tool_name": "write_file", "tool_input": {"Path": "/tmp/id_ed25519"}},
        ]
        for payload in cases:
            with self.subTest(payload=payload):
                res = self._run_pre_tool(payload)
                self.assertEqual(res.returncode, 1)
                self.assertEqual(json.loads(res.stdout)["decision"], "deny")

    def test_pre_tool_allows_safe_commands_and_env_example(self):
        cases = [
            {"tool_name": "Bash", "tool_input": {"command": "ls -la"}},
            {"tool_name": "read_file", "tool_input": {"Path": "/tmp/.env.example"}},
            {"toolCall": {"name": "write_file", "args": {"Path": "README.md"}}},
        ]
        for payload in cases:
            with self.subTest(payload=payload):
                res = self._run_pre_tool(payload)
                self.assertEqual(res.returncode, 0)
                self.assertEqual(json.loads(res.stdout)["decision"], "allow")

    def test_format_file_skips_excalidraw_files(self):
        with mock.patch.object(hook.shutil, "which") as which_mock, mock.patch.object(
            hook.subprocess, "run"
        ) as run_mock:
            hook.format_file("/tmp/diagram.excalidraw.md")
            hook.format_file("/tmp/diagram.excalidraw")
            which_mock.assert_not_called()
            run_mock.assert_not_called()

    def test_post_tool_subprocess_leaves_excalidraw_md_unchanged(self):
        content = "---\nexcalidraw-plugin: parsed\n---\n%%\n{\"a\":1}\n%%\n"
        with tempfile.TemporaryDirectory() as tmp:
            exc_path = Path(tmp) / "sample.excalidraw.md"
            exc_path.write_text(content, encoding="utf-8")
            res = subprocess.run(
                [sys.executable, str(HOOK_PATH), "post-tool"],
                input=json.dumps(
                    {"tool_name": "write_file", "tool_input": {"Path": str(exc_path)}}
                ),
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(res.returncode, 0)
            self.assertEqual(exc_path.read_text(encoding="utf-8"), content)


if __name__ == "__main__":
    unittest.main()
