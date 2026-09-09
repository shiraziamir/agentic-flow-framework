# Workflow prompt — DRAFT TASK

**Version:** 1.1  
**Updated:** 2026-09-09

```text
Create a DRAFT task contract for my request. Do not execute the task.

Authority/read order:
1. ARCHITECTURE.md
2. schemas/TASK_CONTRACT.md
3. skills/00_INDEX.md
4. only the project files/skills necessary to understand this request

Requirements:
- classify governance first: HIGH, MEDIUM, or EVIDENCE_ONLY; justify the minimum sufficient level;
- state the observed symptom separately from hypotheses;
- define goal, EDIT_SET, REFERENCE_SET, EXCLUDED_SET and baseline;
- write Definition of Done before implementation;
- name uncertainties and facts that must be confirmed before mutation;
- select only 0–3 load-bearing skills unless a distinct fourth trigger is justified;
- define stop and escalation conditions;
- define evidence required for closure;
- define expected model roles by phase when routing is material;
- for long/cost-sensitive/multi-agent work, declare optional soft/hard usage budgets and load token-efficiency;
- identify whether draft review and closure review need a human, model supervisor, either, or are not required by the chosen governance level;
- avoid HIGH ceremony for purely evidence/docs corrections that grant no new runtime authority;
- save/propose the task as DRAFT and STOP.

Return task ref, governance classification, selected skills, expected routing/budget, and a short review summary. Do not APPLY.
```
