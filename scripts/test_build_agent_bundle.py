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
        put(root, "VERSION", "1.8\n")
        put(root, "ARCHITECTURE.md", "# architecture\n")
        put(root, "bundle/README.md", "# bundle readme\n")
        put(root, "bundle/BEST_PRACTICES_USED.en.txt", "best practices\n")
        put(root, "docs/agent/START_HERE.md", "# start\n")
        put(root, "docs/agent/MIDSTREAM_ADOPTION.md", "# midstream\n")
        put(root, "docs/agent/TASK_WORKFLOW_DRAFT_REVIEW_APPLY_VERIFY.md", "# workflow\n")
        put(root, "docs/agent/TOKEN_EFFICIENT_WORKFLOW.md", "# token\n")
        put(root, "docs/agent/USAGE_AWARE_TASK_REPORTING.md", "# usage reporting\n")
        put(root, "docs/operator/CLONE_AND_ADOPT.md", "# clone and adopt\n")
        put(root, "docs/operator/CLAUDE_USAGE_NOTIFICATIONS.md", "# claude notifications\n")
        put(root, "docs/operator/USING_PYTHON_TOOLS.en.md", "# python tools\n")
        put(root, "docs/operator/USING_PYTHON_TOOLS.fa.md", "# python tools fa\n")
        put(root, "docs/architecture/WHY.md", "# why\n")
        put(root, "docs/references/PRIMARY_SOURCES.md", "# sources\n")
        put(root, "docs/references/CLAUDE_USAGE_TELEMETRY.md", "# claude usage sources\n")
        put(root, "docs/GETTING_STARTED.md", "# getting started\n")
        put(root, "docs/WHY_AGENTIC_FLOW.md", "# why\n")
        put(root, "docs/COMPARISON.md", "# comparison\n")
        put(root, "docs/VALIDATION_STATUS.md", "# validation\n")
        put(root, "docs/GUIDE.fa.md", "# persian guide\n")
        put(root, "docs/examples/END_TO_END_TASK.md", "# example\n")
        put(root, "docs/operator/CONTEXT_PACKET.md", "# context packet\n")
        put(root, "schemas/MUTATION_APPROVAL_POLICY.md", "# strict preview\n")
        put(root, "schemas/USAGE_QUOTA_SNAPSHOT.md", "# quota schema\n")
        put(root, "prompts/bootstrap/CLONE_AND_ADOPT.md", "# clone prompt\n")

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
            "scripts/test_verification_lint.py",
            "scripts/production_readiness_lint.py",
            "scripts/test_production_readiness_lint.py",
            "scripts/build_agent_bundle.py",
            "scripts/test_build_agent_bundle.py",
            "scripts/usage_ledger.py",
            "scripts/claude_usage_snapshot.py",
            "scripts/test_claude_usage_snapshot.py",
            "scripts/test_docs_onboarding.py",
        ]:
            put(root, rel)

        for rel in [
            "research/R.md",
            "agentic-flow-framework.fa.html",
            "retrospectives/R.md",
            "stories/S.md",
        ]:
            put(root, rel)

        output = root / "bundle.zip"
        manifest = build(root, output)
        selected = {item["path"] for item in manifest["files"]}

        assert manifest["framework_version"] == "1.8"
        assert manifest["entrypoint"] == "START_HERE.md"
        assert manifest["operator_entrypoint"] == "README.md"
        assert "docs/agent/START_HERE.md" in selected
        assert "docs/agent/USAGE_AWARE_TASK_REPORTING.md" in selected
        assert "docs/operator/CLONE_AND_ADOPT.md" in selected
        assert "docs/operator/CLAUDE_USAGE_NOTIFICATIONS.md" in selected
        assert "schemas/MUTATION_APPROVAL_POLICY.md" in selected
        assert "schemas/USAGE_QUOTA_SNAPSHOT.md" in selected
        assert "docs/references/CLAUDE_USAGE_TELEMETRY.md" in selected
        assert "docs/GETTING_STARTED.md" in selected
        assert "docs/GUIDE.fa.md" in selected
        assert "docs/examples/END_TO_END_TASK.md" in selected
        assert "docs/operator/CONTEXT_PACKET.md" in selected
        assert "prompts/bootstrap/CLONE_AND_ADOPT.md" in selected
        assert "docs/operator/USING_PYTHON_TOOLS.en.md" in selected
        assert "docs/architecture/WHY.md" in selected
        assert "docs/references/PRIMARY_SOURCES.md" in selected
        assert "scripts/build_agent_bundle.py" in selected
        assert "scripts/claude_usage_snapshot.py" in selected
        assert "scripts/test_claude_usage_snapshot.py" in selected
        assert "scripts/test_docs_onboarding.py" in selected
        assert "research/R.md" not in selected
        assert "retrospectives/R.md" not in selected
        assert "stories/S.md" not in selected

        with zipfile.ZipFile(output) as zf:
            names = set(zf.namelist())
            required = {
                "agentic-flow/README.md",
                "agentic-flow/START_HERE.md",
                "agentic-flow/INSTALL_PROMPT.txt",
                "agentic-flow/BEST_PRACTICES_USED.en.txt",
                "agentic-flow/PRIMARY_SOURCES.md",
                "agentic-flow/BUNDLE_MANIFEST.json",
                "agentic-flow/ARCHITECTURE.md",
                "agentic-flow/docs/agent/TASK_WORKFLOW_DRAFT_REVIEW_APPLY_VERIFY.md",
                "agentic-flow/docs/agent/TOKEN_EFFICIENT_WORKFLOW.md",
                "agentic-flow/docs/agent/USAGE_AWARE_TASK_REPORTING.md",
                "agentic-flow/docs/operator/CLONE_AND_ADOPT.md",
                "agentic-flow/docs/operator/CLAUDE_USAGE_NOTIFICATIONS.md",
                "agentic-flow/docs/operator/USING_PYTHON_TOOLS.en.md",
                "agentic-flow/docs/references/PRIMARY_SOURCES.md",
                "agentic-flow/docs/references/CLAUDE_USAGE_TELEMETRY.md",
                "agentic-flow/docs/GETTING_STARTED.md",
                "agentic-flow/docs/WHY_AGENTIC_FLOW.md",
                "agentic-flow/docs/COMPARISON.md",
                "agentic-flow/docs/VALIDATION_STATUS.md",
                "agentic-flow/docs/GUIDE.fa.md",
                "agentic-flow/docs/examples/END_TO_END_TASK.md",
                "agentic-flow/docs/operator/CONTEXT_PACKET.md",
                "agentic-flow/schemas/MUTATION_APPROVAL_POLICY.md",
                "agentic-flow/schemas/USAGE_QUOTA_SNAPSHOT.md",
                "agentic-flow/prompts/bootstrap/CLONE_AND_ADOPT.md",
                "agentic-flow/scripts/claude_usage_snapshot.py",
                "agentic-flow/scripts/test_claude_usage_snapshot.py",
                "agentic-flow/scripts/test_docs_onboarding.py",
            }
            assert required <= names
            assert not any("/research/" in name for name in names)
            assert not any("/retrospectives/" in name for name in names)
            assert not any("/stories/" in name for name in names)

            bundled_manifest = json.loads(
                zf.read("agentic-flow/BUNDLE_MANIFEST.json").decode("utf-8")
            )
            assert bundled_manifest == manifest
            assert zf.read("agentic-flow/START_HERE.md") == b"# start\n"
            assert zf.read("agentic-flow/README.md") == b"# bundle readme\n"
            assert zf.read("agentic-flow/BEST_PRACTICES_USED.en.txt") == b"best practices\n"
            assert zf.read("agentic-flow/PRIMARY_SOURCES.md") == b"# sources\n"
            install_prompt = zf.read("agentic-flow/INSTALL_PROMPT.txt")
            assert b"MIDSTREAM_ADOPTION" in install_prompt
            assert b"STRICT_PREVIEW" in install_prompt
            assert b"APPROVE/APPLY" in install_prompt

        print("bundle builder self-test: PASS")


if __name__ == "__main__":
    main()
