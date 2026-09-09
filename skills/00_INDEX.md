# Portable Skills Index

**Version:** 1.3  
**Updated:** 2026-09-09T10:04:00Z

Do not preload the shelf. Default: **0–3 load-bearing skills per task**. A fourth skill should be exceptional and justified by a distinct trigger. Verification profiles under `verification/` are not counted as Skills; load only the profiles selected by change classification.

## CORE

| Skill | Trigger |
|---|---|
| `task-contract` | material task needs explicit scope/DoD/governance/review lifecycle |
| `change-classification` | material change needs FRONTEND/BACKEND/SHARED/DATA/INFRA/CI/etc. surface + cross-cutting risk classification |
| `surface-verification` | material code/config change needs claim-aware verification selected by surface/risk |
| `model-routing` | model/delegation/tier choice is material |
| `context-curation` | non-trivial repo, monorepo, delegation, or context-limit risk |
| `diagnose-before-fix` | failing layer/root cause is not proven |
| `evidence-integrity` | material closure must map DoD/claims to adequate current receipts |
| `durable-context` | long session/handoff/model change/reset/compaction risk |
| `receipts-not-claims` | factual engineering claims need adequate observable evidence/explicit truth boundary |
| `token-efficiency` | long/expensive/multi-agent work needs usage visibility, waste warning, or cheap-worker routing |

## COMMON

| Skill | Trigger |
|---|---|
| `independent-review` | cold/read-only challenge materially improves confidence |
| `blind-spot-audit` | HIGH/evidence-complex MEDIUM closure, broad claims, or false-complete risk |
| `sibling-sweep` | first defect/fix may represent a broader or symmetric class |
| `triage-findings` | 2+ findings or noisy feedback risks silent scope expansion |
| `research-with-provenance` | current external/vendor evidence materially affects a decision |
| `epistemic-decision` | consequential choice remains uncertain after evidence gathering |
| `documentation-freshness` | material verified change may make canonical/index/user docs stale |
| `project-retrospective` | explicit audit/work-reconstruction/governance-analysis request needs timeline, metrics and truth classes from cold durable history |
| `project-storytelling` | user explicitly requests history narrative, architecture story, case study or self-branding; prefer retrospective outputs as input when available |

## RISK_TRIGGERED

| Skill | Trigger |
|---|---|
| `test-mutation-proof` | a load-bearing test itself must be proven capable of failing |
| `live-verification` | runtime/integration/deployment behavior cannot be established statically |
| `systems-under-stress` | I/O/shared state/concurrency/restart/retry/dependency failure is material |

## EXPERIMENTAL

| Skill | Trigger |
|---|---|
| `controlled-agent-experiment` | claiming a model/skill/prompt/route improves quality, cost, latency, or rework |

## Why this is not ranked only by usage frequency

Yara telemetry showed the strongest repeated **observed-association** signals around model routing/delegation, diagnosis-before-fix, sibling/fix audit, and task-contract workflows. That supports making them easy to discover, but it does not establish causality.

Rarely triggered skills are not automatically weak. A concurrency/stress, live-path, mutation-proof, blind-spot audit, retrospective, or storytelling procedure may correctly activate only when its trigger exists.

Promotion/retirement should consider:

1. eligible-trigger denominator, not only raw activations;
2. activation correctness (positive, negative, near-miss);
3. outcome/evidence quality;
4. rework/regression/false-complete prevention;
5. token/cost impact and waste flags where observable;
6. controlled skill-present vs skill-neutralized fixtures when causal claims matter.

## Selection algorithm

1. Start from the approved request/current task/amendment.
2. Use `change-classification` for material work before choosing verification.
3. Load `GENERAL + primary surface + triggered annexes` from `verification/00_INDEX.md`; do not load the whole profile shelf.
4. Use `surface-verification` to map planned claims/DoD to adequate receipts.
5. Select `model-routing` only if model/delegation choice matters.
6. Select `context-curation` when working-set control/delegation is non-trivial.
7. Select `token-efficiency` for long/cost-sensitive/multi-agent work, not as ritual on tiny tasks.
8. Select one diagnosis/failure-mode skill only when that risk exists.
9. Select verification extras (`test-mutation-proof`, `live-verification`, `systems-under-stress`) by risk, not ritual.
10. Use `evidence-integrity` before material closure.
11. Use `blind-spot-audit` for HIGH/evidence-complex closure or broad claims where false confidence is plausible.
12. Use `documentation-freshness` when verified work changes architecture/capability/workflow/docs.
13. Use `independent-review` when independence is part of the assurance argument.
14. `project-retrospective` and `project-storytelling` are cold/on-demand and never normal execution context.
15. Prefer `project-retrospective` first when exact timeline/metrics/governance reconstruction is needed; storytelling may consume that bounded reconstruction instead of raw history.
16. Do not self-activate a newly discovered skill/profile inside a frozen HIGH task when it materially changes strategy/scope/verification; STOP/classify/amend first.

## Claim/report discipline

All material reporting follows `schemas/CLAIM_RECEIPT.md` and `schemas/STATUS_REPORT.md`:

- truth classes: `OBSERVED / DERIVED / INFERRED / UNKNOWN / CONTRADICTED`;
- exact `PASS / FAIL / PARTIAL / SKIPPED / UNVERIFIED` states/counts;
- repository/artifact/environment identity;
- important checks not executed;
- no global/negative claim without a finite verified universe;
- reviewer/model judgment never substitutes for missing behavioral evidence.

Canonical skill IDs are directory names, lowercase kebab-case, with no `.md` suffix.
