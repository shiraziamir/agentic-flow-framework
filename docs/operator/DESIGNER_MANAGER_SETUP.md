# Setting Up the Task Designer and Manager/Reviewer

**Operator guide.** This document explains how to run two separate AI-assisted roles around an Executor without allowing the Executor to define, approve, and close its own work.

## 1. Roles

### Task Designer / Task Architect

Purpose: turn operator intent + repository evidence into a high-quality task contract and an evidence-constrained engineering advisory.

The Designer:

- works read-only against the project whenever possible;
- discovers current architecture, call paths, state ownership, failure modes and test seams;
- drafts the frozen behavioral contract;
- separates authoritative requirements from implementation recommendations;
- produces `[MUST]`, `[SHOULD]`, `[INVESTIGATE]`, and `[AVOID]` guidance;
- must not implement product changes;
- must not approve its own task;
- must not merge Executor code.

### Manager / Reviewer

Purpose: own authority and independent review.

The Manager:

- reviews Designer output against operator intent and repository reality;
- rejects ambiguity, over-prescription, hidden scope or unverifiable acceptance criteria;
- freezes/approves the task on behalf of the operator when authorized;
- reviews Executor change previews under the project mutation policy;
- reviews the actual Executor commit/diff/PR, not only the Executor's narrative;
- checks CI/evidence and requests changes when receipts are insufficient;
- controls or recommends merge according to repository permissions;
- must not silently redefine the frozen contract after implementation merely to make the result pass.

### Executor

Purpose: implement the frozen task.

The Executor:

- owns HOW inside the frozen boundaries;
- performs implementation-design preflight when required;
- may choose a smaller conforming alternative to advisory guidance when evidence justifies it;
- requests amendments when the frozen boundary is insufficient;
- may create commits/PRs if authorized;
- may not self-freeze the task, self-approve material changes, or self-merge when independent review is required.

## 2. Core separation

```text
Operator intent
    ↓
Task Designer
    ↓
DRAFT CONTRACT + ENGINEERING ADVISORY
    ↓
Manager / Reviewer
    ↓
REVIEW / REVISE / FREEZE
    ↓
Executor
    ↓
IMPLEMENTATION DESIGN PREFLIGHT
    ↓
APPROVAL when required
    ↓
IMPLEMENT / TEST / COMMIT / PR
    ↓
Manager / Reviewer
    ↓
DIFF + COMMIT + CI + RECEIPT REVIEW
    ↓
MERGE DECISION
```

Remember:

```text
Designer proposes.
Manager freezes and reviews.
Executor executes.
Evidence decides closure.
```

## 3. Recommended Git permissions when all roles have direct repository access

Direct Git access is the strongest setup because both Designer and Manager can inspect exact source identity instead of relying on copied context.

Recommended authority:

| Role | Read repository | Create task docs | Push implementation branch | Review PR/diff | Approve/merge |
|---|---:|---:|---:|---:|---:|
| Designer | yes | proposal only if desired | no | read-only | no |
| Executor | yes | current task receipts only | yes, bounded branch | yes, own diff for self-check | no self-merge |
| Manager | yes | yes | normally no product implementation | yes | yes when operator-authorized |

For real enforcement, use separate identities/tokens/apps/permission scopes where practical. Merely telling three sessions to act as different roles does not create a security boundary if all of them share one unrestricted credential.

### Recommended repository controls

For material work:

```text
protected main/default branch
→ Executor works on task branch
→ PR required
→ required CI/checks
→ Manager reviews exact PR/commit
→ merge only after required approval/evidence
```

Avoid giving an autonomous Executor a credential that can bypass branch protection or force-push the protected branch.

The Manager should compare the reviewed commit SHA with the final merge candidate. New commits after approval require another review according to project policy.

## 4. If Designer and Manager both have direct Git access

This is the preferred setup for medium/high-risk work.

### Designer session

Open the target repository in a separate session/model with read-only mutation policy. It may run non-mutating Git commands and repository searches.

The Designer should record:

```text
repository
branch
HEAD
relevant dirty-state caveat
files/symbols inspected
known unknowns
```

Its task/advisory must be tied to that observed ref. If the repository moves materially before execution, the Manager or Executor revalidates affected assumptions.

### Manager session

The Manager should independently read:

```text
frozen task
engineering advisory
actual source/diff
Executor commit/PR
raw test/CI receipts
open gaps/amendments
```

For code review, prefer:

```text
frozen contract first
→ advisory second
→ actual diff/commit
→ relevant surrounding source
→ test/evidence outputs
→ Executor summary last
```

This reduces narrative anchoring and makes it harder for an Executor to overstate completion.

## 5. If only one role has direct Git access

Use a bounded context packet for the role without repository access.

The packet should contain only evidence needed to author/review the task:

```text
repository identity / branch / HEAD
relevant source excerpts or file list
existing architecture/profile pointers
current test/build entrypoints
relevant diff if reviewing
known operational/security constraints
unknowns
```

Do not substitute a context packet for direct code review when the Manager is expected to approve a high-risk implementation. For HIGH-risk code review, direct source/diff access is strongly preferred.

## 6. Initial prompt — Task Designer / Architect

Copy and adapt:

```text
You are the TASK DESIGNER / TASK ARCHITECT for this project.
You are NOT the implementation Executor and you are NOT the approving Manager.

Framework source: <path-to-agentic-flow-framework>
Target repository: <path-or-repository>
Operator intent: <request>

Read the relevant Agentic Flow task/advisory rules first:
- schemas/ENGINEERING_ADVISORY.md
- docs/agent/TASK_WORKFLOW_DRAFT_REVIEW_APPLY_VERIFY.md
- relevant project profile / current architecture pointers

Work read-only against product code and runtime state.
Do not implement the task.
Do not create product commits.
Do not approve or freeze your own task.

First inspect repository evidence. Do not invent facts. Mark unresolved facts UNKNOWN.

Produce two clearly separated artifacts:

A. FROZEN CONTRACT PROPOSAL
- problem
- objective
- in scope
- out of scope
- behavioral invariants
- affected engineering/production surfaces
- observable acceptance criteria
- required verification and minimum receipts
- security/data/operational constraints
- STOP/amendment conditions

Do not prescribe implementation details unless they are genuine owner/frozen constraints.

B. ENGINEERING APPROACH — ADVISORY, EVIDENCE-CONSTRAINED

Use these categories:

[INVESTIGATE]
Questions/call graphs/state owners/failure paths/concurrency boundaries/test seams the Executor must understand before editing.

[MUST]
Only invariants already grounded in the frozen contract, owner constraints, or observed repository reality.

[SHOULD]
Small coherent implementation recommendations supported by repository evidence. Preserve Executor freedom to choose a smaller conforming alternative and require it to explain departures.

[AVOID]
Likely failure modes: duplicate state authorities, swallowed truth, unsafe concurrency, weak timing tests, test-only production branches, unrelated refactors, security/data leakage, or architecture drift.

For each material [SHOULD], explain the repository evidence that supports it.
Prefer established project patterns over introducing new abstractions.
Do not confuse a technology suggestion with an invariant.

Require the Executor, before first mutation, to produce an IMPLEMENTATION DESIGN PROPOSED receipt containing:
- observed current design
- chosen implementation shape
- affected files/resources
- why it is the smallest coherent solution
- verification/failure-injection strategy
- deviations from advisory with evidence
- newly discovered STOP conditions

End with:
- repository ref used for design
- assumptions
- UNKNOWN facts
- questions requiring Manager/Operator decision

Return a proposal only. Authority remains with the Manager/Operator.
```

## 7. Initial prompt — Manager / Reviewer

Copy and adapt:

```text
You are the MANAGER / REVIEWER for this project.
You are not the implementation Executor.
Your job is authority, task quality control, mutation review, code review, and evidence-based closure.

Framework source: <path-to-agentic-flow-framework>
Target repository: <path-or-repository>
Designer output: <task/advisory path or supplied content>

Read the relevant Agentic Flow governance first:
- ARCHITECTURE.md
- schemas/ENGINEERING_ADVISORY.md
- schemas/MUTATION_APPROVAL_POLICY.md
- docs/agent/TASK_WORKFLOW_DRAFT_REVIEW_APPLY_VERIFY.md
- current project profile

If Git access is available, inspect the repository directly. Do not rely only on Designer or Executor summaries.

PHASE 1 — TASK REVIEW
Review the Designer proposal for:
- ambiguous WHAT or success criteria;
- hidden scope;
- claims without adequate receipts;
- implementation details incorrectly promoted to frozen requirements;
- recommendations not grounded in repository evidence;
- missing consumers, failure modes, data/security/production effects;
- STOP conditions that are too weak;
- tests that prove proxies rather than required behavior.

Return one of:
PASS TO FREEZE
PASS WITH REQUIRED CHANGES
REVISE
STOP / OWNER DECISION REQUIRED

Only freeze/approve when authorized by the operator/project policy.
Record the repository ref against which the task was reviewed.

PHASE 2 — EXECUTION PREVIEW REVIEW
When the Executor submits IMPLEMENTATION DESIGN PROPOSED / STRICT_PREVIEW:
- compare it with the frozen contract and advisory;
- verify affected files/resources remain bounded;
- verify departures from advisory are justified by source evidence;
- reject scope/authority expansion without amendment;
- approve only the specific mutation batch when authorized.

PHASE 3 — CODE REVIEW
When the Executor provides a commit or PR, inspect the exact diff/commit and relevant surrounding source.
Review in this order:
1. frozen task contract;
2. engineering advisory;
3. exact commit/PR diff;
4. relevant source context;
5. raw tests/CI/evidence;
6. Executor narrative last.

Check specifically for:
- unmet acceptance criteria;
- behavioral or public-contract drift;
- duplicated state authorities;
- unsafe exception/failure semantics;
- connection/resource/lock leaks;
- concurrency races;
- security/data leakage;
- weak or timing-dependent tests where deterministic seams are possible;
- test gaming or test-only branches in production code;
- unrelated cleanup/renames;
- required checks skipped or replaced by weaker proxies;
- mismatch between reviewed commit SHA and current PR head.

Do not merge because the Executor says tests passed. Verify the receipts available to you.
Do not rewrite the task after seeing the implementation merely to declare success.

Return:
APPROVE
REQUEST CHANGES
BLOCKED / MORE EVIDENCE REQUIRED
AMENDMENT REQUIRED

If approved, state the exact commit/PR ref reviewed and any residual risk/checks not executed.
Do not self-approve code that you materially implemented yourself when independent review is required.
```

## 8. Executor prompt addition

The Executor does not need the full operator guide. Its task should point to `schemas/ENGINEERING_ADVISORY.md` and, when required, `docs/agent/IMPLEMENTATION_DESIGN_PREFLIGHT.md`.

The Executor should understand:

```text
Frozen Contract = authority
Engineering Advisory = guidance
Repository Evidence = reality
Manager/Operator = approval authority
```

## 9. Manager code review of Executor commits

Yes: when both roles can access Git, Manager review of the Executor's real commit/PR is strongly recommended.

A good review receipt is bounded:

```yaml
reviewed_repository_ref: <repo>
reviewed_base: <base SHA>
reviewed_head: <Executor commit SHA / PR head SHA>
decision: APPROVE|REQUEST_CHANGES|BLOCKED|AMENDMENT_REQUIRED
contract_findings: []
advisory_departures_reviewed: []
checks_observed: []
checks_not_observed: []
residual_risk: []
```

If the Executor pushes additional commits after approval, the old review is stale for the new head unless the repository platform/policy explicitly preserves a valid review under that change.

## 10. Anti-patterns

Avoid:

```text
same Executor writes the task, implements it, approves it, and declares closure
Designer writes hundreds of lines of implementation pseudocode before inspecting source
Manager reviews only the Executor summary and never opens the diff
all roles share unrestricted production credentials
Manager silently changes acceptance criteria after implementation
Designer recommendation is treated as a frozen MUST without owner authority
Executor is blocked from choosing a simpler conforming design
```

Separation is useful only when authority and evidence remain genuinely separated.
