# Production Profile — Evolvable Code Architecture

**Version:** 1.0  
**Updated:** 2026-09-09T10:40:00Z

Goal: keep code understandable, testable and replaceable as the system grows, without imposing patterns whose ceremony exceeds the problem.

## Core principles

- stable business/domain logic should not depend directly on volatile infrastructure details where avoidable;
- dependencies should be explicit and injectable/testable;
- external/provider/legacy semantics should be isolated behind narrow boundaries when change risk is material;
- public/shared contracts should be versioned/verified and kept smaller than internal implementation surfaces;
- module boundaries should reflect ownership/change reasons, not arbitrary file count;
- architecture decisions with material long-term impact should be durable but cold;
- choose a pattern because it addresses an observed risk/change vector, not because the pattern name is fashionable.

## Adapters / ports / anti-corruption boundaries

Use an adapter-like boundary when:

- external API/provider semantics are volatile or not controlled by the team;
- multiple implementations must be swappable;
- legacy schemas/protocols should not leak through new code;
- domain tests need a stable abstraction around database/network/queue/cloud details;
- a provider-specific SDK would otherwise spread across business logic.

Microsoft's Anti-Corruption Layer pattern explicitly recommends a facade/adapter between subsystems with different semantics so outside/legacy dependencies do not constrain the application's design.

Do **not** create an interface/adapter for every class by default. The abstraction should protect a real change/security/testability boundary.

## Dependency inversion

For medium/large codebases and important domain logic:

- high-level policy owns the abstraction;
- infrastructure implements/adapts to that abstraction;
- global hidden dependencies are avoided;
- constructors/configuration make required collaborators explicit;
- tests can replace boundaries without rewriting business code.

Microsoft's architectural guidance notes that dependency inversion makes applications more loosely coupled, testable, modular and maintainable.

## Complexity scaling

### SMALL

Prefer direct/simple code until a real boundary appears. A clear function/module may be better than repository/service/factory layers with no demonstrated value.

### MEDIUM

Define module ownership and explicit external/data boundaries. Use adapters for providers, contract schemas for shared interfaces, composition/DI at application edges, and architecture tests/linting for important dependency direction.

### LARGE

Additionally consider:

- bounded modules/domains and dependency graph rules;
- generated/contract clients rather than duplicated DTO knowledge;
- per-module public APIs;
- architecture decision records for high-impact choices;
- mechanical checks against forbidden dependency directions/cycles;
- affected-project testing/build selection;
- migration patterns such as strangler/anti-corruption boundaries for incremental replacement.

## Reliability patterns are conditional

Use patterns when the failure mode exists:

- **Circuit Breaker** — prevent repeated calls to a persistently failing dependency;
- **Retry** — bounded handling of genuinely transient failures;
- **Bulkhead** — isolate failure/blast radius/resources;
- **Idempotent Consumer** — tolerate at-least-once delivery/duplicate messages;
- **Saga/compensation** — coordinate multi-step distributed business work when a single transaction is impossible;
- **Health Endpoint** — provide operational health signals;
- **Rate limiting/backpressure** — keep demand from overwhelming bounded dependencies.

Each pattern adds operational state/complexity and therefore needs tests/metrics/runbooks proportional to its use.

## Changeability receipt

Do not claim `maintainable` or `easy to change` as a subjective badge. Prefer bounded evidence such as:

- external provider replaced through one adapter boundary;
- domain tests run without live provider/database;
- dependency graph has no forbidden edge/cycle;
- affected consumers are mechanically discoverable;
- a shared contract change fails the right consumer tests;
- public API surface is intentionally smaller than internal implementation;
- complexity/duplication trend is measured where useful.

## Architecture debt / gaps

Report explicitly:

- provider/database SDK calls spread through business logic;
- circular/module dependency prevents isolated testing/deploy/change;
- public/internal boundaries are ambiguous;
- duplicated contract models drift between frontend/backend/services;
- hidden global state makes tests/order/retries nondeterministic;
- a pattern adds layers but does not protect a real change/failure boundary;
- critical architecture rule exists only as prose and can be mechanically enforced;
- large file/module size masks multiple ownership/change reasons.

## Refactoring rule

Refactoring for architecture follows the task lifecycle. Do not silently turn a feature/bug task into a broad clean-architecture rewrite. Triage architecture debt as in-scope necessity, blocker or bounded follow-up.