# Agentic Flow Framework

**Framework version:** 1.8  
**Status:** evidence-oriented operating framework; see [Validation Status](docs/VALIDATION_STATUS.md)  
**Persian:** [راهنمای جامع فارسی](docs/GUIDE.fa.md)

Agentic Flow is a repository-first, vendor-neutral operating method for coding agents.

> Coding quickly is not the hard part. The hard part is controlling scope, proving behavior, preserving work, reviewing real changes and knowing what remains unproven.

## Why this repository exists

Normal agent use can end in a plausible but false-complete state: scope drifts, mocks are mistaken for real integration proof, one agent plans/codes/approves itself, tests are green for the wrong reason, provider calls happen without clear authority, or the next person must reconstruct decisions from chat history.

Agentic Flow moves durable engineering state into the repository: project policy, bounded task contracts, mutation/environment authority, evidence receipts, gaps and review decisions.

## Start here — do not read the whole repository

A newcomer normally needs only these **four human-facing files**:

1. **[README.md](README.md)** — what this is and the operating model.
2. **[Getting Started](docs/GETTING_STARTED.md)** — how to adopt it on a real project.
3. **[Task Workflow](docs/agent/TASK_WORKFLOW_DRAFT_REVIEW_APPLY_VERIFY.md)** — how work moves from request to closure.
4. **[Comprehensive Persian Guide](docs/GUIDE.fa.md)** — راهنمای کامل فارسی.

Everything else is reference/cold material until needed.

For an Executor agent, the normal entrypoint is only:

```text
docs/agent/START_HERE.md
→ relevant task/profile
→ triggered schema/skill only when needed
```

Canonical policy remains `ARCHITECTURE.md`, but humans do not need to read it before trying the framework.

## What changes compared with ordinary agent use

| Ordinary agent use | Agentic Flow |
|---|---|
| chat/prompt is practical source of truth | repository refs/contracts are durable source of truth |
| one agent often plans, codes and self-closes | Designer proposes, Manager governs/reviews, Executor implements |
| “tests passed” is a general completion signal | each claim is limited by the receipt that proves it |
| mocks may stand in for real behavior | mock evidence closes only the modeled boundary |
| approval and access blur together | task, mutation, environment and external-effect authority are separate |
| fixes trigger ad-hoc loops | risk-adaptive review + bounded remediation windows |
| dirty work can be accidentally overwritten | unknown/unowned work is protected state |

See [Comparison](docs/COMPARISON.md) for trade-offs.

## What is evidence-based

The design draws on primary guidance from OpenAI, Anthropic, GitHub, Microsoft, Google/SRE, OWASP, NIST, SLSA and other engineering sources. Those sources support component practices such as repository-first context, explicit acceptance criteria, layered testing, production-like validation, protected review and observable operations.

They do **not** prove that Agentic Flow as a whole is universally faster or superior. That remains unproven. See [Why Agentic Flow](docs/WHY_AGENTIC_FLOW.md) and [Validation Status](docs/VALIDATION_STATUS.md).

## Operating model

```text
Operator intent
→ Designer: contract + evidence-constrained advisory
→ Manager: review/freeze + bounded authority
→ Executor: preflight + implementation + real tests
→ cold/adversarial review
→ Manager: consolidated findings
→ bounded remediation window when safe
→ exact diff/receipt review
→ closure / merge decision
```

The key optimization is:

```text
Quality requirements stay fixed.
Process ceremony adapts to risk.
```

### LOW

```text
execute → focused test → compact self-review → commit/report
```

### MEDIUM

```text
short preflight → execute → cold review → bounded remediation → Manager review
```

### HIGH

```text
frozen contract
→ failure-surface preflight
→ explicit initial authorization
→ execute
→ adversarial review
→ Manager consolidated review
→ controlled remediation window
→ final / independent closure when required
```

HIGH risk does **not** mean asking permission for every small correction. It means strong boundaries, strong evidence and bounded autonomy inside those boundaries.

## Before coding: inspect the failure surface

For material behavioral work, preflight at least:

```text
NORMAL PATH
BOUNDARY / INVALID INPUT
DEPENDENCY OR I/O FAILURE
CLEANUP / ROLLBACK FAILURE
OBSERVABILITY / HEALTH PROPAGATION
TEST-ORACLE FALSIFICATION
```

Add only when applicable:

```text
THREAD / PROCESS CONCURRENCY
CRASH / RESTART
DURABILITY / PARTIAL WRITE
PERMISSION / IDENTITY
EXTERNAL PROVIDER
MIGRATION / SCHEMA
CACHE / CONSISTENCY
```

The goal is to catch the likely second and third remediation rounds before the first edit.

## Controlled remediation instead of approval spam

After a Manager consolidated review, same-task findings can be repaired inside a bounded window:

```yaml
remediation_window:
  finding_ids: [R1, R2, R3]
  max_iterations: 2
  allowed_files_or_resources: [<bounded paths>]
  owner_review_required_before_closure: true
```

A new provider, migration, public contract, security boundary, production action, dependency, architecture strategy or out-of-scope file invalidates the window and requires a new authorization.

**Remediation autonomy is not scope autonomy.**

## Required execution environment

An Executor that can edit code but cannot exercise the real changed path is not ready to close that behavior claim.

```text
LOCAL / HERMETIC
→ EPHEMERAL TEST
→ SHARED TEST
→ STAGING / PRODUCTION-LIKE
→ CONTROLLED PRODUCTION READ
→ PRODUCTION MUTATION
```

Use the lowest authorized environment that proves the claim. A mock-only pass may close a unit claim; it does not close persistence, migration, integration, deployment or production claims.

## Workspace and external-effect safety

Unknown/unowned dirty work must be preserved. Commands such as `git reset --hard`, `git clean -fd`, `git checkout --` or destructive restore/force operations are treated as potentially destructive when work can be lost.

Test authority also does not imply permission for real provider calls, paid APIs, messages, deployments or other external side effects.

## Compact evidence

Do not turn evidence into hundred-line reports. Keep raw logs/artifacts separately and use compact receipts:

```yaml
claim: C4
environment: ephemeral-postgres-17
command: pytest tests/integration/test_commit_uncertainty.py
result: PASS 7/7
artifact_ref: artifacts/T125/integration-03.log
proves: commit uncertainty classification
does_not_prove: production provider behavior
```

## Five-minute workflow

1. Read this page and [Getting Started](docs/GETTING_STARTED.md).
2. Clone/pin the framework beside the target repository.
3. Ask the agent to begin at `docs/agent/START_HERE.md` and inspect read-only first.
4. Use `STRICT_PREVIEW` for first adoption, but batch related changes.
5. For material work, define the task/environment/evidence boundary before coding.
6. Let the Executor implement on an isolated branch, run real-enough tests, and undergo adversarial + Manager review.
7. Use a bounded remediation window for same-task findings instead of restarting authorization for every small fix.
8. Close only the claims supported by current receipts.

Try the worked [End-to-End Task](docs/examples/END_TO_END_TASK.md).

## Repository map

If you are new, ignore most directories until triggered:

```text
README.md                         human landing page
docs/GETTING_STARTED.md           adoption
docs/GUIDE.fa.md                  comprehensive Persian guide
docs/agent/START_HERE.md          Executor entrypoint
docs/agent/TASK_WORKFLOW...md     canonical practical workflow
schemas/                          durable contracts, loaded when needed
production/                       production/environment profiles, cold by default
verification/                     verification profiles, cold by default
prompts/                          copy-ready role/bootstrap prompts
research/                         historical research notes; never canonical
```

Detailed map: [docs/architecture/DOCUMENT_MAP.md](docs/architecture/DOCUMENT_MAP.md).

## Safety invariants

- `STRICT_PREVIEW` means bounded preview/approval, not line-by-line approval spam.
- Task, mutation, environment and external-side-effect authority are separate.
- Production/destructive actions require explicit authority.
- A claim may be no broader than its current receipt.
- The Executor does not self-certify material closure.
- Missing evidence remains missing.
- Unknown dirty work is preserved.
- Quality requirements stay fixed even when ceremony is reduced.

## Repository checks

```bash
python3 -m unittest discover -s scripts -p 'test_*.py'
python3 scripts/test_docs_onboarding.py
python3 scripts/build_agent_bundle.py
```

These validate repository mechanics and packaging, not real-world superiority of the framework.
