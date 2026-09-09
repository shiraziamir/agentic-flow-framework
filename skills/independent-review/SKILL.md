---
name: independent-review
description: Perform a cold, read-only, falsification-first challenge of a draft, diff, evidence packet or closure claim without substituting reviewer opinion for missing receipts.
metadata:
  class: COMMON
  authority: portable-agentic-flow
---

# Independent Review

**Updated:** 2026-09-09T10:04:00Z

Use when independence materially improves confidence.

## Independence levels

- `SELF_REVIEW` — useful local hygiene; not independent closure.
- `COLD_SAME_MODEL` — separate context/session, no implementation memory.
- `COLD_DIFFERENT_MODEL_OR_HUMAN` — stronger independence where risk/ambiguity warrants it.

A more expensive model is not automatically a better reviewer; use a clear rubric/DoD, adequate receipts and the minimum capable judgment tier.

## Review order — reduce anchoring

When direct access exists, prefer:

1. frozen task/DoD + classification/verification profiles;
2. actual base/head diff and source;
3. raw/bounded receipts and check results;
4. independently selected falsifying/spot checks;
5. executor status/narrative last, then compare claims to observed reality.

Do not start from `executor says everything passes` if independent inspection is possible.

## Direct access

- verify ref/artifact/environment identity;
- inspect actual diff/source/tests;
- check actual surface/consumer classification;
- reproduce falsifying checks where practical;
- inspect important skipped/not-run checks;
- use `blind-spot-audit` for HIGH or evidence-complex closure;
- remain read-only during the review pass.

## Evidence-only access

- consume `schemas/EVIDENCE_PACKET.md`;
- check claim receipt strength/identity/freshness;
- mark non-verifiable items `UNVERIFIED_FROM_PACKET`;
- request missing artifacts instead of guessing;
- do not upgrade packet claims merely because the executor/reviewer is confident.

## Judgment boundary

Reviewer output is a `JUDGMENT` receipt: evidence that a review decision was made. It does **not** replace the underlying test/live/persistence/deployment/security receipt needed for the behavioral claim.

## Mutation authority

NONE. Reviewer must not repair the work it is judging in the same review pass.

## Output

`PASS | FAIL | INCONCLUSIVE`, independence level, findings, falsifying checks, missing/stale evidence, claims that must be narrowed and recommended disposition.
