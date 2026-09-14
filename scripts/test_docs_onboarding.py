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
        for phrase in (
            "The five questions",
            "What exactly is authorized?",
            "MULTI-MODEL AGREEMENT",
            "Independent Judge",
            "Human transports authority; repository transports engineering state.",
            "one remediation round by default",
            "rollback or explicit forward-recovery plan",
            "PRIMARY_TASK",
            "SIDE_TASK DRIFT",
            "RECENCY IS NOT PRIORITY",
            "Operator Runbook",
        ):
            self.assertIn(phrase, text)

    def test_operator_runbook_covers_current_control_model(self) -> None:
        english = read("docs/operator/OPERATOR_GUIDE.en.md")
        persian = read("docs/operator/OPERATOR_GUIDE.fa.md")
        index = read("docs/operator/README.md")
        for text in (english, persian):
            for phrase in (
                "VIBE_PROTOTYPE",
                "PROJECT ARCHITECT",
                "PRIMARY_TASK",
                "SIDE_TASK DRIFT",
                "RECENCY IS NOT PRIORITY",
                "SWAMP ALERT",
                "Independent Judge",
                "MULTI-MODEL AGREEMENT",
                "STRICT_PREVIEW",
                "NO ROLLBACK / RECOVERY PLAN",
            ):
                self.assertIn(phrase, text)
            self.assertIn("Executor", text)
            self.assertIn("Manager", text)
            self.assertIn("read-only", text)
        self.assertIn("single operator control-plane runbook", index)
        self.assertIn("Runbook کامل فارسی اپراتور", index)

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
            self.assertIn("alert_on_side_task_attention_drift: true", text)

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

    def test_independent_closure_is_not_model_voting(self) -> None:
        architecture = read("ARCHITECTURE.md")
        workflow = read("docs/agent/TASK_WORKFLOW_DRAFT_REVIEW_APPLY_VERIFY.md")
        profile = read("schemas/PROJECT_PROFILE_CONFIG.md")
        judge = read("prompts/operator/INDEPENDENT_JUDGE.md")
        manager = read("prompts/operator/MANAGER_REVIEWER.md")
        setup = read("docs/operator/DESIGNER_MANAGER_SETUP.md")
        for text in (architecture, workflow, judge, setup):
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
        workflow = read("docs/agent/TASK_WORKFLOW_DRAFT_REVIEW_APPLY_VERIFY.md")
        getting_started = read("docs/GETTING_STARTED.md")
        profile = read("schemas/PROJECT_PROFILE_CONFIG.md")
        for text in (architecture, workflow, getting_started):
            lowered = text.lower()
            self.assertIn("human transports authority", lowered)
            self.assertIn("repository transports engineering state", lowered)
        self.assertIn("model_routing:", profile)
        self.assertIn("state_handoff:", profile)
        self.assertIn("require_primary_task_ref: true", profile)
        self.assertIn("require_active_task_role: true", profile)
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

    def test_bundle_builder_includes_operator_role_prompts(self) -> None:
        builder = read("scripts/build_agent_bundle.py")
        self.assertIn('"prompts/operator/"', builder)
        self.assertTrue((ROOT / "prompts/operator/INDEPENDENT_JUDGE.md").is_file())

    def test_persian_guide_has_rtl_ltr_and_new_flow(self) -> None:
        text = read("docs/GUIDE.fa.md")
        self.assertGreater(len(re.findall(r"[\u0600-\u06ff]", text)), 1000)
        self.assertTrue(text.startswith('<div dir="rtl" align="right">'))
        self.assertTrue(text.rstrip().endswith("</div>"))
        self.assertNotIn("```", text)
        self.assertGreaterEqual(text.count('<pre dir="ltr" style="text-align:left"'), 10)
        self.assertIn('class="sourceCode bash"', text)
        self.assertIn("MULTI-MODEL AGREEMENT", text)
        self.assertIn("Independent Judge", text)
        self.assertIn("Human transports authority", text)
        self.assertIn("default_max_iterations: 1", text)

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
