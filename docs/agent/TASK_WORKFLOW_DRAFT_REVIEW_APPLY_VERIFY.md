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

Typical workflow:

| Risk | Default workflow |
|---|---|
| LOW | execute → focused test → compact self-review → commit/report |
| MEDIUM | short preflight → execute → cold code review → one bounded remediation → Manager review |
| HIGH | frozen contract → engineering/failure preflight → explicit initial authorization → execute → adversarial review → Manager consolidated review → one remediation round by default → read-only Independent Judge when required |

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

The normal target is **one** consolidated remediation round:

```text
implementation
→ cold/adversarial review
→ Manager consolidated findings
→ ONE bounded remediation
→ final review
```

Inside a valid remediation window, the Executor may fix/test/self-review the listed findings and allowed files/resources without new human approval for each local edit.

A second remediation iteration is exceptional. It requires a **new material finding**, must remain within the configured `maximum_without_escalation`, and must not be used merely because the first review was incomplete.

```text
round 2 without new material finding
→ STOP / MANAGER REVIEW
```

A materially new scope, provider, migration, public contract, security boundary, production action, dependency or architecture strategy invalidates the window and triggers STOP + amendment/re-authorization.

## 8. Independent closure is not model voting

For HIGH-risk work when project policy requires independent closure, use a separate read-only Judge after Manager review/remediation.

The Judge should inspect:

```text
frozen task/profile
→ exact source/diff/head
→ raw tests/CI/receipts
→ gaps and omitted checks
→ authorized runtime/production-read evidence when relevant
→ prior reviewer narratives last
```

Independent closure should separate four dimensions where risk justifies it:

```text
IMPLEMENTATION — Judge did not materially implement the change
CONTEXT        — Judge does not rely only on Executor/Manager summaries
AUTHORITY      — Executor cannot self-approve/merge/close
EVIDENCE       — Judge inspects raw receipts rather than repeating a conclusion
```

Model diversity can improve coverage, but:

```text
MULTI-MODEL AGREEMENT != INDEPENDENT BEHAVIORAL EVIDENCE
```

A second model does not upgrade a mock/unit receipt into integration, deployment or production proof.

The Independent Judge is read-only by default. It may recommend closure, request evidence or fail the review; it does not mutate product code or production.

## 9. Verify claims, not activity

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
three model PASSes  != stronger receipt class
```

Report exact states: `PASS | FAIL | PARTIAL | SKIPPED | UNVERIFIED` and truth classes `OBSERVED | DERIVED | INFERRED | UNKNOWN | CONTRADICTED`.

## 10. Compact receipts, raw evidence elsewhere

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

## 11. Artifact-driven handoff

The human/operator should not be a permanent copy/paste message bus.

Durable task state should make these recoverable from the repository:

```text
current task / frozen contract
base + head identity
current review decision/findings
active remediation window
receipts / gaps / omitted checks
closure state
next required authority decision
```

Use this principle:

```text
Human transports authority.
Repository transports engineering state.
```

A new session should inspect current repository/task state before continuing. Do not require replay of the old chat when the durable checkpoint is sufficient.

## 12. Model/cost routing

Vendor names are adapters, not framework policy. Projects may route roles by capability and cost:

```text
Executor          → task-adequate / cost-efficient
Manager           → higher reasoning when the task justifies it
Independent Judge → high reasoning + separate context; diversity preferred when useful
```

Cost optimization never permits weaker acceptance criteria or evidence.

## 13. Production authority

Production remains a separate boundary. Before every production mutation, follow `production/DELIVERY.md` and project policy: exact target/change identity, health signals, abort condition, rollback or forward recovery, data constraints, recovery owner and post-change verification.

The Independent Judge remains read-only by default. A Judge PASS is not production mutation authority.

## 14. Closure and checkpoint

Preserve a compact durable checkpoint:

```text
repository/environment identity
current task + exact head
verified claims
open findings/gaps
omitted checks
remediation state
independent review state when required
next action / next authority decision
```

Once the checkpoint is durable, the working session may be replaced/reset. Session-reset commands themselves are vendor-specific.

## 15. Measure Flow friction

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
