---
name: task-contract
description: Draft, review, freeze, amend, authorize, verify and close bounded task contracts with surface classification and claim-to-receipt planning.
metadata:
  class: CORE
  authority: portable-agentic-flow
---

# Task Contract

**Updated:** 2026-09-09T10:04:00Z

Use when a material task needs explicit scope/DoD or the user asks to draft/apply reviewed work.

Do not use full HIGH ceremony for a tiny reversible edit where a formal gate adds no risk value.

## Workflow

1. State observed symptom separately from hypotheses.
2. Classify governance and engineering surface/risk using `schemas/CHANGE_CLASSIFICATION.md`.
3. Define goal, edit/reference/excluded sets, baseline, uncertainties and observable DoD.
4. Enumerate material closure claims and map each to a minimum adequate receipt using `schemas/CLAIM_RECEIPT.md`.
5. Select GENERAL + primary verification surface + only triggered annexes.
6. Select the smallest relevant Skill packet.
7. Produce a DRAFT and stop for `REVIEW_DRAFT` when required.
8. Draft review challenges classification, affected consumers, DoD, claim/receipt sufficiency, omitted checks and STOP conditions.
9. Freeze the accepted bytes/version/hash.
10. Treat APPLY authorization as separate from drafting/freeze unless governance explicitly combines them.
11. During APPLY, STOP on material new surface/consumer/risk/strategy or when frozen receipt requirements cannot be met.
12. Amendment updates classification/claims/verification plan when affected; never silently rewrite frozen authority.
13. After implementation use surface verification + reality report/evidence packet; executor reaches EVIDENCE_READY, not CLOSED.
14. Closure requires adequate current DoD/claim receipts plus required independent judgment.

## Mutation authority

Drafting/review: none. Execution authority comes only from active authorized task/amendment.

## Evidence

Contract/classification ref/version/hash, draft-review decision, amendment history, authorization, status/evidence refs and closure decision.

## Fail closed

- Never silently rewrite a frozen contract.
- Never silently substitute a weaker receipt/gate.
- Never absorb a newly discovered material surface/risk without STOP/amendment.

## Output

A task conforming to `schemas/TASK_CONTRACT.md`, linked to classification and receipt-aware verification artifacts.
