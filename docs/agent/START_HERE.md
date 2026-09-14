# Agentic Flow — Agent Start Here

**Agent-facing entrypoint.**

The framework may be available as a cloned repository, sibling directory, or portable `.agentic-flow/` distribution. Do **not** preload the whole framework. Read only the layers triggered by the current project/task.

## 1. Find framework and project state

1. Confirm the framework root containing `ARCHITECTURE.md` and `VERSION`.
2. Read `ARCHITECTURE.md` first.
3. Inspect the target repository read-only: branch/HEAD, dirty paths, current project/task, existing agent instructions, build/test commands and active environment changes.
4. Locate or propose `.agentic/PROJECT_PROFILE.yaml` using `schemas/PROJECT_PROFILE_CONFIG.md`.
5. Determine `project_mode.mode`: `VIBE_PROTOTYPE | PRODUCT_BUILD | MAINTENANCE`.
6. Determine `operating_preset`: `VIBE_FAST | PRODUCT_STANDARD | HIGH_ASSURANCE`. If absent, prefer `PRODUCT_STANDARD` for maintainable product work and use explicit overrides only when justified.
7. Determine `agent_mutation_policy`; if absent during first adoption, use `STRICT_PREVIEW` as the safe default.
8. Use verification/production/skills indexes as routers and load details lazily.

## 2. New / greenfield / unclear architecture

If the repository is new, the architecture baseline is missing/untrusted, or the operator mostly knows the desired product outcome rather than the technical shape, read:

```text
docs/agent/PROJECT_INCEPTION_ARCHITECTURE.md
```

Do **not** start serious product coding directly from the idea.

Normal inception:

```text
PRODUCT INTENT
→ PRODUCT BRIEF
→ QUALITY / EVAL CONTRACT
→ ARCHITECTURE DISCOVERY
→ SYSTEM TRUTH / DATA AUTHORITY MAP
→ CURRENT SCALE BOUNDARY
→ MINIMAL OPTIONS
→ LOAD-BEARING DECISIONS
→ WALKING SKELETON
→ ARCHITECTURE CHECKPOINT
→ PROJECT BASELINE
→ NORMAL TASK FLOW
```

When required, materialize the project map at:

```text
.agentic/SYSTEM_TRUTH_MAP.yaml
```

using `templates/SYSTEM_TRUTH_MAP.example.yaml` and `schemas/SYSTEM_TRUTH_MAP.md`.

If `project_mode.mode: VIBE_PROTOTYPE`, optimize for learning speed but preserve:

```text
VIBE_PROTOTYPE != PRODUCTION BASELINE
```

Prototype code is provisional/sacrificial by default and may not silently inherit production readiness. Promotion to `PRODUCT_BUILD` requires re-baselining and explicit reuse/rewrite/discard decisions.

## 3. Swamp Guard

At material checkpoints, before major architecture/tooling expansion, after repeated remediation, and before Vibe→Product or staging/production promotion, evaluate:

```text
CLEAR | WATCH | ALERT | STOP_REBASELINE
```

Watch for architecture churn, unjustified frameworks/datastores/abstractions, competing mechanisms, AI/RAG tuning before eval baseline, feature growth before a critical vertical slice, chat-only architecture decisions, ambiguous state ownership, prototype-to-production drift, side-task attention drift, unresolved System-Lens risks and complexity growing faster than demonstrated value.

For severe cases return:

```text
SWAMP ALERT: STOP_REBASELINE
Signal: ...
Evidence: ...
Why it matters: ...
Recommended action: ...
Continue allowed: NO
Authority needed: Manager|Operator
```

Do not hide a swamp signal to preserve momentum.

## 4. Mutation approval

Read `schemas/MUTATION_APPROVAL_POLICY.md`.

Under `STRICT_PREVIEW`, read-only discovery needs no separate approval. Before a bounded mutation batch report:

```text
CURRENT STATE
PROPOSED STATE
WHY
WILL CHANGE
IMPACT
VERIFY
ROLLBACK / RECOVERY when material
OUT OF SCOPE
```

Then wait for explicit `APPROVE` / `APPLY`.

Group tightly related edits. Approval is limited to the previewed boundary. Materially new files/resources, behavior, risk, environment, architecture strategy, dependency, public contract, security/data boundary or scope trigger STOP + revised preview.

Mutation approval does not replace task/environment/external-effect/production authority.

## 5. If coding is already in progress

Read `docs/agent/MIDSTREAM_ADOPTION.md` before changing product code. Preserve current valid work and do not fabricate prior framework review or authorization. Existing dirty edits are observed current state, not newly approved work.

## 6. Normal material-task workflow

Once a coherent project baseline exists, read:

```text
docs/agent/TASK_WORKFLOW_DRAFT_REVIEW_APPLY_VERIFY.md
```

Normal flow:

```text
REQUEST
→ establish PRIMARY/SIDE/INTERRUPT focus
→ DRAFT / classify risk
→ required review/authorization
→ APPLY
→ Local Lens + risk-adaptive System Lens
→ VERIFY + REPORT
→ independent closure when required
```

Before material APPLY, define observable DoD, planned closure claims, minimum receipts, affected surfaces, required environment, intentionally omitted checks and STOP conditions.

If implementation reveals a materially new provider, database, public contract, security/data/recovery boundary, production environment or architecture strategy:

```text
STOP → evidence → amend/reclassify → revised preview → authorize → continue
```

If discovery indicates architecture failure rather than local task scope, use the Swamp Guard and return to Project Inception/Architecture Discovery instead of stacking local patches.

## 7. Dual-Lens rule without checklist theater

```text
LOCAL LENS  = does the changed behavior work correctly?
SYSTEM LENS = what system truth may have changed?
```

Use risk-adaptive depth:

- `LOW` + genuinely local: concise System-Lens impact summary; do not mechanically fill 13 rows.
- `MEDIUM/HIGH`: record relevant System-Lens dimensions explicitly.
- any change touching money, privacy, identity, tenant isolation, durability/recovery, destructive state or production semantics: record the affected dimensions regardless of nominal risk.

`UNAFFECTED` is a reviewed conclusion, not a default filler. `OPEN_RISK` remains visible.

## 8. Verification discipline

A claim may not be stronger than its current receipt.

```text
unit green           != user flow proven
HTTP 200             != persistence proven
CI green             != deployed artifact proven
backup configured    != restore proven
reviewer PASS        != missing runtime evidence
multi-model PASS     != independent behavioral evidence
```

Report exact `PASS / FAIL / PARTIAL / SKIPPED / UNVERIFIED` states and preserve `OBSERVED / DERIVED / INFERRED / UNKNOWN / CONTRADICTED` truth boundaries.

For AI/RAG/search systems, do not treat demo quality as evaluation. A representative eval/quality contract is required before serious tuning or claims of improvement.

## 9. Environment policy

Use the lowest environment that directly establishes the required claim:

```text
LOCAL / HERMETIC
→ LOCAL_REAL
→ EPHEMERAL TEST
→ SHARED TEST
→ STAGING / PRODUCTION-LIKE
→ CONTROLLED PRODUCTION READ / CANARY
→ PRODUCTION MUTATION
```

Mock-only evidence may close unit/model claims, not integration, persistence, migration, user-flow, deployment or production claims. If no adequate environment exists, keep the stronger claim `UNVERIFIED` or `BLOCKED`.

## 10. Cross-system audit

Audit triggers are prioritized as:

```text
EVENT
> RISK / AUTHORITY CHANGE
> TASK-COUNT REMINDER
```

Real-customer release, material incident, or material security/data/authority/recovery change can trigger audit immediately. A configured `5–8 material tasks` cadence is only a reminder, not a reason to delay a needed audit or perform a pointless one.

## 11. Production-bound work

Production mutation is separate authority. Every production mutation requires rollback or explicit forward-recovery readiness before execution. A Judge/Reviewer PASS does not grant production authority.

Missing operational requirements remain explicit:

```text
NOT_IMPLEMENTED
PARTIAL
UNVERIFIED
BLOCKED
ACCEPTED_RISK
CLOSED
```

## 12. Context / quota efficiency

For long or log-heavy work, read `docs/agent/TOKEN_EFFICIENT_WORKFLOW.md`.

Default behavior:

- deterministic checks before rediscovery;
- small affected working set;
- bounded logs instead of raw dumps;
- compact evidence handoffs instead of transcripts;
- stronger model reasoning only where ambiguity/risk justifies it;
- checkpoint durable state before session reset.

Acceptance quality must not be lowered to save tokens/quota.

## 13. Agent vs cold documentation

Normal coding-agent context may use:

```text
docs/agent/
ARCHITECTURE.md
selected schemas/
selected verification/
selected production/
selected skills/
current project/task/evidence files
```

Operator/reference/research/history files are cold by default. They may exist in a portable bundle for humans without belonging in default agent context.

## 14. Adoption completion

Before product work begins/resumes, return a concise adoption receipt containing:

- framework version/ref;
- target repository branch/HEAD/dirty paths;
- project mode + operating preset;
- whether architecture/System Truth baseline is trusted;
- Swamp Guard state;
- current primary/active task and open gaps/overrides;
- mutation/environment/external-effect authority;
- build/test/deploy/rollback entrypoints or gaps;
- unresolved conflicts.

For greenfield/unclear projects, successful adoption does **not** mean start coding; route through Project Inception first. Under `STRICT_PREVIEW`, do not perform the first product mutation until the required preview/approval exists.

Do not store chain-of-thought or raw transcripts as project state.
