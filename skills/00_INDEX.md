# Portable Skills Index

**Version:** 1.4  
**Updated:** 2026-09-09T10:40:00Z

Do not preload the shelf. Default: **0–3 load-bearing skills per task**. A fourth skill should be exceptional and justified by a distinct trigger. Verification profiles under `verification/` and production profiles under `production/` are not counted as Skills; load only selected profiles.

## CORE

| Skill | Trigger |
|---|---|
| `task-contract` | material task needs explicit scope/DoD/governance/review lifecycle |
| `change-classification` | material change needs engineering surface + cross-cutting/operational risk classification |
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
| `production-readiness` | project/service is production-bound or a change affects DevOps/security/observability/recovery posture |
| `evolvable-architecture` | module/provider/shared-contract boundaries materially affect changeability/testability |
| `independent-review` | cold/read-only challenge materially improves confidence |
| `blind-spot-audit` | HIGH/evidence-complex MEDIUM closure, broad claims, or false-complete risk |
| `sibling-sweep` | first defect/fix may represent a broader or symmetric class |
| `triage-findings` | 2+ findings or noisy feedback risks silent scope expansion |
| `research-with-provenance` | current external/vendor evidence materially affects a decision |
| `epistemic-decision` | consequential choice remains uncertain after evidence gathering |
| `documentation-freshness` | material verified change may make canonical/index/user docs stale |
| `project-retrospective` | explicit audit/work-reconstruction/governance-analysis request needs timeline, metrics and truth classes from cold history |
| `project-storytelling` | user explicitly requests history narrative/case study/self-branding; prefer retrospective inputs when available |

## RISK_TRIGGERED

| Skill | Trigger |
|---|---|
| `ai-log-analysis` | logs/telemetry are supplied to an LLM/agent for production diagnosis or summarization |
| `resilience-chaos` | failure/recovery behavior or a fault-injection/chaos experiment needs proof |
| `test-mutation-proof` | a load-bearing test itself must be proven capable of failing |
| `live-verification` | runtime/integration/deployment behavior cannot be established statically |
| `systems-under-stress` | I/O/shared state/concurrency/restart/retry/dependency failure is material |

## EXPERIMENTAL

| Skill | Trigger |
|---|---|
| `controlled-agent-experiment` | claiming a model/skill/prompt/route improves quality, cost, latency, or rework |

## Selection algorithm

1. Start from the approved request/current task/amendment.
2. Use `change-classification` for material work before choosing verification/production profiles.
3. Load `GENERAL + primary surface + triggered annexes` from `verification/00_INDEX.md`.
4. If project is production-bound or posture can change, consult current `schemas/PRODUCTION_PROFILE.md` artifact and `production/00_INDEX.md`; load only triggered production profiles.
5. Use `surface-verification` to map planned claims/DoD to adequate receipts.
6. Use `production-readiness` for launch/readiness/posture review, not on every tiny edit.
7. Use `evolvable-architecture` only when a real long-term change/coupling boundary exists.
8. Select `model-routing`, `context-curation` and `token-efficiency` only when those concerns are material.
9. Select diagnosis/failure-mode skills by risk, not ritual.
10. `ai-log-analysis` is mandatory when untrusted telemetry is intentionally fed to a tool-enabled AI workflow unless an equivalent project control exists.
11. `resilience-chaos` is maturity/risk-triggered; production chaos is never a default requirement.
12. Use `evidence-integrity` before material closure and `blind-spot-audit` when false confidence is plausible.
13. Use `documentation-freshness` after material architecture/workflow/readiness changes.
14. Use `independent-review` when independence is part of the assurance argument.
15. Retrospective/storytelling skills remain cold/on-demand.
16. Do not self-activate a newly discovered Skill/profile inside a frozen HIGH task when it materially changes strategy/scope/authority; STOP/classify/amend first.

## Production-readiness discipline

A production-capable repository should expose a compact current profile rather than forcing agents to infer posture from scattered files. Scale and assurance are separate:

```text
codebase_scale   SMALL | MEDIUM | LARGE
readiness_tier   BASIC | STANDARD | HIGH_ASSURANCE
```

Risk overrides size. Material absent/partial/unverified production requirements are durable operational gaps, not hidden TODOs or optimistic prose.

## Claim/report discipline

All material reporting follows `schemas/CLAIM_RECEIPT.md` and `schemas/STATUS_REPORT.md`:

- truth classes: `OBSERVED / DERIVED / INFERRED / UNKNOWN / CONTRADICTED`;
- exact `PASS / FAIL / PARTIAL / SKIPPED / UNVERIFIED` states/counts;
- repository/artifact/environment identity;
- important checks not executed;
- no global/negative claim without a finite verified universe;
- reviewer/model judgment never substitutes for missing behavioral evidence;
- production-readiness claims name profile/tier and open gaps.

Canonical skill IDs are directory names, lowercase kebab-case, with no `.md` suffix.