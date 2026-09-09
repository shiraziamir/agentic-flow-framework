---
name: evidence-integrity
description: Audit every closure claim against exact Definition-of-Done requirements, adequate receipt strength, identity/freshness and the frozen surface verification plan.
metadata:
  class: CORE
  authority: portable-agentic-flow
---

# Evidence Integrity

**Updated:** 2026-09-09T10:04:00Z

Use before material closure, especially with frozen batteries, benchmarks, acceptance gates, user-visible/runtime/security/persistence claims, or statements like `all tests pass`.

## Procedure

1. Enumerate exact frozen DoD items and planned claims.
2. Confirm change classification and selected verification profiles still match the actual diff/affected consumers.
3. Map each claim to its minimum receipt using `schemas/CLAIM_RECEIPT.md`.
4. Map each DoD/claim to current receipts.
5. Check repository/artifact/environment identity and evidence freshness.
6. Preserve counts and statuses: if M of N pass, report M/N plus FAIL/PARTIAL/SKIPPED/UNVERIFIED items.
7. Check that the changed path/real boundary was actually exercised where bypass/cache/mock risk exists.
8. Check methodology identity and baseline comparability.
9. Check negative/global claims have a finite universe/exhaustive method or are narrowed.
10. Check important verification-profile paths that were not executed are explicitly reported.
11. Ensure `JUDGMENT` is not standing in for missing behavioral evidence.

## Fail closed

- Missing receipt → not VERIFIED.
- Receipt below required rung → PARTIAL/UNVERIFIED.
- Stale receipt after material mutation → reverify or establish continued validity.
- Unexpected material surface/consumer/risk → amendment/reclassification before closure.

## Mutation authority

READ ONLY.

## Output

`COMPLETE | INCOMPLETE | CONTRADICTED` plus DoD/claim-to-receipt matrix, profile coverage, stale/missing evidence, checks not executed and residual risks.
