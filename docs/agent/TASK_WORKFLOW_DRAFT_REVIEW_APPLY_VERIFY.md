# Task Workflow — Risk-Adaptive Draft → Execute → Verify

**Agent-facing canonical workflow for material tasks.**

## Goal

Keep the quality bar stable while adapting ceremony to risk. Prevent three common failures:

```text
scope drift
attention drift
local correctness that breaks system truth
```

```text
risk up   → stronger boundaries, broader preflight, stronger evidence/review
risk down → fewer gates, smaller reports, faster execution
```

Do not confuse rigor with repeated permission prompts or checklist filling.

## 1. Establish task focus first

At every durable checkpoint identify:

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

A `SIDE` task keeps a primary-task reference, bounded success condition, scope/round budget and return condition. Normal behavior is:

```text
SIDE_TASK done
→ record result
→ return to PRIMARY_TASK
```

Promotion requires explicit Manager/Operator decision. When a side task exceeds its budget, creates unrelated architecture or becomes the dominant optimization target, raise `SIDE_TASK DRIFT` and recommend `CLOSE | DEFER | PROMOTE_PROPOSAL`.

An `INTERRUPT` checkpoints the primary task before urgent bounded work and records exactly where/how to resume.

## 2. Classify risk and work kind

```yaml
risk_level: LOW|MEDIUM|HIGH
work_kind: IMPLEMENTATION|REMEDIATION|EVIDENCE_ONLY
```

| Risk | Default workflow |
|---|---|
| LOW | execute → focused test → compact diff review → compact System-Lens impact summary |
| MEDIUM | short preflight → execute → Dual-Lens review → cold review → one bounded remediation → Manager review |
| HIGH | frozen contract → failure/System-Lens preflight → explicit authorization → execute → adversarial review → Manager consolidated review → one remediation by default → read-only Independent Judge when required |

If the task exposes a missing/broken architecture baseline, route to `docs/agent/PROJECT_INCEPTION_ARCHITECTURE.md` instead of stacking local patches.

## 3. Draft the observable contract

Before material mutation define:

- task focus and relationship to primary work;
- goal/symptom;
- business/system invariants and failure semantics;
- allowed mutation surface and explicit exclusions;
- observable Definition of Done;
- planned claims and minimum receipts;
- required environment/real boundaries;
- intentionally omitted checks;
- STOP/escalation conditions;
- System Truth Map reference when applicable;
- expected cross-system impact or known `OPEN_RISK`s.

The contract defines **WHAT + SUCCESS**, not every implementation detail.

For complex MEDIUM/HIGH work, advisory algorithm/pseudocode is encouraged when it exposes intended semantics before edits. It remains advisory unless explicitly frozen as an invariant.

## 4. Engineering and failure preflight

For MEDIUM/HIGH, inspect before editing:

```text
What owns the affected state?
What is authoritative vs derived?
What is the real call/data path?
Where do failures propagate or disappear?
What is the smallest coherent change?
What real boundary can prove it?
```

Baseline failure surfaces when relevant:

```text
NORMAL PATH
BOUNDARY / INVALID INPUT
DEPENDENCY OR I/O FAILURE
CLEANUP / ROLLBACK FAILURE
OBSERVABILITY / HEALTH PROPAGATION
TEST-ORACLE FALSIFICATION
```

Add triggered surfaces only when applicable:

```text
THREAD / PROCESS CONCURRENCY
CRASH / RESTART
DURABILITY / PARTIAL WRITE
PERMISSION / IDENTITY
EXTERNAL PROVIDER
MIGRATION / SCHEMA
CACHE / CONSISTENCY
```

Under `STRICT_PREVIEW`, include the material preflight in the mutation preview and wait for `APPROVE/APPLY`.

## 5. Dual-Lens review

```text
LOCAL LENS
Is the changed behavior itself correct?

SYSTEM LENS
What truth does the whole system claim after this change?
```

### Local Lens

Check the actual call path, business invariant, failure semantics, resource ownership/cleanup, focused acceptance tests, related regressions, complete diff and mutation/path-proof seams when load-bearing.

### System Lens dimensions

Use the project System Truth Map and these dimensions when relevant:

```text
WRITE · READ · AGGREGATE · CACHE · RESTART · FAILURE · RECOVERY
ADMIN · METRIC · TENANT_ISOLATION · SCALE · PRIVACY · COST
```

Possible states:

```text
UNAFFECTED | VERIFIED | CHANGED_AND_TESTED | OPEN_RISK | NOT_APPLICABLE
```

### Risk-adaptive depth

Do **not** turn the matrix into checklist theater.

- `LOW` + genuinely local change: write a short impact summary naming only plausible affected dimensions. Do not mechanically fill all rows.
- `MEDIUM/HIGH`: record the relevant matrix dimensions explicitly.
- any risk level touching **money, privacy, identity, tenant isolation, durability/recovery, destructive state or production semantics**: record explicit affected dimensions regardless of nominal task size.

Rules:

- `UNAFFECTED` is a reviewed conclusion, not a filler value;
- `OPEN_RISK` remains visible until resolved, accepted or deliberately deferred;
- caches/projections/summaries/metrics cannot silently become authoritative business truth;
- when data authority, trust boundary, recovery rule or scale boundary materially changes, update `.agentic/SYSTEM_TRUTH_MAP.yaml` or STOP/re-baseline.

## 6. Execute in an adequate environment

Use the lowest authorized environment that can directly exercise the changed behavior. Mock-only evidence closes unit/model claims; it does not silently inherit persistence, migration, integration, user-flow, deployment or production semantics.

During execution:

- run focused checks early;
- preserve project conventions unless intentionally changed;
- do not weaken tests to make output green;
- do not silently broaden scope;
- do not optimize a side task beyond its declared role/budget;
- protect dirty/uncommitted work;
- do not make real provider/external calls without authority.

## 7. Test business behavior, not only functions

For material business behavior, prefer scenario tests that trace actual truth. Examples when applicable:

```text
normal success
fallback/escalation
provider retry / partial charge
failure after external side effect
source-of-truth unavailable
cache restart / projection rebuild
time/month boundary
admin recovery
cross-tenant attempt
concurrency / duplicate work
```

Use only relevant scenarios; templates do not justify irrelevant tests.

## 8. Mutation/path proof for load-bearing tests

A green load-bearing test is stronger when we show it can detect the target defect.

Examples:

```text
remove tenant dimension from cache key
turn authority-read failure into zero/empty success
double-count an aggregate row
remove lock / cleanup / readiness condition
skip projection rebuild after restart
```

Perform manual mutation only in an isolated temporary working copy or equivalent safe mechanism. Do not use destructive Git reset/restore/clean commands against operator work. Preserve and verify restoration of exact bytes.

## 9. Verification sequence

Use risk/size-appropriate checks:

```text
focused tests early
mutation/path proof when load-bearing
related regressions
one final broader/full-suite run when meaningful and bounded
static review of complete diff
Local + System Lens receipt
```

Do not rerun an enormous suite mechanically after every tiny edit; do perform the required final qualification before closure.

## 10. Pre-Manager adversarial review

For MEDIUM/HIGH, prefer cold/read-only review before spending Manager attention. Inspect exact diff + surrounding source for false assumptions, duplicate authority, swallowed errors, cleanup leaks, concurrency/crash gaps, weak test oracles, missing health propagation, unsafe workspace actions, unauthorized external effects, scope/task-focus drift and System-Lens gaps.

## 11. Manager consolidated review

Manager reviews the exact commit/PR head, not only the Executor narrative. Prefer one consolidated finding set:

```text
R1 ...
R2 ...
R3 ...
```

Manager confirms:

- active task still matches real priority;
- Local Lens is supported by tests/diff;
- System Lens is proportionate and honest;
- `OPEN_RISK`s are explicit;
- no recent side issue was silently promoted.

For bounded same-task findings, use a controlled remediation window.

## 12. Controlled remediation

Normal target:

```text
implementation
→ adversarial review
→ Manager consolidated findings
→ ONE bounded remediation
→ final review
```

A second iteration is exceptional: it requires a **new material finding**, stays within configured maximum, and may not hide shallow initial review.

```text
round 2 without new material finding
→ STOP / MANAGER REVIEW
```

New provider/migration/public contract/security boundary/production action/dependency/architecture strategy or out-of-scope resource invalidates the window.

## 13. Swamp Guard checkpoint

Evaluate at material checkpoints, before major architecture/tooling expansion, after repeated rework, when a side task exceeds focus budget, when System-Lens open risks accumulate, and before staging/production promotion.

```text
CLEAR | WATCH | ALERT | STOP_REBASELINE
```

Use `STOP_REBASELINE` when local patching is compounding structural debt or safety risk:

```text
STOP
→ preserve evidence/current state
→ Project Inception / Architecture Discovery
→ simplify / measure / decide
→ establish coherent baseline
→ resume
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

## 14. Cross-system audit trigger order

Periodic audit is a safety net, not a calendar ritual.

```text
EVENT TRIGGER
> RISK / AUTHORITY TRIGGER
> TASK-COUNT REMINDER
```

Trigger immediately when justified by real-customer release, material incident, or material security/data/authority/recovery change. A configured `5–8 material tasks` interval is only a fallback reminder. Harmless docs/local tasks do not force a meaningless audit.

Audit themes when relevant:

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

## 15. Independent closure is not model voting

For HIGH-risk work when required, use a separate read-only Judge after Manager review/remediation.

Prefer separation of:

```text
IMPLEMENTATION
CONTEXT
AUTHORITY
EVIDENCE
```

```text
MULTI-MODEL AGREEMENT != INDEPENDENT BEHAVIORAL EVIDENCE
```

The Judge does not mutate product code or production and does not upgrade missing runtime evidence by opinion.

## 16. Claim discipline

Evidence strength rises roughly through:

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

Report `PASS | FAIL | PARTIAL | SKIPPED | UNVERIFIED` and `OBSERVED | DERIVED | INFERRED | UNKNOWN | CONTRADICTED` honestly.

## 17. Compact closure receipt

End material work with a short report pointing to raw evidence:

```text
What changed
Why it is correct
What was tested
Mutation/path proof caught
What was not tested
System-Lens impact / OPEN_RISK
New findings
Environment mutations
Provider calls/spend
Rollback/recovery
Next authorized action
```

Out-of-scope findings are recorded, not silently absorbed into the task unless current safety requires STOP/amendment.

## 18. Production boundary

Production mutation is separate authority. Before every production mutation require exact target/artifact/change identity, health/success signal, abort condition, rollback or forward-recovery path, state/data constraints, recovery owner and post-change verification.

```text
missing rollback/recovery readiness
→ NOT EXECUTION_READY_FOR_PRODUCTION_MUTATION
```

Independent review never grants production authority.
