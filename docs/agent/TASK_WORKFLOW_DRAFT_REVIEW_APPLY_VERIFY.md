# Task Workflow — Risk-Adaptive Draft → Execute → Verify

**Agent-facing canonical workflow for material tasks.**

## Goal

Keep the quality bar stable while changing ceremony according to risk, while preventing recent side work from silently replacing the real objective and preventing local correctness from silently breaking system truth.

```text
risk up   → stronger boundaries, broader preflight, stronger evidence/review
risk down → fewer gates, smaller reports, faster execution
```

Do not confuse rigor with repeated permission prompts.

## 1. Establish task focus before task mechanics

At every durable checkpoint, identify:

```yaml
primary_task_ref: <task/ref>
active_task_ref: <task/ref>
active_task_role: PRIMARY|SIDE|INTERRUPT
```

There is one durable `PRIMARY_TASK` per workstream.

```text
RECENCY IS NOT PRIORITY.
CONVERSATIONAL MOMENTUM CANNOT PROMOTE A SIDE TASK.
```

Use:

- `PRIMARY` for the current durable objective;
- `SIDE` for bounded supporting work discovered during the primary task;
- `INTERRUPT` for urgent preemption that must temporarily suspend the primary task.

A side task must keep a reference to the primary task, have a bounded success condition, a round/budget limit, and a return condition. After completion, return to the primary task by default.

Promotion is explicit:

```text
SIDE_TASK
→ PROMOTION PROPOSED
→ Manager/Operator decision
→ update durable refs
→ only then become PRIMARY_TASK
```

If a side task exceeds its configured focus-review limit, starts creating unrelated architecture, or becomes the dominant optimization target, raise:

```text
SIDE_TASK DRIFT
Primary: <ref>
Side: <ref>
Why drift is suspected: ...
Rounds/scope consumed: ...
Recommended: CLOSE | DEFER | PROMOTE_PROPOSAL
```

For an `INTERRUPT`, checkpoint the primary task first and record exactly where/how to resume it.

## 2. Classify the work

```yaml
risk_level: LOW|MEDIUM|HIGH
work_kind: IMPLEMENTATION|REMEDIATION|EVIDENCE_ONLY
```

| Risk | Default workflow |
|---|---|
| LOW | execute → focused test → compact self-review → report |
| MEDIUM | short preflight → execute → Dual-Lens check → cold review → one bounded remediation → Manager review |
| HIGH | frozen contract → failure/System-Lens preflight → explicit authorization → execute → adversarial review → Manager consolidated review → one remediation round by default → read-only Independent Judge when required |

If the task exposes that the project architecture baseline itself is missing/broken, do not keep treating it as a local task. Route to `docs/agent/PROJECT_INCEPTION_ARCHITECTURE.md`.

## 3. Draft the observable contract

Define before material mutation:

- task focus and primary-task relationship;
- goal/symptom;
- invariants and failure semantics;
- in-scope / out-of-scope surfaces;
- observable Definition of Done;
- claims and minimum receipts;
- required environment/real boundaries;
- intentionally omitted checks;
- STOP/escalation conditions;
- System Truth Map reference when applicable;
- expected cross-system effects or known `OPEN_RISK`s.

The contract defines **WHAT + SUCCESS**, not an implementation script.

For MEDIUM/HIGH work, the Designer/Executor may include an **advisory algorithm/pseudocode** to expose reasoning before edits. It is guidance, not frozen implementation, unless the task explicitly makes it an invariant.

## 4. Engineering preflight

For MEDIUM/HIGH, inspect the current system before editing:

```text
What owns the affected state?
What is the real call/data path?
Where do failures propagate or disappear?
What is authoritative vs derived?
What is the smallest coherent change?
What real boundary proves it?
```

### Failure-surface matrix

Baseline for material behavior:

```text
NORMAL PATH
BOUNDARY / INVALID INPUT
DEPENDENCY OR I/O FAILURE
CLEANUP / ROLLBACK FAILURE
OBSERVABILITY / HEALTH PROPAGATION
TEST-ORACLE FALSIFICATION
```

Add when applicable:

```text
THREAD CONCURRENCY
PROCESS CONCURRENCY
CRASH / RESTART
DURABILITY / PARTIAL WRITE
PERMISSION / IDENTITY
EXTERNAL PROVIDER
MIGRATION / SCHEMA
CACHE / CONSISTENCY
```

Under `STRICT_PREVIEW`, include the preflight in the first change preview and wait for `APPROVE/APPLY`.

## 5. Dual-Lens preflight

Material changes are viewed through two lenses:

```text
LOCAL LENS
Is the changed behavior itself correct?

SYSTEM LENS
What truth does the whole system claim after this change?
```

### Local Lens

Before/while implementing, identify:

```text
actual call path
business invariant
failure semantics
resource ownership / cleanup
focused acceptance tests
related regressions
mutation-sensitive / path-proof test seams
```

### System Lens

Use the current `schemas/SYSTEM_TRUTH_MAP.md` artifact and review this fixed matrix:

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

Each row gets exactly one state:

```text
UNAFFECTED
VERIFIED
CHANGED_AND_TESTED
OPEN_RISK
NOT_APPLICABLE
```

Rules:

- `UNAFFECTED` is a reviewed conclusion, not a default placeholder.
- `OPEN_RISK` is preserved as a finding/gap and cannot be silently converted to `UNAFFECTED`.
- If a material data authority, trust boundary, recovery rule or scale boundary changes, update the System Truth Map or raise STOP/re-baseline as appropriate.
- Caches/projections/summaries/metrics cannot silently become authoritative business truth.

For LOW/local-only tasks, the System Lens may be a short explicit check. For MEDIUM/HIGH it is recorded in the task receipt/review.

## 6. Execute in an adequate environment

Use the lowest authorized environment that can directly exercise the changed behavior. Mock-only evidence closes only unit/model claims; it cannot silently inherit persistence, migration, integration, user-flow, deployment or production semantics.

During execution:

- run focused checks early;
- preserve project conventions unless intentionally changed;
- do not weaken tests to make output green;
- do not silently broaden scope;
- do not optimize a side task beyond its declared role/budget;
- protect dirty/uncommitted work;
- do not make real provider/external calls without authority.

## 7. Behavioral scenarios before shallow function tests

For material business behavior, prefer scenario tests that trace actual business truth rather than only checking a helper return value.

Examples of scenario dimensions when applicable:

```text
normal success
fallback/escalation
provider retry / partial charge
operation fails after an external side effect
source-of-truth unavailable
cache restart / projection rebuild
month/time boundary
admin recovery
cross-tenant access attempt
concurrency / duplicate work
```

The exact scenarios are project-specific. Do not create irrelevant cases merely to fill a template.

## 8. Mutation-sensitive proof

For load-bearing tests, a green test is not enough. Demonstrate that the test can catch the target defect through controlled mutation/path proof when practical.

Examples:

```text
remove tenant dimension from cache key
turn authority-read failure into zero/empty success
double-count an aggregate row
remove a lock / cleanup / readiness condition
skip projection rebuild after restart
```

Mutation happens only in an isolated temporary working copy or equivalent safe mechanism. Do not use destructive Git restore/reset/clean commands to recover the operator's work. Preserve/restore exact bytes and verify restoration when doing manual mutation proof.

## 9. Focused + related + final suite

Use risk/size appropriate checks:

```text
focused tests early
mutation-sensitive/path-proof tests when load-bearing
related regression tests
one final broader/full-suite run when the project has a meaningful bounded suite
static review of the complete diff
```

Do not rerun an enormous suite mechanically after every tiny edit; do run the required final qualification before closure when the contract requires it.

## 10. Pre-Manager adversarial review

For MEDIUM/HIGH, prefer a cold/read-only review before spending Manager attention. Inspect actual diff and surrounding source for false assumptions, duplicate state authorities, swallowed errors, cleanup leaks, concurrency/crash gaps, weak test oracles, missing health propagation, unsafe workspace actions, unauthorized external effects, scope drift, task-focus drift and System-Lens gaps.

Minimum review surfaces for material source changes include logic, error paths, concurrency/partial operations, resource management, logs/metrics, tenant boundaries, compatibility, unnecessary complexity, naming/structure and the cross-system effect matrix.

## 11. Manager consolidated review

Manager reviews the exact commit/PR head, not only the Executor summary. Prefer one consolidated finding set:

```text
R1 ...
R2 ...
R3 ...
```

If findings are bounded/same-task, authorize a controlled remediation window per `schemas/MUTATION_APPROVAL_POLICY.md`.

Manager must also confirm that:

- the active task role still matches project priority;
- the Local Lens is supported by actual tests/diff review;
- the System Lens matrix is honest and current;
- material `OPEN_RISK`s are accepted/deferred/escalated explicitly rather than hidden.

A recent side issue is not implicitly promoted by receiving more implementation/review attention.

## 12. Controlled remediation

Normal target:

```text
implementation
→ adversarial review
→ Manager consolidated findings
→ ONE bounded remediation
→ final review
```

A second iteration is exceptional: it requires a **new material finding**, stays within the configured maximum, and must not compensate for a shallow first review.

```text
round 2 without new material finding
→ STOP / MANAGER REVIEW
```

Materially new scope/provider/migration/public contract/security boundary/production action/dependency/architecture strategy invalidates the window.

## 13. Swamp Guard checkpoint

The Swamp Guard runs throughout normal work, not only at project inception. Evaluate it:

```text
before a major dependency/provider/datastore/framework
before changing an architecture boundary
after material review/remediation
after repeated rework in the same subsystem
when a SIDE_TASK exceeds its focus budget
when System-Lens OPEN_RISKs accumulate
before broad feature expansion
before staging/production promotion
at durable project checkpoints
```

Classify:

```text
CLEAR | WATCH | ALERT | STOP_REBASELINE
```

Raise at least `WATCH/ALERT` for repeated architecture churn, repeated remediation, abstraction/tooling proliferation without product need, competing mechanisms for one responsibility, AI/RAG tuning without evals, feature growth before a critical vertical slice, chat-only architecture decisions, source-of-truth ambiguity, permanent “temporary” workarounds, complexity growing faster than demonstrated value, side-task attention drift, or repeated unresolved System-Lens risks.

Use `STOP_REBASELINE` when local patching is compounding structural debt or safety risk. Then:

```text
STOP
→ preserve evidence/current state
→ Project Inception / Architecture Discovery
→ simplify / measure / decide
→ establish coherent baseline
→ resume task flow
```

Required alert:

```text
SWAMP ALERT: <WATCH|ALERT|STOP_REBASELINE>
Signal: ...
Evidence: ...
Why it matters: ...
Recommended action: ...
Continue allowed: YES|NO
Authority needed: <none|Manager|Operator>
```

Do not hide a swamp signal merely to maintain velocity.

## 14. Independent closure is not model voting

For HIGH-risk work when required, use a separate read-only Judge after Manager review/remediation.

Independent closure should separate:

```text
IMPLEMENTATION
CONTEXT
AUTHORITY
EVIDENCE
```

Model diversity can improve coverage, but:

```text
MULTI-MODEL AGREEMENT != INDEPENDENT BEHAVIORAL EVIDENCE
```

The Judge is read-only by default and does not mutate product code or production.

## 15. Verify claims, not activity

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
unit PASS          != user flow proven
HTTP 200           != persistence
CI green           != deployed artifact
backup configured  != restore proven
reviewer PASS      != missing runtime evidence
three model PASSes != stronger receipt class
```

Report `PASS | FAIL | PARTIAL | SKIPPED | UNVERIFIED` and truth classes `OBSERVED | DERIVED | INFERRED | UNKNOWN | CONTRADICTED`.

## 16. Compact receipts, raw evidence elsewhere

Preferred receipt:

```yaml
claim: C4
environment: ephemeral-postgres-17
command: pytest tests/integration/test_commit_uncertainty.py
result: PASS 7/7
artifact_ref: artifacts/T125/integration-03.log
proves: commit uncertainty classification
does_not_prove: production provider behavior
```

Task-end summary should stay compact:

```text
What changed
Why it is correct
What was tested
What mutation/path proof was caught
What was not tested
Cross-system effects / OPEN_RISKs
New findings
Environment mutations
Provider calls / spend
Rollback or recovery
Next authorized action
```

Reports index evidence; they do not repeat huge logs.

## 17. Periodic cross-system audit

Even if each task is locally correct, relationships between components can drift. Run a broader audit according to project policy.

Recommended heuristic triggers:

```text
every ~5–8 material tasks (project-configurable)
before a meaningful demo deployment
before every real-customer release
after every material incident
before/after major authority/trust-boundary change
```

Audit themes:

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

This is a System-Lens audit, not another full implementation review. Record findings/gaps and update the System Truth Map when the modeled relationships changed.

## 18. Artifact-driven handoff

```text
Human transports authority.
Repository transports engineering state.
```

Durable state should recover current project mode/baseline, `PRIMARY_TASK`, active task ref/role, suspended/resume state, base/head, findings, remediation window, receipts/gaps, System-Lens open risks, cross-system audit state, Swamp Guard state, closure state and next authority decision. A new session should re-read repository state rather than replay old chat.

## 19. Model/cost routing

Vendor names are adapters, not policy:

```text
Project Architect → stronger reasoning when architecture ambiguity justifies it
Executor          → task-adequate / cost-efficient
Manager           → higher reasoning when justified
Independent Judge → high reasoning + separate context
```

Cost optimization never permits weaker acceptance/evidence.

## 20. Production authority

Before every production mutation follow `production/DELIVERY.md`: exact target/change identity, health signals, abort condition, rollback or forward recovery, data constraints, recovery owner and post-change verification. Judge PASS is not production authority.

## 21. Closure and checkpoint

Preserve:

```text
repository/environment identity
project mode + architecture baseline state
System Truth Map ref/version
PRIMARY_TASK ref
active task ref + role
suspended/resume checkpoint when relevant
current exact head
verified claims
open findings/gaps
System-Lens matrix / OPEN_RISKs
omitted checks
remediation state
Swamp Guard state
cross-system audit state
independent review state when required
next action / authority decision
```

## 22. Measure Flow friction

For material tasks record when available:

```yaml
flow_metrics:
  first_pass_review_passed: true|false|unknown
  remediation_iterations: <integer>
  manager_review_rounds: <integer>
  authorization_round_trips: <integer>
  unplanned_scope_escalations: <integer>
  environment_blocked: true|false
  agent_safety_incidents: <integer>
  side_task_focus_reviews: <integer>
  side_task_promotions: <integer>
  system_lens_open_risks: <integer>
  task_cycle_time: <optional duration>
```

Use these to distinguish quality cost, agent defect cost, governance friction, environment friction, attention drift and system-truth drift. Repeated rework also feeds the Swamp Guard.
