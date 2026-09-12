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
                resolved = (source.parent / clean).resolve()
                self.assertTrue(resolved.exists(), f"{rel}: missing link target {target}")

    def test_landing_page_contains_newcomer_route(self) -> None:
        text = read("README.md")
        for phrase in (
            "Why this repository exists",
            "What changes compared",
            "What is evidence-based",
            "Five-minute workflow",
            "Required execution environment",
            "Designer",
            "Manager",
            "Executor",
            "STRICT_PREVIEW",
            "mock-only",
            "Validation Status",
        ):
            self.assertIn(phrase, text)

    def test_execution_readiness_is_canonical_and_profiled(self) -> None:
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

    def test_role_prompts_preserve_separation_and_real_review(self) -> None:
        designer = read("prompts/operator/TASK_DESIGNER.md")
        manager = read("prompts/operator/MANAGER_REVIEWER.md")
        self.assertIn("MUST", designer)
        self.assertIn("SHOULD", designer)
        self.assertIn("INVESTIGATE", designer)
        self.assertIn("AVOID", designer)
        self.assertIn("environment", designer.lower())
        self.assertIn("exact diff/commit", manager)
        self.assertIn("isolated Executor branch/PR", manager)
        self.assertIn("environment authority", manager)
        self.assertIn("mock-only", manager)

    def test_persian_guide_has_balanced_rtl_and_ltr_code_blocks(self) -> None:
        text = read("docs/GUIDE.fa.md")
        self.assertGreater(len(re.findall(r"[\u0600-\u06ff]", text)), 1000)
        self.assertTrue(text.startswith('<div dir="rtl" align="right">'))
        self.assertTrue(text.rstrip().endswith("</div>"))
        self.assertNotIn("```", text)
        self.assertGreaterEqual(text.count('<pre dir="ltr" style="text-align:left"'), 10)
        self.assertIn('class="sourceCode bash"', text)
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
