# Mutation Approval Policy

**Schema version:** 1.2  
**Updated:** 2026-09-13

This policy controls mutation authority without turning every correction into a new human round-trip.

## Principle

```text
Quality requirements stay fixed.
Process ceremony adapts to risk.
```

Approval is for boundaries, not for every keystroke. High-risk work should have stronger scope, evidence and review boundaries, but can still use bounded remediation autonomy inside an approved task.

## Modes

```text
STRICT_PREVIEW
MATERIAL_CHANGES_ONLY
BOUNDED_AUTONOMY
```

### STRICT_PREVIEW

Recommended for first adoption, unfamiliar repositories and sensitive work. Before the first mutation batch, present:

```yaml
change_preview:
  current_state: []
  proposed_state: []
  reason: []
  files_or_resources: []
  behavior_or_contract_impact: []
  operational_security_data_impact: []
  planned_checks: []
  rollback_or_recovery: []
  scope_boundary: []
```

Then wait for `APPROVE` / `APPLY`.

Do **not** interpret STRICT_PREVIEW as permission spam. Related edits that share one purpose, verification plan and rollback boundary should be one batch.

### MATERIAL_CHANGES_ONLY

Trivial/local/reversible edits inside the frozen task may proceed without a separate approval. Material changes still need a preview.

Material normally includes public contracts, architecture boundaries, persistence/data, dependencies, security/identity, CI/CD, infrastructure, external providers, destructive operations or meaningful scope expansion.

### BOUNDED_AUTONOMY

The agent may mutate inside the frozen task and explicit path/resource boundary. It still stops before material scope, architecture, risk, environment, authority or public-contract expansion.

## Controlled remediation window

A Manager may authorize a **controlled remediation window** after reviewing an implementation or PR. This prevents a high-risk task from requiring a fresh authorization for every finding while preserving boundaries.

Recommended shape:

```yaml
remediation_window:
  review_ref: <review-id/ref>
  finding_ids: [R1, R2]
  max_iterations: 1
  maximum_without_escalation: 2
  extra_iteration_requires_new_material_finding: true
  allowed_files_or_resources: []
  allowed_change_classes:
    - CORRECTNESS_FIX
    - TEST_HARDENING
    - CLEANUP_FAILURE_HANDLING
    - OBSERVABILITY_FIX
  owner_review_required_before_closure: true
```

The normal target is **one** remediation iteration after one consolidated review. That iteration may include implementation, focused tests, self/cold review and corrections for the listed findings without a fresh approval for each local edit.

A second iteration is exceptional. It requires a **new material finding**, must remain inside `maximum_without_escalation`, and must not silently expand the task. If no new material finding exists, a second round indicates the Manager should re-review the state rather than automatically extending the loop.

```text
round 2 without NEW MATERIAL FINDING
→ STOP / MANAGER REVIEW
```

The window ends immediately if work requires any unapproved material expansion, including:

- new database/schema/migration scope;
- new public API/contract behavior;
- new external provider call or external side effect;
- new dependency or architecture boundary;
- new security/identity/secret scope;
- production access or destructive action;
- files/resources outside the approved boundary;
- a materially different implementation strategy or risk class.

Then:

```text
STOP
→ report discovered state
→ revise task/change preview
→ obtain new authority
```

**Remediation autonomy is not scope autonomy.**

## Consolidated review

Prefer one broad review that returns a set of findings over a sequence of narrow reviews that reveal one layer at a time.

Recommended loop:

```text
IMPLEMENT
→ focused tests
→ cold/adversarial agent review
→ executor fixes obvious findings
→ Manager consolidated review
→ ONE bounded remediation by default
→ Manager final review
→ read-only Independent Judge when required
```

The Manager should spend reviewer attention on scope, architecture, risk, product semantics, evidence and unresolved ambiguity—not on repeatedly rediscovering simple local defects that an adversarial pre-review can catch.

## Independent closure does not authorize mutation

When project policy requires an Independent Judge, the Judge is read-only by default. Judge findings return to the Manager/Operator. A Judge does not extend a remediation window, edit code or mutate production by itself.

```text
Judge PASS
!= mutation authority
!= production authority
```

Multiple model/reviewer PASSes also do not upgrade the evidence class of the underlying receipts.

## Read-only discovery

Normally no mutation approval is required for reading files/state, `git status`, diff/log/branch inspection, dependency/search queries, CI/test configuration, planning and non-mutating runtime queries. If a supposedly read-only tool can cause side effects, treat it as mutation-capable.

## Workspace safety

Uncommitted work is protected state unless ownership is proven otherwise.

The following are destructive or potentially destructive and require explicit care/authority when dirty work may exist:

```text
git checkout -- <path>
git restore <path>
git reset --hard
git clean -fd
force checkout
force push
```

Before destructive Git/file operations:

```text
git status / dirty-state inspection
→ identify ownership of changed paths
→ preserve/checkpoint unknown or user-owned work
→ obtain destructive approval when loss is possible
```

Unknown ownership means **preserve**, not discard.

## External side effects

Authorization to run tests does not automatically authorize real provider calls, paid APIs, messages, deployments or other external side effects.

```text
unit/integration test authority
!=
real external-provider-call authority
```

Projects should default real external calls to denied unless a task/environment policy explicitly authorizes them.

## Separation of authority

Mutation approval does not replace:

- task DRAFT/REVIEW/FREEZE;
- environment permissions;
- external-side-effect permission;
- production/destructive authorization;
- security/data controls;
- verification/closure evidence.

A task can therefore be conceptually authorized while a specific mutation, environment action or provider call is still denied.
