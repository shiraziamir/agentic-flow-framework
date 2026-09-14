# Operator Guide — Agentic Flow

**Operator control-plane runbook. Coding agents should not preload this file unless an operator task requires it.**  
**Framework version:** 1.11  
**Updated:** 2026-09-14

This is the single operator-facing explanation of how Agentic Flow is meant to run. Canonical authority remains `ARCHITECTURE.md` and the schemas; this guide explains the operating model, role choreography, guardrails and where the human still decides.

## 1. Control model in one screen

```text
PRODUCT OWNER / OPERATOR
WHY / WHAT / priority / business trade-offs / accepted risk / production authority
        │
        ├── greenfield / architecture uncertain ──► PROJECT ARCHITECT (read-only)
        │                                             │
        │                          product constraints + eval + System Truth Map
        │                                             │
        ▼                                             ▼
DESIGNER / TASK ARCHITECT ──► MANAGER / REVIEWER ──► EXECUTOR
read-only task design          freeze + authority       bounded implementation
                                                        │
                                                        ▼
                                              LOCAL + SYSTEM LENS
                                                        │
                                                        ▼
                                             COLD / ADVERSARIAL REVIEW
                                                        │
                                                        ▼
                                             MANAGER CONSOLIDATED REVIEW
                                                        │
                                               one bounded remediation
                                                        │
                                                        ▼
                                          INDEPENDENT JUDGE (read-only)
                                          when risk/policy requires it
                                                        │
                                                        ▼
                                                OPERATOR decision
                                          merge / production / business risk
```

```text
Human transports authority and priority.
Repository transports engineering state.
```

## 2. Start from a preset, not a wall of configuration

Choose a project phase and an operating preset separately.

```text
Project phase:
VIBE_PROTOTYPE | PRODUCT_BUILD | MAINTENANCE

Operating preset:
VIBE_FAST | PRODUCT_STANDARD | HIGH_ASSURANCE
```

Recommended defaults:

| Preset | When to use | Default posture |
|---|---|---|
| `VIBE_FAST` | disposable experiment, feasibility, UX learning | compact controls, sacrificial code allowed, no production claims |
| `PRODUCT_STANDARD` | normal maintainable product | risk-adaptive Dual-Lens, real-enough verification, bounded review/remediation |
| `HIGH_ASSURANCE` | money, identity, privacy, tenant isolation, critical durability, destructive/regulated/high-consequence work | stronger evidence and independent closure where justified |

Do not manually configure every possible control. Start from a preset and override only true project differences in `.agentic/PROJECT_PROFILE.yaml`.

## 3. Vibe mode is supported—but fenced

```text
VIBE_PROTOTYPE != PRODUCTION BASELINE
```

Vibe mode optimizes learning speed. Architecture may be provisional and code may be sacrificial. It does **not** grant sensitive-data authority, production-readiness claims or production mutation.

Promotion to `PRODUCT_BUILD` requires re-baselining and explicit classification of prototype code:

```text
REUSE_AS_IS | REUSE_AFTER_REVIEW | REWRITE | DISCARD
```

## 4. Greenfield projects: idea does not go straight to code

```text
PRODUCT INTENT
→ PRODUCT BRIEF
→ QUALITY / EVAL CONTRACT
→ ARCHITECTURE DISCOVERY
→ SYSTEM TRUTH / DATA AUTHORITY MAP
→ CURRENT SCALE BOUNDARY
→ MINIMAL OPTIONS when useful
→ WALKING SKELETON
→ ARCHITECTURE CHECKPOINT
→ PRODUCT BASELINE
```

The Product Owner supplies outcomes and trade-offs: who uses it, what success/failure means, privacy, freshness, cost/latency tolerance, acceptable risk and business priority. The Project Architect proposes the smallest viable system shape.

For AI/RAG/search: no serious tuning before a representative eval baseline exists.

Use:

```text
docs/agent/PROJECT_INCEPTION_ARCHITECTURE.md
prompts/operator/PROJECT_ARCHITECT.md
schemas/SYSTEM_TRUTH_MAP.md
templates/SYSTEM_TRUTH_MAP.example.yaml
```

## 5. Roles and authority

| Role | Primary responsibility | Default mutation | Production mutation |
|---|---|---:|---:|
| Operator / Product Owner | outcome, priority, trade-offs, risk, production authority | human authority | explicit human decision |
| Project Architect | constraints, eval, System Truth Map, architecture options | read-only | denied |
| Designer / Task Architect | task contract and advisory | read-only | denied |
| Manager / Reviewer | freeze task, review exact diff/evidence, bounded authority | read/review | denied by default |
| Executor | implementation inside approved boundaries | bounded write | separate owner authority only |
| Cold / Adversarial Reviewer | challenge obvious defects/assumptions before Manager | read-only | denied |
| Independent Judge | HIGH-risk/policy-required closure | read-only | denied |

A second model is not automatically independent. Strong review separates as much as risk requires:

```text
IMPLEMENTATION
CONTEXT
AUTHORITY
EVIDENCE
```

```text
MULTI-MODEL AGREEMENT != INDEPENDENT BEHAVIORAL EVIDENCE
```

## 6. Task focus: the current conversation is not the project priority

```text
PRIMARY_TASK = durable objective
SIDE_TASK    = bounded supporting work
INTERRUPT    = urgent bounded preemption
```

```text
RECENCY IS NOT PRIORITY.
CONVERSATIONAL MOMENTUM CANNOT PROMOTE A SIDE TASK.
```

A side task must keep the primary-task reference, bounded success condition, scope/round budget and return condition. After completion, return to Primary by default.

Promotion requires explicit Manager/Operator decision. If side work keeps expanding, the agent must raise `SIDE_TASK DRIFT` and recommend `CLOSE | DEFER | PROMOTE_PROPOSAL`.

An interrupt checkpoints the primary task and exact resume state before urgent work begins.

## 7. Dual-Lens engineering without checklist theater

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

Possible states:

```text
UNAFFECTED | VERIFIED | CHANGED_AND_TESTED | OPEN_RISK | NOT_APPLICABLE
```

Risk-adaptive rule:

- LOW + genuinely local → compact system-impact summary; do not fill all 13 rows mechanically.
- MEDIUM/HIGH → explicitly record relevant dimensions.
- any risk level touching money, privacy, identity, tenant isolation, durability/recovery, destructive state or production semantics → explicit affected dimensions.

`UNAFFECTED` is a reviewed conclusion. `OPEN_RISK` remains visible. A cache/projection/metric does not silently become authoritative business truth.

## 8. System Truth Map

For PRODUCT_BUILD and stateful/cost/privacy/tenant-sensitive systems, maintain:

```text
.agentic/SYSTEM_TRUTH_MAP.yaml
```

It should expose only load-bearing truth:

```text
entry points / trust boundaries
DBs / caches / queues / providers / workers
admin + observability + deployment/recovery surfaces
authoritative data and derived copies
writers/readers
freshness/size/privacy bounds
restart/failure/recovery behavior
tenant isolation
current scale target / ceiling / safety limit / scale trigger
```

This map is a model, not proof. Runtime claims still need receipts.

## 9. Threat/failure mini-review

At project inception or when a load-bearing boundary changes, ask briefly:

```text
What can leak?
What can be counted twice?
What can be silently lost?
What survives restart?
What becomes stale?
What can grow without a bound?
What happens under concurrency?
What happens when a dependency lies or partially fails?
What can one tenant do to another?
What can cause unexpected provider spend?
What can an administrator safely do later?
```

Record only material risks/decisions. Do not create an unbounded security document.

## 10. Task lifecycle by risk

```text
LOW
execute → focused test → compact diff review → compact system-impact summary

MEDIUM
short preflight → execute → Dual-Lens → cold review
→ one remediation → Manager review

HIGH
frozen contract → failure/System-Lens preflight → explicit authority
→ bounded execution → adversarial review → Manager findings
→ one remediation by default → read-only Independent Judge
→ Operator production/business decision
```

A second remediation round requires a new material finding and stays within the configured boundary.

## 11. Testing and evidence

For material business behavior, test scenarios rather than only helper return values. Depending on the feature, include success, fallback, retry, external side-effect then failure, source-of-truth unavailable, restart/rebuild, time boundary, admin recovery, cross-tenant attempt and concurrency/duplicate-work behavior.

For load-bearing tests, use mutation/path proof when practical. Deliberately break the target behavior in an isolated copy and prove the test goes red.

Never use destructive Git reset/restore/clean against unknown operator work to perform mutation testing.

```text
unit PASS          != user flow proven
HTTP 200           != persistence
CI green           != deployed artifact
backup configured  != restore proven
reviewer PASS      != runtime evidence
```

## 12. Swamp Guard

```text
CLEAR | WATCH | ALERT | STOP_REBASELINE
```

Typical signals: repeated architecture churn/remediation, unjustified tools/abstractions, competing mechanisms, AI/RAG tuning without evals, feature growth before vertical slice, chat-only architecture decisions, source-of-truth ambiguity, prototype-to-production drift, side-task attention drift, unresolved System-Lens risks and complexity growing faster than demonstrated value.

Severe case:

```text
STOP_REBASELINE
→ preserve state/evidence
→ return to architecture discovery
→ simplify / measure / decide
→ continue from coherent baseline
```

The framework itself uses this rule: once controls become numerous, simplify and validate before adding more concepts.

## 13. Cross-system audit

Audit trigger priority:

```text
EVENT
> RISK / AUTHORITY CHANGE
> TASK-COUNT REMINDER
```

Immediate triggers can include real-customer release, material incident, or material security/data/authority/recovery change. The `5–8 material tasks` cadence is only a fallback reminder.

Audit themes include financial truth, privacy, identity/authorization, tenant isolation, restart survival, backup/restore, observability truth, capacity bounds, provider failure/spend and admin recovery.

## 14. Production control

Production mutation is a separate authority boundary. Before **every** production mutation require:

```text
exact target environment
exact artifact/config/change identity
expected health/success signal
abort condition
rollback OR forward-recovery path
state/data constraints
recovery owner/authority
post-change verification
```

```text
NO ROLLBACK / RECOVERY PLAN
→ NOT EXECUTION-READY FOR PRODUCTION MUTATION
```

If rollback is unsafe/impossible, require forward recovery, backup/checkpoint, blast-radius controls and STOP conditions. Judge/Manager PASS does not grant production authority.

## 15. Human should not be the message bus

The repository should durably carry project mode/preset, System Truth Map, primary/active task, exact refs, findings, remediation state, receipts/gaps, Swamp state and next authority decision.

The human should mostly transport real authority:

```text
approve / reject
change priority
accept risk
choose business trade-off
authorize production
```

A fresh session should be able to continue from repository state without replaying the previous chat.

## 16. Operator daily checklist

Before material work:

```text
1. What is the PRIMARY_TASK?
2. What preset/mode are active?
3. Is architecture/System Truth baseline adequate?
4. What is the task risk and allowed mutation surface?
5. What evidence/environment will prove success?
6. What sensitive System-Lens dimensions are plausibly affected?
7. What requires explicit external/production authority?
```

At closure:

```text
What changed?
What proves it?
What remains unproven?
What system truth changed?
What new/open risk exists?
What provider/environment mutation occurred?
How do we stop/recover?
What is the next authorized action?
```

## 17. Where to go deeper

```text
Canonical policy          ARCHITECTURE.md
Project profile/presets   schemas/PROJECT_PROFILE_CONFIG.md
Project inception         docs/agent/PROJECT_INCEPTION_ARCHITECTURE.md
System Truth              schemas/SYSTEM_TRUTH_MAP.md
Task workflow             docs/agent/TASK_WORKFLOW_DRAFT_REVIEW_APPLY_VERIFY.md
Mutation authority        schemas/MUTATION_APPROVAL_POLICY.md
Role setup                docs/operator/DESIGNER_MANAGER_SETUP.md
Independent Judge         prompts/operator/INDEPENDENT_JUDGE.md
Production rollback       production/DELIVERY.md
Validation limits         docs/VALIDATION_STATUS.md
```

The objective is not maximum process. It is **the minimum process that keeps product intent, system truth, evidence and authority coherent at the current risk level**.
