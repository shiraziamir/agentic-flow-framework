---
name: test-mutation-proof
description: Prove a load-bearing test can fail by intentionally breaking behavior, then restoring it.
metadata:
  class: RISK_TRIGGERED
  authority: portable-agentic-flow
---

# test-mutation-proof

Use for new tests that carry important safety/correctness claims.

1. Run test green.
2. Make a minimal temporary mutation expected to violate the asserted behavior.
3. Run the target test and observe failure for the intended reason.
4. Restore exactly.
5. Re-run green.
6. Confirm working tree is restored except intended task changes.

## Mutation authority
Temporary controlled mutation only in safe/local test scope.

## Output
Green → mutation → expected red → restore → green receipts.

## Fail closed
A test that never fails under the mutation has not proved the claim.
