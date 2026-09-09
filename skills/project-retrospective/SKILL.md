---
name: project-retrospective
description: Reconstruct how a project or campaign evolved from Git, task artifacts, evidence, judgments, token/cost telemetry and the cold execution ledger. Use only for audit-grade retrospective, governance analysis, historical metrics or execution reconstruction.
---

# Project Retrospective

## Class
COMMON — intentionally cold/on-demand.

## USE_WHEN

- final campaign/rescue retrospective;
- execution/work reconstruction report;
- governance-overhead analysis;
- architecture/process evolution audit;
- historical token/cost/task metrics;
- owner asks for evidence-grounded counts/timeline of how work progressed.

## DO_NOT_USE_WHEN

- normal implementation;
- current-task diagnosis;
- routine bootstrap;
- merely because history exists;
- a reader-facing narrative/self-branding request that does not require audit-grade reconstruction; use `project-storytelling` instead.

## INPUT_CONTRACT

Prefer, in this order:

1. Git commits/tags/diffs and timestamps;
2. frozen tasks/amendments/authorizations;
3. evidence packets/test receipts/live receipts;
4. supervisor judgments;
5. execution retrospective ledger;
6. token/cost ledger;
7. owner journal or secondary durable notes;
8. conversation history only as a last, explicitly weaker source.

## PROCEDURE

1. Define the requested time/campaign boundary.
2. Discover primary artifacts mechanically; do not load every historical file blindly.
3. Build a compact timeline keyed by task/boundary/commit.
4. Separate every material fact into:
   - `PROVEN FROM GIT / DURABLE ARTIFACTS`
   - `RECONSTRUCTED FROM OWNER JOURNAL / RECEIPTS`
   - `UNKNOWN / NOT LOGGED RELIABLY`
5. Derive only metrics whose denominators are known.
6. Identify false-complete states prevented, STOPs that blocked real mistakes, amendments, independent reviews, deferred findings and scope-creep prevention.
7. Distinguish runtime/implementation work from evidence/governance work.
8. Analyze governance value versus ceremony using evidence, not aesthetics.
9. Explain architecture/process evolution and "what we would do differently next time".
10. Produce bounded source refs that `project-storytelling` can later consume without rereading all raw history.

## SUGGESTED METRICS

```text
tasks closed
amendment loops
independent reviews
pre-closure defects caught
STOP conditions triggered
false-complete states prevented
implementation commits
evidence/governance commits
tests added where derivable
peak/final suite counts
production mutations
test-environment live runs
provider calls/spend when trustworthy
token usage when trustworthy
deferred findings
```

## MUTATION_AUTHORITY

Read-only by default. May generate a retrospective/report artifact when requested. Must not rewrite historical source artifacts to make the reconstruction cleaner.

## EVIDENCE_REQUIRED

Every concrete count or claim needs a source reference or an explicit weaker truth class. Unknown remains unknown.

## FAIL_CLOSED_BEHAVIOR

If early history is incomplete, state the reliable boundary explicitly, for example:

> Before checkpoint X, execution history is only partially reconstructible; exact iteration count and elapsed work are unknown.

Never extrapolate exact historical numbers from incomplete logs.

## OUTPUT_CONTRACT

A timestamped/versioned report containing scope, evidence basis, timeline, metrics with truth classes, notable prevented failures, governance analysis, architecture/process evolution, deferred/unknown items, lessons and bounded source refs for optional later storytelling.
