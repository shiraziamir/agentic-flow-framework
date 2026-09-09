---
name: change-classification
description: Classify a material change by primary engineering surface, change kind, mutation scope and cross-cutting risk so governance and verification are selected before implementation.
metadata:
  class: CORE
  authority: portable-agentic-flow
---

# Change Classification

**Updated:** 2026-09-09T10:04:00Z

## USE WHEN

A material task is drafted or an amendment discovers a new affected surface/risk.

## PROCEDURE

1. Inspect paths/project graph/imports/contracts/config mechanically where possible.
2. Fill `schemas/CHANGE_CLASSIFICATION.md`.
3. Select one primary surface and only applicable cross-cutting flags.
4. Identify affected consumers and mutation scope.
5. Route verification using `verification/00_INDEX.md`.
6. Raise governance when security/persistence/public-contract/migration/production semantics require it.
7. If APPLY reveals a materially undeclared surface/flag, STOP and amend before expanding verification or mutation.

## DO NOT

- classify from filename alone when dependency evidence contradicts it;
- hide a shared/public-contract change inside `FRONTEND` or `BACKEND`;
- downgrade risk to save tokens/test time;
- load every verification profile.

## MUTATION AUTHORITY

None by itself. Classification does not authorize APPLY.

## OUTPUT

A durable change-classification ref plus selected verification profiles and any governance escalation.
