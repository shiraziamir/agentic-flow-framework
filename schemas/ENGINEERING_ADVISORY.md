# Engineering Advisory Schema

**Schema version:** 1.0  
**Updated:** 2026-09-12

Use for material tasks where the operator wants the executor to reason about implementation quality before coding without turning implementation suggestions into frozen requirements.

The advisory is subordinate to the frozen task contract and current repository evidence.

```yaml
advisory_id: <stable-id>
task_id: <task-id>
created_at: <RFC3339>
author_role: TASK_DESIGNER|OPERATOR|OTHER
repository_ref: <commit/ref observed by designer>
level: NONE|LIGHT|REQUIRED

investigate_before_coding:
  - question: <call graph/state owner/failure path/concurrency/test seam to inspect>
    evidence_hint: <optional path/symbol/query>

required_invariants:
  - statement: <must remain true regardless of implementation>
    source: FROZEN_CONTRACT|OWNER_CONSTRAINT|REPOSITORY_EVIDENCE

recommended_shape:
  - recommendation: <small coherent implementation hypothesis>
    evidence_basis: <why repository evidence supports it>
    freedom: EXECUTOR_MAY_CHOOSE_SMALLER_CONFORMING_ALTERNATIVE

avoid:
  - <likely failure mode, duplicated authority, unsafe handling, weak-test pattern, architecture drift>

preflight_receipt_required:
  observed_current_design: true
  chosen_implementation_shape: true
  affected_files_or_resources: true
  why_smallest_coherent_solution: true
  verification_and_failure_injection_strategy: true
  advisory_departures: true
  newly_discovered_stop_conditions: true
```

## Authority

```text
Frozen Task Contract = authoritative WHAT / SUCCESS / boundaries
Engineering Advisory  = evidence-constrained HOW guidance
Repository Evidence   = current reality
Executor               = chooses the smallest conforming design
Manager / Operator     = reviews/freezes/authorizes material mutation
```

The executor must not treat a recommendation as permission to broaden scope or violate the frozen contract.

## Advisory tags

Human-readable advisories should distinguish:

```text
[MUST]         authoritative invariant already grounded in the frozen contract/owner constraint
[SHOULD]       recommended implementation shape supported by current evidence
[INVESTIGATE]  question that must be answered before mutation
[AVOID]        known failure pattern or design trap
```

Do not upgrade `[SHOULD]` into `[MUST]` merely because a model suggested it.

## Design freedom

The advisory should improve reasoning, not replace it.

Prefer:

```text
Reuse the repository's established thread-safe pool pattern; if the current proven
implementation is ThreadedConnectionPool, prefer it over introducing a new abstraction.
```

over:

```text
Use ThreadedConnectionPool.
```

unless the exact technology is itself a frozen requirement.

Every material recommendation should be tied to observed repository evidence. Unknown facts stay `UNKNOWN`.

## Implementation-design preflight

Before the first mutation on a `REQUIRED` advisory task, the executor performs a read-only preflight and reports:

```text
IMPLEMENTATION DESIGN PROPOSED

Observed current design
Chosen implementation shape
Affected files/resources
Why this is the smallest coherent solution
Verification/failure-injection strategy
Departures from advisory, with evidence
New STOP conditions discovered
```

Under `STRICT_PREVIEW`, this preflight becomes part of the mutation preview and the executor waits for `APPROVE` / `APPLY`.

Under a policy that already grants bounded autonomy, the executor may continue only within the frozen task and approved authority boundary unless a STOP condition fires.

## Closure

The execution report should include:

```text
IMPLEMENTATION DESIGN ACTUALLY USED
```

and identify material differences from the proposed preflight or advisory. A justified smaller conforming alternative is acceptable; silent architecture drift is not.
