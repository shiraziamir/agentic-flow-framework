#!/usr/bin/env python3
"""Deterministic checks for newcomer documentation and policy wiring."""
from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ONBOARDING = (
    "README.md",
    "docs/GETTING_STARTED.md",
    "docs/WHY_AGENTIC_FLOW.md",
    "docs/COMPARISON.md",
    "docs/VALIDATION_STATUS.md",
    "docs/GUIDE.fa.md",
    "docs/examples/END_TO_END_TASK.md",
)


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


class OnboardingDocsTest(unittest.TestCase):
    def test_required_files_exist_and_are_nontrivial(self) -> None:
        for rel in ONBOARDING:
            path = ROOT / rel
            self.assertTrue(path.is_file(), rel)
            self.assertGreater(len(path.read_text(encoding="utf-8")), 500, rel)

    def test_local_markdown_links_resolve(self) -> None:
        pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
        for rel in ONBOARDING:
            source = ROOT / rel
            for target in pattern.findall(source.read_text(encoding="utf-8")):
                if "://" in target or target.startswith(("#", "mailto:")):
                    continue
                clean = target.split("#", 1)[0]
                if not clean:
                    continue
                self.assertTrue((source.parent / clean).resolve().exists(), f"{rel}: {target}")

    def test_landing_page_has_small_newcomer_route(self) -> None:
        text = read("README.md")
        for phrase in (
            "Why this repository exists",
            "Start here — do not read the whole repository",
            "Quality requirements stay fixed",
            "Controlled remediation",
            "Required execution environment",
            "Workspace and external-effect safety",
            "Compact evidence",
        ):
            self.assertIn(phrase, text)
        self.assertIn("four human-facing files", text)

    def test_risk_adaptive_policy_is_canonical(self) -> None:
        architecture = read("ARCHITECTURE.md")
        workflow = read("docs/agent/TASK_WORKFLOW_DRAFT_REVIEW_APPLY_VERIFY.md")
        approval = read("schemas/MUTATION_APPROVAL_POLICY.md")
        task = read("schemas/TASK_CONTRACT.md")
        profile = read("schemas/PROJECT_PROFILE_CONFIG.md")
        self.assertIn("Remediation autonomy", architecture)
        self.assertIn("Remediation autonomy", approval)
        for text in (architecture, workflow, approval):
            self.assertIn("remediation", text.lower())
        for text in (architecture, workflow, task):
            self.assertIn("work_kind", text)
            self.assertIn("LOW", text)
            self.assertIn("MEDIUM", text)
            self.assertIn("HIGH", text)
        self.assertIn("remediation_windows:", profile)
        self.assertIn("external_effects:", profile)
        self.assertIn("workspace_safety:", profile)
        self.assertIn("flow_metrics:", profile)

    def test_failure_surface_and_adversarial_review_are_wired(self) -> None:
        workflow = read("docs/agent/TASK_WORKFLOW_DRAFT_REVIEW_APPLY_VERIFY.md")
        designer = read("prompts/operator/TASK_DESIGNER.md")
        manager = read("prompts/operator/MANAGER_REVIEWER.md")
        for phrase in (
            "TEST-ORACLE FALSIFICATION",
            "CLEANUP / ROLLBACK FAILURE",
            "PROCESS CONCURRENCY",
            "EXTERNAL PROVIDER",
        ):
            self.assertIn(phrase, workflow)
            self.assertIn(phrase, designer)
        self.assertIn("CONSOLIDATED FINDING SET", manager)
        self.assertIn("CONTROLLED REMEDIATION WINDOW", manager)
        self.assertIn("adversarial", manager.lower())
        self.assertIn("exact diff/commit", manager)

    def test_execution_readiness_and_mock_limits_remain_canonical(self) -> None:
        architecture = read("ARCHITECTURE.md")
        environments = read("production/AGENT_ENVIRONMENTS.md")
        schema = read("schemas/PROJECT_PROFILE_CONFIG.md")
        template = read("templates/PROJECT_PROFILE.example.yaml")
        for text in (architecture, environments):
            self.assertIn("real changed path", text)
            self.assertIn("mock", text.lower())
        for text in (schema, template):
            self.assertIn("execution_readiness:", text)
            self.assertIn("mock_only_closure:", text)
            self.assertIn("real_application_runtime:", text)

    def test_bundle_builder_includes_operator_role_prompts(self) -> None:
        builder = read("scripts/build_agent_bundle.py")
        self.assertIn('"prompts/operator/"', builder)

    def test_persian_guide_has_rtl_ltr_and_new_flow(self) -> None:
        text = read("docs/GUIDE.fa.md")
        self.assertGreater(len(re.findall(r"[\u0600-\u06ff]", text)), 1000)
        self.assertTrue(text.startswith('<div dir="rtl" align="right">'))
        self.assertTrue(text.rstrip().endswith("</div>"))
        self.assertNotIn("```", text)
        self.assertGreaterEqual(text.count('<pre dir="ltr" style="text-align:left"'), 10)
        self.assertIn('class="sourceCode bash"', text)
        self.assertIn("Controlled Remediation Window", text)
        self.assertIn("mock-only closure", text)

    def test_validation_status_does_not_overclaim(self) -> None:
        text = read("docs/VALIDATION_STATUS.md")
        for phrase in (
            "UNPROVEN",
            "PENDING",
            "not yet empirically validated as superior",
            "not the effectiveness of the framework",
        ):
            self.assertIn(phrase, text)


if __name__ == "__main__":
    unittest.main()
