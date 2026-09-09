# Workflow prompt — DRAFT TASK

**Version:** 1.3  
**Updated:** 2026-09-09T10:40:00Z

```text
Create a DRAFT task contract for my request. Do not execute the task.

Authority/read order:
1. ARCHITECTURE.md
2. schemas/TASK_CONTRACT.md
3. schemas/CHANGE_CLASSIFICATION.md
4. schemas/CLAIM_RECEIPT.md
5. verification/00_INDEX.md
6. if production-bound/relevant: current project production profile + production/00_INDEX.md
7. skills/00_INDEX.md
8. only project files needed to understand this request

Requirements:
- state observed symptom separately from hypotheses;
- classify governance, primary engineering surface, change kind, mutation scope, affected consumers, cross-cutting and operational flags using evidence;
- if production-bound, identify current production profile/tier, relevant open gaps and production profiles affected by this task;
- explicitly consider whether change introduces/modifies build/deploy/artifact, monitoring/metrics/logs/traces/SLO, durable data/backup/recovery, security/authz/secrets/supply-chain, troubleshooting/runbook, provider/failure behavior or architecture boundaries;
- define goal, EDIT_SET, REFERENCE_SET, EXCLUDED_SET and baseline;
- write observable Definition of Done before implementation;
- enumerate material closure claims and map each to minimum adequate receipt rung;
- select GENERAL + primary surface + triggered verification annexes;
- select only triggered production profiles; do not preload the whole production shelf;
- include important checks intentionally outside scope and why;
- name uncertainties/facts that must be confirmed before mutation;
- select only 0–3 load-bearing Skills unless a distinct fourth trigger is justified;
- define STOP/escalation/reclassification conditions, including new operational/readiness requirements;
- define evidence required for closure with ref/artifact/environment identity;
- identify draft review, blind-spot audit and closure-review requirements;
- if a material missing production capability is already known, reference/create a proposed operational gap rather than hiding it in prose;
- save/propose the task as DRAFT and STOP.

Return:
- task ref/version;
- classification + production-impact summary;
- planned claim -> receipt matrix;
- selected verification/production profiles;
- known gap refs/unresolved assumptions;
- concise review summary.

Do not APPLY.
```