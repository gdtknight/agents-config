import importlib.util
import io
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
WIKI_TOOL_PATH = (
    REPO_ROOT / "shared" / "skills" / "llm-wiki" / "scripts" / "wiki_tool.py"
)


def _load_wiki_tool():
    spec = importlib.util.spec_from_file_location("wiki_tool", WIKI_TOOL_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


wiki_tool = _load_wiki_tool()


class TestWikiTool(unittest.TestCase):
    def test_init_and_idempotency_and_no_templates(self):
        with tempfile.TemporaryDirectory() as tmp:
            vault = Path(tmp) / "vault"
            rc = wiki_tool.cmd_init(
                str(vault), "My Wiki", "Testing", force=False, include_templates=True
            )
            self.assertEqual(rc, 0)
            self.assertTrue((vault / "raw" / "assets").is_dir())
            self.assertTrue((vault / "wiki" / "visuals").is_dir())
            self.assertTrue((vault / "templates" / "source.md").is_file())

            overview = vault / "wiki" / "overview.md"
            overview.write_text(
                overview.read_text(encoding="utf-8") + "\nCustom note\n",
                encoding="utf-8",
            )
            wiki_tool.cmd_init(
                str(vault), "My Wiki", "Testing", force=False, include_templates=True
            )
            self.assertIn("Custom note", overview.read_text(encoding="utf-8"))

            repo_like = Path(tmp) / "repo-like"
            wiki_tool.cmd_init(
                str(repo_like),
                "Repo Wiki",
                "Repo",
                force=False,
                include_templates=False,
            )
            self.assertFalse((repo_like / "templates").exists())

    def test_lint_passes_on_repo_and_flags_errors_and_warnings(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            rc = wiki_tool.cmd_lint(str(REPO_ROOT))
        self.assertEqual(rc, 0, msg=buf.getvalue())
        self.assertIn("- Errors: 0", buf.getvalue())
        self.assertIn("- Warnings: 0", buf.getvalue())

        with tempfile.TemporaryDirectory() as tmp:
            vault = Path(tmp) / "vault"
            wiki_tool.cmd_init(
                str(vault), "Test Vault", "Domain", force=False, include_templates=False
            )
            # Page with broken link, missing frontmatter key, and ignored code/comment links
            bad_page = vault / "wiki" / "concepts" / "broken.md"
            bad_page.write_text(
                "---\nid: broken\ntype: concept\ntags: [test]\n---\n"
                "Real broken link: [[does-not-exist]]\n"
                "```markdown\n[[ignored-in-code]]\n```\n"
                "<!-- [[ignored-in-comment]] -->\n",
                encoding="utf-8",
            )
            out = io.StringIO()
            with redirect_stdout(out):
                lint_rc = wiki_tool.cmd_lint(str(vault))
            report = out.getvalue()
            self.assertEqual(lint_rc, 1)
            self.assertIn("Frontmatter missing required key(s): updated", report)
            self.assertIn("Broken wikilink [[does-not-exist]]", report)
            self.assertNotIn("ignored-in-code", report)
            self.assertNotIn("ignored-in-comment", report)
            self.assertIn("Not listed in wiki/index.md", report)
            self.assertIn("Orphan page", report)

    def test_log_appends_entry(self):
        with tempfile.TemporaryDirectory() as tmp:
            vault = Path(tmp) / "vault"
            wiki_tool.cmd_init(
                str(vault), "Log Vault", "Domain", force=False, include_templates=False
            )
            rc = wiki_tool.cmd_log(str(vault), "ingest", "Paper A", "Summary added")
            self.assertEqual(rc, 0)
            log_text = (vault / "wiki" / "log.md").read_text(encoding="utf-8")
            self.assertIn("] ingest | Paper A", log_text)
            self.assertIn("- Summary added", log_text)


if __name__ == "__main__":
    unittest.main()
