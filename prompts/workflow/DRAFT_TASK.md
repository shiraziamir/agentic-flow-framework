# Workflow prompt — DRAFT TASK

```text
Create a DRAFT task contract for my request. Do not execute the task.

Authority/read order:
1. ARCHITECTURE.md
2. schemas/TASK_CONTRACT.md
3. skills/00_INDEX.md
4. only the project files/skills necessary to understand this request

Requirements:
- state the observed symptom separately from hypotheses;
- define goal, EDIT_SET, REFERENCE_SET, EXCLUDED_SET and baseline;
- write Definition of Done before implementation;
- name uncertainties and facts that must be confirmed before mutation;
- select only 0–3 load-bearing skills unless a distinct fourth trigger is justified;
- define stop and escalation conditions;
- define evidence required for closure;
- identify whether draft review and closure review need a human, model supervisor, or either;
- save/propose the task as DRAFT and STOP.

Return the task ref plus a short review summary. Do not APPLY.
```
