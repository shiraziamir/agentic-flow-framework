# Task Workflow — DRAFT → REVIEW → APPLY → VERIFY

**Agent-facing practical guide.** Load this when a material task is being planned, changed, implemented, or closed.

## Purpose

Separate task design from implementation so scope, acceptance and verification are clear before mutation. The goal is not bureaucracy; the goal is to stop accidental scope growth and unsupported closure claims.

Mutation authority is controlled separately by `schemas/MUTATION_APPROVAL_POLICY.md`. A project may require a compact current-vs-proposed preview before every mutation batch even after the task itself has been reviewed.

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

## 4. CHANGE PREVIEW / MUTATION APPROVAL

Check `.agentic/PROJECT_PROFILE.yaml` and `schemas/MUTATION_APPROVAL_POLICY.md`.

Under `STRICT_PREVIEW`, before each bounded mutation batch report:

```text
CURRENT STATE      what is true now
PROPOSED STATE     what will be true after the batch
WHY                reason for the change
WILL CHANGE        files/resources expected to mutate
IMPACT             behavior/API/security/data/operations impact
VERIFY             planned tests/checks
ROLLBACK/RECOVERY  when material
OUT OF SCOPE       explicit boundary
```

Then stop and wait for explicit `APPROVE` / `APPLY`.

Approval is limited to the previewed batch. Group tightly related edits into one batch when they share one purpose and verification boundary; do not create line-by-line approval spam.

Task approval and mutation approval are distinct:

```text
TASK AUTHORIZATION
= this work is allowed conceptually

MUTATION APPROVAL
= this specific bounded change is allowed now
```

Neither one automatically grants production/destructive authority.

## 5. APPLY

Use:

```text
prompts/workflow/APPLY_TASK.md
```

Implement only inside the approved task scope **and**, where required, the approved mutation preview.

During APPLY:

- keep exact repository/task/environment identity visible;
- run focused checks as soon as useful;
- preserve existing project conventions unless the task explicitly changes them;
- use the lowest environment that can prove the required behavior;
- do not weaken a test, mock a real boundary, disable a control or broaden scope merely to get green output;
- record new material facts that affect verification or production posture.

If implementation discovers a materially new database, provider, public interface, production environment, security boundary, migration, durable-data requirement, operational dependency, architecture strategy, or a materially different file/resource set than the approved preview:

```text
STOP
→ record evidence / newly discovered current state
→ amend / reclassify task if needed
→ present revised change preview
→ review / authorize as required
→ continue only inside the new boundary
```

## 6. VERIFY + REPORT

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

After mutation, report the actual delta against the approved preview. If something planned was not changed, or something changed unexpectedly, state it explicitly.

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

### Optional usage/quota footer

After the engineering status is complete, check the project's `usage_reporting` policy. If `quota_snapshot` is enabled/optional **and trustworthy telemetry is available**, append one compact footer using `schemas/USAGE_QUOTA_SNAPSHOT.md` and `docs/agent/USAGE_AWARE_TASK_REPORTING.md`.

For Claude Code:

```bash
python3 <framework>/scripts/claude_usage_snapshot.py
```

Example:

```text
Usage
- session: 15% used / 85% remaining
- weekly: 23% used / 77% remaining
- source: CLAUDE_STATUSLINE_RATE_LIMITS
- freshness: current
```

If telemetry is missing:

```text
Usage
- session: unavailable
- weekly: unavailable
- source: UNAVAILABLE
```

Quota reporting happens **after** claim/evidence reporting so it cannot be confused with task proof. Low quota can trigger an operator notification/checkpoint recommendation, but never silently reduces required verification.

## 7. INDEPENDENT CLOSURE

Use independent/cold closure when project risk, task classification or the evidence surface requires it.

The reviewer should prefer this order:

```text
frozen task / project profile
→ approved mutation preview(s)
→ actual diff / source
→ raw receipts / gaps
→ falsifying checks
→ executor narrative last
```

Reviewer judgment can challenge evidence but cannot replace a missing behavioral receipt.

## 8. CHECKPOINT

At closure, preserve a compact durable checkpoint:

- repository/artifact/environment identity;
- task status;
- approved mutation batch(es) when applicable;
- verified claims and receipts;
- checks not run;
- open gaps / overrides;
- unresolved risks;
- usage quota snapshot when configured and observable;
- next action if any.

Do not store chain-of-thought or full transcripts as project state.

## Small tasks

Do not force the full HIGH-risk ceremony onto trivial edits. The invariant is proportional control:

```text
risk up   → stronger draft/review/authorization/evidence
risk down → lighter workflow
```

However, if the project explicitly selects `STRICT_PREVIEW`, even a small mutation still gets a short preview and approval. Keep that preview compact and batch related edits.

Likewise, quota reporting defaults to **material task/checkpoint** cadence; do not spend extra tool calls/notifications on every trivial read or tiny interaction unless the operator explicitly asks for per-turn reporting.
