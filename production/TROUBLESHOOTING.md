# Production Profile — Troubleshooting

**Version:** 1.0  
**Updated:** 2026-09-09T10:40:00Z

Goal: make failures diagnosable across delivery/runtime/data/network/provider layers without turning incidents into unbounded log excavation.

## Troubleshooting ladder

Start from the user-visible symptom and walk the delivery/runtime chain with receipts:

```text
REQUEST / USER SYMPTOM
↓
DNS / EDGE / LOAD BALANCER / INGRESS
↓
APPLICATION / PROCESS / POD
↓
DEPENDENCIES / NETWORK / AUTH
↓
CACHE / QUEUE / DATABASE / STORAGE
↓
EXTERNAL PROVIDER
↓
RECENT CHANGE / ARTIFACT / CONFIG
```

For build/release failures use:

```text
SOURCE REF
↓
DEPENDENCY RESOLUTION
↓
BUILD
↓
TEST
↓
ARTIFACT
↓
PUBLISH/REGISTRY
↓
DEPLOYMENT CONTROLLER
↓
TARGET ENVIRONMENT
↓
RUNTIME HEALTH
```

## Investigation rules

- separate **symptom** from hypothesized cause;
- establish environment/account/cluster/namespace/service/version identity first;
- compare against known-good baseline/time window;
- inspect recent deployment/config/feature-flag/dependency changes early;
- use the cheapest discriminating check before broad log scans;
- correlate metrics, traces and logs via timestamp/release/trace/request IDs;
- record the exact query/window/filter used to support a finding;
- missing telemetry is `UNKNOWN`, not evidence the event did not occur;
- distinguish provider error from application interpretation/fallback behavior;
- preserve failed hypotheses when they materially prevent repeated dead ends.

## BASIC

- known place to retrieve application/runtime logs;
- service/version/environment visible;
- health/status check documented;
- basic runbook for restart/redeploy/rollback and common dependencies;
- owner/contact path for operational incidents.

## STANDARD

Additionally:

- deploy/release markers searchable in telemetry;
- correlation IDs/trace IDs through important service boundaries;
- dashboards for latency/error/traffic/saturation plus key dependencies;
- runbooks for common DNS/TLS/auth/database/queue/provider/deployment failures;
- bounded log queries and representative error examples;
- incident timeline/checkpoint artifact for significant outages;
- known-good baseline or comparison query;
- post-incident finding/follow-up tracking.

## HIGH_ASSURANCE

Additionally:

- service/dependency topology is discoverable and versioned;
- black-box and white-box signals allow symptom/cause separation;
- incident response roles, communication/escalation and decision authority are defined;
- production access is audited/least privilege/break-glass where appropriate;
- important remediation actions are scripted/rehearsed rather than improvised;
- chaos/recovery drills validate troubleshooting runbooks and telemetry;
- incident review focuses on system/process improvements rather than individual blame.

## Kubernetes-specific checks

When applicable verify:

- desired vs current Deployment/StatefulSet/DaemonSet status;
- pod scheduling/restarts/OOM/termination reason;
- Service/EndpointSlice/Ingress/Gateway resolution;
- events around the failure window;
- resource requests/limits and saturation;
- DNS/TLS/network policy/identity;
- ConfigMap/Secret/version/image digest actually mounted/running;
- logs retained beyond pod/node lifetime when required.

## Evidence packet for troubleshooting

Prefer compact evidence:

```yaml
symptom:
environment:
repository_ref:
artifact_or_image:
time_window:
known_good_comparison:
queries_or_commands: []
observations: []
hypotheses_tested: []
current_best_explanation:
truth_class: OBSERVED|DERIVED|INFERRED|UNKNOWN|CONTRADICTED
residual_unknowns: []
next_discriminating_check:
```

Do not attach megabytes of raw logs to normal agent context. Store/query raw telemetry separately and hand the reasoning tier bounded slices plus source/query refs.