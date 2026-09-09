---
name: surface-verification
description: Build and execute the minimum sufficient verification plan for the classified frontend, backend, shared, data, infra/CI, tooling/docs and cross-cutting risk surfaces.
metadata:
  class: CORE
  authority: portable-agentic-flow
---

# Surface Verification

**Updated:** 2026-09-09T10:04:00Z

## USE WHEN

A material code/config change needs a verification plan or evidence collection.

## PROCEDURE

1. Read the frozen classification and `verification/00_INDEX.md`.
2. Load `GENERAL` + primary surface + only triggered annexes.
3. Enumerate the claims the task expects to make at closure.
4. For each claim, use `schemas/CLAIM_RECEIPT.md` to select the minimum receipt that directly establishes it.
5. Prefer deterministic/build/focused checks before broader live checks; use broader checks when the claim requires them.
6. Record artifact/ref/environment identity for every material receipt.
7. Record important checks not executed and why.
8. If the planned verification cannot establish a frozen DoD claim, STOP/amend rather than replacing it silently with a proxy.
9. Produce `schemas/STATUS_REPORT.md` plus evidence refs.

## QUALITY RULE

A lower-level receipt never inherits the authority of a higher-level claim. Examples:

- static source inspection != runtime behavior;
- unit test != frontend user flow;
- HTTP success != persistence;
- CI green != proof every relevant job/test executed;
- reviewer approval != behavioral evidence.

## MUTATION AUTHORITY

Verification itself is read-only except for explicitly authorized test fixtures/testenv operations in the frozen task.

## OUTPUT

Claim → required receipt → actual receipt matrix, executed/not-executed checks, unknowns and residual risks.
