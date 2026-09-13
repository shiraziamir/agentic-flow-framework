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
        fixtures = {
            "VERSION": "1.9\n",
            "ARCHITECTURE.md": "# architecture\n",
            "bundle/README.md": "# bundle readme\n",
            "bundle/BEST_PRACTICES_USED.en.txt": "best practices\n",
            "docs/agent/START_HERE.md": "# start\n",
            "docs/agent/TASK_WORKFLOW_DRAFT_REVIEW_APPLY_VERIFY.md": "# workflow\n",
            "docs/references/PRIMARY_SOURCES.md": "# sources\n",
            "docs/GETTING_STARTED.md": "# getting started\n",
            "docs/GUIDE.fa.md": "# persian guide\n",
            "schemas/MUTATION_APPROVAL_POLICY.md": "# approval\n",
            "schemas/TASK_CONTRACT.md": "# task\n",
            "schemas/PROJECT_PROFILE_CONFIG.md": "# profile\n",
            "prompts/operator/TASK_DESIGNER.md": "# designer\n",
            "prompts/operator/MANAGER_REVIEWER.md": "# manager\n",
            "prompts/operator/INDEPENDENT_JUDGE.md": "# judge\n",
            "prompts/bootstrap/CLONE_AND_ADOPT.md": "# clone\n",
            "prompts/workflow/APPLY_TASK.md": "# apply\n",
            "prompts/supervisor/REVIEW.md": "# review\n",
            "templates/PROJECT_PROFILE.example.yaml": "profile: 1\n",
            "scripts/build_agent_bundle.py": "x\n",
            "scripts/test_build_agent_bundle.py": "x\n",
            "scripts/verification_lint.py": "x\n",
            "scripts/test_verification_lint.py": "x\n",
            "scripts/production_readiness_lint.py": "x\n",
            "scripts/test_production_readiness_lint.py": "x\n",
            "scripts/usage_ledger.py": "x\n",
            "scripts/claude_usage_snapshot.py": "x\n",
            "scripts/test_claude_usage_snapshot.py": "x\n",
            "scripts/test_docs_onboarding.py": "x\n",
            "research/R.md": "cold\n",
            "retrospectives/R.md": "cold\n",
            "stories/S.md": "cold\n",
            "agentic-flow-framework.fa.html": "old reader\n",
        }
        for rel, text in fixtures.items():
            put(root, rel, text)

        output = root / "bundle.zip"
        manifest = build(root, output)
        selected = {item["path"] for item in manifest["files"]}

        assert manifest["framework_version"] == "1.9"
        assert manifest["entrypoint"] == "START_HERE.md"
        assert manifest["operator_entrypoint"] == "README.md"

        required_selected = {
            "docs/agent/START_HERE.md",
            "docs/agent/TASK_WORKFLOW_DRAFT_REVIEW_APPLY_VERIFY.md",
            "docs/GETTING_STARTED.md",
            "docs/GUIDE.fa.md",
            "schemas/MUTATION_APPROVAL_POLICY.md",
            "schemas/TASK_CONTRACT.md",
            "schemas/PROJECT_PROFILE_CONFIG.md",
            "prompts/operator/TASK_DESIGNER.md",
            "prompts/operator/MANAGER_REVIEWER.md",
            "prompts/operator/INDEPENDENT_JUDGE.md",
            "prompts/bootstrap/CLONE_AND_ADOPT.md",
            "scripts/build_agent_bundle.py",
        }
        assert required_selected <= selected
        assert "research/R.md" not in selected
        assert "retrospectives/R.md" not in selected
        assert "stories/S.md" not in selected
        assert "agentic-flow-framework.fa.html" not in selected

        with zipfile.ZipFile(output) as zf:
            names = set(zf.namelist())
            required_zip = {
                "agentic-flow/README.md",
                "agentic-flow/START_HERE.md",
                "agentic-flow/INSTALL_PROMPT.txt",
                "agentic-flow/BEST_PRACTICES_USED.en.txt",
                "agentic-flow/PRIMARY_SOURCES.md",
                "agentic-flow/BUNDLE_MANIFEST.json",
                "agentic-flow/ARCHITECTURE.md",
                "agentic-flow/prompts/operator/TASK_DESIGNER.md",
                "agentic-flow/prompts/operator/MANAGER_REVIEWER.md",
                "agentic-flow/prompts/operator/INDEPENDENT_JUDGE.md",
                "agentic-flow/schemas/MUTATION_APPROVAL_POLICY.md",
                "agentic-flow/schemas/TASK_CONTRACT.md",
                "agentic-flow/docs/GUIDE.fa.md",
            }
            assert required_zip <= names
            assert not any("/research/" in name for name in names)
            assert not any("/retrospectives/" in name for name in names)
            assert not any("/stories/" in name for name in names)
            assert not any(name.endswith(".html") for name in names)

            bundled_manifest = json.loads(zf.read("agentic-flow/BUNDLE_MANIFEST.json"))
            assert bundled_manifest == manifest
            assert zf.read("agentic-flow/START_HERE.md") == b"# start\n"
            assert zf.read("agentic-flow/README.md") == b"# bundle readme\n"
            assert zf.read("agentic-flow/PRIMARY_SOURCES.md") == b"# sources\n"
            assert zf.read("agentic-flow/prompts/operator/INDEPENDENT_JUDGE.md") == b"# judge\n"
            install_prompt = zf.read("agentic-flow/INSTALL_PROMPT.txt")
            assert b"MIDSTREAM_ADOPTION" in install_prompt
            assert b"STRICT_PREVIEW" in install_prompt
            assert b"APPROVE/APPLY" in install_prompt

        print("bundle builder self-test: PASS")


if __name__ == "__main__":
    main()
