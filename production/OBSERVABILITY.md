# Production Profile — Observability

**Version:** 1.0  
**Updated:** 2026-09-09T10:40:00Z

Goal: make user impact, system health and likely causes observable without requiring guesswork or full raw-log excavation.

## Signal model

Use three correlated telemetry signals where appropriate:

- **metrics** — quantitative health, trends and alerting;
- **logs** — event detail and forensic/debug context;
- **traces** — request/dependency path and latency correlation.

OpenTelemetry provides a common model for these signals. Logs should carry timestamps, resource/service identity and, where available, `TraceId`/`SpanId` so logs can be correlated with traces.

## Service health

For user-facing/request-driven services, begin with Google SRE's four golden signals:

```text
latency
traffic
errors
saturation
```

Track successful and failed latency separately where that distinction matters. Add domain-specific SLIs for correctness, freshness, queue lag, data pipeline delay, payment/auth success or other user-critical outcomes.

## BASIC

- service/application identity and version visible in runtime;
- logs available after process/container restart where required;
- basic health/readiness signal;
- error count/rate and latency observable for core flow;
- resource saturation signal appropriate to the runtime;
- production deployment marker/date can be correlated with symptoms;
- retention/ownership for essential telemetry known.

## STANDARD

Additionally:

- structured metrics with stable naming/units;
- Prometheus labels avoid high-cardinality identifiers such as user IDs/emails;
- centralized logs with service/environment/release/correlation fields;
- traces for material distributed/external dependency paths;
- dashboards centered on user/service symptoms, not only machine internals;
- alerts are actionable and link to useful dashboards/runbooks;
- symptom alerts distinguish user impact from likely causes;
- alert noise/skips and telemetry pipeline health are monitored;
- SLI/SLO defined for important user journeys when the service is customer-facing or operationally material.

## HIGH_ASSURANCE

Additionally:

- SLO/error-budget driven alerting for critical flows;
- multi-window/burn-rate or equivalent alerting chosen to balance detection speed/noise;
- black-box checks complement white-box telemetry;
- dependency/service-map correlation and release annotations;
- telemetry access, integrity and retention controls appropriate to data sensitivity;
- capacity/saturation forecasting for critical bounded resources;
- regular review removes low-value/noisy metrics/alerts;
- telemetry outage is itself detectable.

## Prometheus discipline

- one metric should represent one quantity/unit;
- use labels for bounded dimensions instead of generated metric names;
- avoid unbounded/high-cardinality labels;
- use counters/gauges/histograms according to semantics;
- define recording rules when queries become expensive/repeated;
- dashboards and alerts should preserve the exact query/window/labels used for evidence.

## Health endpoints

A `200 OK` from a shallow health endpoint proves little beyond reachability. Where readiness depends on storage or critical dependencies, distinguish liveness from readiness/dependency health and avoid creating cascading failure by making every health probe perform expensive dependency calls.

## SLO receipt

A claim such as `SLO met` identifies:

```text
SLI definition
SLO target
measurement window
data source/query
excluded traffic if any
missing-data behavior
observed result
```

## Gaps

Report explicitly when:

- metrics/logs/traces exist but cannot be correlated;
- logs disappear with pods/nodes;
- no production version/deployment marker exists;
- monitoring sees infrastructure but not user outcomes;
- alerts exist but no owner/runbook/action exists;
- metric cardinality is uncontrolled;
- SLO is required but undefined;
- telemetry access exposes sensitive data or secrets;
- monitoring pipeline failure is indistinguishable from service health.