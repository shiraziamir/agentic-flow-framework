# Evidence Recovery and Measurement Qualification

**Purpose:** define what to do when a verification run is mechanically successful but the measuring environment, runtime identity, baseline, or authorization boundary is wrong or stale.

This schema is for evidence recovery. It is not permission to change product behavior just to make verification pass.

## Core rule

> Evidence about behavior is valid only when the runtime, artifact, environment, inputs, and authorization that produced it are the ones the claim requires.

A successful request against the wrong runtime is not partial proof of the intended runtime. Preserve it as history and classify it honestly.

Recommended dispositions:

```text
VALID_FOR_CLAIM
PARTIAL_FOR_CLAIM
VOID_FOR_CLAIM
HISTORICAL_ONLY
UNKNOWN
```

`VOID_FOR_CLAIM` does not mean the run never happened. It means the run cannot establish the claim it was intended to prove.

## Designed / implemented / proven boundary

Keep these states separate when reporting capability maturity:

```text
DESIGNED
IMPLEMENTED_IN_SOURCE
MECHANICALLY_TESTED
QUALIFIED_IN_NAMED_ENVIRONMENT
LIVE_BEHAVIOR_PROVEN
DEPLOYED_ARTIFACT_PROVEN
PRODUCTION_BEHAVIOR_PROVEN
```

Do not compress them into one word such as `done`, `ready`, or `supported`.

Examples:

- source code + unit tests may establish `IMPLEMENTED_IN_SOURCE` and `MECHANICALLY_TESTED`;
- a testenv miss/hit trace may establish `LIVE_BEHAVIOR_PROVEN` for that testenv;
- none of those establish `PRODUCTION_BEHAVIOR_PROVEN` without production deployment/runtime evidence.

## Pre-execution qualification

For material live/integration evidence, define the minimum qualification before the expensive or mutation-capable run begins.

Typical checks:

```yaml
qualification:
  repository_ref: <exact commit>
  artifact_or_image_ref: <digest/hash>
  runtime_identity_match: true|false|unknown
  environment_identity: <testenv/staging/prod + mechanical proof>
  writable_paths: [<actual writable state locations>]
  baseline_ref: <exact durable baseline or NONE>
  prerequisite_state:
    - <non-null record, migration complete, budget available, dependency reachable, etc.>
  forbidden_preconditioning:
    - cache_flush
    - corpus_reset
    - hidden_warmup
    - production_state_reuse
  qualification_receipts: []
```

Use the smallest set that is load-bearing for the claim. Do not turn the list into a generic checklist detached from the system being measured.

## Measurement-instrument failure

If execution reveals that the runtime/environment itself cannot measure the intended behavior, STOP before improvising.

Examples:

- container image predates the source under review;
- the expected module/config/migration is absent from the running artifact;
- test traffic is routed to the wrong environment;
- host-side tests write production state while claiming test isolation;
- the baseline was produced under a materially different/confounded state;
- the tracing path needed to prove the claim is not present in the runtime.

Classify the finding:

```text
IMPLEMENTATION_DEFECT
EVIDENCE_ENVIRONMENT_DEFECT
BASELINE_DEFECT
AUTHORIZATION_DEFECT
MIXED
```

An `EVIDENCE_ENVIRONMENT_DEFECT` may be repaired as same-task recovery when the product design/source does not need to change and the recovery only fixes the measuring instrument. High-risk environment mutation still requires the appropriate authorization.

## Authorization consumption

Bounded execution authorization is a consumable capability when it says `exactly one`, names a finite request/test count, or otherwise limits attempts.

Default rule:

```text
attempt performed -> authorization consumed
```

unless the durable authorization explicitly says otherwise.

A void/failed run does not silently grant a rerun. Persist the finding and obtain new authorization when the original authority was consumed or the recovery requires new mutation scope such as rebuild/recreate/restart.

Recommended fields:

```yaml
authorization:
  ref: <durable authorization>
  execution_limit: <integer|unbounded>
  consumed_on_attempt: true|false
  attempts_used: <integer>
  rerun_requires_new_authorization: true|false
```

## Recovery sequence

A bounded recovery should normally follow:

```text
PRESERVE INVALID EVIDENCE
→ INDEPENDENTLY CLASSIFY FAILURE
→ DEFINE MINIMUM RECOVERY SCOPE
→ NEW AUTHORIZATION IF REQUIRED
→ QUALIFY RUNTIME / ENVIRONMENT
→ EXECUTE FRESH EVIDENCE RUN
→ VERIFY ISOLATION / SIDE EFFECTS
→ RECONCILE CLAIMS
→ INDEPENDENT CLOSURE WHEN REQUIRED
```

Do not overwrite the invalid artifact with the fresh one. Use distinct paths/IDs and make the disposition explicit.

## Baseline comparison

A baseline is evidence, not a ritual target.

Record:

- exact baseline artifact/ref;
- environment and state that produced it;
- exact members/IDs for bounded failure sets when later exact-set comparison matters;
- known confounds;
- whether the new run is directly comparable.

If a controlled recovery removes a known confound and previously failing checks disappear, do not call that a regression merely because the failure set changed. Judge against the stated acceptance purpose. Conversely, do not replace an exact-set requirement with count/signature similarity when the contract requires literal identity.

## Side-effect accounting

Verification itself can mutate state. Before material host/integration tests, identify writable paths and environment bindings when those writes could reach shared or production state.

Report separately:

```text
SOURCE_MUTATION
TESTENV_MUTATION
PRODUCTION_MUTATION
CORPUS_OR_DURABLE_DATA_MUTATION
CACHE_MUTATION
PROVIDER_CALLS / SPEND
```

`no corpus mutation` is not equivalent to `no production mutation`.

If an earlier receipt was wrong, correct the historical record explicitly; do not erase the incorrect claim as if it never existed.

## Context reset after high-risk closure

After a long HIGH-risk task or recovery campaign, create the durable closure/checkpoint first. Then a fresh execution context may be preferable before Task N+1 so stale conversational authority, superseded amendments, and void evidence are not accidentally carried forward.

The reset is a context-hygiene tool, not an authorization mechanism. Task N+1 still requires its own durable authority.
