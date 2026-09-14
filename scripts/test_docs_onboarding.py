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

    def test_landing_page_is_fast_and_complete(self) -> None:
        text = read("README.md")
        lowered = text.lower()
        for phrase in (
            "understand it in 30 seconds",
            "what exactly is authorized?",
            "vibe_fast",
            "product_standard",
            "high_assurance",
            "multi-model agreement",
            "independent judge",
            "human transports authority",
            "primary_task",
            "recency is not priority",
            "system truth",
            "no rollback / recovery plan",
        ):
            self.assertIn(phrase, lowered)

    def test_operator_runbooks_cover_current_control_model(self) -> None:
        english = read("docs/operator/OPERATOR_GUIDE.en.md")
        persian = read("docs/operator/OPERATOR_GUIDE.fa.md")
        for text in (english, persian):
            lowered = text.lower()
            for phrase in (
                "vibe_prototype",
                "product_standard",
                "high_assurance",
                "project architect",
                "primary_task",
                "side_task drift",
                "recency is not priority",
                "independent judge",
                "multi-model agreement",
                "system truth",
                "no rollback / recovery plan",
            ):
                self.assertIn(phrase, lowered)
            self.assertIn("executor", lowered)
            self.assertIn("manager", lowered)
            self.assertIn("read-only", lowered)

    def test_task_focus_and_attention_drift_are_canonical(self) -> None:
        architecture = read("ARCHITECTURE.md")
        workflow = read("docs/agent/TASK_WORKFLOW_DRAFT_REVIEW_APPLY_VERIFY.md")
        task = read("schemas/TASK_CONTRACT.md")
        profile = read("schemas/PROJECT_PROFILE_CONFIG.md")
        template = read("templates/PROJECT_PROFILE.example.yaml")
        for text in (architecture, workflow, task):
            self.assertIn("PRIMARY_TASK", text)
            self.assertIn("SIDE_TASK", text)
            self.assertIn("INTERRUPT", text)
        for text in (architecture, workflow):
            self.assertIn("SIDE_TASK DRIFT", text)
            self.assertIn("conversational momentum", text.lower())
        self.assertIn("focus:", task)
        self.assertIn("promotion_requires: MANAGER_OR_OPERATOR_DECISION", task)
        for text in (profile, template):
            self.assertIn("task_focus_policy:", text)
            self.assertIn("require_single_primary_task: true", text)
            self.assertIn("side_task_max_rounds_without_focus_review: 3", text)
            self.assertIn("side_task_may_redefine_primary_objective: false", text)
            self.assertIn("interrupt_requires_primary_checkpoint: true", text)

    def test_presets_simplify_without_weakening_sensitive_controls(self) -> None:
        profile = read("schemas/PROJECT_PROFILE_CONFIG.md")
        template = read("templates/PROJECT_PROFILE.example.yaml")
        start = read("docs/agent/START_HERE.md")
        for preset in ("VIBE_FAST", "PRODUCT_STANDARD", "HIGH_ASSURANCE"):
            self.assertIn(preset, profile)
            self.assertIn(preset, start)
        self.assertIn("operating_preset: PRODUCT_STANDARD", template)
        self.assertIn("overrides: {}", template)
        self.assertIn("production mutation", profile.lower())
        self.assertIn("rollback_or_forward_recovery_required_for_every_mutation: true", profile)

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
        self.assertIn("default_max_iterations: 1", profile)
        self.assertIn("maximum_without_escalation: 2", profile)
        self.assertIn("extra_iteration_requires_new_material_finding: true", profile)

    def test_dual_lens_depth_is_risk_adaptive(self) -> None:
        architecture = read("ARCHITECTURE.md")
        workflow = read("docs/agent/TASK_WORKFLOW_DRAFT_REVIEW_APPLY_VERIFY.md")
        profile = read("schemas/PROJECT_PROFILE_CONFIG.md")
        for text in (architecture, workflow):
            self.assertIn("compact System-Lens", text)
            self.assertIn("money", text.lower())
            self.assertIn("tenant", text.lower())
        self.assertIn("low_risk_mode: COMPACT_IMPACT_SUMMARY", profile)
        self.assertIn("force_explicit_dimensions_for_sensitive_boundaries: true", profile)

    def test_independent_closure_is_not_model_voting(self) -> None:
        architecture = read("ARCHITECTURE.md")
        workflow = read("docs/agent/TASK_WORKFLOW_DRAFT_REVIEW_APPLY_VERIFY.md")
        profile = read("schemas/PROJECT_PROFILE_CONFIG.md")
        judge = read("prompts/operator/INDEPENDENT_JUDGE.md")
        manager = read("prompts/operator/MANAGER_REVIEWER.md")
        operator = read("docs/operator/OPERATOR_GUIDE.en.md")
        for text in (architecture, workflow, judge, operator):
            self.assertIn("multi-model agreement", text.lower())
        for phrase in ("IMPLEMENTATION", "CONTEXT", "AUTHORITY", "EVIDENCE"):
            self.assertIn(phrase, judge)
        self.assertIn("production mutation: DENIED", judge)
        self.assertIn("multi_model_agreement_upgrades_evidence: false", profile)
        self.assertIn("independent_judge:", profile)
        self.assertIn("production_mutation: DENIED", profile)
        self.assertIn("APPROVE FOR INDEPENDENT CLOSURE", manager)

    def test_artifact_handoff_and_routing_are_wired(self) -> None:
        architecture = read("ARCHITECTURE.md")
        getting_started = read("docs/GETTING_STARTED.md")
        operator = read("docs/operator/OPERATOR_GUIDE.en.md")
        profile = read("schemas/PROJECT_PROFILE_CONFIG.md")
        for text in (architecture, getting_started, operator):
            lowered = text.lower()
            self.assertIn("human transports authority", lowered)
            self.assertIn("repository transports engineering state", lowered)
        self.assertIn("model_routing:", profile)
        self.assertIn("state_handoff:", profile)
        self.assertIn("require_primary_task_ref: true", profile)
        self.assertIn("never_reduce_acceptance_or_evidence_for_cost: true", profile)

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

    def test_execution_readiness_and_production_recovery_remain_canonical(self) -> None:
        architecture = read("ARCHITECTURE.md")
        environments = read("production/AGENT_ENVIRONMENTS.md")
        delivery = read("production/DELIVERY.md")
        schema = read("schemas/PROJECT_PROFILE_CONFIG.md")
        template = read("templates/PROJECT_PROFILE.example.yaml")
        for text in (architecture, environments):
            self.assertIn("real changed path", text)
            self.assertIn("mock", text.lower())
        for text in (schema, template):
            self.assertIn("execution_readiness:", text)
            self.assertIn("mock_only_closure:", text)
            self.assertIn("production_mode:", text)
            self.assertIn("rollback_or_forward_recovery_required_for_every_mutation: true", text)
        self.assertIn("rollback or forward-recovery", delivery.lower())

    def test_bundle_builder_includes_operator_role_prompts_and_dual_lens_test(self) -> None:
        builder = read("scripts/build_agent_bundle.py")
        self.assertIn('"prompts/operator/"', builder)
        self.assertIn('"scripts/test_dual_lens_docs.py"', builder)
        self.assertTrue((ROOT / "prompts/operator/INDEPENDENT_JUDGE.md").is_file())

    def test_persian_guide_is_current_and_role_clear(self) -> None:
        text = read("docs/GUIDE.fa.md")
        self.assertGreater(len(re.findall(r"[\u0600-\u06ff]", text)), 700)
        self.assertTrue(text.startswith('<div dir="rtl" align="right">'))
        self.assertTrue(text.rstrip().endswith("</div>"))
        self.assertNotIn("```", text)
        self.assertGreaterEqual(text.count('<pre dir="ltr" style="text-align:left"'), 8)
        for phrase in (
            "1.11",
            "VIBE_FAST",
            "PRODUCT_STANDARD",
            "HIGH_ASSURANCE",
            "System Truth Map",
            "MULTI-MODEL AGREEMENT",
            "Independent Judge",
            "Human transports authority",
        ):
            self.assertIn(phrase, text)

    def test_validation_status_does_not_overclaim(self) -> None:
        text = read("docs/VALIDATION_STATUS.md")
        for phrase in (
            "UNPROVEN",
            "not yet empirically validated as superior",
            "Multiple models agreeing is **not** treated as independent behavioral evidence",
            "Model diversity does not guarantee statistical or cognitive independence",
        ):
            self.assertIn(phrase, text)


if __name__ == "__main__":
    unittest.main()
