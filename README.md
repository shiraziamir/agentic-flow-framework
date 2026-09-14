# Agentic Flow Framework

**Framework version:** 1.11 · **Vendor-neutral** · **Repository-first** · **Risk-adaptive**  
**فارسی:** [راهنمای جامع فارسی](docs/GUIDE.fa.md)

> **Use coding agents fast without letting “looks done” become project truth—or letting fast prototyping become architecture by accident.**

Agentic Flow is an operating framework for coding agents. It separates **product intent**, **architecture**, **task priority**, **authority**, **execution**, **evidence**, **review**, and **production control** so agents can move quickly without silently changing what “done” means.

## Understand it in 30 seconds

Every material change must answer five questions:

1. **What exactly is authorized?**
2. **What actually changed?**
3. **What evidence really proves it?**
4. **What remains unproven?**
5. **If it is wrong, how do we stop or recover?**

Normal product flow:

```text
PRODUCT INTENT
→ PRODUCT / EVAL CONSTRAINTS
→ ARCHITECTURE DISCOVERY
→ SYSTEM TRUTH / DATA AUTHORITY MAP
→ WALKING SKELETON
→ PRIMARY TASK
→ BOUNDED IMPLEMENTATION
→ LOCAL LENS + SYSTEM LENS
→ REVIEW / REMEDIATION
→ INDEPENDENT CLOSURE when justified
→ OPERATOR PRODUCTION AUTHORITY
→ ROLLBACK / RECOVERY READY
```

**Quality requirements stay fixed. Ceremony adapts to risk.**

## Three practical operating presets

You should not configure twenty controls before doing useful work. Start from a preset and override only what the project truly needs.

```yaml
operating_preset: VIBE_FAST | PRODUCT_STANDARD | HIGH_ASSURANCE
```

| Preset | Use for | Default posture |
|---|---|---|
| `VIBE_FAST` | disposable experiments / “can this idea work?” | fast, compact review, sacrificial code allowed, no production claims |
| `PRODUCT_STANDARD` | normal maintainable product | inception when needed, bounded tasks, Dual-Lens, real-enough tests, one remediation by default |
| `HIGH_ASSURANCE` | money, identity, privacy, tenant isolation, critical durability, destructive/regulated/high-consequence work | stronger evidence, explicit affected system dimensions, independent closure where justified |

Project phase is separate from the preset:

```text
VIBE_PROTOTYPE | PRODUCT_BUILD | MAINTENANCE
```

`VIBE_PROTOTYPE` is a learning mode, **not** a production baseline.

## Starting from only a product idea

You do not need to know the implementation stack. The Product Owner should define the outcome and business constraints; the Project Architect discovers the smallest viable system shape.

```text
PRODUCT INTENT
→ PRODUCT BRIEF
→ QUALITY / EVAL CONTRACT
→ ARCHITECTURE DISCOVERY
→ SYSTEM TRUTH / DATA AUTHORITY MAP
→ CURRENT SCALE BOUNDARY
→ 2–3 MINIMAL OPTIONS when useful
→ WALKING SKELETON
→ ARCHITECTURE CHECKPOINT
→ PRODUCT BASELINE
```

For AI/RAG/search work: **no serious tuning before a representative eval baseline exists.** Do not freeze vector vendor, chunk size, reranker, prompt or framework merely because an agent knows one well.

Read [Project Inception](docs/agent/PROJECT_INCEPTION_ARCHITECTURE.md).

## Dual-Lens engineering

Every material change is seen through two lenses:

```text
LOCAL LENS
Does the changed behavior work correctly?

SYSTEM LENS
What truth does the whole system claim after this change?
```

System dimensions include:

```text
WRITE · READ · AGGREGATE · CACHE · RESTART · FAILURE · RECOVERY
ADMIN · METRIC · TENANT_ISOLATION · SCALE · PRIVACY · COST
```

But the framework deliberately avoids checklist theater:

- `LOW` + genuinely local change → short System-Lens impact summary;
- `MEDIUM/HIGH` → record relevant dimensions explicitly;
- money/privacy/identity/tenant/durability/recovery/destructive/production-sensitive work → explicit affected dimensions regardless of nominal task size.

Possible states:

```text
UNAFFECTED | VERIFIED | CHANGED_AND_TESTED | OPEN_RISK | NOT_APPLICABLE
```

Project-level truth lives in `.agentic/SYSTEM_TRUTH_MAP.yaml`, created from [the template](templates/SYSTEM_TRUTH_MAP.example.yaml) and governed by [the schema](schemas/SYSTEM_TRUTH_MAP.md).

A cache, metric or projection does not become authoritative business truth because it is convenient to read.

## Primary tasks stay primary

```text
PRIMARY_TASK = durable objective
SIDE_TASK    = bounded supporting work
INTERRUPT    = urgent bounded preemption
```

```text
RECENCY IS NOT PRIORITY.
CONVERSATIONAL MOMENTUM CANNOT PROMOTE A SIDE TASK.
```

A side task keeps its primary reference, bounded success condition, scope/round budget and return condition. Promotion requires explicit Manager/Operator decision.

If side work starts consuming the project, raise `SIDE_TASK DRIFT` instead of silently optimizing it forever.

## Swamp Guard

The agent continuously watches for compounding complexity:

```text
CLEAR | WATCH | ALERT | STOP_REBASELINE
```

Signals include repeated architecture churn/remediation, unjustified frameworks/datastores/abstractions, competing mechanisms, eval-free AI/RAG tuning, feature growth before vertical slice, ambiguous source-of-truth, prototype-to-production drift, unresolved System-Lens risks and side-task attention drift.

Hard case:

```text
SWAMP ALERT: STOP_REBASELINE
→ stop stacking local patches
→ preserve evidence/current state
→ return to architecture discovery
→ simplify / measure / decide
→ resume from a coherent baseline
```

Agentic Flow applies the same rule to itself: once governance surface grows, prefer **simplify + validate + use + measure** over adding more concepts.

## The normal task model

```text
Operator intent
→ Designer: task contract + advisory
→ Manager: review / bounded authority
→ Executor: implement + real-enough tests
→ Local Lens + System Lens
→ cold/adversarial review for MEDIUM/HIGH
→ Manager: one consolidated finding set
→ one bounded remediation round by default
→ Independent Judge for HIGH-risk closure when required (read-only)
→ Operator: production / business authority
```

| Risk | Default flow |
|---|---|
| LOW | implement → focused test → compact diff review → compact system-impact summary |
| MEDIUM | short preflight → implement → Dual-Lens → cold review → one remediation → Manager |
| HIGH | frozen contract → failure/System-Lens preflight → bounded execution → adversarial review → Manager/remediation → read-only independent closure |

A second remediation round requires a **new material finding** and stays inside the configured boundary.

## Independent review is not model voting

```text
MULTI-MODEL AGREEMENT
!=
INDEPENDENT BEHAVIORAL EVIDENCE
```

Different models can share the same assumption, bad oracle or incomplete context. Strong closure separates as much as risk requires:

```text
IMPLEMENTATION
CONTEXT
AUTHORITY
EVIDENCE
```

The Independent Judge is read-only by default and cannot mutate production.

## Real evidence, not “looks green”

```text
prototype works       != product architecture validated
local function works  != whole-system truth preserved
cache has a number    != authoritative business truth
unit test passes      != real integration
HTTP 200              != persistence
CI green              != deployed behavior
backup enabled        != recoverability
reviewer says PASS    != behavioral evidence
three models say PASS != three independent engineers
```

Load-bearing tests should use mutation/path proof when practical: deliberately break the target behavior in an isolated copy and prove the test goes red. Never destroy unknown operator work to perform mutation testing.

## Cross-system audit without calendar theater

Task-local correctness is not enough forever. Cross-system audit trigger priority is:

```text
EVENT
> RISK / AUTHORITY CHANGE
> TASK-COUNT REMINDER
```

Real-customer release, material incident, or material security/data/authority/recovery change can trigger an audit immediately. `5–8 material tasks` is only a fallback reminder, not a law.

## Production mode

Every production mutation requires **rollback or explicit forward-recovery readiness before execution**.

Minimum production-change contract:

```text
exact target + artifact/config/change identity
success/health signals
abort condition
rollback OR forward-recovery steps
state/data constraints
recovery owner/authority
post-change verification
```

```text
NO ROLLBACK / RECOVERY PLAN
→ NOT EXECUTION-READY FOR PRODUCTION MUTATION
```

Irreversible changes require forward recovery, backup/checkpoint, blast-radius controls and STOP conditions. Reviewer/Judge PASS never grants production authority.

## Fast adoption

1. Clone/pin the framework beside the target project or use the portable bundle.
2. Read [Getting Started](docs/GETTING_STARTED.md).
3. Operator: read the [Operator Runbook](docs/operator/OPERATOR_GUIDE.en.md) or [راهنمای اپراتور فارسی](docs/operator/OPERATOR_GUIDE.fa.md).
4. Choose project mode + `VIBE_FAST | PRODUCT_STANDARD | HIGH_ASSURANCE`.
5. Give the Executor [START_HERE](docs/agent/START_HERE.md).
6. If greenfield/untrusted architecture, run [Project Inception](docs/agent/PROJECT_INCEPTION_ARCHITECTURE.md).
7. For stateful/cost/privacy/tenant-sensitive product work, create `.agentic/SYSTEM_TRUTH_MAP.yaml` from [the template](templates/SYSTEM_TRUTH_MAP.example.yaml).
8. Keep one durable `PRIMARY_TASK` and bound side work.
9. Start with `STRICT_PREVIEW` unless the profile intentionally grants more autonomy.
10. Require evidence appropriate to the claim and separate production authority.

## Key rules

- **Human transports authority; repository transports engineering state.**
- **VIBE_PROTOTYPE != PRODUCTION BASELINE.**
- **Freeze hard-to-change invariants, not easy experiment variables.**
- **Recency is not priority.**
- **Local correctness does not prove System truth.**
- **LOW work should stay light; sensitive/high-risk work earns stronger ceremony.**
- **Unknown/unowned dirty work is protected.**
- **Task authority ≠ mutation authority ≠ environment authority ≠ external-effect authority ≠ production authority.**
- **Claims may not be broader than receipts.**
- **One remediation round by default; second only for a new material finding.**
- **Production mutation requires rollback or forward-recovery readiness.**

## Read only what you need

Human newcomer:

```text
README.md
→ docs/GETTING_STARTED.md
→ docs/operator/OPERATOR_GUIDE.*.md
```

Executor:

```text
docs/agent/START_HERE.md
→ current profile / primary task
→ only triggered schemas, verification, production profiles and skills
```

Greenfield/architecture work:

```text
docs/agent/PROJECT_INCEPTION_ARCHITECTURE.md
```

Material task execution:

```text
docs/agent/TASK_WORKFLOW_DRAFT_REVIEW_APPLY_VERIFY.md
```

Current limitations and what is actually proven:

```text
docs/VALIDATION_STATUS.md
```

Canonical policy:

```text
ARCHITECTURE.md
```
