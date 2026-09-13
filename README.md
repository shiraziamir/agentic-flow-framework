# Agentic Flow Framework

**Framework version:** 1.10 · **Vendor-neutral** · **Repository-first** · **Risk-adaptive**  
**فارسی:** [راهنمای جامع فارسی](docs/GUIDE.fa.md)

> **Use coding agents fast without letting “looks done” become project truth—or letting fast prototyping become architecture by accident.**

Agentic Flow is a practical operating framework for coding agents. It separates **product intent**, **architecture discovery**, **what is authorized**, **what an agent may change**, **where it may run**, and **what evidence is strong enough to call the work done**.

## The five questions

If your agent workflow cannot answer these quickly, this project is for you:

1. **What exactly is authorized?**
2. **What actually changed?**
3. **What evidence really proves it?**
4. **What remains unproven?**
5. **If it is wrong, how do we stop or recover?**

## Starting a new project? Do not jump from idea to code

If you only know the product outcome, that is enough to start—but not enough to start coding blindly.

```text
PRODUCT INTENT
→ PRODUCT BRIEF
→ QUALITY / EVAL CONTRACT
→ ARCHITECTURE DISCOVERY
→ 2–3 MINIMAL OPTIONS
→ WALKING SKELETON
→ ARCHITECTURE CHECKPOINT
→ PRODUCT BASELINE
→ NORMAL TASK FLOW
```

The Product Owner owns **WHY / WHAT / business trade-offs**. The Project Architect owns **system-shape discovery**. The Executor owns **implementation**.

Read [Project Inception & Architecture Discovery](docs/agent/PROJECT_INCEPTION_ARCHITECTURE.md) or use the copy-ready [Project Architect prompt](prompts/operator/PROJECT_ARCHITECT.md).

## Vibe Coding is a supported mode—but it is explicit

Set the project to:

```yaml
project_mode:
  mode: VIBE_PROTOTYPE
```

Use `VIBE_PROTOTYPE` when the main question is “can this idea work?” or “do users like this interaction?”. It deliberately optimizes for learning speed.

But:

```text
VIBE_PROTOTYPE
!=
PRODUCTION BASELINE
```

Defaults in Vibe mode:

- fast experimentation is allowed;
- architecture may be provisional;
- code may be sacrificial;
- sensitive/production data and production mutation stay separately controlled;
- production-readiness claims are denied;
- moving to `PRODUCT_BUILD` requires explicit re-baselining and an architecture checkpoint;
- prototype code must be classified as `REUSE_AS_IS | REUSE_AFTER_REVIEW | REWRITE | DISCARD` before becoming product baseline.

**Do not “promote the prototype” by simply continuing to code.** Preserve the learnings, evals and useful code; then establish the product architecture intentionally.

## Swamp Guard — detect the bog before it compounds

Agentic Flow continuously checks for architectural/process drift at material checkpoints. It does not wait until the project is already expensive to repair.

```text
CLEAR
WATCH
ALERT
STOP_REBASELINE
```

Typical swamp signals:

- the same subsystem is repeatedly redesigned or remediated;
- new frameworks, datastores or abstractions appear without a product constraint that requires them;
- multiple mechanisms compete for the same responsibility;
- AI/RAG tuning starts before a representative eval baseline exists;
- features keep growing before a real end-to-end vertical slice works;
- architecture decisions exist only in chat;
- source-of-truth/state ownership becomes ambiguous;
- “temporary” exceptions become permanent structure;
- a prototype quietly accumulates production expectations;
- complexity grows faster than demonstrated product value.

Hard cases trigger:

```text
SWAMP ALERT: STOP_REBASELINE
→ stop compounding local patches
→ return to architecture discovery
→ simplify / measure / decide
→ continue only from a coherent baseline
```

The goal is not to kill experimentation. The goal is to stop **unmeasured complexity from becoming architecture by accident**.

## Why use it?

- **Less scope drift** — tasks are bounded before implementation.
- **Better greenfield starts** — product intent is converted into constraints, evals and architecture options before serious coding.
- **Less architecture debt** — hard-to-change invariants are frozen early; easy experiment variables remain open.
- **Early swamp detection** — architecture churn, framework proliferation and eval-free tuning trigger alerts/re-baselining.
- **Less false confidence** — mocks, CI, screenshots and reviewer agreement cannot silently prove stronger behavior.
- **Safer autonomy** — agents move quickly inside explicit boundaries instead of asking permission for every line.
- **Real testing** — behavior claims require an environment that can exercise the changed path.
- **Independent review** — implementation, context, authority and evidence are separated for material closure.
- **No fake consensus** — multiple models agreeing is useful review coverage, not independent behavioral evidence.
- **Less human copy/paste** — engineering state moves through repository artifacts; humans transport authority and decisions.
- **Controlled production** — production actions require explicit authority and rollback or forward-recovery readiness.
- **Durable project memory** — a fresh session can continue from committed state without replaying old chats.

## The normal task model in 20 seconds

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

## What it prevents

```text
prototype works       != product architecture validated
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
3. If greenfield/early-stage, choose `VIBE_PROTOTYPE` or `PRODUCT_BUILD` and run [Project Inception](docs/agent/PROJECT_INCEPTION_ARCHITECTURE.md) before serious coding.
4. Give the Executor [`docs/agent/START_HERE.md`](docs/agent/START_HERE.md).
5. Start with `STRICT_PREVIEW`; group related edits into bounded batches.
6. For material tasks, use the [Designer](prompts/operator/TASK_DESIGNER.md) and [Manager](prompts/operator/MANAGER_REVIEWER.md) prompts.
7. For HIGH-risk closure, use the read-only [Independent Judge](prompts/operator/INDEPENDENT_JUDGE.md).
8. Require real-enough test access for the claims being closed.
9. Let repository artifacts carry project/task/review/receipt state; involve the human for actual product, authority, risk and business decisions.

## Key rules

- **VIBE_PROTOTYPE is an experiment mode, not a production-readiness claim.**
- **Freeze hard-to-change invariants, not easy-to-change implementation choices.**
- **No broad feature expansion before the critical walking skeleton is exercised.**
- **For AI/RAG, no serious tuning without a representative eval/quality baseline.**
- **Swamp signals must be surfaced early; severe signals require `STOP_REBASELINE`.**
- Task authority ≠ mutation authority ≠ environment authority ≠ external-side-effect authority.
- A claim may be no broader than its current receipt.
- Model agreement does not upgrade evidence strength.
- The Independent Judge is read-only by default and cannot mutate production.
- HIGH risk means strong boundaries + bounded autonomy, not approval spam.
- Same-task findings get one remediation round by default; a second requires a new material finding.
- Unknown/unowned dirty work must be preserved.
- Production mutation requires rollback or explicit forward-recovery readiness.
- **Human transports authority; repository transports engineering state.**

## Read only what you need

For a human newcomer:

1. **This README** — purpose, Vibe mode and operating model.
2. **[Getting Started](docs/GETTING_STARTED.md)** — adoption steps.
3. **[Project Inception](docs/agent/PROJECT_INCEPTION_ARCHITECTURE.md)** — greenfield/vibe/product architecture lifecycle.
4. **[Task Workflow](docs/agent/TASK_WORKFLOW_DRAFT_REVIEW_APPLY_VERIFY.md)** — execution lifecycle after the project baseline exists.
5. **[Persian Guide](docs/GUIDE.fa.md)** — راهنمای فارسی کامل.

For an Executor:

```text
docs/agent/START_HERE.md
→ current project mode/profile
→ project inception when baseline is missing
→ current task
→ only triggered schemas / verification / production profiles
```

## Deeper references

- [Project Architect Prompt](prompts/operator/PROJECT_ARCHITECT.md) — architecture discovery without premature coding.
- [Why Agentic Flow](docs/WHY_AGENTIC_FLOW.md) — problem and evidence map.
- [Comparison](docs/COMPARISON.md) — trade-offs vs ordinary coding-agent use.
- [Validation Status](docs/VALIDATION_STATUS.md) — what is proven and what is not.
- [Role Setup](docs/operator/DESIGNER_MANAGER_SETUP.md) — Designer/Manager/Executor/Judge permissions.
- [Architecture](ARCHITECTURE.md) — canonical invariants.
- [Project Profile](schemas/PROJECT_PROFILE_CONFIG.md) — project-level operating policy.
- [Primary Sources](docs/references/PRIMARY_SOURCES.md) — external provenance.

## What this project does **not** claim

Agentic Flow does **not** claim that more process is always better, that different models are statistically independent, that Vibe mode makes prototype code production-ready, that AI always makes engineering faster, or that this framework has been empirically proven superior to every alternative. The goal is narrower: **move quickly while making product constraints, architecture, scope, authority, evidence, recovery and closure explicit—and detect the architectural swamp before it compounds.**

## Repository checks

```bash
python3 -m unittest discover -s scripts -p 'test_*.py'
python3 scripts/test_docs_onboarding.py
python3 scripts/build_agent_bundle.py
```