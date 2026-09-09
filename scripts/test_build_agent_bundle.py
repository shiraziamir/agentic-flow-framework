#!/usr/bin/env python3
from pathlib import Path
import json
import tempfile
import zipfile

from build_agent_bundle import build


def put(root: Path, rel: str, text: str = "x") -> None:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    with tempfile.TemporaryDirectory() as temp_dir:
        root = Path(temp_dir)
        put(root, "VERSION", "1.7\n")
        put(root, "ARCHITECTURE.md", "# architecture\n")
        put(root, "docs/agent/START_HERE.md", "# start\n")

        for rel in [
            "schemas/X.md",
            "verification/X.md",
            "production/X.md",
            "skills/x/SKILL.md",
            "prompts/bootstrap/X.md",
            "prompts/workflow/Y.md",
            "prompts/supervisor/Z.md",
            "templates/X.yaml",
            "scripts/verification_lint.py",
            "scripts/production_readiness_lint.py",
            "scripts/usage_ledger.py",
        ]:
            put(root, rel)

        for rel in [
            "docs/operator/SECRET.md",
            "docs/references/SOURCES.md",
            "docs/architecture/WHY.md",
            "research/R.md",
            "agentic-flow-framework.fa.html",
            "retrospectives/R.md",
        ]:
            put(root, rel)

        output = root / "bundle.zip"
        manifest = build(root, output)
        selected = {item["path"] for item in manifest["files"]}

        assert manifest["framework_version"] == "1.7"
        assert manifest["entrypoint"] == "START_HERE.md"
        assert "docs/agent/START_HERE.md" in selected
        assert "docs/operator/SECRET.md" not in selected
        assert "docs/references/SOURCES.md" not in selected
        assert "docs/architecture/WHY.md" not in selected
        assert "research/R.md" not in selected

        with zipfile.ZipFile(output) as zf:
            names = set(zf.namelist())
            assert "agentic-flow/BUNDLE_MANIFEST.json" in names
            assert "agentic-flow/START_HERE.md" in names
            assert "agentic-flow/INSTALL_PROMPT.txt" in names
            assert "agentic-flow/ARCHITECTURE.md" in names
            assert "agentic-flow/docs/agent/START_HERE.md" in names
            assert not any("/docs/operator/" in name for name in names)
            assert not any("/docs/references/" in name for name in names)
            assert not any("/research/" in name for name in names)

            bundled_manifest = json.loads(
                zf.read("agentic-flow/BUNDLE_MANIFEST.json").decode("utf-8")
            )
            assert bundled_manifest == manifest
            assert zf.read("agentic-flow/START_HERE.md") == b"# start\n"
            assert b"MIDSTREAM_ADOPTION" in zf.read("agentic-flow/INSTALL_PROMPT.txt")

        print("bundle builder self-test: PASS")


if __name__ == "__main__":
    main()
