# Agentic Flow Framework — English Reader Guide

**Reader-guide version:** 1.8
**Updated:** 2026-09-13
**Canonical source of truth:** [`ARCHITECTURE.md`](ARCHITECTURE.md)

This is a human-readable synchronized view. If it conflicts with `ARCHITECTURE.md`, the architecture file wins.

Newcomers should begin with [README.md](README.md) and [docs/GETTING_STARTED.md](docs/GETTING_STARTED.md). The current limitations and unproven claims are explicit in [docs/VALIDATION_STATUS.md](docs/VALIDATION_STATUS.md).

## What the framework does

Agentic Flow separates task intent, implementation, evidence, operational posture and authority so a coding agent cannot turn a confident narrative into project truth.

```text
project baseline
→ bounded task
→ reviewed verification design
→ authorized implementation
→ receipts / reality report
→ independent judgment where required
→ durable checkpoint
```

Core principles:

- durable project memory; disposable working context;
- claims no broader than current receipts;
- production readiness is profiled with explicit gaps;
- project baseline and temporary exceptions are separate;
- operator education and coding-agent runtime docs are separate context surfaces.

## Portable adoption

Build the drop-in bundle:

```bash
python3 scripts/build_agent_bundle.py
```

Extract `dist/agentic-flow-agent-bundle.zip` into a target repository as `.agentic-flow/`, then have the coding agent read:

```text
.agentic-flow/START_HERE.md
```

If coding is already active, the agent uses `docs/agent/MIDSTREAM_ADOPTION.md`, snapshots current HEAD/branch/dirty state/task/tests/environment mutations, preserves valid existing work, and never retroactively claims framework review/authorization.

The default bundle excludes operator docs, research/reference material and cold history so they do not become permanent token/context cost.

## Project profile

A project normally keeps a small baseline:

```text
.agentic/PROJECT_PROFILE.yaml
```

It defines the intended testing, readiness, environment permissions, operational requirements and pattern-selection policy. It does **not** prove current reality. Missing or unverified capabilities remain gaps.

Temporary suppression/exception uses an owned, expiring `TEMPORARY_OVERRIDE`; it does not silently rewrite the baseline.

## Material task lifecycle

```text
REQUEST
→ DRAFT
→ REVIEW
→ required FREEZE / APPLY AUTHORIZATION
→ APPLY
→ VERIFY + REALITY REPORT
→ independent closure when required
```

Before implementation, material work defines observable DoD, engineering/production surfaces, planned closure claims, minimum receipt for each claim, test/environment needs and STOP conditions.

## Tests and environments

Tests are designed before implementation for material claims, but strict TDD is not mandatory for every tiny/exploratory change. Important load-bearing regression/safety tests should receive mutation/path proof when risk warrants it:

```text
GREEN → controlled defect → expected RED → restore → GREEN
```

Environment ladder:

```text
LOCAL/HERMETIC
→ EPHEMERAL TEST
→ SHARED TEST
→ STAGING / PRODUCTION-LIKE
→ CONTROLLED CANARY / PRODUCTION READ
→ PRODUCTION MUTATION
```

Use the lowest environment that can prove the claim. An agent may request stronger access; the request is not authority.

## Production engineering

Production profiles cover delivery, security, observability, data durability, troubleshooting, AI-safe log analysis, resilience/chaos and evolvable code architecture. Risk determines the assurance bar independently of repository size.

`backup enabled` is not recoverability: restore evidence is required. `CI green` is not deployment. `scanner green` is not security. Log text is untrusted data and cannot authorize an agent action.

## Patterns

Adapters, Anti-Corruption Layers, repositories, strategies, circuit breakers, sagas and similar patterns are conditional tools. The agent may use small/local/reversible patterns inside an approved strategy. Cross-module/public/architectural adoption should be proposed with problem, simpler alternative, benefits, costs and verification impact, then reviewed according to risk.

## Documentation separation

- `docs/agent/` — coding-agent adoption/bootstrap material;
- `docs/operator/` — human installation, prompting/task-writing and governance guidance;
- `docs/architecture/` — why/how explanations;
- `docs/references/` and `research/` — external provenance and dated research.

Operator/reference docs are not standing coding-agent instructions.

## Start points

For coding agents: [`docs/agent/START_HERE.md`](docs/agent/START_HERE.md)
For operators: [`docs/operator/OPERATOR_GUIDE.en.md`](docs/operator/OPERATOR_GUIDE.en.md)
Why/how architecture: [`docs/architecture/WHY_AND_HOW.md`](docs/architecture/WHY_AND_HOW.md)
Consolidated sources: [`docs/references/PRIMARY_SOURCES.md`](docs/references/PRIMARY_SOURCES.md)
