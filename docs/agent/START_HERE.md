# Agentic Flow — Agent Start Here

**Agent-facing entrypoint.**

The framework may be available as a cloned repository, a sibling directory, or a portable `.agentic-flow/` distribution. Operator, architecture and source-reference documentation may be present, but **do not preload those files**. Read them only when the current task explicitly needs them.

## 1. Find the framework and project state

1. Confirm the framework root containing `ARCHITECTURE.md` and `VERSION`.
2. Read `ARCHITECTURE.md` first.
3. Inspect the target repository read-only before mutation: branch/HEAD, dirty paths, current task/issue, existing agent instructions, build/test commands and any active environment changes.
4. Locate or propose the target project's `.agentic/PROJECT_PROFILE.yaml` using `schemas/PROJECT_PROFILE_CONFIG.md`.
5. Determine the project's `agent_mutation_policy`. If none is defined during first adoption, use `STRICT_PREVIEW` as the safe default and ask the operator to persist/override it.
6. Check `usage_reporting`. If quota snapshots are enabled/optional and the current harness exposes trustworthy telemetry, route to `docs/agent/USAGE_AWARE_TASK_REPORTING.md`.
7. Use `verification/00_INDEX.md`, `production/00_INDEX.md`, and `skills/00_INDEX.md` as routers. Load detailed profiles/skills lazily.

If the framework is a sibling clone such as `../agentic-flow-framework`, framework paths are resolved from that root; project-owned `.agentic/` state stays in the target project.

## 2. Mutation approval

Read:

```text
schemas/MUTATION_APPROVAL_POLICY.md
```

Under `STRICT_PREVIEW`, read-only discovery does not need separate approval. Before every bounded mutation batch, report:

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

Then **STOP and wait for explicit `APPROVE` / `APPLY`** before mutating files, configuration, infrastructure, data, external systems or runtime state.

Group tightly related edits into one bounded batch. Do not ask permission line-by-line unless the operator explicitly requests per-file approval.

Approval is limited to the previewed batch. If implementation discovers a materially different file/resource, behavior, risk, environment, architecture strategy, dependency, public contract, security/data boundary or scope, STOP and present a revised preview before continuing.

Mutation approval does not replace task authorization or environment authority. An approved source edit is not permission to mutate production.

## 3. If coding is already in progress

Read:

```text
docs/agent/MIDSTREAM_ADOPTION.md
```

before changing product code. Preserve current valid work and do not fabricate prior framework review or authorization. Treat existing dirty edits as observed current state, not as newly approved framework work.

## 4. Practical task workflow

For a material task, read:

```text
docs/agent/TASK_WORKFLOW_DRAFT_REVIEW_APPLY_VERIFY.md
```

Normal flow:

```text
REQUEST
→ DRAFT
→ REVIEW
→ FREEZE / APPLY AUTHORIZATION when required
→ CHANGE PREVIEW / MUTATION APPROVAL when policy requires
→ APPLY
→ VERIFY + REPORT
→ independent closure when required
```

Before material APPLY, define observable DoD, planned closure claims, minimum receipt per claim, affected engineering/production surfaces, required test/environment, intentionally omitted checks and STOP conditions.

If APPLY discovers a materially new provider, database, public contract, security/data/recovery boundary, production environment or architecture strategy:

```text
STOP → evidence → amend/reclassify → revised change preview → review/authorize as required → continue
```

## 5. Verification discipline

A claim may not be stronger than its current receipt.

```text
unit green           != user flow proven
HTTP 200             != persistence proven
CI green             != deployed artifact proven
backup configured    != restore proven
scanner green        != secure
reviewer PASS        != missing runtime evidence
```

Report exact `PASS / FAIL / PARTIAL / SKIPPED / UNVERIFIED` states and preserve `OBSERVED / DERIVED / INFERRED / UNKNOWN / CONTRADICTED` truth boundaries.

When live/integration evidence depends on a runtime/environment, use `schemas/EVIDENCE_RECOVERY.md` to qualify the measuring environment and preserve stale/wrong-runtime evidence honestly.

## 6. Production-bound work

A task may close while the project still has operational gaps. Consult only the current project/production profile and triggered production profiles.

Missing requirements remain explicit:

```text
NOT_IMPLEMENTED
PARTIAL
UNVERIFIED
BLOCKED
ACCEPTED_RISK
CLOSED
```

Do not infer production readiness from configuration presence alone.

## 7. Environment policy

Use the lowest environment that can directly establish the required claim:

```text
LOCAL / HERMETIC
→ EPHEMERAL TEST
→ SHARED TEST
→ STAGING / PRODUCTION-LIKE
→ CONTROLLED PRODUCTION READ / CANARY
→ PRODUCTION MUTATION
```

A request for stronger access is not authorization. Production mutation follows the project's explicit authority path.

## 8. Token/context and quota efficiency

For long, multi-agent, repository-wide or log-heavy work, read:

```text
docs/agent/TOKEN_EFFICIENT_WORKFLOW.md
```

Default behavior:

- deterministic checks before model rediscovery;
- small affected working set;
- bounded log packets instead of raw dumps;
- cheap/read-only workers for mechanically checkable discovery when useful;
- compact evidence handoffs instead of transcripts;
- stronger model judgment only for ambiguity, architecture, security, diagnosis or closure risk.

`STRICT_PREVIEW` should batch related mutations so approval discipline does not become token/interaction spam.

If quota reporting is enabled, append one compact snapshot after each material task/checkpoint. For Claude Code use `scripts/claude_usage_snapshot.py` and `schemas/USAGE_QUOTA_SNAPSHOT.md`. Report both **used** and **remaining**, plus source/freshness. Missing telemetry stays unavailable.

Acceptance quality must not be lowered merely to save tokens or quota.

## 9. Agent vs operator/reference files

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

These are cold by default:

```text
docs/operator/
docs/architecture/
docs/references/
PRIMARY_SOURCES.md
BEST_PRACTICES_USED.en.txt
```

Do not read all of them simply because they exist.

## 10. Vendor adapter

Inspect existing `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, OpenCode configuration or equivalent before generating anything. Use the matching `prompts/bootstrap/*` file and create/update only the minimum adapter required by the current harness.

Preserve valid project-specific rules. Report conflicts instead of silently overwriting them.

## 11. Adoption completion

Before product work begins/resumes, return a concise read-only adoption receipt containing:

- framework version/ref and location;
- source of truth;
- target project branch/HEAD/dirty paths;
- current task/project profile/open gaps/overrides;
- mutation approval mode;
- usage-reporting policy and whether current harness telemetry is available;
- build/test/deploy/rollback entrypoints or explicit gaps;
- verification and production routers;
- relevant environment authority;
- unresolved conflicts.

Do not perform the first product mutation merely because adoption succeeded. Under `STRICT_PREVIEW`, present the first change preview and wait for explicit approval.

Do not store chain-of-thought or raw transcripts as project state.
