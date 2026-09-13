# Task Workflow — Risk-Adaptive Draft → Execute → Verify

**Agent-facing canonical workflow for material tasks.**

## Goal

Keep the quality bar stable while changing ceremony according to risk.

```text
risk up   → stronger boundaries, broader preflight, stronger evidence/review
risk down → fewer gates, smaller reports, faster execution
```

Do not confuse rigor with repeated permission prompts.

## 1. Classify the work

Prefer two independent dimensions:

```yaml
risk_level: LOW|MEDIUM|HIGH
work_kind: IMPLEMENTATION|REMEDIATION|EVIDENCE_ONLY
```

Legacy task contracts may still use `governance: HIGH|MEDIUM|EVIDENCE_ONLY`; interpret `EVIDENCE_ONLY` as work kind rather than as a risk level when migrating.

Typical workflow:

| Risk | Default workflow |
|---|---|
| LOW | execute → focused test → compact self-review → commit/report |
| MEDIUM | short preflight → execute → cold code review → bounded remediation → Manager review |
| HIGH | frozen contract → engineering/failure preflight → explicit initial authorization → execute → adversarial review → Manager consolidated review → remediation window → final/independent closure when required |

## 2. Draft the observable contract

For material work, define before mutation:

- goal and symptom;
- in-scope / out-of-scope surfaces;
- observable Definition of Done;
- planned claims and minimum receipts;
- required environment and real boundaries;
- important checks intentionally omitted;
- STOP/escalation conditions.

The contract defines **WHAT + SUCCESS**, not an implementation script.

## 3. Engineering preflight

For MEDIUM/HIGH or advisory-required tasks, inspect the current system before editing.

At minimum answer:

```text
What owns the affected state?
What is the real call/data path?
Where are exceptions/failures swallowed or propagated?
What are the authoritative vs derived states?
What is the smallest coherent change?
What test seam and real boundary prove it?
```

### Failure-surface matrix

Use a triggered matrix instead of blindly applying every failure case to every task.

Baseline questions for material behavioral work:

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
THREAD CONCURRENCY
PROCESS CONCURRENCY
CRASH / RESTART
DURABILITY / PARTIAL WRITE
PERMISSION / IDENTITY
EXTERNAL PROVIDER
MIGRATION / SCHEMA
CACHE / CONSISTENCY
```

For each applicable row, state the expected invariant, failure signal and planned evidence. This is intended to reduce serial remediation rounds by finding the failure surface before coding.

Under `STRICT_PREVIEW`, include the implementation preflight in the first change preview and wait for `APPROVE` / `APPLY`.

## 4. Execute in an adequate environment

Implement only inside the frozen/approved boundaries.

Use the lowest authorized environment that can directly exercise the changed behavior. Mock-only evidence may close only unit/model claims; it cannot silently inherit persistence, migration, integration, user-flow, deployment or production semantics.

During execution:

- run focused checks early;
- preserve existing project conventions unless explicitly changed;
- do not weaken tests to make output green;
- do not silently broaden scope;
- protect dirty/uncommitted work;
- do not make real provider/external calls unless explicitly authorized.

## 5. Pre-Manager adversarial review

Before spending Manager attention on MEDIUM/HIGH work, use a cold/read-only reviewer or separate review context where practical.

Review the actual diff and relevant surrounding source for:

- incorrect assumptions and missing consumers;
- duplicated state authorities;
- swallowed truth / broad exception handling;
- cleanup/rollback leaks;
- concurrency or crash gaps;
- false-positive tests or proxy assertions;
- missing propagation to health/observability;
- unsafe Git/workspace operations;
- unauthorized provider/external effects;
- scope drift.

The Executor may fix obvious findings inside existing authority when the change remains within the frozen scope and mutation policy.

## 6. Manager consolidated review

The Manager reviews the exact commit/PR head, not only the Executor summary.

Prefer returning one consolidated finding set:

```text
R1 ...
R2 ...
R3 ...
```

rather than repeatedly opening a new authorization cycle for every local defect.

If findings are bounded and same-task, the Manager can authorize a `remediation_window` per `schemas/MUTATION_APPROVAL_POLICY.md`.

## 7. Controlled remediation

Inside a valid remediation window, the Executor may perform up to the authorized number of fix/test/self-review iterations for the listed findings and allowed files/resources.

A materially new scope, provider, migration, public contract, security boundary, production action, dependency or architecture strategy invalidates the window and triggers STOP + amendment/re-authorization.

## 8. Verify claims, not activity

Map each DoD/claim to current receipts.

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
unit test PASS      != end-user flow proven
HTTP 200            != persistence proven
CI green            != deployed artifact proven
backup configured   != restore proven
reviewer PASS       != missing runtime evidence
```

Report exact states: `PASS | FAIL | PARTIAL | SKIPPED | UNVERIFIED` and truth classes `OBSERVED | DERIVED | INFERRED | UNKNOWN | CONTRADICTED`.

## 9. Compact receipts, raw evidence elsewhere

Evidence richness must not require verbose task reports.

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

Store raw logs/artifacts separately when useful. The report should index evidence, not repeat hundreds of lines of it.

## 10. Closure and checkpoint

For HIGH risk, independent/cold closure remains recommended when required by project policy. Review in this order:

```text
frozen task/profile
→ approved boundaries/remediation window
→ exact diff/source
→ raw receipts/gaps
→ falsifying checks
→ executor narrative last
```

Preserve a compact checkpoint: repository/environment identity, task state, verified claims, omitted checks, open gaps/risks and next action.

## 11. Measure Flow friction

For material tasks, record cheap process counters when available:

```yaml
flow_metrics:
  first_pass_review_passed: true|false|unknown
  remediation_iterations: <integer>
  manager_review_rounds: <integer>
  authorization_round_trips: <integer>
  unplanned_scope_escalations: <integer>
  environment_blocked: true|false
  agent_safety_incidents: <integer>
  task_cycle_time: <optional duration>
```

These are process-improvement signals, not developer-performance scores. Use them to distinguish:

```text
quality cost
vs agent defect cost
vs governance friction
vs environment friction
```

The objective is fewer unnecessary round-trips without weakening the acceptance bar.
