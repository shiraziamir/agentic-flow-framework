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
        │                                  architecture options + eval contract
        │                                             │
        ▼                                             ▼
DESIGNER / TASK ARCHITECT ──► MANAGER / REVIEWER ──► EXECUTOR
read-only task design          freeze + authority       bounded implementation
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
| Project Architect | convert product intent into constraints, evals and architecture options | read-only | denied |
| Designer / Task Architect | turn a bounded objective into a frozen task contract | read-only | denied |
| Manager / Reviewer | freeze task, control bounded authority, inspect exact diff/receipts | normally read/review | denied by default |
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

Use when building the product baseline. Product constraints, quality/eval contract and load-bearing architecture should be explicit before broad feature growth.

### MAINTENANCE

Use the established baseline and normal task flow. Return to architecture discovery when a material boundary changes or the Swamp Guard reports structural drift.

## 4. Greenfield / product inception

Do not route an idea directly to an Executor.

```text
PRODUCT INTENT
→ PRODUCT BRIEF
→ QUALITY / EVAL CONTRACT
→ ARCHITECTURE DISCOVERY
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
Prompt: `prompts/operator/PROJECT_ARCHITECT.md`

## 5. Task hierarchy: protect the real objective

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

## 6. Normal task lifecycle

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
short preflight → execute → cold review → one bounded remediation → Manager review

HIGH
frozen contract
→ failure-surface preflight
→ explicit apply authority
→ bounded execution
→ adversarial review
→ Manager consolidated findings
→ one remediation round by default
→ read-only Independent Judge when required
→ Operator production/business decision
```

A second remediation iteration is exceptional and requires a new material finding. Repeated remediation is also a Swamp Guard signal.

## 7. Authority is split deliberately

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

## 8. Swamp Guard — continuous anti-bog control

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
- `SIDE_TASK` attention replacing the `PRIMARY_TASK`.

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

## 9. Review choreography

The Executor does not close its own material work.

For MEDIUM/HIGH, use a cold/adversarial review before Manager attention when configured. The Manager should review in this order:

```text
frozen contract
→ exact base/head / diff
→ surrounding source
→ raw tests / CI / receipts
→ gaps / omitted checks
→ Executor narrative last
```

Manager returns one consolidated finding set where practical. Same-task fixes use one controlled remediation window by default.

For HIGH-risk closure, the Independent Judge is read-only and separately checks claims against exact source/diff and receipts. It cannot edit code, weaken the task, call providers or mutate production.

## 10. Evidence rules

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

## 11. Repository-driven handoff

The operator should not become a message bus between sessions/models.

Durable state should let a fresh session recover:

```text
project mode / architecture baseline
PRIMARY_TASK
active SIDE_TASK / INTERRUPT if any
suspended/resume state
exact repository base/head
frozen task contract
review findings
remediation window
receipts / gaps
Swamp Guard state
closure state
next authority decision
```

Checkpoint durable state before clearing/replacing a session. Session recency must never replace project priority.

## 12. Production control

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

## 13. Workspace safety and external effects

Unknown/unowned dirty work is protected state. Do not use destructive Git restore/reset/clean as a convenience.

Real provider calls, paid APIs, sends/messages, deployments and destructive data operations need their own explicit authority. A test requirement does not imply authority for a real external side effect.

## 14. Model/cost routing

The framework is vendor-neutral. Route by capability and cost, not brand:

```text
Project Architect → stronger reasoning when architecture ambiguity warrants it
Executor          → task-adequate / cost-efficient
Manager           → stronger judgment when warranted
Independent Judge → high reasoning + separate context
```

Cost optimization never lowers acceptance or evidence quality.

## 15. What the operator should inspect regularly

At meaningful checkpoints, confirm:

- current project mode is still correct;
- `PRIMARY_TASK` is explicit and has not been displaced by side work;
- side tasks are bounded and return conditions are respected;
- Swamp Guard state is reviewed, not ignored;
- architecture/eval baseline still matches product reality;
- exact reviewed HEAD still matches the candidate;
- required receipts are current and claim-strength is honest;
- expired temporary overrides are removed;
- restore/recovery evidence is fresh enough;
- production authority has not leaked into reviewer/judge roles;
- governance friction is not producing repeated pointless round-trips.

## 16. Operator quick-start

```text
1. Read README.md.
2. Create/confirm .agentic/PROJECT_PROFILE.yaml.
3. Choose VIBE_PROTOTYPE | PRODUCT_BUILD | MAINTENANCE.
4. If greenfield/untrusted architecture: run Project Architect / Project Inception.
5. Record one PRIMARY_TASK.
6. Use Designer for material task contract.
7. Manager freezes contract and grants bounded authority.
8. Executor implements/tests.
9. Cold review → Manager consolidated findings → one remediation round.
10. Independent Judge for HIGH-risk when required.
11. Operator decides production/business risk.
12. Repository carries state to the next session.
```

## 17. Canonical references

- `ARCHITECTURE.md` — canonical invariants.
- `schemas/PROJECT_PROFILE_CONFIG.md` — project mode, Swamp Guard, task-focus and authority defaults.
- `schemas/TASK_CONTRACT.md` — primary/side/interrupt, scope, claims and authority.
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