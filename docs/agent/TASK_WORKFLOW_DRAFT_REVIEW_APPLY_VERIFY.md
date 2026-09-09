# Task Workflow — DRAFT → REVIEW → APPLY → VERIFY

**Agent-facing practical guide.** Load this when a material task is being planned, changed, implemented, or closed.

## Purpose

Separate task design from implementation so scope, acceptance and verification are clear before mutation. The goal is not bureaucracy; the goal is to stop accidental scope growth and unsupported closure claims.

## 1. DRAFT

Use:

```text
prompts/workflow/DRAFT_TASK.md
```

Create or update the durable task contract before material APPLY.

The draft should answer:

```text
What exactly is changing?
What is explicitly out of scope?
Which code / data / infra / CI / production surfaces are affected?
What observable Definition of Done must be true?
What claims do we expect to make at closure?
What minimum receipt proves each claim?
Which tests and environments are required?
Which checks are intentionally omitted?
What causes STOP / amendment / escalation?
```

Do not start with implementation details alone. A good draft defines the observable result and evidence boundary.

## 2. REVIEW

Use:

```text
prompts/workflow/REVIEW_DRAFT.md
```

Review the draft before high-risk mutation. The reviewer checks for missing consumers, environments, data effects, security/authorization changes, deployment/rollback implications, observability/recovery impact, weak acceptance criteria and claims that cannot be verified with the planned environment.

For HIGH-risk work, the reviewer should be independent/cold where practical and remain read-only during review.

Possible outcomes:

```text
PASS
PASS WITH REQUIRED CHANGES
REVISE
STOP / NEEDS OWNER DECISION
```

## 3. FREEZE / APPLY AUTHORIZATION

For HIGH-risk work, freeze the reviewed task and obtain separate authorization before mutation.

For ordinary bounded work, project policy may allow the reviewed task itself to authorize APPLY.

Never treat a request for production access, a model recommendation or a reviewer suggestion as authority by itself.

## 4. APPLY

Use:

```text
prompts/workflow/APPLY_TASK.md
```

Implement only inside the approved scope and strategy.

During APPLY:

- keep the exact repository/task/environment identity visible;
- run focused checks as soon as useful;
- preserve existing project conventions unless the task explicitly changes them;
- use the lowest environment that can prove the required behavior;
- do not weaken a test, mock a real boundary, disable a control or broaden scope merely to get green output;
- record new material facts that affect verification or production posture.

If implementation discovers a materially new database, provider, public interface, production environment, security boundary, migration, durable-data requirement, operational dependency or architecture strategy:

```text
STOP
→ record evidence
→ amend / reclassify the task
→ review / authorize as required
→ continue only inside the new boundary
```

## 5. VERIFY + REPORT

Use:

```text
prompts/workflow/VERIFY_AND_REPORT.md
```

Map every material DoD item and planned claim to current receipts.

Verification strength should match the claim:

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
scanner green       != secure
reviewer PASS       != missing runtime receipt
```

Report exact reality:

```text
PASS
FAIL
PARTIAL
SKIPPED
UNVERIFIED
```

Truth classes remain:

```text
OBSERVED
DERIVED
INFERRED
UNKNOWN
CONTRADICTED
```

Do not hide skipped or unavailable checks.

## 6. INDEPENDENT CLOSURE

Use independent/cold closure when project risk, task classification or the evidence surface requires it.

The reviewer should prefer this order:

```text
frozen task / project profile
→ actual diff / source
→ raw receipts / gaps
→ falsifying checks
→ executor narrative last
```

Reviewer judgment can challenge evidence but cannot replace a missing behavioral receipt.

## 7. CHECKPOINT

At closure, preserve a compact durable checkpoint:

- repository/artifact/environment identity;
- task status;
- verified claims and receipts;
- checks not run;
- open gaps / overrides;
- unresolved risks;
- next action if any.

Do not store chain-of-thought or full transcripts as project state.

## Small tasks

Do not force the full HIGH-risk ceremony onto trivial edits. The invariant is proportional control:

```text
risk up   → stronger draft/review/authorization/evidence
risk down → lighter workflow
```

The claim/receipt and scope boundaries still apply.
