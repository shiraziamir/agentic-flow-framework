#!/usr/bin/env python3
"""Deterministic checks for Dual-Lens system-impact wiring."""
from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


class DualLensDocsTest(unittest.TestCase):
    def test_system_truth_map_exists_and_has_required_surfaces(self) -> None:
        path = ROOT / "schemas/SYSTEM_TRUTH_MAP.md"
        self.assertTrue(path.is_file())
        text = path.read_text(encoding="utf-8")
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
            self.assertIn(phrase, text)

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

    def test_fixed_system_effect_matrix_is_wired(self) -> None:
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

    def test_periodic_cross_system_audit_is_configured(self) -> None:
        profile = read("schemas/PROJECT_PROFILE_CONFIG.md")
        template = read("templates/PROJECT_PROFILE.example.yaml")
        workflow = read("docs/agent/TASK_WORKFLOW_DRAFT_REVIEW_APPLY_VERIFY.md")
        for text in (profile, template):
            self.assertIn("cross_system_audit:", text)
            self.assertIn("material_task_interval: 6", text)
            self.assertIn("before_real_customer_release: true", text)
            self.assertIn("after_material_incident: true", text)
        self.assertIn("Periodic cross-system audit", workflow)

    def test_mutation_proof_and_safe_restore_are_explicit(self) -> None:
        workflow = read("docs/agent/TASK_WORKFLOW_DRAFT_REVIEW_APPLY_VERIFY.md")
        status = read("schemas/STATUS_REPORT.md")
        self.assertIn("Mutation-sensitive proof", workflow)
        self.assertIn("Do not use destructive Git restore/reset/clean", workflow)
        self.assertIn("mutation_or_path_proof:", status)
        self.assertIn("mutations_caught", status)

    def test_project_inception_builds_truth_and_scale_baseline(self) -> None:
        inception = read("docs/agent/PROJECT_INCEPTION_ARCHITECTURE.md")
        for phrase in (
            "SYSTEM TRUTH / DATA AUTHORITY MAP",
            "CURRENT SCALE BOUNDARY",
            "What can leak?",
            "What can be counted twice?",
            "What can grow without a bound?",
        ):
            self.assertIn(phrase, inception)


if __name__ == "__main__":
    unittest.main()
