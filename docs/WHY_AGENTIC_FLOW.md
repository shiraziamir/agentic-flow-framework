# Why Agentic Flow

## The problem

Coding agents can generate and edit code quickly. Reliability breaks down around the code: ambiguous authority, hidden scope growth, stale context, weak tests, unobserved runtime behavior, unsupported deployment claims and self-review.

A plausible implementation and a confident summary can create a false-complete state. The repository may contain code that looks right while the changed path was never exercised through the boundary named by the claim.

## The response

Agentic Flow makes five things durable and separate:

```text
WHAT SHOULD BE TRUE   frozen task + project profile
WHAT MAY CHANGE NOW   mutation approval
WHERE ACTION MAY RUN  environment authority
WHAT WAS DONE         exact diff/commit/artifact identity
WHAT WAS OBSERVED     claim-bound receipts, gaps and unknowns
WHO DECIDES           operator/manager authority
```

It also separates roles:

- Designer turns intent and repository evidence into a contract proposal and advisory.
- Manager checks the proposal, freezes/authorizes bounded work and independently reviews the real result.
- Executor chooses the smallest conforming implementation and produces receipts.
- Evidence—not role confidence—limits closure language.

## Why real execution matters

Verification strength must match claim strength. A unit test may establish a local transformation. It cannot automatically establish a database transaction, provider contract, end-user flow or deployed behavior.

The environment ladder is therefore part of task design, not an afterthought:

```text
LOCAL/HERMETIC → EPHEMERAL TEST → SHARED TEST → STAGING
→ CONTROLLED PRODUCTION READ/CANARY → PRODUCTION MUTATION
```

Use the lowest authorized rung that exercises the real affected path. For normal behavior changes, `LOCAL_REAL` or `EPHEMERAL_TEST` is the baseline when it can host the actual application and affected dependencies. Missing access produces an environment request and an honest `UNVERIFIED/BLOCKED` status; it does not justify a stronger claim from a weaker mock.

## Evidence map

This is a concise map, not a claim that any source endorses Agentic Flow as a complete framework.

| Framework idea | External evidence used | What it supports | What it does not prove |
|---|---|---|---|
| repository-first instructions and compact context | OpenAI harness engineering; Gemini CLI and OpenCode project-context guidance | durable repository context, concise maps, lazy loading | superiority of this exact file layout |
| explicit, structured prompts | OpenAI, Anthropic and Google prompting guidance | clarity, delimiters, output contracts, critical constraints | deterministic compliance by every model |
| outcome/receipt-based review | Anthropic evaluation/outcome guidance; Playwright and Pact practices | measurable success criteria and boundary-relevant checks | that every chosen receipt is sufficient |
| production-like and layered validation | Microsoft Well-Architected testing; Google SRE canarying | risk-proportionate environments and limits of lower environments | blanket need for production testing |
| protected branch + required review/checks | GitHub protected-branch guidance | branch isolation and enforceable review gates | that a green status means every intended check ran |
| security and supply-chain profiles | OWASP ASVS/SAMM, NIST SSDF, SLSA, GitHub dependency review | established control categories and versioned assurance concepts | that a project is secure because files mention them |
| operational evidence | Google SRE, Prometheus, OpenTelemetry, database vendor docs | observable signals and restore/persistence semantics | production readiness without project receipts |

See the complete, dated links and usage notes in [Primary Sources](references/PRIMARY_SOURCES.md). Vendor behavior and standards are time-sensitive; recheck them when a current decision depends on them.

## Limits by design

Agentic Flow does not:

- guarantee correct code or prevent every agent failure;
- create a security boundary when all roles share one unrestricted credential;
- replace product-specific tests, threat models, operations or human accountability;
- prove production readiness from templates or documentation;
- make a context packet equivalent to direct high-risk code review;
- authorize production or destructive action;
- prove its own effectiveness without comparative field evidence.

Its current validation is described in [Validation Status](VALIDATION_STATUS.md).
