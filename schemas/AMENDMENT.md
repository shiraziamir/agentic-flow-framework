# Amendment Schema

**Schema version:** 1.0  
**Updated:** 2026-09-09

An amendment changes an already-approved task without pretending it is a new task. Its ceremony depends on the task governance level and the amendment's effect.

```yaml
amendment_id: <stable-id>
task_id: <existing-task-id>
created_at: <RFC3339 timestamp>
version: <integer or semver>
governance: MEDIUM|EVIDENCE_ONLY
owner_approved: true|false
reason: <new evidence or correction>
changes:
  scope: []
  definition_of_done: []
  evidence_contract: []
  wording_only: []
new_runtime_authority: true|false
requires_execution: true|false
required_tests: []
stop_conditions: []
source_refs: []
content_hash: <hash/ref when frozen>
status: DRAFT|APPROVED|APPLIED|SUPERSEDED
```

Rules:

- `EVIDENCE_ONLY` is valid only when the change grants no new runtime/mutation authority and does not alter product behavior.
- `MEDIUM` may authorize a bounded same-task correction, but it must preserve the original task identity and closure gate.
- If scope, architecture, persistence, production semantics, security boundary, or durable data authority changes materially, escalate to `HIGH` governance and use the full task lifecycle.
- An amendment never authorizes Task N+1 or silent scope expansion.
- Keep one durable amendment artifact with identity/hash instead of reproducing the whole original lifecycle as duplicate receipts.
