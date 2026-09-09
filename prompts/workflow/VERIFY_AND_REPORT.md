# Workflow prompt — VERIFY AND REPORT

**Version:** 1.1  
**Updated:** 2026-09-09T10:40:00Z

```text
Verify the current implementation and produce a reality-reflecting report. Do not invent completion or project readiness.

Read:
1. ARCHITECTURE.md
2. frozen task/amendment + change classification
3. schemas/CLAIM_RECEIPT.md
4. schemas/EVIDENCE_PACKET.md
5. schemas/STATUS_REPORT.md
6. verification/00_INDEX.md + only frozen profiles/annexes
7. if production-bound: current project production profile + selected production profiles + relevant gap refs
8. skills/evidence-integrity/SKILL.md
9. skills/blind-spot-audit/SKILL.md when triggered

Process:
- identify exact repository ref, dirty state, build/artifact and environment being checked;
- inspect actual diff/affected surfaces and production impact;
- enumerate frozen DoD/planned closure claims;
- run/inspect required verification at the minimum receipt rung that directly establishes each claim;
- preserve exact PASS/FAIL/PARTIAL/SKIPPED/UNVERIFIED states/counts;
- prove changed-path execution when bypass/cache/mock risk makes green tests ambiguous;
- if deployment is claimed, bind source/artifact/deployed runtime identity and post-deploy health receipt;
- if observability changed, verify emitted/queried signal and useful correlation/labels rather than config presence alone;
- if data durability changed, distinguish backup configuration from restore/PITR/recovery evidence and measured RPO/RTO when claimed;
- if security changed, preserve scoped security requirements and negative/authz/privilege receipts; scanner green is not a global secure claim;
- if AI log analysis is relevant, verify redaction/minimization, untrusted-data boundary, exact query/window/raw refs and tool authorization separation;
- if resilience/chaos is relevant, verify steady state, fault, blast radius, abort/recovery and actual result;
- report important checks not executed;
- classify statements OBSERVED/DERIVED/INFERRED/UNKNOWN/CONTRADICTED;
- narrow global/negative/readiness claims unless a finite universe/profile was checked;
- do not use reviewer/model confidence as behavioral evidence;
- if evidence is stale/weaker than claim or actual surface/production requirement differs from frozen plan, return AMENDMENT_REQUIRED/NEEDS_EVIDENCE;
- update current project production profile/gap only for capability changes actually established by receipts;
- missing or partially verified operational requirements remain/create explicit gap artifacts.

Output:
1. schemas/STATUS_REPORT.md-conformant report;
2. schemas/EVIDENCE_PACKET.md-conformant packet/ref;
3. claim -> required receipt -> actual receipt matrix;
4. checks not executed;
5. production profile/gap delta, or `NONE`;
6. unknowns/residual risk;
7. requested supervisor disposition.

Use bounded language such as `128/128 required tests passed at <ref>` or `restore completed in 41m against backup X`; never `everything is good` or `production-ready` while required material gaps remain unresolved/unaccepted.
```