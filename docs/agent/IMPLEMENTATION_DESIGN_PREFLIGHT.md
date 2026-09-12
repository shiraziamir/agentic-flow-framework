# Implementation Design Preflight

**Agent-facing.** Load when the current task references an Engineering Advisory with `level: REQUIRED` or when the Manager explicitly requests a design preflight.

## Purpose

Do not start material implementation by patching prompt items one-by-one. First establish enough repository evidence to choose a coherent design.

The preflight is read-only.

## Authority model

```text
Frozen Contract       = authoritative WHAT / SUCCESS / boundaries
Engineering Advisory  = evidence-constrained HOW guidance
Repository Evidence   = current reality
Executor               = chooses smallest conforming design
Manager / Operator     = approval authority
```

A recommendation is not permission to expand scope. A repository fact does not let the Executor silently rewrite the frozen task.

## Required investigation

Use the advisory's `[INVESTIGATE]` items plus any directly triggered questions. Typical examples:

- real call graph / consumers of the behavior being changed;
- current state owner(s) and duplicated authority;
- exact failure propagation/swallowing paths;
- persistence/transaction phases;
- concurrency and locking boundaries;
- public/data/security/operational contracts;
- existing project patterns worth reusing;
- smallest deterministic test seams and fault-injection points.

Prefer deterministic search/graph/source inspection over broad speculative reasoning.

## Required pre-mutation receipt

Report briefly:

```text
IMPLEMENTATION DESIGN PROPOSED

OBSERVED CURRENT DESIGN
- <facts with paths/symbols where useful>

CHOSEN IMPLEMENTATION SHAPE
- <small cohesive design>

WHY THIS IS THE SMALLEST COHERENT SOLUTION
- <reasoning bounded by observed source>

AFFECTED FILES / RESOURCES
- <expected mutation boundary>

VERIFICATION / FAILURE-INJECTION STRATEGY
- <tests/checks tied to behavior>

EXECUTION READINESS
- <changed behavior to exercise>
- <lowest adequate authorized environment>
- <real dependencies/boundaries required>
- <what mock-only evidence can and cannot establish>

ADVISORY DEPARTURES
- <none or recommendation + evidence-backed reason>

NEW STOP CONDITIONS / UNKNOWNS
- <none or material discoveries>
```

Under `STRICT_PREVIEW`, append the normal mutation preview fields and wait for explicit `APPROVE` / `APPLY`.

If a frozen STOP condition fires, do not solve around it. Request amendment/decision.

If no authorized environment can exercise the changed path at the required claim strength, report `BLOCKED` or `UNVERIFIED` and issue an environment request. Do not preserve an integration-or-stronger claim while substituting a mock-only receipt.

## During implementation

The Executor may choose a smaller conforming alternative to `[SHOULD]` guidance. It may not violate `[MUST]` requirements grounded in the frozen contract.

If source evidence invalidates an advisory recommendation:

```text
record evidence
→ choose smallest conforming alternative
→ explain departure
→ continue only if still within frozen/approved boundary
```

If the alternative broadens architecture, scope, permissions, public contract, persistence, data/security boundary, or environment authority:

```text
STOP → amendment / revised preview → Manager/Operator decision
```

## Closure

Include:

```text
IMPLEMENTATION DESIGN ACTUALLY USED
```

with:

- final placement of important types/state owners/helpers/boundaries;
- material differences from proposed design;
- material departures from advisory and why;
- verification receipts for load-bearing behavior.

Do not claim the advisory was followed merely because the code resembles it. Report actual design and evidence.
