# Agentic Flow Framework

**Framework version:** 1.7  
**Updated:** 2026-09-09T12:40:00Z  
**Canonical policy:** [`ARCHITECTURE.md`](ARCHITECTURE.md)

A repository-first, vendor-neutral operating framework for reliable, cost-aware and production-operable coding agents.

> Durable project memory; disposable working context.

> A claim may be no broader than the receipt that establishes it.

## Fastest use: portable bundle

Build and self-test:

```bash
python3 scripts/test_build_agent_bundle.py
python3 scripts/build_agent_bundle.py
```

Output:

```text
dist/agentic-flow-agent-bundle.zip
```

Extract the `agentic-flow/` directory into a target repository as:

```text
.agentic-flow/
```

Human/operator starts at:

```text
.agentic-flow/README.md
```

Coding agent starts at:

```text
.agentic-flow/START_HERE.md
```

Copy-ready prompt:

```text
Read .agentic-flow/START_HERE.md and adopt Agentic Flow for this repository.
Do not start or change product work until adoption validation is complete.
```

If work is already active, `START_HERE.md` routes to `docs/agent/MIDSTREAM_ADOPTION.md` before further product mutation.

## What the portable distribution contains

The bundle is self-contained for both the operator and coding agent:

```text
README.md                          operator install/start instructions
START_HERE.md                      coding-agent entrypoint
INSTALL_PROMPT.txt                 copy-ready prompt
BEST_PRACTICES_USED.en.txt         concise English practice summary
ARCHITECTURE.md                    canonical architecture
PRIMARY_SOURCES.md                 source/provenance convenience copy
BUNDLE_MANIFEST.json               source hashes and byte counts

docs/agent/                        agent adoption/execution guides
docs/operator/                     human/operator guides
docs/architecture/                 why/how explanations
docs/references/                   primary-source index
schemas/                            durable contracts
verification/                       verification profiles
production/                         production profiles
skills/                             lazy procedures
prompts/                            workflow/bootstrap/supervisor prompts
templates/                          project examples
scripts/                            deterministic helpers
```

`docs/operator/`, `docs/architecture/` and `docs/references/` are physically present for offline use but remain **cold by default** for the coding agent. Distribution completeness does not mean preload everything into model context.

Deeper `research/`, reader HTML and cold history are not included in the default bundle.

See [`docs/architecture/BUNDLE_BOUNDARY.md`](docs/architecture/BUNDLE_BOUNDARY.md).

## Practical task lifecycle

For material changes:

```text
REQUEST
→ DRAFT
→ REVIEW
→ FREEZE / APPLY AUTHORIZATION when required
→ APPLY
→ VERIFY + REPORT
→ independent closure when required
```

Practical explanation:

[`docs/agent/TASK_WORKFLOW_DRAFT_REVIEW_APPLY_VERIFY.md`](docs/agent/TASK_WORKFLOW_DRAFT_REVIEW_APPLY_VERIFY.md)

The workflow is risk-adaptive: high-risk work gets stronger review/authorization/evidence; small low-risk edits stay lightweight.

## Token/context-efficient workflow

Use deterministic tools for deterministic facts, small affected working sets, bounded log packets, cheap/read-only workers for mechanically checkable discovery, compact handoffs and stronger model judgment only for ambiguity/risk.

Practical guide:

[`docs/agent/TOKEN_EFFICIENT_WORKFLOW.md`](docs/agent/TOKEN_EFFICIENT_WORKFLOW.md)

Token savings may not silently lower acceptance quality.

## Python helpers

Operator guides:

- [`docs/operator/USING_PYTHON_TOOLS.en.md`](docs/operator/USING_PYTHON_TOOLS.en.md)
- [`docs/operator/USING_PYTHON_TOOLS.fa.md`](docs/operator/USING_PYTHON_TOOLS.fa.md)

Main tools:

```text
verification_lint.py            task/evidence/status invariant checks
production_readiness_lint.py    profile/gap invariant checks
build_agent_bundle.py           portable ZIP + manifest builder
usage_ledger.py                 observable usage-counter ledger
```

These scripts check deterministic invariants. They do not replace behavioral tests, security review, deployment evidence or restore proof.

## Project baseline and production reality

A target project should normally maintain:

```text
.agentic/PROJECT_PROFILE.yaml
```

The project profile defines what **should** be true: testing policy, readiness tier, environment permissions, operational/security requirements and pattern-selection policy.

Reality is established by receipts and explicit operational gaps. Temporary exceptions use owned/expiring `TEMPORARY_OVERRIDE` artifacts instead of silently weakening the baseline.

## Core production concerns

Production profiles cover:

- build → immutable artifact → deploy → running identity → rollback/recovery;
- metrics/logs/traces, SLI/SLO and actionable alerting;
- RPO/RTO, backup/PITR and restore proof;
- security-first SDLC and supply-chain provenance;
- troubleshooting/runbooks;
- AI-safe log analysis with log text treated as untrusted data;
- resilience/chaos only with maturity, bounded blast radius and recovery controls;
- evolvable architecture/patterns selected for real boundaries rather than checklists.

> Backup enabled is not recoverability. Restore is the receipt.

## Documentation routes

Coding agent:

[`docs/agent/START_HERE.md`](docs/agent/START_HERE.md)

Operator:

- [`docs/operator/OPERATOR_GUIDE.en.md`](docs/operator/OPERATOR_GUIDE.en.md)
- [`docs/operator/OPERATOR_GUIDE.fa.md`](docs/operator/OPERATOR_GUIDE.fa.md)

Architecture explanation:

[`docs/architecture/WHY_AND_HOW.md`](docs/architecture/WHY_AND_HOW.md)

Primary external sources:

[`docs/references/PRIMARY_SOURCES.md`](docs/references/PRIMARY_SOURCES.md)

Canonical policy remains [`ARCHITECTURE.md`](ARCHITECTURE.md).

## Release checks

Local:

```bash
python3 scripts/test_verification_lint.py
python3 scripts/test_production_readiness_lint.py
python3 scripts/test_build_agent_bundle.py
python3 scripts/build_agent_bundle.py
```

GitHub Actions then rebuilds the bundle from a clean repository checkout, verifies version freshness, compiles the helpers, reruns self-tests, verifies manifest hashes/boundaries and publishes the ZIP + SHA-256 + manifest as an Actions Artifact.
