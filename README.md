# Agentic Flow Framework

**Framework version:** 1.8
**Updated:** 2026-09-13
**Status:** an evidence-oriented operating framework; see [validation status](docs/VALIDATION_STATUS.md)
**Persian:** [راهنمای جامع فارسی](docs/GUIDE.fa.md)

Agentic Flow is a repository-first, vendor-neutral way to make coding-agent work reviewable, bounded and honest about what is known.

> Coding quickly is not the hard part. The hard part is knowing what was authorized, what changed, what was actually exercised, what the evidence proves, and what remains unknown.

## Why this repository exists

A normal chat-driven coding-agent session can end in a plausible but false-complete state:

- the agent silently broadens scope;
- a passing mock is reported as proof of a real integration;
- implementation, approval and closure happen in one context;
- runtime or deployment claims are inferred from code or CI;
- the next person must reconstruct decisions from chat history;
- production gaps disappear behind the phrase “done.”

Agentic Flow moves the durable parts of the work into the repository: a project profile, frozen task contract, mutation policy, evidence receipts, explicit gaps and review decisions. Conversation remains disposable working context.

Read the short rationale in [Why Agentic Flow](docs/WHY_AGENTIC_FLOW.md).

## What changes compared with ordinary agent use

| Ordinary agent use | Agentic Flow |
|---|---|
| prompt/chat is the practical source of truth | repository contracts and current refs are the durable source of truth |
| one agent often plans, codes, approves and closes | Designer proposes, Manager freezes/reviews, Executor implements |
| “tests pass” is treated as a general completion signal | each claim is bounded by the receipt that directly establishes it |
| mocks may stand in for real behavior without qualification | mock evidence closes only the modeled boundary |
| access and approval are often conflated | task, mutation and environment authority are separate |
| continuation requires replaying history | compact current state and context packets support handoff |

This is more ceremony than an informal prompt for material work, but it is risk-adaptive: tiny/docs work can remain light. See the fuller [comparison](docs/COMPARISON.md).

## What is evidence-based—and what is not yet proven

The design draws on primary guidance from OpenAI, Anthropic, Google, Microsoft, GitHub, OWASP, NIST, SLSA, Playwright, Pact, PostgreSQL, Prometheus, OpenTelemetry and SRE/chaos-engineering sources. The concise [evidence map](docs/WHY_AGENTIC_FLOW.md#evidence-map) links each design idea to the repository’s full [primary-source index](docs/references/PRIMARY_SOURCES.md).

Those sources support component practices such as explicit instructions, repository context, layered tests, protected branches, production-like validation, secure development and observable operations. They do **not** prove that this framework as a whole is superior, complete, or production-ready for every project. The repository currently has deterministic self-tests for its linters and portable bundle, plus documentation consistency checks; it does not yet have controlled comparative studies or broad field evidence. See [Validation Status](docs/VALIDATION_STATUS.md).

## The operating model

```text
Operator intent
→ Designer: contract proposal + evidence-constrained advisory
→ Manager: review, freeze, authorize bounded work
→ Executor: preflight, implement, test, commit/PR
→ Manager: inspect exact diff/commit + raw receipts
→ evidence-based closure / merge decision
```

The advisory vocabulary is deliberate:

- `MUST` — frozen/owner constraint or observed invariant;
- `SHOULD` — evidence-backed recommendation, not authority;
- `INVESTIGATE` — fact that must be established before mutation;
- `AVOID` — likely failure pattern or design trap.

For material code work, direct Git access with branch/PR isolation is preferred. The Designer reads an identified ref; the Executor changes a bounded branch; the Manager reviews the real PR head and relevant surrounding source. A [context packet](docs/operator/CONTEXT_PACKET.md) is available when a role lacks direct access, but is not equivalent to direct review for high-risk code.

## Required execution environment

An Executor that can edit code but cannot exercise the real changed path is not ready to close that behavior claim.

```text
LOCAL / HERMETIC
→ EPHEMERAL TEST
→ SHARED TEST
→ STAGING / PRODUCTION-LIKE
→ CONTROLLED PRODUCTION READ / CANARY
→ PRODUCTION MUTATION
```

Use the lowest authorized environment that directly establishes the claim. For non-documentation behavior changes, the normal baseline is `LOCAL_REAL` or `EPHEMERAL_TEST`, with the real affected dependencies when needed. A mock-only pass may close a unit claim; it may not close integration, persistence, migration, user-flow, deployment or production claims.

If an adequate environment is unavailable, report `UNVERIFIED` or `BLOCKED` and request the environment. Do not weaken the receipt while retaining the stronger claim. Environment access is separate from task and mutation authority; none of this grants production access.

## Five-minute workflow

1. Read this page and [Getting Started](docs/GETTING_STARTED.md).
2. Clone/pin this framework beside the target repository, then ask the agent to begin at `docs/agent/START_HERE.md`.
3. Create or map `.agentic/PROJECT_PROFILE.yaml` from [the template](templates/PROJECT_PROFILE.example.yaml). Keep `STRICT_PREVIEW` for first adoption.
4. For material work, have the Designer draft the contract/advisory and the Manager freeze it. Use the copy-ready [Designer](prompts/operator/TASK_DESIGNER.md) and [Manager](prompts/operator/MANAGER_REVIEWER.md) prompts.
5. Let the Executor preflight, implement on an isolated branch, exercise the changed path in an adequate environment, and provide exact receipts. The Manager reviews the actual commit/PR before closure.

Try the worked [end-to-end task](docs/examples/END_TO_END_TASK.md).

## Install/adopt

Recommended layout:

```text
workspace/
├── agentic-flow-framework/   # pin to a reviewed commit/tag for higher assurance
└── my-project/
```

Give the coding agent:

```text
Adopt Agentic Flow for this repository.
Framework source: ../agentic-flow-framework
Read docs/agent/START_HERE.md and ARCHITECTURE.md from the framework.
Inspect the target repository read-only first.
Use STRICT_PREVIEW unless the existing project profile explicitly says otherwise.
Do not treat task approval as mutation or environment authority.
For behavior changes, verify that an authorized environment can exercise the real changed path; mock-only evidence must not close stronger claims.
If work is already active, follow MIDSTREAM_ADOPTION and preserve current edits.
```

Then follow [Getting Started](docs/GETTING_STARTED.md). The generated portable ZIP remains available for offline distribution:

```bash
python3 scripts/build_agent_bundle.py
```

## Safety invariants

- `STRICT_PREVIEW` requires a compact current/proposed-state preview before each bounded mutation batch.
- Frozen task authority, mutation approval and environment access are separate.
- Production mutation always requires explicit authority; this repository does not grant it.
- A claim may be no broader than its current receipt.
- The Executor does not self-certify material closure.
- Missing evidence stays missing; it is not replaced by model confidence or a weaker proxy.
- Task closure does not erase operational gaps.

Canonical policy: [ARCHITECTURE.md](ARCHITECTURE.md). Durable schemas live in [schemas](schemas/), verification routes in [verification](verification/), and production profiles in [production](production/).

## Documentation map

- [Getting Started](docs/GETTING_STARTED.md) — practical adoption path.
- [Why Agentic Flow](docs/WHY_AGENTIC_FLOW.md) — problem, model and concise evidence map.
- [Comparison](docs/COMPARISON.md) — trade-offs against ordinary and policy-only agent use.
- [Validation Status](docs/VALIDATION_STATUS.md) — verified, partially verified and unproven claims.
- [End-to-End Task](docs/examples/END_TO_END_TASK.md) — worked Designer → Manager → Executor flow.
- [Comprehensive Persian Guide](docs/GUIDE.fa.md) — راهنمای مستقل و جامع فارسی.
- [Designer/Manager Setup](docs/operator/DESIGNER_MANAGER_SETUP.md) — direct Git and role setup.
- [Context Packet](docs/operator/CONTEXT_PACKET.md) — bounded alternative when direct access is unavailable.
- [Agent entrypoint](docs/agent/START_HERE.md) — minimal agent-facing adoption route.
- [Primary Sources](docs/references/PRIMARY_SOURCES.md) — full provenance index.

## Repository checks

```bash
python3 -m unittest discover -s scripts -p 'test_*.py'
python3 scripts/test_docs_onboarding.py
python3 scripts/build_agent_bundle.py
```

The checks validate deterministic repository invariants and packaging. They are not evidence that the framework improves real projects; that limitation is intentional and explicit.
