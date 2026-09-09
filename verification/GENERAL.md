# Verification Profile — GENERAL

**Version:** 1.0  
**Updated:** 2026-09-09T10:04:00Z

Use for every material code/config change before adding the primary surface profile.

## Identity first

Capture:

- base/head commit or exact working-tree identity;
- dirty/untracked state that could affect results;
- changed path list/diff scope;
- build/image/artifact identity when relevant;
- target environment/config identity for live checks.

A receipt without identity is weak because it may describe a different revision/environment.

## Minimum checks

1. Confirm the observed problem/baseline where reproducible.
2. Inspect actual diff, not only executor summary.
3. Run the project’s applicable syntax/lint/type/build checks.
4. Run focused tests for changed behavior.
5. Run affected/baseline checks frozen by the task.
6. Establish changed-path execution when a passing test could bypass/cache/mock the changed path.
7. Check unexpected changed files/generated artifacts/config drift.
8. Record failures/skips/not-run checks separately.

## General blind spots

- test passed against stale build/cache/artifact;
- test never exercised the changed branch;
- generated output differs from source or was not regenerated;
- wrong worktree/ref/environment was tested;
- proxy check substituted for frozen acceptance gate;
- mock/fake proves only the fake interaction, not the real boundary;
- baseline already failed and new failure was misclassified;
- flaky retry converted nondeterminism into an apparent pass;
- global/negative claim made without a defined universe;
- reviewer opinion substituted for behavioral evidence;
- executor summary omitted an unexpected diff or skipped check.

## Report

Use `schemas/STATUS_REPORT.md` and `schemas/CLAIM_RECEIPT.md`.
