#!/usr/bin/env python3
"""Deterministic checks for Dual-Lens and productization wiring."""
from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


class DualLensDocsTest(unittest.TestCase):
    def test_system_truth_map_schema_and_template_exist(self) -> None:
        schema = read("schemas/SYSTEM_TRUTH_MAP.md")
        template_path = ROOT / "templates/SYSTEM_TRUTH_MAP.example.yaml"
        self.assertTrue(template_path.is_file())
        template = template_path.read_text(encoding="utf-8")
        for phrase in (
            "authoritative_source",
            "trust_boundaries",
            "restart_behavior",
            "failure_behavior",
            "recovery_procedure",
            "tenant_isolation",
            "scale_boundaries",
            "cross_system_audit",
        ):
            self.assertIn(phrase, schema)
            self.assertIn(phrase, template)

    def test_dual_lens_is_canonical_and_operator_visible(self) -> None:
        files = (
            "README.md",
            "ARCHITECTURE.md",
            "docs/agent/TASK_WORKFLOW_DRAFT_REVIEW_APPLY_VERIFY.md",
            "docs/operator/OPERATOR_GUIDE.en.md",
            "docs/operator/OPERATOR_GUIDE.fa.md",
            "schemas/TASK_CONTRACT.md",
        )
        for rel in files:
            text = read(rel).lower()
            self.assertIn("local lens", text, rel)
            self.assertIn("system lens", text, rel)

    def test_system_effect_vocabulary_is_stable(self) -> None:
        files = (
            "schemas/SYSTEM_TRUTH_MAP.md",
            "schemas/TASK_CONTRACT.md",
            "schemas/STATUS_REPORT.md",
            "docs/agent/TASK_WORKFLOW_DRAFT_REVIEW_APPLY_VERIFY.md",
            "prompts/operator/TASK_DESIGNER.md",
            "prompts/operator/MANAGER_REVIEWER.md",
        )
        required = (
            "WRITE",
            "READ",
            "AGGREGATE",
            "CACHE",
            "RESTART",
            "FAILURE",
            "RECOVERY",
            "ADMIN",
            "METRIC",
            "TENANT_ISOLATION",
            "SCALE",
            "PRIVACY",
            "COST",
        )
        for rel in files:
            text = read(rel)
            for phrase in required:
                self.assertIn(phrase, text, f"{rel}: {phrase}")

    def test_system_effect_states_and_open_risk_are_explicit(self) -> None:
        files = (
            "schemas/SYSTEM_TRUTH_MAP.md",
            "schemas/TASK_CONTRACT.md",
            "schemas/PROJECT_PROFILE_CONFIG.md",
            "templates/PROJECT_PROFILE.example.yaml",
            "docs/agent/TASK_WORKFLOW_DRAFT_REVIEW_APPLY_VERIFY.md",
        )
        for rel in files:
            text = read(rel)
            for state in (
                "UNAFFECTED",
                "VERIFIED",
                "CHANGED_AND_TESTED",
                "OPEN_RISK",
                "NOT_APPLICABLE",
            ):
                self.assertIn(state, text, f"{rel}: {state}")

    def test_low_risk_does_not_require_checklist_theater(self) -> None:
        profile = read("schemas/PROJECT_PROFILE_CONFIG.md")
        template = read("templates/PROJECT_PROFILE.example.yaml")
        workflow = read("docs/agent/TASK_WORKFLOW_DRAFT_REVIEW_APPLY_VERIFY.md")
        architecture = read("ARCHITECTURE.md")
        for text in (profile, template):
            self.assertIn("low_risk_mode: COMPACT_IMPACT_SUMMARY", text)
        lowered = workflow.lower()
        self.assertIn("checklist theater", lowered)
        self.assertIn("do not mechanically fill all rows", lowered)
        self.assertIn("LOW", architecture)
        self.assertIn("compact System-Lens", architecture)

    def test_cross_system_audit_is_event_and_risk_first(self) -> None:
        profile = read("schemas/PROJECT_PROFILE_CONFIG.md")
        template = read("templates/PROJECT_PROFILE.example.yaml")
        workflow = read("docs/agent/TASK_WORKFLOW_DRAFT_REVIEW_APPLY_VERIFY.md")
        for text in (profile, template):
            self.assertIn("trigger_precedence: EVENT_THEN_RISK_THEN_COUNT", text)
            self.assertIn("material_task_interval: 6", text)
            self.assertIn("before_real_customer_release: true", text)
            self.assertIn("after_material_incident: true", text)
        self.assertIn("EVENT TRIGGER", workflow)
        self.assertIn("TASK-COUNT REMINDER", workflow)

    def test_operating_presets_reduce_profile_burden(self) -> None:
        profile = read("schemas/PROJECT_PROFILE_CONFIG.md")
        template = read("templates/PROJECT_PROFILE.example.yaml")
        start = read("docs/agent/START_HERE.md")
        readme = read("README.md")
        for preset in ("VIBE_FAST", "PRODUCT_STANDARD", "HIGH_ASSURANCE"):
            self.assertIn(preset, profile)
            self.assertIn(preset, readme)
        self.assertIn("operating_preset: PRODUCT_STANDARD", template)
        self.assertIn("operating_preset", start)
        self.assertIn("overrides: {}", template)

    def test_mutation_proof_and_safe_restore_are_explicit(self) -> None:
        workflow = read("docs/agent/TASK_WORKFLOW_DRAFT_REVIEW_APPLY_VERIFY.md")
        status = read("schemas/STATUS_REPORT.md")
        self.assertIn("Mutation/path proof", workflow)
        self.assertIn("Do not use destructive Git reset/restore/clean", workflow)
        self.assertIn("mutation_or_path_proof:", status)
        self.assertIn("mutations_caught", status)

    def test_project_inception_builds_truth_and_scale_baseline(self) -> None:
        inception = read("docs/agent/PROJECT_INCEPTION_ARCHITECTURE.md")
        start = read("docs/agent/START_HERE.md")
        for phrase in (
            "SYSTEM TRUTH / DATA AUTHORITY MAP",
            "CURRENT SCALE BOUNDARY",
        ):
            self.assertIn(phrase, inception)
            self.assertIn(phrase, start)
        for phrase in (
            "What can leak?",
            "What can be counted twice?",
            "What can grow without a bound?",
        ):
            self.assertIn(phrase, inception)

    def test_bundle_vs_context_semantics_are_not_contradictory(self) -> None:
        agents = read("AGENTS.md").lower()
        bundle_readme = read("bundle/README.md").lower()
        self.assertIn("included in the bundle does not mean included in default agent context", agents)
        self.assertIn("docs/operator/", bundle_readme)
        self.assertIn("presence in the zip", bundle_readme)
        self.assertIn("preload", bundle_readme)


if __name__ == "__main__":
    unittest.main()
