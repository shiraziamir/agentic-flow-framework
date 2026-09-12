# Comparison

Agentic Flow is an operating framework, not a coding model or autonomous orchestration runtime. The relevant comparison is how work is governed and evidenced.

| Dimension | Ordinary chat-driven agent | Prompt/policy file only | Agentic Flow |
|---|---|---|---|
| durable source of truth | mostly conversation | standing instructions | canonical policy + profile + frozen task + receipts |
| role separation | commonly one context | optional wording | explicit Designer / Manager / Executor responsibilities |
| task vs mutation permission | often implicit | may be stated | separate contracts; `STRICT_PREVIEW` available |
| environment authority | often implicit | usually a warning | explicit ladder and per-environment permission |
| execution readiness | “can run tests” | rarely modeled | claim-specific real changed-path requirement |
| mock semantics | frequently ambiguous | project-dependent | mock closes only the modeled boundary |
| closure | narrative + test summary | checklist | claim → minimum receipt → current identity |
| code review | may review own changes | project-dependent | Manager reviews exact commit/PR head when material |
| context handoff | replay chat | static instructions | compact hot state or bounded context packet |
| production gaps | easily lost | checklist item | durable explicit gap states |
| cost/complexity | lowest upfront | low | higher for material work; risk-adaptive |

## When ordinary use may be enough

A lightweight prompt can be appropriate for trivial, reversible, low-risk work where the result is immediately inspectable and no strong behavioral or production claim is made. Agentic Flow should not turn a typo fix into a ceremony-heavy program.

## When Agentic Flow is useful

The framework becomes more valuable when work has one or more of these traits:

- multiple agents or handoffs;
- meaningful scope/authority boundaries;
- database, provider, security, deployment or durable-data effects;
- costly false-positive closure;
- a need to preserve decisions outside chat;
- independent review requirements;
- an execution environment that may be weaker than the claim.

## Costs and trade-offs

- Operators must define authority and maintain a project profile.
- Material tasks require up-front claim/test thinking.
- Independent roles and real integration environments cost time and compute.
- Repository artifacts can become stale if teams do not maintain them.
- Some controls are procedural unless enforced with branch protection, identities and CI.
- The framework’s own comparative benefit is not yet established by controlled studies.

## What is genuinely different

The central difference is not more checklists. It is the combination of:

1. durable repository state instead of conversation authority;
2. separation of Designer, Manager and Executor;
3. independent task, mutation and environment authority;
4. claim-strength semantics tied to receipts and exact identity;
5. an execution-readiness gate that refuses mock-only closure for stronger claims;
6. explicit unknowns and operational gaps.

See [Getting Started](GETTING_STARTED.md) for practical adoption and [Validation Status](VALIDATION_STATUS.md) for current evidence.
