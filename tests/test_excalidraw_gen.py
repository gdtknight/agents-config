import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
EXCALIDRAW_GEN_PATH = (
    REPO_ROOT / "shared" / "skills" / "llm-wiki" / "scripts" / "excalidraw_gen.py"
)


def _load_excalidraw_gen():
    spec = importlib.util.spec_from_file_location("excalidraw_gen", EXCALIDRAW_GEN_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


excalidraw_gen = _load_excalidraw_gen()


class TestExcalidrawGen(unittest.TestCase):
    def _sample_spec(self, direction: str = "LR") -> dict:
        return {
            "title": "Sample Diagram",
            "direction": direction,
            "tags": ["test"],
            "sources": ["[[overview]]"],
            "groups": [{"id": "g1", "label": "Core Group", "color": "#1971c2"}],
            "nodes": [
                {
                    "id": "n1",
                    "label": "원본 소스",
                    "kind": "source",
                    "group": "g1",
                    "link": "overview",
                },
                {
                    "id": "n2",
                    "label": "분기 조건",
                    "kind": "decision",
                    "group": "g1",
                },
                {"id": "n3", "label": "Output", "kind": "synthesis"},
            ],
            "edges": [
                {"from": "n1", "to": "n2", "label": "ingest"},
                {"from": "n2", "to": "n3", "style": "dashed", "bidirectional": True},
            ],
        }

    def test_cjk_measurement_exceeds_ascii(self):
        w_cjk, _ = excalidraw_gen._measure_text("가나다라", font_size=16)
        w_asc, _ = excalidraw_gen._measure_text("abcd", font_size=16)
        self.assertGreater(w_cjk, w_asc)

    def test_generate_is_deterministic_and_validates_in_both_directions(self):
        for direction in ("LR", "TB"):
            spec = self._sample_spec(direction)
            scene1, texts1, links1 = excalidraw_gen.build_scene(spec)
            scene2, texts2, links2 = excalidraw_gen.build_scene(spec)
            self.assertEqual(scene1, scene2)

            # Group rectangle placed first so it renders behind nodes
            self.assertEqual(scene1["elements"][0]["id"], "grp-g1")
            self.assertEqual(links1, [("n1", "[[overview]]")])

            md = excalidraw_gen.render_obsidian_md(spec, scene1, texts1, links1)
            self.assertIn("excalidraw-plugin: parsed", md)
            self.assertIn("## Element Links", md)
            self.assertIn("^n1: [[overview]]", md)

            with tempfile.TemporaryDirectory() as tmp:
                out = Path(tmp) / f"sample-{direction}.excalidraw.md"
                out.write_text(md, encoding="utf-8")
                ok, errs = excalidraw_gen.validate_file(str(out))
                self.assertTrue(ok, msg=f"Unexpected validation errors: {errs}")

    def test_validate_file_rejects_broken_frontmatter_and_bindings(self):
        with tempfile.TemporaryDirectory() as tmp:
            bad_fm = Path(tmp) / "bad-fm.excalidraw.md"
            bad_fm.write_text("---\ntype: note\n---\n", encoding="utf-8")
            ok, errs = excalidraw_gen.validate_file(str(bad_fm))
            self.assertFalse(ok)
            self.assertTrue(any("excalidraw-plugin" in e for e in errs))

            bad_bind = Path(tmp) / "bad-bind.excalidraw"
            bad_bind.write_text(
                json.dumps(
                    {
                        "type": "excalidraw",
                        "version": 2,
                        "elements": [
                            {"id": "box1", "type": "rectangle", "boundElements": []},
                            {
                                "id": "txt1",
                                "type": "text",
                                "containerId": "box1",
                                "boundElements": None,
                            },
                        ],
                    }
                ),
                encoding="utf-8",
            )
            ok2, errs2 = excalidraw_gen.validate_file(str(bad_bind))
            self.assertFalse(ok2)
            self.assertTrue(any("boundElements missing bound text" in e for e in errs2))


if __name__ == "__main__":
    unittest.main()
