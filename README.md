# Agentic Flow Framework

**Framework version:** 1.7  
**Updated:** 2026-09-12  
**Canonical policy:** [`ARCHITECTURE.md`](ARCHITECTURE.md)

A repository-first, vendor-neutral operating framework for reliable, cost-aware and production-operable coding agents.

> Durable project memory; disposable working context.

> A claim may be no broader than the receipt that establishes it.

## Recommended use: clone the framework

The normal distribution path is the Git repository itself:

```bash
git clone https://github.com/shiraziamir/agentic-flow-framework.git
```

Recommended layout:

```text
workspace/
├── agentic-flow-framework/
└── my-project/
```

Then open `my-project/` with your coding agent and give it:

```text
Adopt Agentic Flow for this repository.
Framework source: ../agentic-flow-framework
Start by reading ../agentic-flow-framework/docs/agent/START_HERE.md and ../agentic-flow-framework/ARCHITECTURE.md.
Inspect this project read-only first.
Use STRICT_PREVIEW mutation approval unless this project's existing .agentic/PROJECT_PROFILE.yaml explicitly says otherwise.
Before every mutation batch, tell me the current state, proposed state, files/resources affected, impact, planned checks, rollback/recovery when relevant, and what remains out of scope. Then wait for my explicit APPROVE/APPLY before mutating.
If coding is already in progress, follow MIDSTREAM_ADOPTION and preserve current edits.
```

A copy-ready version is in:

[`prompts/bootstrap/CLONE_AND_ADOPT.md`](prompts/bootstrap/CLONE_AND_ADOPT.md)

Human/operator walkthrough:

[`docs/operator/CLONE_AND_ADOPT.md`](docs/operator/CLONE_AND_ADOPT.md)

### Why clone is the default

- the framework remains visible and versionable as normal Git content;
- updates are explicit with `git fetch` / `git pull --ff-only` or a pinned commit/tag;
- no one has to discover a separate Actions Artifact to start using the framework;
- the target project's `.agentic/` state stays project-owned;
- the coding agent can read framework files lazily without copying the whole framework into product source.

For higher-assurance use, pin the framework to a reviewed commit/tag rather than automatically tracking the newest `main`.

## Mutation approval modes

The project profile may define:

```text
STRICT_PREVIEW
MATERIAL_CHANGES_ONLY
BOUNDED_AUTONOMY
```

See [`schemas/MUTATION_APPROVAL_POLICY.md`](schemas/MUTATION_APPROVAL_POLICY.md).

Recommended first-adoption default:

```text
STRICT_PREVIEW
```

In this mode, read-only discovery is allowed, but every bounded mutation batch requires a compact preview:

```text
CURRENT STATE
→ PROPOSED STATE
→ WHY
→ WILL CHANGE
→ IMPACT
→ VERIFY
→ ROLLBACK / RECOVERY when material
→ OUT OF SCOPE
→ wait for APPROVE / APPLY
```

The agent should group tightly related edits into one batch instead of asking permission line-by-line. If implementation discovers a materially different change, it stops and asks again with a revised preview.

Mutation approval does not authorize production access or destructive/data-sensitive operations; environment and task-governance rules remain separate.

## GitHub Actions Artifact

GitHub Actions still builds a portable ZIP as a release/checking output. That Artifact is stored under the workflow run in **GitHub Actions**, not committed into the repository file tree.

The Artifact is useful for:

- offline distribution;
- reproducible release receipts;
- manifest/hash verification;
- CI proof that the portable package can be built from a clean checkout.

It is optional for normal adoption; cloning the repository is the simpler default.

Local bundle commands:

```bash
python3 scripts/test_build_agent_bundle.py
python3 scripts/build_agent_bundle.py
```

Default output:

```text
dist/agentic-flow-agent-bundle.zip
```

## If you use the portable bundle

Extract its `agentic-flow/` directory into the target repository as:

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

The bundle includes operator/architecture/reference material for offline use, but those files remain cold by default for coding-agent context.

## Practical task lifecycle

For material changes:

```text
REQUEST
→ DRAFT
→ REVIEW
→ FREEZE / APPLY AUTHORIZATION when required
→ CHANGE PREVIEW / APPROVAL when policy requires
→ APPLY
→ VERIFY + REPORT
→ independent closure when required
```

Practical explanation:

[`docs/agent/TASK_WORKFLOW_DRAFT_REVIEW_APPLY_VERIFY.md`](docs/agent/TASK_WORKFLOW_DRAFT_REVIEW_APPLY_VERIFY.md)

If the project uses `STRICT_PREVIEW`, task approval and mutation approval are related but distinct: the frozen task says what work is authorized conceptually; the change preview says what the agent is about to mutate now.

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

The project profile defines what **should** be true: testing policy, mutation-approval mode, readiness tier, environment permissions, operational/security requirements and pattern-selection policy.

Reality is established by receipts and explicit operational gaps. Temporary exceptions use owned/expiring `TEMPORARY_OVERRIDE` artifacts instead of silently weakening the baseline.

## Documentation routes

Coding agent:

[`docs/agent/START_HERE.md`](docs/agent/START_HERE.md)

Operator:

- [`docs/operator/CLONE_AND_ADOPT.md`](docs/operator/CLONE_AND_ADOPT.md)
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

GitHub Actions rebuilds the bundle from a clean checkout, verifies version freshness, compiles the helpers, reruns self-tests, verifies manifest hashes/boundaries and publishes the ZIP + SHA-256 + manifest as an Actions Artifact.
