# A/B Trial 001 — TenantRAG Mini

**Purpose:** compare a normal coding-agent workflow against Agentic Flow 1.11 on the same realistic project evolution.

This experiment is pre-registered before either implementation starts. Do not change the product queue, scoring rubric, freeze point, or evaluator oracle after seeing one arm's output.

## Two arms

| Arm | Repository | Bootstrap |
|---|---|---|
| A — Baseline | `tenant-rag-baseline` | normal coding-agent workflow; no Agentic Flow concepts/instructions |
| B — Agentic Flow | `tenant-rag-agentic` | Agentic Flow 1.11, `PRODUCT_STANDARD`, repository-first state, risk-adaptive Dual-Lens |

Both arms receive the **same project spec and the same 12 product prompts in the same order**. The same model/harness, machine class, tool access, network policy, and starting repository state should be used where practical. The Flow arm may use fresh role contexts because that is part of the treatment, but model/provider upgrades are not allowed unless the same upgrade is made available to the baseline arm and recorded.

## Why this project

TenantRAG Mini is deliberately small enough to finish yet rich enough to expose real engineering failure modes:

- API behavior and persistence;
- multi-tenant isolation;
- cache invalidation;
- authoritative cost accounting;
- restart/recovery semantics;
- external-provider retry/failure behavior;
- concurrency/idempotency;
- admin operations;
- observability;
- backup/restore and deployment/rollback.

A toy calculator would not exercise the framework. A full production RAG platform would make the experiment mostly about project size. This sits in between.

## Fixed experiment sequence

```text
prepare two empty repos from the same seed
→ apply arm-specific bootstrap once
→ release Queue item 01
→ agent completes + commits + records metrics
→ release 02 ... 12 in order
→ FREEZE immediately after Queue 12 closure
→ no fixes after freeze
→ run evaluator/oracle against both frozen heads
→ compare raw metrics + defects + evidence quality
```

### Prompt count

**Freeze after 12 product prompts.**

Twelve is intentional: prompts 1–4 create the product core; 5–8 introduce system-truth and failure-semantics pressure; 9–11 exercise concurrency/recovery/release engineering; prompt 12 is a release-candidate hardening pass. It is long enough for architecture and attention drift to appear, but short enough to repeat later.

## Blindness / queue discipline

Best experiment mode: an operator or queue runner releases one prompt at a time. The implementation agent must not see future prompt bodies.

If running fully autonomously from the stored queue, both arms must receive the same full queue visibility. Record that as a limitation because future-task visibility can improve architectural anticipation.

Evaluator files are **not implementation input**. Do not expose `EVALUATOR_ORACLE.md` to either implementation agent before freeze.

## Human intervention rule

Default: **zero corrective prompts** beyond the 12 queue items.

If an arm is truly blocked, the operator may answer a factual environment question. Record every such message as `human_intervention`. Do not coach one arm on architecture, bugs, tests, or next steps unless the identical information is supplied to both arms before either uses it.

## Commit rule

Each queue item ends with at least one identifiable commit whose message begins:

```text
Q01 ...
Q02 ...
...
Q12 ...
```

Extra internal commits are allowed and counted. Do not squash before freeze.

## What counts as the treatment

Only Arm B is told to use Agentic Flow. The **product requirements remain identical**.

Arm A may use ordinary good engineering judgment, tests, refactoring, and code review habits. It must not be intentionally handicapped.

Arm B must not receive secret evaluator knowledge. Agentic Flow may add its own durable artifacts, contracts, receipts, System Truth Map, reviews, or role handoffs as required by its current policy.

## Primary hypotheses

1. Agentic Flow will reduce escaped material defects and system-truth failures at the frozen head.
2. It will especially improve tenant isolation, cost authority, restart/recovery, failure semantics, production-readiness evidence, and attention/scope control.
3. It may consume more tokens/tool calls/time. The comparison must report that overhead rather than hiding it.
4. A useful win is not “more documents”; it is a better quality/effort trade-off.

## Files

- `PROJECT_SPEC.md` — identical product contract for both arms.
- `QUEUE.md` — the 12 product prompts, fixed order.
- `BASELINE_BOOTSTRAP.md` — launch instruction for Arm A.
- `AGENTIC_FLOW_BOOTSTRAP.md` — launch instruction for Arm B.
- `METRICS_AND_SCORING.md` — pre-registered metrics and comparison method.
- `FREEZE_AND_COMPARE.md` — exact freeze/evaluation procedure.
- `EVALUATOR_ORACLE.md` — evaluator-only acceptance/fault model; do not give to implementation agents before freeze.
- `RUN_RECORD.template.md` — copy once per arm and fill during execution.
- `OPERATOR_LAUNCH.md` — operator steps for a fair run.

## Experiment validity warnings

This is a paired engineering trial, not a statistically powered study. One run can reveal concrete strengths, friction, and failure classes; it cannot prove universal superiority. Repeat with different project shapes and, ideally, swap execution order to reduce learning/carryover effects.
