# Production Engineering Profiles

**Version:** 1.2  
**Updated:** 2026-09-09T11:30:00Z

Production engineering is progressive disclosure. Do not preload every profile on every task.

## Project baseline

A target project should normally keep a concise `.agentic/PROJECT_PROFILE.yaml` conforming to `schemas/PROJECT_PROFILE_CONFIG.md`.

It defines baseline intent/guardrails such as codebase scale, readiness tier, test strategy, operations/security requirements, agent environment permissions and architecture-pattern governance. **It is not evidence that those requirements are currently satisfied.** Current receipts and operational gaps determine reality.

Temporary weakening/disablement of a baseline requirement uses `schemas/TEMPORARY_OVERRIDE.md` with owner, authority, reason, expiry, risk, compensating controls and restore verification. Do not silently edit the baseline merely to make a task pass.

## Always evaluate

| Profile | Purpose |
|---|---|
| [`DELIVERY.md`](DELIVERY.md) | build → artifact → deploy → rollback/recovery of releases |
| [`SECURITY_FIRST.md`](SECURITY_FIRST.md) | security across SDLC/runtime/supply chain |
| [`OBSERVABILITY.md`](OBSERVABILITY.md) | metrics/logs/traces/health/SLOs/alerts |

## Triggered profiles

| Trigger | Profile |
|---|---|
| material implementation/verification strategy | [`TEST_STRATEGY.md`](TEST_STRATEGY.md) |
| agent needs real execution/runtime environment | [`AGENT_ENVIRONMENTS.md`](AGENT_ENVIRONMENTS.md) |
| new abstraction/pattern/changeability decision | [`PATTERN_SELECTION.md`](PATTERN_SELECTION.md) |
| durable/stateful/critical data | [`DATA_DURABILITY.md`](DATA_DURABILITY.md) |
| service operated/troubleshot by humans or agents | [`TROUBLESHOOTING.md`](TROUBLESHOOTING.md) |
| logs/telemetry supplied to AI/agents | [`AI_LOG_ANALYSIS.md`](AI_LOG_ANALYSIS.md) |
| distributed/high-availability/recovery-sensitive system | [`RESILIENCE_CHAOS.md`](RESILIENCE_CHAOS.md) |
| non-trivial codebase/external systems/changeability concerns | [`CODE_ARCHITECTURE.md`](CODE_ARCHITECTURE.md) |

## Test default

Default framework recommendation is **test-first for material claims**, not strict TDD for every edit:

```text
observable DoD / planned claim
→ freeze important acceptance examples/receipt level
→ implement
→ run focused checks
→ for load-bearing new tests, prove defect-detection with mutation/path proof when practical
→ restore
→ broader affected/baseline checks
```

Strict red-green-refactor TDD may be selected by the project/team in `PROJECT_PROFILE.yaml`.

## Agent environment default

Use the lowest environment that can directly establish the required claim:

```text
LOCAL/HERMETIC
→ EPHEMERAL TEST
→ SHARED TEST
→ STAGING/PRODUCTION-LIKE
→ CONTROLLED PRODUCTION READ/CANARY
→ PRODUCTION MUTATION (explicit authority only)
```

If the authorized environment is insufficient, the agent requests the environment; the request does not grant access.

## Pattern default

Recommended default is `AGENT_PROPOSES_OWNER_MAY_OVERRIDE`. Agents may choose small local implementation patterns within project conventions, but material shared/public architectural abstractions should carry a problem/boundary/cost/benefit rationale and be reviewed according to task risk. Do not create layers merely to satisfy a style doctrine.

## Maturity selection

First read `schemas/PRODUCTION_PROFILE.md`.

```text
codebase scale      SMALL | MEDIUM | LARGE
readiness tier      BASIC | STANDARD | HIGH_ASSURANCE
```

Scale controls decomposition/automation burden. Readiness tier controls production assurance. Risk overrides size.

## Core invariant

> A production-readiness claim is valid only inside the named project profile, environment and evidence boundary.

Missing capabilities are durable `schemas/OPERATIONAL_GAP.md` artifacts with states such as `NOT_IMPLEMENTED`, `PARTIAL` or `UNVERIFIED`; they are never silently converted to PASS.

## Deterministic validation

Where target artifacts use compatible JSON/YAML, use:

```bash
python3 scripts/production_readiness_lint.py <profile-or-gap-files>
python3 scripts/test_production_readiness_lint.py
```

The linter checks mechanical contradictions. It does **not** prove runtime readiness, security, monitoring quality, test quality or recoverability; those require actual receipts.

## Release decision

A production-bound task identifies which project-profile requirements it changes/depends on. If a new material operational/security/data/resilience requirement appears during APPLY, STOP and amend/reclassify instead of silently adding infrastructure or lowering the readiness bar.
