# Production Profile — Delivery

**Version:** 1.2  
**Updated:** 2026-09-13

Goal: make the path from source to production repeatable, inspectable, reversible, attributable and measurably improvable.

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

## Production mutation readiness — mandatory per change

When production mutation is enabled, **every production change** must have recovery defined before execution. This applies to application deploys, configuration, infrastructure, migrations, feature flags with material effect, external integrations and other production mutations.

Required before execution:

- named production target;
- exact artifact/config/change identity;
- expected success and health signals;
- explicit abort condition;
- executable rollback path **or** explicit forward-recovery path;
- stateful/data compatibility and rollback constraints;
- recovery owner/authority;
- post-change verification;
- blast-radius limit when the change can affect multiple users/services/regions.

```text
NO ROLLBACK / FORWARD-RECOVERY PLAN
→ NOT EXECUTION-READY FOR PRODUCTION MUTATION
```

If rollback is technically possible, it must be documented and usable before execution. Do not defer rollback design until after failure.

If rollback is unsafe or impossible, record why and require all applicable controls:

- tested or otherwise qualified forward-recovery procedure;
- backup/checkpoint/snapshot or equivalent recovery anchor;
- compatibility ordering for schema/state changes;
- reduced blast radius / progressive exposure where practical;
- STOP/abort conditions;
- explicit residual-risk acceptance when recovery remains incomplete.

A production change may be correctly blocked even when the implementation itself is complete.

## BASIC

- documented/repeatable build command;
- tests appropriate to the changed surface;
- version/ref embedded or otherwise recoverable from artifact;
- named deployment target and operator/automation owner;
- explicit secrets/config source; no credentials committed to source;
- basic post-deploy health check;
- documented rollback/redeploy path for each production mutation;
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
- provenance target recorded in the project profile;
- delivery outcomes can be reconstructed from durable events when useful.

## HIGH_ASSURANCE

Additionally, where risk justifies:

- progressive exposure/canary/blue-green or equivalent safe rollout;
- health/SLO-based gates before increasing exposure;
- deployment stops and recovery begins when the frozen health boundary fails;
- signed/verifiable build provenance; target SLSA build level documented;
- protected/reviewed production change path and separation of duties;
- destructive migration/release ordering proven for rolling compatibility;
- recovery drill or rollback rehearsal for material release mechanisms;
- production artifact identity independently verifiable from runtime.

## Delivery performance — outcomes, not pipeline theater

Where useful, track DORA's delivery outcomes over time:

```text
deployment frequency
lead time for changes
change failure rate
time to restore service
```

The first two describe throughput; the latter two describe stability. Use trends/system-level outcomes to find bottlenecks and improve the delivery system. Do not game them by splitting/deploying work artificially, ranking individuals, or optimizing deployment frequency at the expense of quality/security/recovery.

The metric event definitions must be stable enough to compare over time: what counts as production deployment, start/end of lead time, qualifying change failure and service restoration.

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

- rollout unit/ring and blast radius;
- success/steady-state/health signals;
- gates before progressive exposure;
- abort/rollback/roll-forward conditions;
- migration ordering and stateful rollback constraints;
- what constitutes `DEPLOYED_ARTIFACT` evidence;
- owner during deployment and after-hours behavior if relevant.

Progressive rollout is useful only when each stage has a meaningful health model and the automation/operator can stop exposure. A canary with no decision signal is ceremony.

## Infrastructure as code

For non-trivial infrastructure, declarative/versioned IaC improves repeatability, reviewability and drift detection. Keep modules/layers aligned with real lifecycle/ownership boundaries and avoid unnecessary abstractions. Multi-stamp/cell architectures need especially strong automation/observability/drift control because copies can diverge.

## Gaps

Examples that must be explicit rather than implied away:

- build is only reproducible on one engineer laptop;
- production artifact digest cannot be identified;
- deployment is manual/unreviewed;
- rollback is undocumented, untested where required, or known unsafe;
- irreversible production mutation lacks forward-recovery/checkpoint strategy;
- staging differs materially from production;
- CI job is skipped for relevant branch/path;
- progressive rollout exists but has no health/abort gate;
- DORA/event measurements are claimed but event definitions are ambiguous;
- supply-chain provenance/SBOM is not available despite a required tier;
- production health verification is absent.
