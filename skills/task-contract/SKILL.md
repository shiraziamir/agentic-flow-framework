---
name: task-contract
description: Draft, review, freeze, amend, authorize, and close bounded task contracts.
metadata:
  class: CORE
  authority: portable-agentic-flow
---

# task-contract

Use when a material task needs explicit scope/DoD or when the user asks to draft/apply work.

Do not use for a tiny reversible edit where a formal review gate adds no value.

## Workflow
1. Restate the symptom, not an assumed diagnosis.
2. Define goal, edit/reference/excluded sets, baseline, uncertainties and DoD.
3. Select the smallest relevant skill packet.
4. Produce a DRAFT and stop for supervisor/owner review when required.
5. Freeze the accepted bytes/version.
6. Treat APPLY authorization as separate from drafting/freeze.
7. If execution disproves scope/strategy, STOP and request amendment.
8. Closure requires DoD-to-receipt mapping.

## Mutation authority
Drafting: none. Execution authority comes only from the active task contract.

## Evidence
Contract ref/version, amendment history, authorization receipt, closure decision.

## Fail closed
Never silently rewrite a frozen contract.

## Output
A task conforming to `schemas/TASK_CONTRACT.md`.
