# Workflow prompt — REVIEW DRAFT

**Version:** 1.0  
**Updated:** 2026-09-09T10:04:00Z

```text
Review the DRAFT task contract. Do not APPLY or edit product code.

Read, in order:
1. ARCHITECTURE.md
2. the DRAFT task
3. schemas/CHANGE_CLASSIFICATION.md
4. schemas/CLAIM_RECEIPT.md
5. verification/00_INDEX.md and only selected profiles/annexes
6. relevant project architecture/dependency/source evidence needed to challenge the draft

Review questions:
- Is governance proportional to actual risk?
- Is the primary surface/change kind/cross-cutting classification supported by actual paths/dependencies/contracts?
- Are affected consumers/systems/environments missing?
- Is the goal/DoD observable rather than implementation-only?
- Does every material planned closure claim have an adequate receipt plan?
- Does the verification plan match FRONTEND/BACKEND/SHARED/DATA/INFRA/CI/etc. reality?
- Are relevant negative/error/auth/persistence/live/failure paths omitted?
- Are any claims global/absolute without a finite verification universe?
- Are any required checks being replaced by a weaker proxy?
- Are STOP/reclassification/escalation conditions sufficient to prevent scope creep?
- Are important checks intentionally not required stated explicitly?
- Does closure need a cold independent reviewer/blind-spot audit?
- Is the plan wasting expensive model/context where deterministic or cheap read-only work can preserve quality?

Return exactly one disposition:
- ACCEPT_DRAFT
- AMEND_DRAFT
- NEEDS_EVIDENCE
- REJECT_DRAFT

For non-acceptance, return bounded findings with required amendments/evidence. Do not silently rewrite and approve the task in the same pass unless the owner workflow explicitly authorizes that behavior.

ACCEPT_DRAFT freezes the reviewed contract/version/hash. It does not authorize APPLY unless the active governance explicitly combines those gates.
```
