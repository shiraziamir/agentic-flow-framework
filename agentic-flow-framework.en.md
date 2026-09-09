# Agentic Flow Framework — English Reader Guide

**Reader-guide version:** 1.6  
**Updated:** 2026-09-09T10:40:00Z  
**Canonical source of truth:** [`ARCHITECTURE.md`](ARCHITECTURE.md)

This is a synchronized reader-facing guide. If it conflicts with `ARCHITECTURE.md`, the architecture file wins.

## Core idea

> Durable project memory; disposable, high-quality working context.

> Claims are limited by receipts; production readiness is limited by the current profile and explicit gaps.

## Task lifecycle

Material work follows risk-adaptive governance:

```text
DRAFT → REVIEW → FREEZE/AUTHORIZE → APPLY → VERIFY → INDEPENDENT CLOSURE when required
```

The draft freezes engineering surface, operational flags, DoD, planned claims/minimum receipts and production impacts before mutation. New material risks discovered during APPLY trigger STOP/amendment.

## Reality and verification

Reports distinguish:

```text
OBSERVED | DERIVED | INFERRED | UNKNOWN | CONTRADICTED
```

A unit test, HTTP 200, screenshot, green CI, security scanner, backup setting or reviewer PASS cannot silently be upgraded into a stronger runtime/security/recovery claim.

## Production profile

Production projects use `schemas/PRODUCTION_PROFILE.md`.

```text
codebase_scale   SMALL | MEDIUM | LARGE
readiness_tier   BASIC | STANDARD | HIGH_ASSURANCE
```

Size and assurance are separate. Risk, blast radius, sensitive data, statefulness and recovery needs can raise the tier regardless of repository size.

Missing/partial/unverified capabilities become `schemas/OPERATIONAL_GAP.md` artifacts rather than being hidden by a `production-ready` label.

## DevOps-friendly delivery

`production/DELIVERY.md` covers:

```text
source → build/test → immutable artifact → deploy target
→ running artifact identity → health verification → rollback/forward recovery
```

STANDARD/HIGH_ASSURANCE projects add automated gates, artifact digests, safe rollout, supply-chain review/provenance and stronger release evidence according to risk.

## Observability and SRE

`production/OBSERVABILITY.md` uses metrics, logs and traces as correlated evidence. User-facing systems start from latency, traffic, errors and saturation plus domain SLIs. Important services add useful dashboards, actionable alerts and SLO/error-budget operations where appropriate.

Prometheus labels are bounded; unbounded user/email identifiers do not belong in metric labels. OpenTelemetry-style service/resource and TraceId/SpanId correlation is preferred.

## Data durability

`production/DATA_DURABILITY.md` requires important durable stores to define owner/source-of-truth, data class, RPO/RTO, backup/retention, PITR if needed and restore evidence.

> Backup success is not recoverability proof. Restore is the receipt.

PostgreSQL PITR depends on a base backup plus required WAL; MySQL PITR depends on a full backup plus subsequent binary logs. Managed backup services still need restore validation.

## Troubleshooting

`production/TROUBLESHOOTING.md` starts from user symptom and exact environment/release identity, then checks bounded layers: edge/DNS → runtime → dependency/network/auth → cache/queue/database/storage → provider → recent release/config.

Use deployment markers, correlation IDs, traces/metrics and reproducible bounded log queries. Missing telemetry is UNKNOWN.

## AI-assisted log analysis

`production/AI_LOG_ANALYSIS.md` treats logs as structured, privacy-sensitive and **untrusted external data**. AI workflows redact/minimize secrets/PII, preserve exact query/time-window/raw source refs, use read-only/least-privilege discovery and never authorize tools from instructions embedded in log text.

This explicitly addresses indirect prompt injection in user/provider-controlled telemetry.

## Security first

`production/SECURITY_FIRST.md` uses OWASP ASVS/SAMM, NIST SSDF, CISA Secure by Design and SLSA as scoped/versioned references, not badges.

Security spans design through runtime: trust/data/threat boundaries, secure defaults, server-side authorization, secrets/identity, dependencies/SBOM/provenance, vulnerability ownership, least privilege, secure telemetry and incident response.

## Resilience and chaos

`production/RESILIENCE_CHAOS.md` requires steady-state evidence, hypothesis, bounded fault, blast radius, abort conditions and recovery. BASIC projects do not need production chaos. STANDARD can use non-production fault injection; controlled production chaos belongs only to mature/high-assurance workflows with explicit authorization and proven recovery.

## Evolvable architecture

`production/CODE_ARCHITECTURE.md` applies adapters/anti-corruption layers and dependency inversion only where they protect real provider/legacy/data/shared-contract change boundaries. SMALL projects stay simple; MEDIUM/LARGE projects may add module/API/dependency-graph enforcement as complexity justifies it.

## Context economy

Normal work loads only the current task/classification, current project production profile/open-gap pointers when relevant, selected verification/production profiles and 0–3 triggered Skills. Historical gaps/incidents/runbooks/tasks stay cold.

## Start here

1. `README.md`
2. `ARCHITECTURE.md`
3. matching `prompts/bootstrap/*`
4. target-project `schemas/PRODUCTION_PROFILE.md` artifact if production-bound
5. current task/classification + only triggered verification/production profiles and Skills

Current production-engineering evidence is recorded in `research/2026-09-09-production-engineering.md`.