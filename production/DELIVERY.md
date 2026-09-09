# Production Profile — Delivery

**Version:** 1.0  
**Updated:** 2026-09-09T10:40:00Z

Goal: make the path from source to production repeatable, inspectable, reversible and attributable.

## Required chain

```text
SOURCE REF
→ BUILD/TEST
→ IMMUTABLE ARTIFACT IDENTITY
→ SECURITY/SUPPLY-CHAIN CHECKS
→ ENVIRONMENT-SPECIFIC DEPLOYMENT
→ HEALTH/RELEASE VERIFICATION
→ ROLLBACK OR FORWARD-RECOVERY PATH
```

A green source build is not a deployment receipt. A deployment command is not proof the intended artifact is serving traffic.

## BASIC

- documented/repeatable build command;
- tests appropriate to the changed surface;
- version/ref embedded or otherwise recoverable from artifact;
- named deployment target and operator/automation owner;
- explicit secrets/config source; no credentials committed to source;
- basic post-deploy health check;
- documented rollback/redeploy path;
- stateful changes identify data migration/backup implications.

## STANDARD

Additionally:

- automated CI gates and deterministic artifact creation;
- build once, promote the same immutable artifact where practical;
- image/package digest or equivalent immutable identity;
- environment/config drift is detectable;
- deployment uses least-privilege credentials/workload identity where available;
- release markers correlate deployment with logs/metrics/traces;
- smoke/contract/live checks against the deployed artifact;
- rollback/forward-fix decision conditions;
- dependency/vulnerability review and SBOM where ecosystem/tooling supports it;
- provenance target recorded in the project profile.

## HIGH_ASSURANCE

Additionally, where risk justifies:

- progressive exposure/canary/blue-green or equivalent safe rollout;
- automated health/SLO-based release analysis and abort criteria;
- signed/verifiable build provenance; target SLSA build level documented;
- protected/reviewed production change path and separation of duties;
- destructive migration/release ordering proven for rolling compatibility;
- recovery drill or rollback rehearsal for material release mechanisms;
- production artifact identity independently verifiable from runtime.

## Supply-chain receipts

Prefer evidence that binds:

```text
source revision
→ build platform/workflow
→ dependencies/materials
→ artifact digest
→ provenance/attestation where available
→ deployed digest/version
```

SLSA v1.2 uses increasing Build levels: L1 provenance exists, L2 uses a hosted build platform with signed provenance, and L3 uses a hardened build platform. Do not claim a SLSA level unless its requirements are actually met and verified.

## Safe deployment

For material user-facing changes define before deployment:

- rollout unit and blast radius;
- success/steady-state signals;
- abort/rollback conditions;
- migration ordering;
- what constitutes `DEPLOYED_ARTIFACT` evidence;
- owner during deployment and after-hours behavior if relevant.

## Gaps

Examples that must be explicit rather than implied away:

- build is only reproducible on one engineer laptop;
- production artifact digest cannot be identified;
- deployment is manual/unreviewed;
- rollback is undocumented or known unsafe;
- staging differs materially from production;
- CI job is skipped for relevant branch/path;
- supply-chain provenance/SBOM is not available despite a required tier;
- production health verification is absent.