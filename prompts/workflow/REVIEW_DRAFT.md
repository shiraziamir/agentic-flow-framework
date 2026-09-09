# Workflow prompt — REVIEW DRAFT

**Version:** 1.1  
**Updated:** 2026-09-09T10:40:00Z

```text
Review the DRAFT task contract. Do not APPLY or edit product code.

Read, in order:
1. ARCHITECTURE.md
2. the DRAFT task
3. schemas/CHANGE_CLASSIFICATION.md
4. schemas/CLAIM_RECEIPT.md
5. verification/00_INDEX.md + only selected profiles
6. when production-bound: current schemas/PRODUCTION_PROFILE.md artifact, relevant open gaps and only selected production profiles
7. relevant project architecture/dependency/source/runtime evidence needed to challenge the draft

Review questions:
- Is governance proportional to actual risk?
- Is engineering + operational classification supported by actual paths/dependencies/contracts/runtime?
- Are affected consumers/systems/environments missing?
- Is the goal/DoD observable rather than implementation-only?
- Does every material planned claim have an adequate receipt plan?
- Does verification match actual FRONTEND/BACKEND/SHARED/DATA/INFRA/CI/etc. behavior?
- For production changes, is build→artifact→deploy→running-artifact/rollback impact understood?
- Does the change require/alter metrics/logs/traces/health/SLO/alerts?
- Does it introduce or alter durable data, RPO/RTO, backup/PITR/restore, migration or destructive-change risk?
- Are authz/tenant/secrets/identity/dependency/supply-chain/security boundaries covered?
- Is troubleshooting/release correlation/runbook support adequate for the changed operational path?
- Are provider/cache/queue/network/retry/idempotency/failure modes relevant?
- Does code architecture leak volatile provider/legacy/data semantics across boundaries or add unjustified pattern ceremony?
- If logs will enter AI, are privacy/redaction/provenance/prompt-injection/read-only controls included?
- If chaos/fault injection is proposed, are maturity, steady state, blast radius, abort and recovery preconditions met?
- Are existing operational gaps properly referenced and any new gap made explicit?
- Are relevant negative/error/live paths omitted?
- Are claims global/absolute without a finite verification/readiness universe?
- Are required checks being replaced by a weaker proxy?
- Are STOP/reclassification/escalation conditions sufficient?
- Are important checks intentionally not required stated explicitly?
- Does closure need a cold independent reviewer/blind-spot audit?
- Is the plan wasting expensive model/context where deterministic or cheap read-only work preserves quality?

Return exactly one disposition:
- ACCEPT_DRAFT
- AMEND_DRAFT
- NEEDS_EVIDENCE
- REJECT_DRAFT

For non-acceptance, return bounded findings with required amendments/evidence/gap updates. Do not silently rewrite and approve the task in the same pass unless owner workflow explicitly permits it.

ACCEPT_DRAFT freezes the reviewed contract/version/hash. It does not authorize APPLY unless active governance explicitly combines those gates.
```