# Bootstrap prompt — generic coding agent

**Version:** 1.2  
**Updated:** 2026-09-09T10:04:00Z

Use this after cloning Agentic Flow Framework into a project or making it available as a reference.

```text
You are bootstrapping this repository's agent operating layer.

1. Read, in order:
   - ARCHITECTURE.md
   - schemas/TASK_CONTRACT.md
   - schemas/AMENDMENT.md
   - schemas/CHANGE_CLASSIFICATION.md
   - schemas/CLAIM_RECEIPT.md
   - schemas/EVIDENCE_PACKET.md
   - schemas/STATUS_REPORT.md
   - schemas/PROJECT_LAYOUT.md
   - verification/00_INDEX.md
   - skills/00_INDEX.md
2. Record the canonical architecture version you are generating from.
3. Inspect the target project's existing agent instructions, source layout, project/dependency graph, frontend/backend/shared/data/infra/CI boundaries, build/test mechanics, task/history stores, provider/harness telemetry and model/subagent capabilities. Do not overwrite working project-specific rules blindly and do not create shadow stores when equivalents already exist.
4. Derive a project-local surface map and commands without assuming a specific language/framework. Identify how this project can mechanically find affected consumers/modules.
5. Generate/update the minimum vendor-specific adapter files needed by this harness.
6. Adapters are NON-AUTHORITATIVE. They point to canonical files and must not invent conflicting policy.
7. Keep always-on instructions concise. Do not copy ARCHITECTURE.md, all verification profiles, completed-task history, judgment history, usage ledger, or every skill body into permanent context. Expose skills/tools/history/verification profiles lazily where supported.
8. Preserve risk-adaptive governance: HIGH / MEDIUM / EVIDENCE_ONLY.
9. Preserve the material lifecycle: DRAFT_TASK -> REVIEW_DRAFT -> freeze/authorization -> APPLY_TASK -> VERIFY_AND_REPORT -> required independent closure.
10. Ensure material tasks classify primary surface/cross-cutting risks and freeze planned claim -> minimum receipt requirements before APPLY.
11. Configure semantic roles using capabilities actually available: ORCHESTRATOR / CHEAP_READONLY / EXECUTION_TIER / JUDGMENT_TIER / INDEPENDENT_REVIEWER.
12. Direct reviewers should remain read-only in the review pass and prefer task/diff/raw receipts before executor narrative. Evidence-only reviewers may not upgrade missing evidence.
13. Where observable, wire provider/harness usage counters to the portable usage ledger; where unavailable, document telemetry as UNKNOWN rather than inventing it.
14. Enable/operator-document TOKEN_WASTE_WARNING behavior for long/cost-sensitive work. Cheap workers remain read-only by default and cannot weaken acceptance quality.
15. If structured task/evidence/status JSON/YAML artifacts are used, expose scripts/verification_lint.py as a deterministic check when practical.
16. Preserve hot-state/cold-history separation: ordinary runs discover current task/classification/checkpoint/index without recursively reading completed tasks/judgments/stories/retrospectives.
17. If the harness lacks a feature, document the limitation and preserve conceptual lifecycle using files/prompts instead of pretending the feature exists.
18. Before writing, report the adapter plan and conflicts with existing files.
19. After writing, verify a fresh session can discover:
   - source of truth and canonical version;
   - governance + change-surface classification;
   - verification profile router and claim-receipt rules;
   - DRAFT review / APPLY / VERIFY_AND_REPORT workflow;
   - supervisor workflow;
   - token-efficiency/usage path when applicable;
   - current project state without loading cold history;
   - build/test/affected-project commands;
   without loading the entire framework into permanent context.
20. Return changed paths and a concise validation receipt. Do not start product work.
```
