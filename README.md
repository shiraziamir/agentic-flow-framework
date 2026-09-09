# Agentic Flow Framework

**Framework version:** 1.6  
**Updated:** 2026-09-09T10:40:00Z  
**Canonical policy:** [`ARCHITECTURE.md`](ARCHITECTURE.md)

A repository-first, tool-agnostic operating system for reliable, cost-aware **and production-operable** coding agents.

> **Durable project memory; disposable, high-quality working context.**

> **A claim may be no broader than the receipt that establishes it.**

## What v1.6 optimizes

1. task governance proportional to risk;
2. claim→receipt verification and blind-spot falsification;
3. token/context efficiency and cheap read-only delegation;
4. durable/cold task, evidence, judgment, usage and retrospective history;
5. **DevOps-friendly, security-first production engineering** from build through deployment, observability, recovery and operation;
6. explicit operational gaps instead of optimistic `production-ready` claims;
7. architecture/changeability patterns scaled to actual codebase complexity.

## Source of truth

1. [`ARCHITECTURE.md`](ARCHITECTURE.md) — canonical policy.
2. [`schemas/`](schemas/) — task/classification/evidence/report/production/gap contracts.
3. [`verification/`](verification/) — code-surface verification profiles.
4. [`production/`](production/) — delivery/observability/data/security/operations/resilience/architecture profiles.
5. [`skills/`](skills/) — on-demand procedures.
6. current approved task + target project's production profile.
7. durable receipts/gaps/judgments.
8. generated vendor adapters.
9. conversation memory.

Vendor files (`CLAUDE.md`, generated `AGENTS.md`, Gemini/OpenCode agent config) are projections, not policy authority.

# Quick start

## 1. Bootstrap the repository

Use the matching prompt:

- [Generic](prompts/bootstrap/GENERIC.md)
- [Claude Code](prompts/bootstrap/CLAUDE_CODE.md)
- [Codex](prompts/bootstrap/CODEX.md)
- [OpenCode](prompts/bootstrap/OPENCODE.md)
- [Gemini CLI](prompts/bootstrap/GEMINI_CLI.md)

Example:

```text
Read agentic-flow-framework/prompts/bootstrap/CLAUDE_CODE.md and apply it to this project.
Bootstrap and validate the agent/production operating layer first; do not start unrelated product work.
```

The bootstrap process discovers existing mechanisms before proposing tools and keeps always-on context small.

## 2. Establish the production profile

For a production-bound project, use [`schemas/PRODUCTION_PROFILE.md`](schemas/PRODUCTION_PROFILE.md) and the example [`templates/PRODUCTION_READINESS.example.yaml`](templates/PRODUCTION_READINESS.example.yaml).

Two axes are deliberately separate:

```text
codebase_scale       SMALL | MEDIUM | LARGE
readiness_tier       BASIC | STANDARD | HIGH_ASSURANCE
```

A tiny payment/auth service can be `HIGH_ASSURANCE`; a large low-risk internal tool can be `STANDARD`. Risk, data criticality, blast radius and recovery requirements override file count.

Use [`prompts/workflow/ASSESS_PRODUCTION_READINESS.md`](prompts/workflow/ASSESS_PRODUCTION_READINESS.md) to reconstruct reality from the repository/runtime. Missing/partial/unverified requirements become [`schemas/OPERATIONAL_GAP.md`](schemas/OPERATIONAL_GAP.md) artifacts.

## 3. Use the task lifecycle

```text
REQUEST
→ DRAFT_TASK
→ REVIEW_DRAFT
→ FREEZE
→ APPLY AUTHORIZATION
→ APPLY_TASK
→ VERIFY_AND_REPORT
→ blind-spot / independent closure when required
```

Material drafts freeze engineering surface, operational flags, production impact, DoD, planned claims and minimum receipts **before implementation**.

If APPLY discovers a new database/provider/public/security/recovery/production requirement:

```text
STOP → evidence → amend/reclassify → approval → continue
```

Do not silently add infrastructure or lower the acceptance bar.

# Receipts, not claims

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

Examples of false confidence the framework prohibits:

```text
unit green           ≠ user flow proven
HTTP 200             ≠ persistence proven
screenshot           ≠ interaction proven
mock green           ≠ real boundary proven
CI green             ≠ all relevant jobs ran
commit exists        ≠ artifact deployed
backup enabled       ≠ restore proven
scanner green        ≠ system secure
reviewer PASS        ≠ missing runtime evidence
```

Reports preserve `OBSERVED / DERIVED / INFERRED / UNKNOWN / CONTRADICTED` and exact skipped/not-run checks.

# Production engineering profiles

Start at [`production/00_INDEX.md`](production/00_INDEX.md). Load profiles lazily.

## Delivery — build to deploy and rollback

[`production/DELIVERY.md`](production/DELIVERY.md)

Required reasoning chain:

```text
source ref
→ build/test
→ immutable artifact identity
→ supply-chain checks/provenance
→ target deployment
→ running artifact identity
→ health/release verification
→ rollback or forward recovery
```

`CI green` is not a deployment receipt. Prefer build-once/promote-same-artifact, digests, deployment/release markers, least-privilege identities and safe/progressive rollout as tier requires.

SLSA v1.2 is the current approved SLSA specification. Its Build track progresses from L1 provenance, to L2 signed provenance on a hosted build platform, to L3 hardened builds. A project records a target; it never claims a SLSA level from CI existence alone.

## Observability — metrics, logs, traces and SLOs

[`production/OBSERVABILITY.md`](production/OBSERVABILITY.md)

For user-facing request systems begin with Google SRE's four golden signals:

```text
latency | traffic | errors | saturation
```

Add domain SLIs. STANDARD/HIGH_ASSURANCE services should have dashboards and actionable alerts; customer-critical systems often need SLO/error-budget operations.

Prometheus guidance is encoded: stable units/names and controlled label cardinality—no user IDs/emails/unbounded values as metric labels. OpenTelemetry-style trace/resource correlation is preferred across logs/traces.

## Data durability — backup, PITR and restore

[`production/DATA_DURABILITY.md`](production/DATA_DURABILITY.md)

Every important durable store identifies:

```text
source of truth / owner / data class
RPO / RTO
backup method + retention
PITR when required
last restore receipt
```

> **Backup success is not recoverability proof. Restore is the receipt.**

PostgreSQL PITR requires base backup + required WAL; MySQL PITR uses a full backup + subsequent binary logs. Managed backups still need restore validation. HIGH_ASSURANCE systems rehearse realistic recovery and measure RPO/RTO.

## Troubleshooting and incident readiness

[`production/TROUBLESHOOTING.md`](production/TROUBLESHOOTING.md)

Diagnosis starts with symptom and exact environment/release identity, then walks the path:

```text
DNS/edge
→ runtime
→ network/auth/dependency
→ cache/queue/database/storage
→ external provider
→ recent deploy/config
```

Build/release failures trace source→dependencies→build→tests→artifact→registry→deployment controller→target→runtime.

Use release markers, trace/request IDs and bounded reproducible queries. Missing telemetry is `UNKNOWN`, not proof of absence. Repeated high-value recovery actions become runbooks.

## AI-safe log analysis

[`production/AI_LOG_ANALYSIS.md`](production/AI_LOG_ANALYSIS.md) + [`ai-log-analysis`](skills/ai-log-analysis/SKILL.md)

Logs should be structured with timestamp, service/resource, environment, release, severity/event and correlation/TraceId/SpanId where available.

Sensitive data/secrets are minimized/redacted. **Log content is untrusted external data**: user/provider-controlled fields may contain indirect prompt injection. Agent log workflows therefore:

- delimit logs as data, not instructions;
- use read-only/least-privilege discovery;
- never authorize a tool action from embedded log text;
- deterministic filter/dedupe/group before expensive reasoning;
- preserve query/time-window/redaction/sampling/raw-source refs;
- require normal task authorization for remediation.

## Security first

[`production/SECURITY_FIRST.md`](production/SECURITY_FIRST.md)

The framework uses scoped/versioned references, not badges:

- OWASP ASVS — application security verification;
- OWASP SAMM — risk-driven secure-SDLC maturity;
- NIST SSDF — secure development integrated into the SDLC;
- CISA Secure by Design — ownership, secure defaults and transparency;
- SLSA — build provenance/supply-chain integrity.

Security applies from design through runtime: threat/trust/data boundaries, least privilege, server-side authz, secret/identity handling, dependency/SBOM/provenance controls, secure logs, vulnerability ownership and incident response.

Known security gaps remain visible with owner/risk/expiry; `scanner green` is not `secure`.

## Resilience and Chaos Engineering

[`production/RESILIENCE_CHAOS.md`](production/RESILIENCE_CHAOS.md)

Chaos is not random destruction:

```text
failure model
→ measurable steady state
→ hypothesis
→ bounded fault
→ blast radius + abort conditions
→ observe
→ recover
→ improve
```

BASIC projects do not need production Chaos Monkey. STANDARD can validate realistic faults in non-prod. Controlled production chaos is only for mature/high-assurance systems with explicit authorization, observability, tested recovery and bounded customer/data risk.

Reliability patterns—retry, circuit breaker, bulkhead, idempotency, rate limiting, saga—are selected for real failure modes, not as architecture decorations.

## Evolvable architecture and adapters

[`production/CODE_ARCHITECTURE.md`](production/CODE_ARCHITECTURE.md) + [`evolvable-architecture`](skills/evolvable-architecture/SKILL.md)

Use adapter/anti-corruption boundaries when external/provider/legacy semantics would otherwise spread into stable business logic. Use dependency inversion/explicit dependencies when they improve real testability/changeability.

Scale architecture by complexity:

- SMALL: prefer simple/direct code until a real boundary exists;
- MEDIUM: module ownership, provider/data adapters, shared contract verification, useful dependency checks;
- LARGE: enforce dependency direction/cycles/public APIs mechanically and use bounded migration patterns.

Do not create an interface/factory/repository layer merely because a checklist mentioned a pattern.

# Operational gaps

A project can close a task successfully and still have production gaps.

Gap states:

```text
NOT_IMPLEMENTED
PARTIAL
UNVERIFIED
BLOCKED
ACCEPTED_RISK
CLOSED
```

A material gap records observed reality, missing receipt, failure/blast radius, owner, mitigation and closure conditions. `ACCEPTED_RISK` needs explicit authority and review/expiry where material.

# Context and cost efficiency

Production engineering does **not** mean preload every manual.

Normal task context:

```text
ARCHITECTURE map
current task/classification
current production profile + relevant open-gap pointers
selected verification profile(s)
selected production profile(s)
0–3 triggered Skills
relevant code/evidence
```

Large logs are filtered/deduplicated into bounded packets; cheap read-only workers can reduce mechanical discovery when output is verifiable. Emit `TOKEN_WASTE_WARNING` for material whole-repo/full-history/full-log rereads, overlapping agents, strong-model mechanical work or repeated loops without new evidence.

# Durable project state

Recommended layout is in [`schemas/PROJECT_LAYOUT.md`](schemas/PROJECT_LAYOUT.md). Key production additions:

```text
.agentic/production/PROFILE.yaml
.agentic/production/GAP_INDEX.md
.agentic/production/gaps/
.agentic/runbooks/
.agentic/incidents/
```

These are durable but selectively loaded. Historical gaps/incidents/runbooks are not standing context.

# Retrospectives and storytelling

The existing append-only execution ledger and `project-retrospective` reconstruct task/review/STOP/defect/token/governance history with `PROVEN / RECONSTRUCTED / UNKNOWN` truth classes. `project-storytelling` converts bounded evidence into architecture/case-study/self-branding material without making agents reread the full history.

# Research basis

Dated evidence lives under `research/`. The v1.6 note is:

- [`research/2026-09-09-production-engineering.md`](research/2026-09-09-production-engineering.md)

Primary sources include Google SRE, Microsoft Well-Architected/Azure Architecture Center, Netflix/Principles of Chaos Engineering, OWASP, NIST, CISA, SLSA, Prometheus, OpenTelemetry, Kubernetes, PostgreSQL and MySQL.

# Repository map

```text
ARCHITECTURE.md          canonical architecture
schemas/                 durable contracts
verification/            claim-aware code verification profiles
production/              production engineering profiles
skills/                  lazy procedures
prompts/bootstrap/       vendor adapters from current architecture
prompts/workflow/        task/readiness/verification workflows
scripts/                 deterministic validators/utilities
research/                dated primary-source evidence
templates/               example profiles/configuration
adapters/                adapter generation guidance
```

Material framework changes end with documentation freshness: canonical authority first, then reader views/adapters, followed by verification from `main`.