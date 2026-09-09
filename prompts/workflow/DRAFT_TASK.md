# Workflow prompt — DRAFT TASK

**Version:** 1.2  
**Updated:** 2026-09-09T10:04:00Z

```text
Create a DRAFT task contract for my request. Do not execute the task.

Authority/read order:
1. ARCHITECTURE.md
2. schemas/TASK_CONTRACT.md
3. schemas/CHANGE_CLASSIFICATION.md
4. schemas/CLAIM_RECEIPT.md
5. verification/00_INDEX.md
6. skills/00_INDEX.md
7. only the project files/skills necessary to understand this request

Requirements:
- state observed symptom separately from hypotheses;
- classify governance level, primary engineering surface, change kind, mutation scope, affected consumers and cross-cutting flags using evidence rather than filename intuition;
- define goal, EDIT_SET, REFERENCE_SET, EXCLUDED_SET and baseline;
- write observable Definition of Done before implementation;
- enumerate the material claims the executor expects to make at closure;
- map each planned claim to the minimum adequate receipt rung;
- select GENERAL + primary surface + only triggered verification annexes;
- include important checks intentionally outside scope and why;
- name uncertainties/facts that must be confirmed before mutation;
- select only 0–3 load-bearing skills unless a distinct fourth trigger is justified;
- define stop/escalation/reclassification conditions;
- define evidence required for closure with ref/artifact/environment identity where relevant;
- identify draft review, blind-spot audit and closure-review requirements;
- save/propose the task as DRAFT and STOP.

Return:
- task ref/version;
- classification summary;
- planned claim -> receipt matrix;
- selected verification profiles;
- unresolved assumptions;
- concise review summary.

Do not APPLY.
```
