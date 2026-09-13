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

```yaml
risk_level: LOW|MEDIUM|HIGH
work_kind: IMPLEMENTATION|REMEDIATION|EVIDENCE_ONLY
```

| Risk | Default workflow |
|---|---|
| LOW | execute → focused test → compact self-review → commit/report |
| MEDIUM | short preflight → execute → cold review → one bounded remediation → Manager review |
| HIGH | frozen contract → failure preflight → explicit authorization → execute → adversarial review → Manager consolidated review → one remediation round by default → read-only Independent Judge when required |

If the task exposes that the project architecture baseline itself is missing/broken, do not keep treating it as a local task. Route to `docs/agent/PROJECT_INCEPTION_ARCHITECTURE.md`.

## 2. Draft the observable contract

Define before material mutation:

- goal/symptom;
- in-scope / out-of-scope surfaces;
- observable Definition of Done;
- claims and minimum receipts;
- required environment/real boundaries;
- intentionally omitted checks;
- STOP/escalation conditions.

The contract defines **WHAT + SUCCESS**, not an implementation script.

## 3. Engineering preflight

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

## 4. Execute in an adequate environment

Use the lowest authorized environment that can directly exercise the changed behavior. Mock-only evidence closes only unit/model claims; it cannot silently inherit persistence, migration, integration, user-flow, deployment or production semantics.

During execution:

- run focused checks early;
- preserve project conventions unless intentionally changed;
- do not weaken tests to make output green;
- do not silently broaden scope;
- protect dirty/uncommitted work;
- do not make real provider/external calls without authority.

## 5. Pre-Manager adversarial review

For MEDIUM/HIGH, prefer a cold/read-only review before spending Manager attention. Inspect actual diff and surrounding source for false assumptions, duplicate state authorities, swallowed errors, cleanup leaks, concurrency/crash gaps, weak test oracles, missing health propagation, unsafe workspace actions, unauthorized external effects and scope drift.

## 6. Manager consolidated review

Manager reviews the exact commit/PR head, not only the Executor summary. Prefer one consolidated finding set:

```text
R1 ...
R2 ...
R3 ...
```

If findings are bounded/same-task, authorize a controlled remediation window per `schemas/MUTATION_APPROVAL_POLICY.md`.

## 7. Controlled remediation

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

## 8. Swamp Guard checkpoint

The Swamp Guard runs throughout normal work, not only at project inception. Evaluate it:

```text
before a major dependency/provider/datastore/framework
before changing an architecture boundary
after material review/remediation
after repeated rework in the same subsystem
before broad feature expansion
before staging/production promotion
at durable project checkpoints
```

Classify:

```text
CLEAR | WATCH | ALERT | STOP_REBASELINE
```

Raise at least `WATCH/ALERT` for repeated architecture churn, repeated remediation, abstraction/tooling proliferation without product need, competing mechanisms for one responsibility, AI/RAG tuning without evals, feature growth before a critical vertical slice, chat-only architecture decisions, source-of-truth ambiguity, permanent “temporary” workarounds, or complexity growing faster than demonstrated value.

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

## 9. Independent closure is not model voting

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

## 10. Verify claims, not activity

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

## 11. Compact receipts, raw evidence elsewhere

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

Reports index evidence; they do not repeat huge logs.

## 12. Artifact-driven handoff

```text
Human transports authority.
Repository transports engineering state.
```

Durable state should recover current project mode/baseline, task, base/head, findings, remediation window, receipts/gaps, Swamp Guard state, closure state and next authority decision. A new session should re-read repository state rather than replay old chat.

## 13. Model/cost routing

Vendor names are adapters, not policy:

```text
Project Architect → stronger reasoning when architecture ambiguity justifies it
Executor          → task-adequate / cost-efficient
Manager           → higher reasoning when justified
Independent Judge → high reasoning + separate context
```

Cost optimization never permits weaker acceptance/evidence.

## 14. Production authority

Before every production mutation follow `production/DELIVERY.md`: exact target/change identity, health signals, abort condition, rollback or forward recovery, data constraints, recovery owner and post-change verification. Judge PASS is not production authority.

## 15. Closure and checkpoint

Preserve:

```text
repository/environment identity
project mode + architecture baseline state
current task + exact head
verified claims
open findings/gaps
omitted checks
remediation state
Swamp Guard state
independent review state when required
next action / authority decision
```

## 16. Measure Flow friction

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
  task_cycle_time: <optional duration>
```

Use these to distinguish quality cost, agent defect cost, governance friction and environment friction. Repeated rework also feeds the Swamp Guard.
