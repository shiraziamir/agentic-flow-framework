# Workflow prompt — AMEND TASK

**Version:** 1.2  
**Updated:** 2026-09-09T10:04:00Z

```text
Amend the existing task only in response to supplied supervisor/owner decision or new durable evidence.

Read:
- ARCHITECTURE.md
- schemas/AMENDMENT.md
- schemas/CHANGE_CLASSIFICATION.md
- schemas/CLAIM_RECEIPT.md
- the current task contract + classification
- relevant supervisor decision/new evidence
- current selected verification profiles when affected

First classify the amendment governance:
- HIGH: materially changes architecture, persistence, security/trust, production semantics, durable data, public contract, or grants major new authority;
- MEDIUM: bounded same-task correction requiring execution;
- EVIDENCE_ONLY: wording/evidence/test-contract/docs correction with no new runtime authority.

Then check whether the amendment changes any of:
- primary surface / cross-cutting risk / affected consumers / mutation environment;
- DoD or planned closure claims;
- minimum receipt required for a claim;
- selected verification profiles/annexes;
- important checks out of scope;
- STOP/escalation conditions.

Rules:
- preserve original task identity;
- make the smallest amendment that addresses the finding;
- do not use amendment for unrelated cleanup or Task N+1;
- record version/timestamp, reason, exact delta, scope, classification delta, claim/receipt delta, STOP conditions, required tests/evidence and durable hash/ref;
- HIGH follows full freeze/re-authorization discipline;
- MEDIUM uses owner-approved amendment + bounded apply + required verification/evidence + closure review;
- EVIDENCE_ONLY does not repeat freeze/apply ceremony unless execution/mutation follows;
- if a new surface/risk changes verification authority, amend/re-freeze the verification plan before APPLY;
- if classification is uncertain in a way that affects safety/receipt sufficiency, escalate rather than downgrade;
- STOP after producing/approving amendment unless execution is authorized by its governance path.

Return old ref, amendment ref/version/hash, governance classification, classification/claim/verification delta, exact scope delta, and next authorization required.
```
