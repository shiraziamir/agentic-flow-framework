# Production Profile — Resilience and Chaos Engineering

**Version:** 1.0  
**Updated:** 2026-09-09T10:40:00Z

Goal: prove the system can tolerate/recover from realistic failures without turning chaos testing into uncontrolled production damage.

## Resilience before chaos

Chaos engineering is not random destruction. Begin with known service objectives, observability, recovery controls and a bounded experiment.

Use this order:

```text
failure-mode analysis
→ steady-state metric/SLI
→ hypothesis
→ bounded fault
→ blast-radius/abort controls
→ observe system + user impact
→ restore
→ evidence/follow-up
```

The Principles of Chaos Engineering define steady state, a hypothesis that steady state will continue, real-world failure variables and attempts to disprove that hypothesis. Netflix's Chaos Monkey work intentionally exposed instance failure because such failures are inevitable and used that pressure to build resilient services.

## BASIC

For low-complexity production systems:

- enumerate important dependency/failure modes;
- define restart/redeploy/rollback/recovery path;
- timeouts are explicit at remote boundaries;
- retries are finite and only used for safe/transient failures;
- health monitoring exists;
- single-instance/node failure assumptions are explicit;
- no production chaos experiment is required.

## STANDARD

Additionally:

- failure-mode analysis for critical flows;
- circuit breaker/bulkhead/rate limit/idempotency/retry-budget patterns used where their failure mode justifies them;
- queue/provider/database/cache/network failure behavior tested in lower environment;
- recovery/backup/runbooks exercised;
- non-production fault-injection experiments validate telemetry and failure behavior;
- alerts respond to user-impact/SLI changes during failure;
- retry storms, duplicate side effects and graceful-degradation semantics tested where applicable.

## HIGH_ASSURANCE

Additionally, where justified:

- controlled production experiments may be allowed only with explicit owner authorization;
- steady-state SLI/SLO and abort threshold frozen before experiment;
- smallest practical blast radius and progressive expansion;
- experiment avoids peak/sensitive business windows unless intentionally required;
- on-call/operators can abort immediately;
- rollback/recovery path is already proven;
- security/data-durability boundaries are not bypassed by chaos tooling;
- results generate concrete reliability improvements or retire low-value experiments.

## Chaos experiment contract

```yaml
experiment_id:
environment: nonprod|production
owner:
steady_state:
  metric_or_sli:
  expected_range:
hypothesis:
fault:
  target:
  type:
blast_radius:
abort_conditions: []
security_and_data_guards: []
start_window:
max_duration:
recovery_procedure:
observability_queries: []
expected_user_impact:
result: PASS|FAIL|ABORTED|INCONCLUSIVE
findings: []
```

## Failure patterns to consider

Only when relevant:

- process/pod/VM termination;
- dependency timeout/error/throttling;
- DNS/TLS/network partition/latency;
- database failover/connection exhaustion;
- cache loss/staleness;
- queue lag/redelivery/duplicate message;
- disk/storage pressure;
- credential/secret rotation;
- external provider outage;
- zone/region loss for systems designed for it;
- telemetry pipeline failure.

## Retry discipline

Retries can amplify incidents. Use bounded exponential backoff/jitter and aggregate retry budgets where appropriate. Persistent failure should fail fast or degrade through circuit breaker/bulkhead semantics rather than create a retry storm.

## Gaps

Explicitly report:

- failover/recovery assumptions have never been tested;
- timeout/retry defaults are unknown;
- no measurable steady state exists;
- chaos experiment has no abort path;
- blast radius cannot be bounded;
- fault injection can affect customer data without tested recovery;
- production experiment is proposed before non-production validation;
- observability cannot distinguish controlled experiment from unrelated incident;
- incident/runbook findings are not fed back into engineering work.