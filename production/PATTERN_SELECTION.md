# Production Profile — Pattern Selection

**Version:** 1.0  
**Updated:** 2026-09-09T11:30:00Z

Goal: make architecture patterns deliberate responses to real change/failure boundaries rather than mandatory ceremony.

## Default governance

Recommended default: `AGENT_PROPOSES_OWNER_MAY_OVERRIDE`.

The agent may propose a pattern when evidence shows a real problem such as:

- volatile external provider/API semantics;
- multiple implementations behind one business capability;
- legacy model leakage;
- cross-cutting persistence/queue/cache coupling;
- public contract versioning;
- testability blocked by hard dependency;
- repeated change touching many unrelated modules;
- failure isolation or resilience requirement.

For a material new abstraction, report:

```yaml
pattern_proposal:
  problem: <observed coupling/change/failure problem>
  proposed_pattern: <Adapter|Anti-Corruption Layer|Strategy|Factory|Repository|Circuit Breaker|...>
  boundary_protected: <exact boundary>
  simpler_alternative: <what happens without pattern>
  benefits: []
  costs: []
  migration_scope: []
  verification: []
  recommendation: ADOPT|DEFER|NOT_NEEDED
```

## Who decides?

- small/local/reversible implementation detail: agent may choose within project conventions;
- new shared/public architectural abstraction: agent proposes; owner/supervisor approves when material;
- architecture/security/data/production contract change: freeze the choice in the reviewed task/decision artifact before broad implementation.

## Pattern restraint

Do not create an interface/factory/adapter/repository/service layer merely to satisfy a style doctrine. A pattern should pay for itself through one or more of:

- reduced coupling;
- isolated volatility;
- explicit trust/failure boundary;
- replaceability;
- testability;
- clearer ownership;
- reduced blast radius of future change.

If those benefits cannot be named and verified, prefer the simpler design.

## Review later

A pattern decision is not permanent. When the boundary disappears or costs exceed benefits, the agent may propose simplification/refactoring through the normal task-review flow.
