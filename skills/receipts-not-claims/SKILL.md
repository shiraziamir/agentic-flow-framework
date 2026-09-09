---
name: receipts-not-claims
description: Require factual engineering claims to carry an adequate observable receipt, bounded truth class, identity/freshness boundary, or an explicit unverified label.
metadata:
  class: CORE
  authority: portable-agentic-flow
---

# Receipts, Not Claims

**Updated:** 2026-09-09T10:04:00Z

Use whenever status, diagnosis, implementation, test, deployment, performance, security or closure claims matter.

## Procedure

1. Write the exact bounded claim.
2. Classify it with `schemas/CLAIM_RECEIPT.md`.
3. Assign truth class: `OBSERVED | DERIVED | INFERRED | UNKNOWN | CONTRADICTED`.
4. Determine the minimum receipt rung that directly establishes the claim.
5. Attach receipt(s) with repository/artifact/environment identity and observation time where material.
6. State method/validity boundary.
7. If the receipt is weaker than the claim, narrow the claim or mark it `PARTIAL/UNVERIFIED`.

## Never silently equate

```text
plan/intention                 != implementation
source/config presence         != runtime behavior
unit/component test            != full user/integration flow
HTTP success                   != durable persistence/downstream effect
CI green                       != every relevant check executed
screenshot                     != working interaction
mock success                   != real boundary compatibility
repository commit              != deployed artifact
reviewer/model approval        != behavioral receipt
no observed issue in checks A  != no issue exists anywhere
```

## Negative/global claims

Words like `all`, `none`, `only`, `no regression`, `secure`, `fully tested`, `nothing else` require a finite named universe plus exhaustive method. Otherwise report the bounded check scope.

## Mutation authority

None.

## Output

Claim → truth class → required receipt → actual receipt → validity boundary, with unsupported claims explicitly narrowed/unverified.
