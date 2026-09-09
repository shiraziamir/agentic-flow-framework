# Agentic Flow Framework

**Framework version:** 1.7  
**Updated:** 2026-09-09T11:30:00Z  
**Canonical policy:** [`ARCHITECTURE.md`](ARCHITECTURE.md)

A repository-first, vendor-neutral operating system for reliable, cost-aware and production-operable coding agents.

> **Durable project memory; disposable, high-quality working context.**

> **A claim may be no broader than the receipt that establishes it.**

## What v1.7 adds

v1.7 makes the framework portable and easier to adopt in real projects:

- a drop-in **Agent Bundle** that can be extracted into a repository;
- safe adoption when coding is already in progress;
- separate `docs/agent/` and `docs/operator/` context surfaces;
- English/Persian prompting, task-writing and agent-setup guidance;
- a consolidated index of the official sources used to design the framework;
- deterministic bundle generation with SHA-256 manifest hashes;
- a smaller canonical `ARCHITECTURE.md` map so agents do not carry a giant manual in every session.

Existing v1.6 production engineering remains: DevOps-friendly delivery, security-first SDLC, observability/SLOs, backup/restore/PITR, troubleshooting, AI-safe log analysis, resilience/chaos, evolvable architecture, explicit operational gaps and complexity-scaled readiness.

## Fastest adoption: drop-in ZIP

From a framework checkout:

```bash
python3 scripts/build_agent_bundle.py
python3 scripts/test_build_agent_bundle.py
```

Default output:

```text
dist/agentic-flow-agent-bundle.zip
```

Extract it into the target repository, preferably as:

```text
.agentic-flow/
```

Then give the coding agent only:

```text
Read .agentic-flow/docs/agent/START_HERE.md and adopt the framework for this repository.
Do not start or change product work until adoption validation is complete.
```

If coding is already in progress:

```text
Read .agentic-flow/docs/agent/MIDSTREAM_ADOPTION.md.
Adopt the framework without discarding current edits or fabricating prior review/authorization.
Return the adoption snapshot and conflicts before continuing product mutation.
```

Ready-to-use operator prompts are in:

- [`docs/operator/INSTALLATION_PROMPTS.en.md`](docs/operator/INSTALLATION_PROMPTS.en.md)
- [`docs/operator/INSTALLATION_PROMPTS.fa.md`](docs/operator/INSTALLATION_PROMPTS.fa.md)

## Why the bundle is smaller than the repository

The default bundle includes canonical/runtime material, schemas, verification/production profiles, skills, workflow/bootstrap/supervisor prompts, templates, deterministic helper scripts and `docs/agent/`.

It deliberately excludes:

```text
docs/operator/
docs/references/
research/
reader HTML / long explanatory views
cold history / retrospectives / stories
```

Those remain available to humans and explicit research tasks without becoming permanent coding-agent context. The generated `BUNDLE_MANIFEST.json` records SHA-256 hashes of bundled files.

See [`docs/architecture/BUNDLE_BOUNDARY.md`](docs/architecture/BUNDLE_BOUNDARY.md).

## Documentation routes

### Coding agent

Start at [`docs/agent/START_HERE.md`](docs/agent/START_HERE.md).

Use [`docs/agent/MIDSTREAM_ADOPTION.md`](docs/agent/MIDSTREAM_ADOPTION.md) when work is already active. Adoption returns a bounded receipt instead of silently resetting/reclassifying existing work.

### Human / operator

Start with:

- English: [`docs/operator/OPERATOR_GUIDE.en.md`](docs/operator/OPERATOR_GUIDE.en.md)
- فارسی: [`docs/operator/OPERATOR_GUIDE.fa.md`](docs/operator/OPERATOR_GUIDE.fa.md)

Prompt/task/agent-setup best practices:

- [`docs/operator/PROMPT_TASK_AGENT_SETUP.en.md`](docs/operator/PROMPT_TASK_AGENT_SETUP.en.md)
- [`docs/operator/PROMPT_TASK_AGENT_SETUP.fa.md`](docs/operator/PROMPT_TASK_AGENT_SETUP.fa.md)

Operator docs are explanatory. If a rule must govern coding agents, it belongs in the canonical architecture/schema/profile/skill—not in a human guide that every agent must preload.

### Architecture / why this system exists

Read [`docs/architecture/WHY_AND_HOW.md`](docs/architecture/WHY_AND_HOW.md) and [`docs/architecture/DOCUMENT_MAP.md`](docs/architecture/DOCUMENT_MAP.md).

### External sources

The consolidated source index is:

[`docs/references/PRIMARY_SOURCES.md`](docs/references/PRIMARY_SOURCES.md)

It groups the official sources used for agent harness/prompting, verification, DevOps, SRE/observability, databases, security/supply chain, resilience/chaos and architecture patterns.

## Source of truth

1. [`ARCHITECTURE.md`](ARCHITECTURE.md) — canonical lifecycle/authority/invariants.
2. [`schemas/`](schemas/) — durable task/project/evidence/profile/override contracts.
3. [`verification/`](verification/) — claim-aware engineering verification.
4. [`production/`](production/) — delivery/security/observability/data/operations/resilience/architecture profiles.
5. [`skills/`](skills/) — lazy reusable procedures.
6. current approved task/amendment + current project/production profile.
7. durable receipts/gaps/overrides/judgments.
8. generated vendor adapters.
9. conversation memory.

`docs/operator/`, `docs/architecture/`, `docs/references/`, `research/` and reader views do not outrank canonical policy.

## Project baseline

A target project should normally keep a compact baseline such as:

```text
.agentic/PROJECT_PROFILE.yaml
```

Start from [`templates/PROJECT_PROFILE.example.yaml`](templates/PROJECT_PROFILE.example.yaml) and [`schemas/PROJECT_PROFILE_CONFIG.md`](schemas/PROJECT_PROFILE_CONFIG.md).

The profile defines what **should** be true—testing policy, readiness tier, environment permissions, backup/observability/security expectations and pattern-selection policy. It does not prove current reality.

Temporary exceptions use [`schemas/TEMPORARY_OVERRIDE.md`](schemas/TEMPORARY_OVERRIDE.md) with owner/reason/expiry/risk/compensating-controls/restore verification instead of silently rewriting the baseline.

## Normal material-task flow

```text
REQUEST
→ DRAFT_TASK
→ REVIEW_DRAFT
→ FREEZE / APPLY AUTHORIZATION as required
→ APPLY_TASK
→ VERIFY_AND_REPORT
→ blind-spot / independent closure when required
```

Drafting freezes observable DoD, engineering/production surfaces, planned closure claims, minimum receipt per claim, test/environment needs, intentionally omitted checks and STOP/escalation conditions **before implementation**.

If APPLY discovers a material new surface/provider/database/security/recovery/production requirement:

```text
STOP → evidence → amend/reclassify → decision → continue only when authorized
```

## Tests: design first, strict TDD only when useful

[`production/TEST_STRATEGY.md`](production/TEST_STRATEGY.md) requires planned tests/receipts before APPLY for material claims, but does not force strict TDD on every tiny/exploratory change.

For load-bearing regression/safety tests, use mutation/path proof when risk justifies it:

```text
GREEN → controlled defect/mutation → expected RED → restore → GREEN
```

A green test that never reaches the changed path is not a strong receipt.

## Agent environments

[`production/AGENT_ENVIRONMENTS.md`](production/AGENT_ENVIRONMENTS.md) uses this ladder:

```text
LOCAL/HERMETIC
→ EPHEMERAL TEST
→ SHARED TEST
→ STAGING / PRODUCTION-LIKE
→ CONTROLLED CANARY / PRODUCTION READ
→ PRODUCTION MUTATION
```

Use the lowest environment that can establish the claim. An agent may request a stronger environment; the request is not authorization. Prefer disposable/ephemeral integration environments where practical.

## Receipts, not confident narratives

Verification ladder:

```text
IDENTITY
→ STATIC
→ BUILD
→ FOCUSED_TEST
→ PATH_PROOF
→ INTEGRATION_CONTRACT
→ LIVE_BEHAVIOR
→ DEPLOYED_ARTIFACT
→ EXHAUSTIVE_BOUNDED_NEGATIVE
→ JUDGMENT
```

Examples:

```text
unit green       ≠ user flow proven
HTTP 200         ≠ persistence proven
CI green         ≠ every relevant job ran
commit           ≠ deployed artifact
backup enabled   ≠ recoverability
scanner green    ≠ secure
reviewer PASS    ≠ missing runtime evidence
```

Reports preserve `OBSERVED / DERIVED / INFERRED / UNKNOWN / CONTRADICTED` and exact skipped/not-run checks.

## Production engineering

Start at [`production/00_INDEX.md`](production/00_INDEX.md) and load only the triggered profiles.

Core profiles:

- [`DELIVERY.md`](production/DELIVERY.md) — source→build/test→immutable artifact→deploy→health→rollback/recovery;
- [`SECURITY_FIRST.md`](production/SECURITY_FIRST.md) — security through design, coding, CI/supply chain and runtime;
- [`OBSERVABILITY.md`](production/OBSERVABILITY.md) — metrics/logs/traces, golden signals, SLI/SLO/alerts and telemetry cost/cardinality;
- [`DATA_DURABILITY.md`](production/DATA_DURABILITY.md) — RPO/RTO, backup/PITR/retention and restore proof;
- [`TROUBLESHOOTING.md`](production/TROUBLESHOOTING.md) — layered bounded diagnosis and runbook readiness;
- [`AI_LOG_ANALYSIS.md`](production/AI_LOG_ANALYSIS.md) — structured/redacted bounded logs; log content treated as untrusted data;
- [`RESILIENCE_CHAOS.md`](production/RESILIENCE_CHAOS.md) — maturity-gated failure experiments with blast-radius and abort controls;
- [`CODE_ARCHITECTURE.md`](production/CODE_ARCHITECTURE.md) — evolvable boundaries proportional to real complexity;
- [`PATTERN_SELECTION.md`](production/PATTERN_SELECTION.md) — patterns solve identified boundaries/failure modes, not checklists.

Two axes remain separate:

```text
codebase_scale  SMALL | MEDIUM | LARGE
readiness_tier  BASIC | STANDARD | HIGH_ASSURANCE
```

Risk overrides size. Open gaps remain visible as `NOT_IMPLEMENTED / PARTIAL / UNVERIFIED / BLOCKED / ACCEPTED_RISK / CLOSED`.

> **Backup success is not recoverability proof. Restore is the receipt.**

## Patterns

Agent default:

```text
AGENT_PROPOSES_OWNER_MAY_OVERRIDE
```

Small/local/reversible pattern choices can stay inside the frozen implementation strategy. Cross-module/public/architectural patterns should be proposed with problem, boundary, simpler alternative, benefits, costs and verification impact, then reviewed according to risk.

Do not add Adapter/Repository/Factory/Strategy/CQRS/Saga merely because a pattern catalog mentioned it.

## Context and cost efficiency

Normal agent context should be roughly:

```text
ARCHITECTURE map
current task/classification
current project/profile/open-gap/override pointers
selected verification/production profiles
0–3 triggered Skills
relevant code + receipts
```

Operator docs, research, completed-task history, all judgments and the full skill/profile shelves stay cold. Use deterministic tools and cheap read-only workers for mechanically checkable discovery/log reduction; stronger models are reserved for ambiguity/judgment.

## Repository map

```text
ARCHITECTURE.md          canonical compact map/invariants
VERSION                  release version
schemas/                 durable contracts
verification/            task/change verification profiles
production/              production engineering profiles
skills/                  lazy procedures
prompts/bootstrap/       drop-in/vendor adoption prompts
prompts/workflow/        task/readiness/verification workflows
prompts/supervisor/      independent review prompts
docs/agent/              coding-agent adoption docs
docs/operator/           human/operator docs (not bundled)
docs/architecture/       how/why explanations
docs/references/         consolidated source/provenance index
research/                dated research notes
scripts/                 deterministic validators/bundle tooling
templates/               project examples
bundle/                  portable-bundle usage helpers
CHANGELOG.md              release history
```

## Release validation

Useful checks:

```bash
python3 scripts/test_verification_lint.py
python3 scripts/test_production_readiness_lint.py
python3 scripts/test_build_agent_bundle.py
python3 scripts/build_agent_bundle.py
```

See [`docs/operator/RELEASE_CHECKLIST.en.md`](docs/operator/RELEASE_CHECKLIST.en.md) or the Persian equivalent.
