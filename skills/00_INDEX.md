# Portable Skills Index

Do not preload the shelf. Default: **0–3 load-bearing skills per task**. A fourth skill should be exceptional and justified by a distinct trigger.

## CORE

| Skill | Trigger |
|---|---|
| `task-contract` | material task needs explicit scope/DoD/review/freeze/apply lifecycle |
| `model-routing` | model/delegation/tier choice is material |
| `context-curation` | non-trivial repo, monorepo, delegation, or context-limit risk |
| `diagnose-before-fix` | failing layer/root cause is not proven |
| `evidence-integrity` | material closure must be mapped exactly to DoD receipts |
| `durable-context` | long session, handoff, model/provider change, reset/compaction risk |
| `receipts-not-claims` | factual engineering claims need observable evidence |

## COMMON

| Skill | Trigger |
|---|---|
| `independent-review` | cold/read-only challenge materially improves confidence |
| `sibling-sweep` | first defect/fix may represent a broader or symmetric class |
| `triage-findings` | 2+ findings or noisy feedback risks silent scope expansion |
| `research-with-provenance` | current external/vendor evidence materially affects a decision |
| `epistemic-decision` | consequential choice remains uncertain after evidence gathering |

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

Yara's recent skill telemetry showed the strongest repeated **observed-association** signals around model routing/delegation, diagnosis-before-fix, sibling/fix audit, and task-contract workflows. That supports keeping those procedures hot in the router, but it does not establish causality.

Rarely triggered skills are not automatically weak. A concurrency/stress, cache/live-path, or mutation-proof procedure may correctly activate only once in many tasks. Risk-triggered skills should stay cold until their specific risk exists.

Promotion/retirement should consider:

1. eligible-trigger denominator, not only raw activations;
2. activation correctness (positive, negative, near-miss);
3. outcome evidence level;
4. rework/regression/verification quality;
5. controlled skill-present vs skill-neutralized fixtures when causal claims matter.

## Selection algorithm

1. Start from the approved task and its risks.
2. Select `model-routing` only if model/delegation choice matters.
3. Select `context-curation` when working-set control/delegation is non-trivial.
4. Select one diagnosis/failure-mode skill only when that risk exists.
5. Select verification by risk, not ritual.
6. Use `evidence-integrity` before material closure.
7. Use `independent-review` when independence is part of the assurance argument.
8. Do not self-activate a newly discovered skill inside a frozen task; STOP/amend when it would materially alter strategy or scope.

Canonical skill IDs are directory names, lowercase kebab-case, with no `.md` suffix.
