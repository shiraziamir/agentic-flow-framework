# Agentic Flow — Agent Start Here

**Agent-facing entrypoint.**

The portable distribution also contains operator, architecture and source-reference documentation for humans. **Do not preload those files.** Read them only when the current task explicitly needs them.

## 1. Find the framework and project state

1. Confirm the framework root containing `ARCHITECTURE.md` and `VERSION`.
2. Read `ARCHITECTURE.md` first.
3. Inspect repository state before mutation: branch/HEAD, dirty paths, current task/issue, existing agent instructions, build/test commands and any active environment changes.
4. Locate or propose the target project's `.agentic/PROJECT_PROFILE.yaml` using `schemas/PROJECT_PROFILE_CONFIG.md`.
5. Use `verification/00_INDEX.md`, `production/00_INDEX.md`, and `skills/00_INDEX.md` as routers. Load detailed profiles/skills lazily.

## 2. If coding is already in progress

Read:

```text
docs/agent/MIDSTREAM_ADOPTION.md
```

before changing product code. Preserve current valid work and do not fabricate prior framework review or authorization.

## 3. Practical task workflow

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
→ APPLY
→ VERIFY + REPORT
→ independent closure when required
```

Before material APPLY, define observable DoD, planned closure claims, minimum receipt per claim, affected engineering/production surfaces, required test/environment, intentionally omitted checks and STOP conditions.

If APPLY discovers a materially new provider, database, public contract, security/data/recovery boundary, production environment or architecture strategy:

```text
STOP → evidence → amend/reclassify → review/authorize as required → continue
```

## 4. Verification discipline

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

## 5. Production-bound work

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

## 6. Environment policy

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

## 7. Token/context efficiency

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

Acceptance quality must not be lowered merely to save tokens.

## 8. Agent vs operator/reference files

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

These are present in the distribution but **cold by default**:

```text
docs/operator/
docs/architecture/
docs/references/
PRIMARY_SOURCES.md
BEST_PRACTICES_USED.en.txt
```

Do not read all of them simply because they exist in the ZIP.

## 9. Vendor adapter

Inspect existing `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, OpenCode configuration or equivalent before generating anything. Use the matching `prompts/bootstrap/*` file and create/update only the minimum adapter required by the current harness.

Preserve valid project-specific rules. Report conflicts instead of silently overwriting them.

## 10. Adoption completion

Before product work begins/resumes, a fresh agent session should be able to discover without loading the whole framework:

- source of truth and framework version;
- current task/project profile/open gaps/overrides;
- build/test/deploy/rollback entrypoints or explicit gaps;
- verification and production routers;
- the DRAFT/REVIEW/APPLY/VERIFY workflow;
- the relevant environment authority;
- the token/context-efficiency path.

Return a concise adoption receipt and unresolved conflicts. Do not store chain-of-thought or raw transcripts as project state.
