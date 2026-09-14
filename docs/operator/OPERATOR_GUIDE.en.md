# Operator Guide — Agentic Flow

**Operator control-plane runbook. Coding agents should not preload this file unless the operator task requires it.**  
**Framework version:** 1.10  
**Updated:** 2026-09-14

This is the single operator-facing explanation of how Agentic Flow is meant to be run. Canonical authority remains `ARCHITECTURE.md` and the schemas; this guide explains the operating model, role choreography, guardrails, escalation paths and what the human still owns.

## 1. Control model in one screen

```text
PRODUCT OWNER / OPERATOR
WHY / WHAT / priority / business trade-offs / accepted risk / production authority
        │
        ├── greenfield or uncertain architecture ──► PROJECT ARCHITECT (read-only)
        │                                             │
        │                                             ▼
        │                             architecture + System Truth Map + eval contract
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
                                              bounded remediation
                                                        │
                                                        ▼
                                          INDEPENDENT JUDGE (read-only)
                                          when HIGH-risk/policy requires
                                                        │
                                                        ▼
                                                OPERATOR decision
                                          merge / production / business risk
```

The human transports **authority and priority**. The repository transports **engineering state**.

## 2. The roles

| Role | Primary job | Default mutation authority | Production mutation |
|---|---|---:|---:|
| Operator / Product Owner | outcome, priority, trade-offs, risk, production authority | human authority | explicit human decision |
| Project Architect | convert product intent into constraints, evals, System Truth Map and architecture options | read-only | denied |
| Designer / Task Architect | turn a bounded objective into a frozen task contract | read-only | denied |
| Manager / Reviewer | freeze task, control bounded authority, inspect exact diff/receipts and system effects | normally read/review | denied by default |
| Executor | implement HOW inside frozen boundaries | bounded write | separately owner-authorized only |
| Cold / Adversarial Reviewer | falsify assumptions and obvious defects before Manager attention | read-only | denied |
| Independent Judge | independent closure for HIGH-risk/policy-required work | read-only | denied |

A different model name is not enough to create independence. Independent closure should separate implementation, context, authority and evidence. Model/provider diversity is useful defense-in-depth, not a stronger receipt class.

```text
MULTI-MODEL AGREEMENT != INDEPENDENT BEHAVIORAL EVIDENCE
```

## 3. Development modes

### VIBE_PROTOTYPE

Enable explicitly:

```yaml
project_mode:
  mode: VIBE_PROTOTYPE
```

Use it when the main question is whether an idea or interaction is worth pursuing. It optimizes learning speed. Architecture may be provisional and code may be sacrificial.

```text
VIBE_PROTOTYPE != PRODUCTION BASELINE
```

Production-readiness claims remain denied. Sensitive/production data and production mutation remain separately controlled. Promotion to `PRODUCT_BUILD` requires re-baselining, an architecture checkpoint and classification of prototype code as `REUSE_AS_IS | REUSE_AFTER_REVIEW | REWRITE | DISCARD`.

### PRODUCT_BUILD

Use when building the product baseline. Product constraints, quality/eval contract, System Truth Map and load-bearing architecture should be explicit before broad feature growth.

### MAINTENANCE

Use the established baseline and normal task flow. Return to architecture discovery when a material boundary changes or the Swamp Guard reports structural drift.

## 4. Greenfield / product inception

Do not route an idea directly to an Executor.

```text
PRODUCT INTENT
→ PRODUCT BRIEF
→ QUALITY / EVAL CONTRACT
→ ARCHITECTURE DISCOVERY
→ SYSTEM TRUTH / DATA AUTHORITY MAP
→ CURRENT SCALE BOUNDARY
→ 2–3 MINIMAL OPTIONS when meaningful
→ LOAD-BEARING DECISIONS
→ WALKING SKELETON
→ ARCHITECTURE CHECKPOINT
→ PRODUCT BASELINE
→ NORMAL TASK FLOW
```

The operator should answer product questions, not pretend to be a software architect. Examples: user, job-to-be-done, unacceptable behavior, privacy, freshness, latency, cost tolerance, citation/trust expectations and business trade-offs.

The Project Architect owns system-shape discovery and must not prematurely code. Freeze hard-to-change invariants; keep cheap implementation choices open until evidence justifies them.

For AI/RAG: do not seriously tune chunking, embeddings, top-k, reranking, prompts or vector vendors before a representative eval baseline exists.

Canonical guide: `docs/agent/PROJECT_INCEPTION_ARCHITECTURE.md`  
System/data map: `schemas/SYSTEM_TRUTH_MAP.md`  
Prompt: `prompts/operator/PROJECT_ARCHITECT.md`

## 5. Dual-Lens operating model

Every material change is reviewed through two lenses:

```text
LOCAL LENS
Is the changed behavior itself correct?

SYSTEM LENS
What truth does the whole system claim after this change?
```

### Local Lens

The Executor/Reviewer checks the real call path, business invariant, failure semantics, resource/cleanup behavior, focused and related regression tests, and mutation/path proof for load-bearing tests.

### System Lens

The project keeps a compact `System Truth Map` covering components, trust boundaries, authoritative data, caches/projections, restart/failure/recovery behavior, tenant isolation and current scale boundaries.

For each material task review this matrix:

```text
WRITE
READ
AGGREGATE
CACHE
RESTART
FAILURE
RECOVERY
ADMIN
METRIC
TENANT_ISOLATION
SCALE
PRIVACY
COST
```

Each row is one of:

```text
UNAFFECTED
VERIFIED
CHANGED_AND_TESTED
OPEN_RISK
NOT_APPLICABLE
```

Important rules:

- `UNAFFECTED` is a reviewed conclusion, not a default.
- A cache/projection/summary/metric is not authoritative merely because it is easy to read.
- `OPEN_RISK` remains visible until resolved, accepted, deferred or escalated.
- When a material authority, trust boundary, recovery rule or scale boundary changes, update the System Truth Map.
- A locally green function does not close a system-level claim.

The System Lens should stay short for small/local work; it becomes explicit for MEDIUM/HIGH or stateful/cost/privacy/tenant-sensitive work.

## 6. Periodic cross-system audit

Even correct tasks can gradually change relationships between components. Run a broader System-Lens audit on a project-configured cadence.

Recommended heuristic triggers:

```text
every ~5–8 material tasks (default example: 6)
before a meaningful demo deployment
before every real-customer release
after every material incident
before/after a material data-authority or trust-boundary change
```

Review:

```text
FINANCIAL TRUTH
PRIVACY TRUTH
IDENTITY / AUTHORIZATION
TENANT ISOLATION
RESTART SURVIVAL
BACKUP / RESTORE
OBSERVABILITY TRUTH
CAPACITY BOUNDS
EXTERNAL-PROVIDER FAILURE / SPEND
ADMIN RECOVERY
```

This is not another full code review. Its job is to detect relationship drift that task-local review can miss.

## 7. Task hierarchy: protect the real objective

At any moment a workstream has one durable primary objective.

```text
PRIMARY_TASK = current durable objective
SIDE_TASK    = bounded supporting work
INTERRUPT    = urgent bounded preemption
```

Core rule:

```text
RECENCY IS NOT PRIORITY.
CONVERSATIONAL MOMENTUM CANNOT PROMOTE A SIDE TASK.
```

A `SIDE_TASK` must keep `primary_task_ref`, a bounded success condition, scope/budget, return condition and promotion authority. When it finishes, record the result and return to the primary task.

A side task may become primary only through explicit Manager/Operator promotion. A long discussion, recent failure or repeated prompt is not promotion.

If a side task consumes excessive rounds, starts inventing unrelated architecture or becomes the de-facto optimization target, the agent must raise:

```text
SIDE_TASK DRIFT
Recommended action: CLOSE | DEFER | PROMOTE_PROPOSAL
```

For an `INTERRUPT`, checkpoint the primary task and exact resume state first. After the urgent work, resume or explicitly re-prioritize.

## 8. Normal task lifecycle

Risk and work kind are separate:

```text
risk.level = LOW | MEDIUM | HIGH
work_kind  = IMPLEMENTATION | REMEDIATION | EVIDENCE_ONLY
```

Default flow:

```text
LOW
execute → focused test → compact self-review → report

MEDIUM
short preflight → execute → Dual-Lens check → cold review → one bounded remediation → Manager review

HIGH
frozen contract
→ failure/System-Lens preflight
→ explicit apply authority
→ bounded execution
→ adversarial review
→ Manager consolidated findings
→ one remediation round by default
→ read-only Independent Judge when required
→ Operator production/business decision
```

A second remediation iteration is exceptional and requires a new material finding. Repeated remediation is also a Swamp Guard signal.

## 9. Authority is split deliberately

Never collapse these into one vague “go ahead”:

```text
TASK AUTHORITY
MUTATION AUTHORITY
ENVIRONMENT AUTHORITY
EXTERNAL-SIDE-EFFECT AUTHORITY
PRODUCTION AUTHORITY
```

Examples:

- task approved != source mutation approved under `STRICT_PREVIEW`;
- test execution approved != paid provider API call approved;
- staging read approved != production mutation approved;
- Judge PASS != production deployment authority.

First-adoption default is `STRICT_PREVIEW`. Group related edits into coherent mutation batches; do not create permission spam per line/file.

## 10. Swamp Guard — continuous anti-bog control

The Swamp Guard runs at material checkpoints and before architecture/tooling expansion:

```text
CLEAR | WATCH | ALERT | STOP_REBASELINE
```

Watch for:

- repeated redesign/remediation in the same subsystem;
- frameworks, datastores or abstractions without a product/failure constraint;
- multiple mechanisms owning the same responsibility;
- AI/RAG tuning without evals;
- broad feature growth before a working end-to-end slice;
- architecture decisions only in chat;
- ambiguous source-of-truth/state ownership;
- permanent “temporary” workarounds;
- prototype code quietly acquiring production expectations;
- complexity growing faster than demonstrated value;
- `SIDE_TASK` attention replacing the `PRIMARY_TASK`;
- repeated System-Lens `OPEN_RISK`s or business authority drifting into a cache/projection.

Required alert shape:

```text
SWAMP ALERT: <WATCH|ALERT|STOP_REBASELINE>
Signal: ...
Evidence: ...
Why it matters: ...
Recommended action: ...
Continue allowed: YES|NO
Authority needed: <none|Manager|Operator>
```

`STOP_REBASELINE` means stop compounding patches, preserve evidence/current state, return to architecture discovery, simplify/measure/decide, then resume from a coherent baseline.

## 11. Review choreography

The Executor does not close its own material work.

For MEDIUM/HIGH, use a cold/adversarial review before Manager attention when configured. The Manager should review in this order:

```text
frozen contract
→ System Truth Map / engineering advisory
→ exact base/head / diff
→ surrounding source
→ raw tests / CI / receipts
→ Dual-Lens matrix / OPEN_RISKs
→ Executor narrative last
```

Manager returns one consolidated finding set where practical. Same-task fixes use one controlled remediation window by default.

For HIGH-risk closure, the Independent Judge is read-only and separately checks claims against exact source/diff and receipts. It cannot edit code, weaken the task, call providers or mutate production.

## 12. Evidence rules

A claim may be no broader than the receipt that directly establishes it.

```text
unit PASS          != integration proven
mock PASS          != real boundary proven
HTTP 200           != persistence proven
CI green           != deployed behavior proven
backup configured  != restore proven
reviewer PASS      != runtime evidence
three models PASS  != three independent engineers
```

Use the lowest authorized environment that can exercise the real changed path. If that environment does not exist, report `UNVERIFIED`/`BLOCKED`; do not weaken the claim.

## 13. Repository-driven handoff

The operator should not become a message bus between sessions/models.

Durable state should let a fresh session recover:

```text
project mode / architecture baseline
System Truth Map ref/version
PRIMARY_TASK
active SIDE_TASK / INTERRUPT if any
suspended/resume state
exact repository base/head
frozen task contract
review findings
remediation window
receipts / gaps
System-Lens OPEN_RISKs
cross-system audit state
Swamp Guard state
closure state
next authority decision
```

Checkpoint durable state before clearing/replacing a session. Session recency must never replace project priority.

## 14. Production control

Every production mutation requires, before execution:

```text
exact target and change identity
success / health signals
abort condition
rollback OR explicit forward-recovery path
stateful/data rollback constraints
recovery authority/owner
post-change verification
```

```text
NO ROLLBACK / RECOVERY PLAN
→ NOT EXECUTION-READY FOR PRODUCTION MUTATION
```

If rollback is unsafe/impossible, require forward recovery, backup/checkpoint, blast-radius controls and explicit STOP conditions. The Independent Judge remains read-only.

## 15. Workspace safety and external effects

Unknown/unowned dirty work is protected state. Do not use destructive Git restore/reset/clean as a convenience.

Real provider calls, paid APIs, sends/messages, deployments and destructive data operations need their own explicit authority. A test requirement does not imply authority for a real external side effect.

## 16. Model/cost routing

The framework is vendor-neutral. Route by capability and cost, not brand:

```text
Project Architect → stronger reasoning when architecture ambiguity warrants it
Executor          → task-adequate / cost-efficient
Manager           → stronger judgment when warranted
Independent Judge → high reasoning + separate context
```

Cost optimization never lowers acceptance or evidence quality.

## 17. What the operator should inspect regularly

At meaningful checkpoints, confirm:

- current project mode is still correct;
- `PRIMARY_TASK` is explicit and has not been displaced by side work;
- side tasks are bounded and return conditions are respected;
- Swamp Guard state is reviewed, not ignored;
- System Truth Map still matches load-bearing implementation;
- System-Lens `OPEN_RISK`s are resolved/owned rather than accumulating silently;
- cross-system audit is not overdue;
- architecture/eval baseline still matches product reality;
- exact reviewed HEAD still matches the candidate;
- required receipts are current and claim-strength is honest;
- expired temporary overrides are removed;
- restore/recovery evidence is fresh enough;
- production authority has not leaked into reviewer/judge roles;
- governance friction is not producing repeated pointless round-trips.

## 18. Operator quick-start

```text
1. Read README.md.
2. Create/confirm .agentic/PROJECT_PROFILE.yaml.
3. Choose VIBE_PROTOTYPE | PRODUCT_BUILD | MAINTENANCE.
4. If greenfield/untrusted architecture: run Project Architect / Project Inception.
5. Build/confirm System Truth Map + current scale boundary.
6. Record one PRIMARY_TASK.
7. Use Designer for material task contract + Dual-Lens preflight.
8. Manager freezes contract and grants bounded authority.
9. Executor implements/tests.
10. Local Lens + System Lens → Cold review → Manager findings → one remediation round.
11. Independent Judge for HIGH-risk when required.
12. Run periodic cross-system audit when due.
13. Operator decides production/business risk.
14. Repository carries state to the next session.
```

## 19. Canonical references

- `ARCHITECTURE.md` — canonical invariants.
- `schemas/PROJECT_PROFILE_CONFIG.md` — project mode, Dual-Lens, Swamp Guard, task-focus and authority defaults.
- `schemas/SYSTEM_TRUTH_MAP.md` — component map, data authority, recovery and scale boundaries.
- `schemas/TASK_CONTRACT.md` — primary/side/interrupt, Local/System Lens, scope, claims and authority.
- `docs/agent/PROJECT_INCEPTION_ARCHITECTURE.md` — greenfield/vibe/product inception.
- `docs/agent/TASK_WORKFLOW_DRAFT_REVIEW_APPLY_VERIFY.md` — task lifecycle.
- `schemas/MUTATION_APPROVAL_POLICY.md` — apply/remediation authority.
- `docs/operator/DESIGNER_MANAGER_SETUP.md` — role setup and repository permissions.
- `prompts/operator/PROJECT_ARCHITECT.md` — Project Architect prompt.
- `prompts/operator/TASK_DESIGNER.md` — Designer prompt.
- `prompts/operator/MANAGER_REVIEWER.md` — Manager prompt.
- `prompts/operator/INDEPENDENT_JUDGE.md` — read-only Judge prompt.
- `production/DELIVERY.md` — production rollback/recovery policy.

Operator documents explain how to use the system; they do not override canonical policy.