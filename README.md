# Agentic Flow Framework

**Framework version:** 1.9 · **Vendor-neutral** · **Repository-first** · **Risk-adaptive**  
**فارسی:** [راهنمای جامع فارسی](docs/GUIDE.fa.md)

> **Use coding agents fast without letting “looks done” become project truth.**

Agentic Flow is a practical operating framework for coding agents. It separates **what should be done**, **who may approve it**, **what the agent may change**, **where it may run**, and **what evidence is strong enough to call it done**.

## Why use it?

- **Less scope drift** — tasks are bounded before implementation.
- **Less false confidence** — mocks, CI, screenshots and HTTP 200s cannot silently prove stronger claims.
- **Safer autonomy** — agents can move quickly inside explicit boundaries instead of asking permission for every line.
- **Real testing** — behavior claims require an environment that can actually exercise the changed path.
- **Independent review** — the Executor does not self-certify material closure.
- **Safer Git work** — unknown dirty work is protected from destructive restore/reset operations.
- **Controlled production** — production actions require explicit authority and a recovery plan.
- **Durable project memory** — important state lives in the repository, not buried in chat history.

## The model in 20 seconds

```text
Operator intent
→ Designer: task contract + engineering advisory
→ Manager: review / freeze / bounded authority
→ Executor: implement + test on isolated branch
→ adversarial review
→ Manager: consolidated findings
→ bounded remediation
→ evidence-based closure / merge
```

**Quality requirements stay fixed. Process ceremony adapts to risk.**

| Risk | Default flow |
|---|---|
| LOW | implement → focused test → compact review |
| MEDIUM | short preflight → implement → cold review → bounded remediation |
| HIGH | frozen contract → failure-surface preflight → explicit apply authority → adversarial review → Manager closure |

## Production mode

When production mutation is enabled, **every production change must have a rollback or explicit forward-recovery plan before execution**.

Minimum production-change contract:

- exact target environment;
- exact artifact/config/change identity;
- expected success and health signals;
- abort condition;
- rollback/recovery steps;
- stateful/data rollback constraints;
- person/agent authorized to execute recovery;
- post-change verification.

```text
NO ROLLBACK / RECOVERY PLAN
→ NOT EXECUTION-READY FOR PRODUCTION MUTATION
```

For irreversible changes, the plan must state why rollback is impossible and define the tested forward-recovery path, backups/checkpoints, blast-radius controls and STOP conditions.

See [Production Delivery](production/DELIVERY.md) and [Architecture](ARCHITECTURE.md).

## What it prevents

```text
plan exists           != implementation
unit test passes      != real integration
HTTP 200              != persistence
CI green              != deployed behavior
commit                != deployed artifact
backup enabled        != recoverability
reviewer says PASS    != behavioral evidence
```

## Fast adoption

1. Clone/pin this framework beside your project.
2. Read [Getting Started](docs/GETTING_STARTED.md).
3. Give the coding agent [`docs/agent/START_HERE.md`](docs/agent/START_HERE.md).
4. Start with `STRICT_PREVIEW` and let related edits be grouped into bounded batches.
5. For material work, use the copy-ready [Designer](prompts/operator/TASK_DESIGNER.md) and [Manager](prompts/operator/MANAGER_REVIEWER.md) prompts.
6. Require real-enough test access for the claims being closed.
7. Review the actual commit/PR and receipts—not only the Executor summary.

Recommended layout:

```text
workspace/
├── agentic-flow-framework/
└── your-project/
```

## Key rules

- **Task authority ≠ mutation authority ≠ environment authority ≠ external-side-effect authority.**
- A claim may be **no broader than its current receipt**.
- Mock-only evidence closes only the modeled/unit boundary.
- HIGH risk means **strong boundaries + bounded autonomy**, not approval spam.
- Same-task review findings may use a **Controlled Remediation Window**.
- New provider/schema/public API/security boundary/production scope invalidates that window.
- Real provider calls, paid APIs, messages and deployments require explicit authority.
- Unknown/unowned dirty work must be preserved.
- Production mutation requires rollback or explicit forward-recovery readiness.

## Read only what you need

For a human newcomer:

1. **This README** — purpose and operating model.
2. **[Getting Started](docs/GETTING_STARTED.md)** — adoption steps.
3. **[Task Workflow](docs/agent/TASK_WORKFLOW_DRAFT_REVIEW_APPLY_VERIFY.md)** — execution lifecycle.
4. **[Persian Guide](docs/GUIDE.fa.md)** — راهنمای فارسی کامل.

For an Executor:

```text
docs/agent/START_HERE.md
→ current project profile
→ current task
→ only triggered schemas / verification / production profiles
```

## Deeper references

- [Why Agentic Flow](docs/WHY_AGENTIC_FLOW.md) — problem and evidence map.
- [Comparison](docs/COMPARISON.md) — trade-offs vs ordinary coding-agent use.
- [Validation Status](docs/VALIDATION_STATUS.md) — what is proven and what is not.
- [End-to-End Example](docs/examples/END_TO_END_TASK.md) — worked flow.
- [Architecture](ARCHITECTURE.md) — canonical invariants.
- [Mutation Approval Policy](schemas/MUTATION_APPROVAL_POLICY.md) — approvals and remediation windows.
- [Project Profile](schemas/PROJECT_PROFILE_CONFIG.md) — project-level operating policy.
- [Primary Sources](docs/references/PRIMARY_SOURCES.md) — external provenance.

## What this project does **not** claim

Agentic Flow does **not** claim that more process is always better, that AI always makes engineering faster, or that this framework has been empirically proven superior to every alternative. The goal is narrower: **keep agentic development fast while making scope, authority, evidence, recovery and closure explicit.**

## Repository checks

```bash
python3 -m unittest discover -s scripts -p 'test_*.py'
python3 scripts/test_docs_onboarding.py
python3 scripts/build_agent_bundle.py
```
