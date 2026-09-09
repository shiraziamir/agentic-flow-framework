# Workflow prompt — RECORD EXECUTION BOUNDARY

**Version:** 1.0  
**Updated:** 2026-09-09T08:22:00Z

Use only for long campaigns/rescues/migrations that have enabled the cold execution ledger.

```text
Append one compact boundary event to the project's execution retrospective ledger.

Read:
1. schemas/EXECUTION_RETROSPECTIVE_LEDGER.md
2. the current task/amendment/checkpoint
3. only the source artifacts needed to prove this boundary

Rules:
- record only a meaningful lifecycle boundary: DRAFT_REVIEW, AMENDMENT, FREEZE, APPLY_START, STOP, EVIDENCE_READY, CLOSURE_REVIEW, CLOSED, or FOLLOWUP_CREATED;
- point to existing commit/task/judgment/evidence/usage artifacts instead of copying their content;
- keep counters short and mechanically derived where possible;
- classify truth_basis as PROVEN, RECONSTRUCTED, or UNKNOWN;
- missing token/cost/provider/time data stays null/UNKNOWN;
- do not store prompts, full model responses, raw logs, transcripts, chain-of-thought, or narrative;
- this ledger is COLD and must not be added to ordinary agent preload/context.

Return the appended event identity and source refs only.
```
