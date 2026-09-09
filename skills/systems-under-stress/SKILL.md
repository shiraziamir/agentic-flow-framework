---
name: systems-under-stress
description: Review concurrency, restart, dependency failure, shared-state, and load behavior before shipping affected paths.
metadata:
  class: RISK_TRIGGERED
  authority: portable-agentic-flow
---

# systems-under-stress

Use when request-path code touches I/O, shared state, locks, queues, external dependencies, retries, or multi-worker behavior.

Ask:
- blocking I/O on event loop?
- read/modify/write race?
- restart returns empty/stale state?
- reconciliation exists?
- timeout cancels downstream work or only the waiter?
- fail open/closed and observable?
- idempotency/retry effects?

## Mutation authority
None by itself.

## Output
Risk matrix, falsifying stress tests, unresolved architecture questions.
