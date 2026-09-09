# Workflow prompt — AMEND TASK

```text
Amend the existing frozen/draft task only in response to the supplied supervisor decision or new durable evidence.

Read:
- ARCHITECTURE.md
- the current task contract
- schemas/SUPERVISOR_DECISION.md
- the supervisor decision/new evidence

Rules:
- preserve unchanged contract sections exactly where possible;
- make the smallest amendment that addresses the finding;
- do not use amendment as permission for unrelated cleanup;
- if the new evidence changes strategy, scope, DoD, baseline, skill set, or authority, make that change explicit;
- record what changed and why;
- re-freeze/re-authorize only according to the active owner workflow;
- STOP after producing the amended contract unless APPLY is separately authorized.

Return old ref, new ref, amendment delta, and next authorization required.
```
