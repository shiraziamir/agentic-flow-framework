# Agentic Flow Framework

**Framework version:** 1.5  
**Updated:** 2026-09-09T10:04:00Z  
**Canonical policy:** [`ARCHITECTURE.md`](ARCHITECTURE.md)

A repository-first, tool-agnostic operating system for reliable, cost-aware coding agents.

> **Durable project memory; disposable, high-quality working context.**

This GitHub repository is the authoritative home of the framework. The old Google Drive folder is an archived snapshot only.

## What v1.5 adds

The framework already had risk-adaptive task governance, token/cost visibility, cold project history and independent closure. v1.5 closes a major verification gap: **a report may not make a claim stronger than the current receipt that directly establishes it.**

Version 1.5 adds:

1. **engineering-surface classification** — FRONTEND / BACKEND / SHARED / DATA / INFRA / CI_CD / TOOLING / DOCS_EVIDENCE plus cross-cutting security, persistence, contract, cache, reliability and production flags;
2. **claim → receipt strength contracts** — static source, build, unit test, browser flow, persistence, deployment and security claims are no longer interchangeable;
3. **reality-reflecting reports** — OBSERVED / DERIVED / INFERRED / UNKNOWN / CONTRADICTED, exact counts, skipped/not-run checks and residual risk;
4. **formal draft review before APPLY** — review the verification design before implementation starts;
5. **surface-specific verification profiles** — frontend, backend, shared/API, data, infra/CI, security and reliability blind spots;
6. **blind-spot audit** — falsification-first closure challenge for high/evidence-complex work;
7. **deterministic verification linting** for structured task/evidence/report artifacts.

## Source of truth

Read/order of authority:

1. [`ARCHITECTURE.md`](ARCHITECTURE.md) — **canonical policy, authority and lifecycle**.
2. [`schemas/`](schemas/) — task, change classification, claim/evidence/report, supervisor, usage and history contracts.
3. [`verification/`](verification/00_INDEX.md) — verification profiles selected by engineering surface/risk.
4. [`skills/`](skills/00_INDEX.md) — reusable on-demand procedures.
5. Current approved/frozen task or amendment.
6. Durable evidence and supervisor decisions.
7. Generated vendor adapters.
8. Conversation memory.

**Vendor files are not policy authority.** `CLAUDE.md`, Gemini/OpenCode configuration, subagents and generated instruction files are projections of canonical policy and should identify the architecture version they were generated from.

## Quick start

### 1. Bootstrap the target project

Make this repository available beside/inside the target project, then use the matching bootstrap prompt:

- [Generic](prompts/bootstrap/GENERIC.md)
- [Claude Code](prompts/bootstrap/CLAUDE_CODE.md)
- [Codex](prompts/bootstrap/CODEX.md)
- [OpenCode](prompts/bootstrap/OPENCODE.md)
- [Gemini CLI](prompts/bootstrap/GEMINI_CLI.md)

Example:

```text
Read agentic-flow-framework/prompts/bootstrap/CLAUDE_CODE.md and apply it to this project.
Do not execute product work yet; only bootstrap and validate the agent operating layer.
```

Keep the generated adapter short. Do not copy the framework or historical task trail into permanent context.

### 2. Classify governance and engineering surface

Governance controls ceremony/authority:

| Level | Use for | Lifecycle |
|---|---|---|
| `HIGH` | architecture, persistence, production/security/trust, durable data, major public contracts | draft → review → freeze → separate apply → verify/evidence → blind-spot/independent closure |
| `MEDIUM` | bounded same-task correction | owner-approved amendment → bounded apply → verification/evidence → independent closure when material |
| `EVIDENCE_ONLY` | docs/evidence/test-contract correction with no new runtime authority | durable approved amendment + hash/ref; no separate freeze/apply unless mutation follows |

Surface classification controls **how to verify** the work. See [`schemas/CHANGE_CLASSIFICATION.md`](schemas/CHANGE_CLASSIFICATION.md):

```text
FRONTEND
BACKEND
SHARED
DATA
INFRA
CI_CD
TOOLING
DOCS_EVIDENCE
```

Then add cross-cutting flags such as:

```text
AUTH_SECURITY
PUBLIC_CONTRACT
PERSISTENCE
CONCURRENCY
CACHE_STATE
EXTERNAL_PROVIDER
PERFORMANCE
MIGRATION
OBSERVABILITY
PRODUCTION
```

Verification selection is:

```text
GENERAL
+ primary surface profile
+ only triggered cross-cutting annexes
```

See [`verification/00_INDEX.md`](verification/00_INDEX.md).

### 3. Draft before implementation

Use:

- [`prompts/workflow/DRAFT_TASK.md`](prompts/workflow/DRAFT_TASK.md)
- [`schemas/TASK_CONTRACT.md`](schemas/TASK_CONTRACT.md)
- [`schemas/CHANGE_CLASSIFICATION.md`](schemas/CHANGE_CLASSIFICATION.md)
- [`schemas/CLAIM_RECEIPT.md`](schemas/CLAIM_RECEIPT.md)

A material draft contains not only scope/DoD but also:

- engineering surface and affected consumers;
- planned closure claims;
- minimum receipt required for every material claim;
- selected verification profiles;
- important checks intentionally outside scope;
- STOP/reclassification/escalation conditions.

### 4. Review the DRAFT before APPLY

Use [`prompts/workflow/REVIEW_DRAFT.md`](prompts/workflow/REVIEW_DRAFT.md).

The draft reviewer challenges the verification design:

```text
Is FRONTEND/BACKEND/SHARED/DATA/etc. classification correct?
Are affected consumers missing?
Can the planned checks really establish the planned claims?
Are error/auth/persistence/live paths missing?
Is a weaker proxy being substituted for an acceptance gate?
Are global claims too broad for the planned evidence?
```

Allowed dispositions:

```text
ACCEPT_DRAFT
AMEND_DRAFT
NEEDS_EVIDENCE
REJECT_DRAFT
```

`ACCEPT_DRAFT` freezes the reviewed task; it does not automatically authorize APPLY unless governance explicitly combines the gates.

### 5. APPLY the frozen task

Use [`prompts/workflow/APPLY_TASK.md`](prompts/workflow/APPLY_TASK.md).

If implementation discovers a new material surface/consumer or security/persistence/public-contract/production risk, **STOP and amend**. Do not silently widen scope or verification.

Collect receipts during work and bind them to the exact repository ref, build/artifact and environment they describe.

### 6. Verify and report reality

Use [`prompts/workflow/VERIFY_AND_REPORT.md`](prompts/workflow/VERIFY_AND_REPORT.md), [`schemas/EVIDENCE_PACKET.md`](schemas/EVIDENCE_PACKET.md) and [`schemas/STATUS_REPORT.md`](schemas/STATUS_REPORT.md).

The central rule is in [`schemas/CLAIM_RECEIPT.md`](schemas/CLAIM_RECEIPT.md):

> A claim may be no broader than the identified, current receipt that directly establishes it.

Verification ladder:

```text
IDENTITY
→ STATIC
→ BUILD
→ FOCUSED_TEST
→ PATH_PROOF
→ INTEGRATION_CONTRACT
→ LIVE_BEHAVIOR
→ DEPLOYED_ARTIFACT
→ EXHAUSTIVE_BOUNDED_NEGATIVE
→ JUDGMENT
```

Examples:

```text
source/config exists        != runtime behavior
unit test passes            != frontend user flow works
HTTP 200                    != data persisted
screenshot                  != interaction works
mock success                != real API compatibility
CI green                    != every relevant job/test executed
commit exists               != that artifact is deployed
reviewer says PASS          != missing behavioral evidence appeared
```

### 7. Use bounded truth language in reports

Material status uses:

```text
OBSERVED
DERIVED
INFERRED
UNKNOWN
CONTRADICTED
```

and verification states such as:

```text
VERIFIED
PARTIAL
UNVERIFIED
CONTRADICTED
```

Report exact counts and important checks not executed.

Prefer:

```text
128/128 frozen tests passed at commit abc123.
Frontend browser flows login + checkout passed in testenv X.
The production deployment was not checked.
Security was not exhaustively assessed.
```

not:

```text
Everything is good. No regressions. Production ready.
```

Global/negative language (`all`, `none`, `only`, `no regressions`, `secure`, `fully tested`) requires a finite named universe plus exhaustive method.

### 8. Independent closure

#### Direct repository/tool access — preferred

Use [`prompts/supervisor/DIRECT_ACCESS.md`](prompts/supervisor/DIRECT_ACCESS.md).

To reduce anchoring, the reviewer should prefer this order:

```text
frozen task/DoD/classification
→ actual diff/source
→ raw receipts/checks
→ independent falsifying checks
→ executor narrative last
```

For HIGH/evidence-complex work load [`blind-spot-audit`](skills/blind-spot-audit/SKILL.md).

#### Evidence-only supervisor

Use [`prompts/supervisor/EVIDENCE_ONLY.md`](prompts/supervisor/EVIDENCE_ONLY.md). Missing access never becomes approval. The reviewer distinguishes:

```text
VERIFIED_FROM_PACKET
PARTIAL_FROM_PACKET
UNVERIFIED_FROM_PACKET
CONTRADICTED_BY_PACKET
```

A human/model supervisor produces a `JUDGMENT` receipt. Judgment does not replace missing runtime/persistence/deployment/security evidence.

## Verification profiles

### FRONTEND

[`verification/FRONTEND.md`](verification/FRONTEND.md) focuses on user-visible browser behavior, actual interaction paths, console/network errors, loading/error/empty/permission states and real frontend API-client compatibility. A screenshot proves a state, not a working flow.

### BACKEND

[`verification/BACKEND.md`](verification/BACKEND.md) covers handler/service/repository integration, validation, authz/tenant boundaries, error mapping, timeouts/retries/idempotency, persistence and operational behavior. `200 OK` is not a persistence receipt.

### SHARED / contracts

[`verification/SHARED.md`](verification/SHARED.md) requires affected-consumer verification. Producer tests alone do not prove consumer compatibility; type compatibility alone does not prove runtime serialization/protocol behavior.

### DATA

[`verification/DATA.md`](verification/DATA.md) covers representative existing data, migrations, durable write/read, constraints, transactions, idempotency and rollback/restore boundaries. A migration that works only on a new empty DB is weak evidence for existing production-shaped data.

### INFRA / CI_CD

[`verification/INFRA_CI.md`](verification/INFRA_CI.md) tracks target environment, plan/rendered diff, pipeline triggers/conditions, permissions, artifact handoff, exact deployed artifact and real-run receipts when the claim requires them. Green CI may contain skipped/neutral checks.

### SECURITY / AUTH

[`verification/SECURITY_AUTH.md`](verification/SECURITY_AUTH.md) requires relevant negative/unauthorized/tenant/ownership checks and a bounded standards scope when claims use OWASP ASVS or another standard.

### RELIABILITY / PERFORMANCE

[`verification/RELIABILITY_PERFORMANCE.md`](verification/RELIABILITY_PERFORMANCE.md) covers comparable baselines, repeated measurements, cache/warm state, retries/timeouts, concurrency, providers, logs/metrics/traces and validity boundaries.

## Deterministic verification lint

For JSON artifacts (or YAML when PyYAML is installed):

```bash
python3 scripts/verification_lint.py .agentic/tasks/active/TASK-123.json
python3 scripts/verification_lint.py .agentic/evidence/TASK-123.evidence.json
python3 scripts/verification_lint.py --strict .agentic/evidence/TASK-123.evidence.json
```

It catches mechanical contradictions such as:

- VERIFIED claim without evidence refs;
- missing evidence IDs;
- receipt weaker than frozen minimum;
- behavioral evidence tied to a different `head_ref`;
- DoD PASS without evidence;
- UNKNOWN + VERIFIED contradiction;
- verified global/negative claim without exhaustive-bounded-negative receipt.

It cannot decide semantic sufficiency; that remains the job of project tests, verification profiles and independent judgment.

## Token/context efficiency

For long, expensive or multi-agent work load [`token-efficiency`](skills/token-efficiency/SKILL.md).

```text
mechanical/deterministic tools
→ bounded affected/dependency graph
→ cheap read-only discovery/partitions when checkable
→ compact evidence handoff
→ standard executor
→ stronger judgment only on escalation
```

Never weaken DoD/receipt requirements/security to save tokens.

The agent should emit `TOKEN_WASTE_WARNING` for material unjustified patterns such as whole-repo scans, repeated large-file rereads, full-history loading, huge raw logs, expensive models doing mechanical work, overlapping subagents, repeated failed loops without new discriminating evidence, or budget overrun.

### Usage ledger

When counters are observable:

```bash
python3 scripts/usage_ledger.py record \
  --task-id TASK-123 \
  --phase EXECUTION \
  --role EXECUTION_TIER \
  --provider anthropic \
  --model '<observable-model>' \
  --source API_USAGE \
  --input-tokens 12000 \
  --output-tokens 1800

python3 scripts/usage_ledger.py report --task-id TASK-123
```

Missing telemetry is **unknown, not zero**.

## Large frontend / monorepo workflow

Do not feed a bigger model the whole repository just because context exists.

```text
mechanical dependency/affected graph
→ EDIT/REFERENCE/EXCLUDED/CHECK sets
→ cheap read-only discovery child
→ compact handoff
→ bounded implementation
→ surface-aware affected verification
→ stronger judgment only on escalation
```

Use `context-curation`, `change-classification`, `surface-verification`, `model-routing` and `token-efficiency` only when their triggers fire.

## Durable project state without history pollution

Recommended layout: [`schemas/PROJECT_LAYOUT.md`](schemas/PROJECT_LAYOUT.md).

Normal execution reads **hot state** only: current task/amendment/classification/checkpoint/index and directly relevant docs/skills/verification profiles. Completed tasks, judgments, evidence, usage, execution ledger, retrospectives and stories are cold history.

## Formal retrospective and storytelling

For long campaigns/rescues/migrations:

- ledger schema: [`schemas/EXECUTION_RETROSPECTIVE_LEDGER.md`](schemas/EXECUTION_RETROSPECTIVE_LEDGER.md)
- audit reconstruction: [`skills/project-retrospective/SKILL.md`](skills/project-retrospective/SKILL.md)
- prompt: [`prompts/workflow/BUILD_PROJECT_RETROSPECTIVE.md`](prompts/workflow/BUILD_PROJECT_RETROSPECTIVE.md)

Historical truth classes remain:

```text
PROVEN FROM GIT / DURABLE ARTIFACTS
RECONSTRUCTED FROM OWNER JOURNAL / RECEIPTS
UNKNOWN / NOT LOGGED RELIABLY
```

`project-storytelling` is separate and may consume the bounded retrospective to build architecture narrative, lessons learned, case studies and self-branding without reloading all raw history.

## Documentation freshness

Canonical/index/retrospective/story documents carry version and update timestamp. Material verified changes use [`documentation-freshness`](skills/documentation-freshness/SKILL.md): update authoritative source first, then synchronize reader views and generated adapters.

## Repository map

```text
ARCHITECTURE.md          canonical policy/source of truth
schemas/                 task/classification/claim/evidence/report/usage/history contracts
verification/            lazy surface-specific verification profiles/annexes
skills/                  portable on-demand procedures
prompts/bootstrap/       generate vendor adapters from latest architecture
prompts/workflow/        draft/review/apply/verify/evidence/history workflows
prompts/supervisor/      independent closure prompts
scripts/                 deterministic control-plane utilities
research/                dated primary-source research, not policy
templates/               optional examples
adapters/                adapter-generation guidance
```

## Research basis

Current dated notes:

- [`research/2026-09-09-context-model-routing.md`](research/2026-09-09-context-model-routing.md)
- [`research/2026-09-09-bootstrap-supervision.md`](research/2026-09-09-bootstrap-supervision.md)
- [`research/2026-09-09-adaptive-governance-token-efficiency.md`](research/2026-09-09-adaptive-governance-token-efficiency.md)
- [`research/2026-09-09-execution-retrospective.md`](research/2026-09-09-execution-retrospective.md)
- [`research/2026-09-09-verification-blind-spots.md`](research/2026-09-09-verification-blind-spots.md)

Primary sources used in v1.5 include OpenAI Harness Engineering and Codex safety deployment notes, Anthropic eval/outcome/Skill lifecycle docs, Playwright frontend testing guidance, Pact contract-testing guidance, OWASP ASVS, GitHub protected-branch semantics and TypeScript project-reference documentation.

Prefer primary/current sources. Product-specific model names/defaults/pricing/CLI behavior must be rechecked when they materially affect a decision.
