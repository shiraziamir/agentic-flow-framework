---
name: token-efficiency
description: Control token/context waste, record usage when observable, warn the operator on waste patterns, and route bounded low-risk work to cheaper workers without lowering acceptance quality.
---
# Token Efficiency and Waste Guard

**Class:** CORE for long/expensive tasks; otherwise COMMON  
**Updated:** 2026-09-09

## USE WHEN
- the task is long-running, multi-agent, monorepo-scale, or cost-sensitive;
- context limits or repeated compaction/reset occur;
- a strong model is being used for large amounts of discovery/mechanical work;
- usage telemetry is available from the provider/harness;
- the operator asks for token/cost accountability.

## DO NOT USE WHEN
A tiny bounded task has negligible context/cost and no meaningful routing decision.

## RULES
1. **Deterministic first.** Use graph queries, grep/AST, linters, test selection, parsers, and scripts before asking a model to rediscover mechanically derivable facts.
2. **Small working set.** Do not scan/read the whole repository unless dependency evidence or the task contract justifies it.
3. **Cheap read-only workers.** Discovery, inventory, log reduction, repetitive classification, and independent partitions may use a cheaper model when quality can be mechanically checked. No mutation authority by default.
4. **Acceptance quality is invariant.** Cheap routing may change who gathers evidence; it must not silently weaken DoD, tests, review, or security boundaries.
5. **Escalate on uncertainty.** Ambiguous root cause, public-contract changes, security/data changes, conflicting evidence, or repeated failed loops move to the stronger justified tier.
6. **Compact handoff.** Pass conclusions, files, receipts, unresolved facts, and next action—not child transcripts.
7. **Do not read cold history by default.** Use current task/checkpoint/index. Historical task/judgment/usage logs are on-demand.
8. **Control tool context.** Prefer lazy/deferred tool loading when available; batch/programmatic tool calls when intermediate results add no value; trim stale large tool results where the harness supports it.
9. **Cache stable prefixes when supported, but never call caching compression.** Cached tokens may still occupy context.
10. **Record observable usage.** Write provider/harness usage fields to the usage ledger when available; otherwise record unknown rather than estimate falsely.

## OPERATOR WARNING CONTRACT
Emit a visible `TOKEN_WASTE_WARNING` before continuing when one or more of these are materially true and not already authorized:

- whole-repo scan without scope/dependency justification;
- repeated large-file rereads that could use a durable summary/index;
- full completed-task/judgment history loaded for ordinary execution;
- large raw logs pasted/read when filtering could isolate the relevant slice;
- expensive/judgment model used primarily for mechanical discovery;
- parallel child agents overlap substantially on the same search surface;
- more than two materially failed execution loops without new discriminating evidence;
- large unused tool definitions remain permanently loaded when lazy discovery exists;
- the task exceeds its declared soft budget or is trending to exceed the hard budget.

Warning format:

```text
TOKEN_WASTE_WARNING
reason: <observable pattern>
current evidence: <usage/path/tool receipts>
cheaper/smaller alternative: <concrete action>
quality guard: <how acceptance quality remains unchanged>
operator decision needed: yes|no
```

For a hard budget breach or a proposed quality tradeoff, STOP for operator/judgment approval. A soft-budget breach may continue only with an explicit recorded reason.

## OUTPUT
- current task budget state;
- route used by phase/model role;
- any waste warnings;
- usage-event receipts when observable;
- optimization action and quality guard.

## EVIDENCE
Use `schemas/USAGE_EVENT.md`. Do not store prompts, chain-of-thought, or raw transcripts.
