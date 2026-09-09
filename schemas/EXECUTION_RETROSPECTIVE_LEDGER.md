# Execution Retrospective Ledger Schema

**Purpose:** keep a compact, append-only, cold-history record that makes later project reconstruction possible without forcing everyday agents to reread full history.

This ledger is not a task board and not runtime authority. It records durable boundary facts only.

Recommended target-project path:

```text
.agentic/history/EXECUTION_LEDGER.jsonl
```

Each line is one JSON object:

```json
{
  "schema_version": "1",
  "timestamp": "2026-09-09T12:00:00Z",
  "task_id": "TASK-123",
  "boundary": "DRAFT_REVIEW|AMENDMENT|FREEZE|APPLY_START|STOP|EVIDENCE_READY|CLOSURE_REVIEW|CLOSED|FOLLOWUP_CREATED",
  "governance_class": "HIGH|MEDIUM|EVIDENCE_ONLY",
  "commit_refs": [],
  "contract_ref": null,
  "contract_hash": null,
  "judgment_refs": [],
  "evidence_refs": [],
  "tests": {
    "focused_passed": null,
    "focused_failed": null,
    "suite_passed": null,
    "suite_failed": null
  },
  "stop_or_amendment_reason": null,
  "mutation_accounting": {
    "repository": null,
    "test_environment": null,
    "production": null,
    "provider_calls": null
  },
  "token_usage_ref": null,
  "outcome": "<short factual outcome>",
  "truth_basis": "PROVEN|RECONSTRUCTED|UNKNOWN"
}
```

## Truth classes

- `PROVEN` — directly supported by Git, immutable/durable artifact, test receipt, provider usage record, or equivalent mechanical evidence.
- `RECONSTRUCTED` — supported by owner journal, timestamped receipts, or other secondary durable evidence but not fully mechanically provable.
- `UNKNOWN` — not logged reliably. Never fabricate a number to fill the gap.

## Recording rules

- Append at meaningful boundaries, not every agent turn.
- Keep entries concise. Point to evidence; do not duplicate diffs, logs, judgments, prompts, or transcripts.
- Never store chain-of-thought, private deliberation, raw prompts, or full model responses.
- A supervisor result should be referenced by durable decision ID/path, not copied in full.
- Token/cost values may be `null`/`UNKNOWN` when the provider or harness does not expose trustworthy data.
- Retrospective metrics must be derived from this ledger plus primary artifacts; the ledger itself must not become a narrative summary.

## Cold-history rule

Normal task execution MUST NOT preload this ledger. Read it only for explicit history/audit/retrospective/storytelling/governance-analysis requests, or when a specific historical decision is required and cannot be resolved from the active task artifacts.
