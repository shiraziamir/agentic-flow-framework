# Workflow prompt — ASSESS PRODUCTION READINESS

**Version:** 1.0  
**Updated:** 2026-09-09T10:40:00Z

```text
Assess this project's production readiness without claiming capabilities from configuration/prose alone.

Read:
1. ARCHITECTURE.md
2. schemas/PRODUCTION_PROFILE.md
3. schemas/OPERATIONAL_GAP.md
4. production/00_INDEX.md
5. the target project's build/deploy/runtime/monitoring/security/data files needed for evidence

Procedure:
- determine codebase_scale and operational_complexity separately from readiness_tier;
- risk/criticality may raise the tier regardless of repository size;
- discover existing mechanisms before proposing new tools;
- load only the production profiles triggered by the project;
- for each required capability classify VERIFIED / PARTIAL / UNVERIFIED / NOT_IMPLEMENTED / NOT_APPLICABLE;
- attach receipts to VERIFIED claims;
- create/update durable gaps for anything material that is missing or unverified;
- identify build→artifact→deploy→runtime identity and rollback path;
- assess metrics/logs/traces/health/SLO/alerts appropriate to tier;
- inventory durable data and verify RPO/RTO/backup/restore evidence;
- assess security design, authz, secrets, dependencies, supply-chain and production identity;
- assess troubleshooting/runbook/correlation and recovery behavior;
- assess resilience/failure-mode/chaos maturity only to the level justified by tier;
- assess code boundaries/changeability without adding patterns merely for ceremony;
- if logs are used by AI, assess privacy/redaction/provenance/prompt-injection/tool-authorization controls;
- prioritize improvements by risk reduction and operational leverage, not checklist count.

Return:
1. production profile ref/version;
2. readiness summary by area;
3. exact gaps with risk and owner state;
4. top prioritized improvements;
5. checks/evidence used;
6. important checks not performed;
7. validity boundary.

Do not report the project as production-ready if required material gaps remain unaccepted or unverified.
```
