# Workflow prompt — AMEND TASK

**Version:** 1.1  
**Updated:** 2026-09-09

```text
Amend the existing task only in response to the supplied supervisor/owner decision or new durable evidence.

Read:
- ARCHITECTURE.md
- schemas/AMENDMENT.md
- the current task contract
- relevant supervisor decision/new evidence

First classify the amendment:
- HIGH: materially changes architecture, persistence, security/trust, production semantics, durable data, public contract, or grants major new authority;
- MEDIUM: bounded same-task correction requiring execution;
- EVIDENCE_ONLY: wording/evidence/test-contract/docs correction with no new runtime authority.

Rules:
- preserve the original task identity;
- make the smallest amendment that addresses the finding;
- do not use amendment as permission for unrelated cleanup or Task N+1;
- record version/timestamp, reason, exact delta, scope, STOP conditions, required tests/evidence and durable hash/ref;
- HIGH follows the full freeze/re-authorization discipline;
- MEDIUM uses owner-approved amendment + bounded apply + required tests/evidence + closure review;
- EVIDENCE_ONLY does not repeat freeze/apply ceremony unless execution/mutation follows;
- if classification is uncertain in a way that affects safety, escalate rather than downgrade;
- STOP after producing/approving the amendment unless execution is authorized by its governance path.

Return old ref, amendment ref/version/hash, governance classification, exact delta, and next authorization required.
```
