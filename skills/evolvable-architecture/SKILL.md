---
name: evolvable-architecture
description: Review or design code boundaries for changeability, explicit dependencies, provider adapters, shared contracts and mechanically enforceable architecture without unnecessary pattern ceremony.
metadata:
  class: COMMON
  authority: portable-agentic-flow
---

# Evolvable Architecture

## USE WHEN

Architecture/module/provider/shared-contract choices materially affect future change, testing or operational risk.

## PROCEDURE

1. Name the concrete change/failure boundary being protected.
2. Inspect current dependency graph and ownership before proposing layers.
3. Keep stable policy/domain code separate from volatile provider/storage/runtime details where useful.
4. Use an adapter/anti-corruption boundary for uncontrolled external/legacy semantics when that boundary reduces coupling.
5. Make dependencies explicit/injectable rather than hidden global state.
6. Keep shared/public contracts narrow and test affected consumers.
7. Mechanically enforce important dependency/cycle/public-API rules when practical.
8. Scale architecture to codebase complexity; simple projects should remain simple.
9. Record material debt/follow-ups instead of silently broadening the current task.

## NON-TRIGGER

Do not create interfaces/repositories/factories/DDD layers merely to satisfy a pattern checklist.

## EVIDENCE

Prefer dependency graph/architecture tests, consumer build/tests, provider replacement boundaries and focused change diffs over subjective claims such as `clean` or `maintainable`.

## OUTPUT

Boundary rationale, dependency/change map, selected pattern or explicit decision not to add one, verification and remaining architecture debt.