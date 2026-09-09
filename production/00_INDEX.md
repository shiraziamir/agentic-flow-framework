# Production Engineering Profiles

**Version:** 1.0  
**Updated:** 2026-09-09T10:40:00Z

Production engineering is progressive disclosure. Do not preload every profile on every task.

## Always evaluate

| Profile | Purpose |
|---|---|
| [`DELIVERY.md`](DELIVERY.md) | build → artifact → deploy → rollback/recovery of releases |
| [`SECURITY_FIRST.md`](SECURITY_FIRST.md) | security across SDLC/runtime/supply chain |
| [`OBSERVABILITY.md`](OBSERVABILITY.md) | metrics/logs/traces/health/SLOs/alerts |

## Triggered profiles

| Trigger | Profile |
|---|---|
| durable/stateful/critical data | [`DATA_DURABILITY.md`](DATA_DURABILITY.md) |
| service operated/troubleshot by humans or agents | [`TROUBLESHOOTING.md`](TROUBLESHOOTING.md) |
| logs/telemetry will be supplied to AI/agents | [`AI_LOG_ANALYSIS.md`](AI_LOG_ANALYSIS.md) |
| distributed/high-availability/recovery-sensitive system | [`RESILIENCE_CHAOS.md`](RESILIENCE_CHAOS.md) |
| non-trivial codebase/external systems/changeability concerns | [`CODE_ARCHITECTURE.md`](CODE_ARCHITECTURE.md) |

## Maturity selection

First read `schemas/PRODUCTION_PROFILE.md`.

```text
codebase scale      SMALL | MEDIUM | LARGE
readiness tier      BASIC | STANDARD | HIGH_ASSURANCE
```

Scale controls decomposition/automation burden. Readiness tier controls the production assurance bar. Risk overrides size.

## Core invariant

> A production-readiness claim is valid only inside the named project profile, environment and evidence boundary.

Missing capabilities are durable `schemas/OPERATIONAL_GAP.md` artifacts with states such as `NOT_IMPLEMENTED`, `PARTIAL` or `UNVERIFIED`; they are never silently converted to PASS.

## Release decision

A production-bound task must identify which project-profile requirements it changes or depends on. If a new material operational/security/data/resilience requirement appears during APPLY, STOP and amend/reclassify instead of silently adding infrastructure or lowering the readiness bar.