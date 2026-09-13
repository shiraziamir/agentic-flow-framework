# Agentic Flow Framework

**Framework version:** 1.9 · **Vendor-neutral** · **Repository-first** · **Risk-adaptive**  
**فارسی:** [راهنمای جامع فارسی](docs/GUIDE.fa.md)

> **Use coding agents fast without letting “looks done” become project truth.**

Agentic Flow is a practical operating framework for coding agents. It separates **what should be done**, **who may approve it**, **what an agent may change**, **where it may run**, and **what evidence is strong enough to call the work done**.

## The five questions

If your agent workflow cannot answer these quickly, this project is for you:

1. **What exactly is authorized?**
2. **What actually changed?**
3. **What evidence really proves it?**
4. **What remains unproven?**
5. **If it is wrong, how do we stop or recover?**

## Why use it?

- **Less scope drift** — tasks are bounded before implementation.
- **Less false confidence** — mocks, CI, screenshots and reviewer agreement cannot silently prove stronger behavior.
- **Safer autonomy** — agents move quickly inside explicit boundaries instead of asking permission for every line.
- **Real testing** — behavior claims require an environment that can exercise the changed path.
- **Independent review** — implementation, context, authority and evidence are separated for material closure.
- **No fake consensus** — multiple models agreeing is useful review coverage, not independent behavioral evidence.
- **Less human copy/paste** — engineering state moves through repository artifacts; humans transport authority and decisions.
- **Safer Git work** — unknown dirty work is protected from destructive restore/reset operations.
- **Controlled production** — production actions require explicit authority and rollback or forward-recovery readiness.
- **Durable project memory** — a fresh session can continue from committed state without replaying old chats.

## The model in 20 seconds

```text
Operator intent
→ Designer: task contract + engineering advisory
→ Manager: review / freeze / bounded authority
→ Executor: implement + real-enough tests
→ cold/adversarial review
→ Manager: one consolidated finding set
→ one bounded remediation round by default
→ Independent Judge for HIGH-risk closure (read-only)
→ Operator: production / business authority
```

**Quality requirements stay fixed. Process ceremony adapts to risk.**

| Risk | Default flow |
|---|---|
| LOW | implement → focused test → compact review |
| MEDIUM | short preflight → implement → cold review → one bounded remediation → Manager review |
| HIGH | frozen contract → failure-surface preflight → bounded execution → adversarial review → Manager review/remediation → read-only independent closure |

## One rule that prevents fake confidence

```text
MULTI-MODEL AGREEMENT
!=
INDEPENDENT BEHAVIORAL EVIDENCE
```

A second or third model may improve review coverage. It does **not** upgrade a unit/mock claim into integration, deployment or production proof. Raw receipts, real execution paths and runtime observations decide claim strength.

## Production mode

When production mutation is enabled, **every production change must have a rollback or explicit forward-recovery plan before execution**.

Minimum production-change contract:

- exact target environment and artifact/config/change identity;
- expected success and health signals;
- abort condition;
- rollback/recovery steps;
- stateful/data rollback constraints;
- recovery authority/owner;
- post-change verification.

```text
NO ROLLBACK / RECOVERY PLAN
→ NOT EXECUTION-READY FOR PRODUCTION MUTATION
```

The Independent Judge is **read-only by default**. Production mutation remains a separate Operator-authorized action. For irreversible changes, define why rollback is unsafe/impossible plus forward recovery, backup/checkpoint, blast-radius controls and STOP conditions.

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
three models say PASS != three independent engineers
```

## Fast adoption

1. Clone/pin this framework beside your project.
2. Read [Getting Started](docs/GETTING_STARTED.md).
3. Give the Executor [`docs/agent/START_HERE.md`](docs/agent/START_HERE.md).
4. Start with `STRICT_PREVIEW`; group related edits into bounded batches.
5. For material work, use the [Designer](prompts/operator/TASK_DESIGNER.md) and [Manager](prompts/operator/MANAGER_REVIEWER.md) prompts.
6. For HIGH-risk closure, use the read-only [Independent Judge](prompts/operator/INDEPENDENT_JUDGE.md).
7. Require real-enough test access for the claims being closed.
8. Let repository artifacts carry task/review/receipt state; involve the human for actual authority, risk and business decisions.

Recommended layout:

```text
workspace/
├── agentic-flow-framework/
└── your-project/
```

## Key rules

- **Task authority ≠ mutation authority ≠ environment authority ≠ external-side-effect authority.**
- A claim may be **no broader than its current receipt**.
- **Model agreement does not upgrade evidence strength.**
- Independent closure separates implementation, context, authority and evidence; model diversity is optional defense-in-depth.
- The Independent Judge is read-only by default and cannot mutate production.
- HIGH risk means **strong boundaries + bounded autonomy**, not approval spam.
- Same-task findings get **one remediation round by default**; a second round requires a new material finding and stays within the configured maximum.
- Real provider calls, paid APIs, messages and deployments require explicit authority.
- Unknown/unowned dirty work must be preserved.
- Production mutation requires rollback or explicit forward-recovery readiness.
- **Human transports authority; repository transports engineering state.**
- A fresh session is safe only after durable state is checkpointed.

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
- [Role Setup](docs/operator/DESIGNER_MANAGER_SETUP.md) — Designer/Manager/Executor/Judge permissions.
- [End-to-End Example](docs/examples/END_TO_END_TASK.md) — worked flow.
- [Architecture](ARCHITECTURE.md) — canonical invariants.
- [Project Profile](schemas/PROJECT_PROFILE_CONFIG.md) — project-level operating policy.
- [Primary Sources](docs/references/PRIMARY_SOURCES.md) — external provenance.

## What this project does **not** claim

Agentic Flow does **not** claim that more process is always better, that different models are statistically independent, that AI always makes engineering faster, or that this framework has been empirically proven superior to every alternative. The goal is narrower: **keep agentic development fast while making scope, authority, evidence, independence, recovery and closure explicit.**

## Repository checks

```bash
python3 -m unittest discover -s scripts -p 'test_*.py'
python3 scripts/test_docs_onboarding.py
python3 scripts/build_agent_bundle.py
```
