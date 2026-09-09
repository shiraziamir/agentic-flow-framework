# Operational Gap Schema

**Schema version:** 1.0  
**Updated:** 2026-09-09T10:40:00Z

Use this artifact when a production-readiness/security/reliability capability is missing, partially implemented, not verified, intentionally deferred or outside current authority.

```yaml
gap_id: <stable-id>
project_profile_ref: <path/version/hash>
detected_at: <RFC3339>
updated_at: <RFC3339>

area: DELIVERY|OBSERVABILITY|DATA_DURABILITY|TROUBLESHOOTING|SECURITY|SUPPLY_CHAIN|RESILIENCE|AI_LOG_ANALYSIS|CODE_ARCHITECTURE|OTHER
requirement: <exact expected capability>
state: NOT_IMPLEMENTED|PARTIAL|UNVERIFIED|BLOCKED|ACCEPTED_RISK|CLOSED

reality:
  observed: <what is actually known>
  evidence_refs: []
  missing_receipt: <what would establish the capability>

risk:
  failure_mode: <what can go wrong>
  blast_radius: LOCAL|SERVICE|MULTI_SERVICE|CUSTOMER_CRITICAL
  data_or_security_impact: <bounded statement>

owner: <person/team/role|UNASSIGNED>
target_date: <date|NONE>
accepted_by: <owner/judgment ref|NONE>
acceptance_expiry: <date|NONE>

mitigation_now: []
closure_requirements: []
```

## Rules

- A gap is not closed by prose. Closure requires the named receipts.
- `UNVERIFIED` means the capability may exist but current evidence is insufficient.
- `ACCEPTED_RISK` requires a named owner/judgment and expiry/review point when material.
- Do not hide a material gap in a narrative report footnote; link it from the current project profile/index.
- A production release may proceed with a gap only if the active governance permits it and residual risk is explicit.