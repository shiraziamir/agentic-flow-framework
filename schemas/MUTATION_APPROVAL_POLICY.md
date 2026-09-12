# Mutation Approval Policy

**Schema version:** 1.0  
**Updated:** 2026-09-12

This policy controls whether a coding agent may mutate files, configuration, infrastructure, data, external systems, or runtime state after read-only discovery.

## Modes

```text
STRICT_PREVIEW
MATERIAL_CHANGES_ONLY
BOUNDED_AUTONOMY
```

### STRICT_PREVIEW

Default recommended mode for first adoption, unfamiliar repositories, sensitive projects, or operators who want explicit control.

Every mutation batch requires an explicit operator approval before execution. Read-only discovery does not require approval.

Before requesting approval, the agent must present a compact change preview:

```yaml
change_preview:
  current_state:
    - <what is true now, with file/ref/evidence where useful>
  proposed_state:
    - <what will be true after the change>
  reason:
    - <why this change is needed>
  files_or_resources:
    - <paths/resources expected to change>
  behavior_or_contract_impact:
    - <none or concise impact>
  operational_security_data_impact:
    - <none or concise impact>
  planned_checks:
    - <tests/lints/build/live checks>
  rollback_or_recovery:
    - <how to revert/recover if material>
  scope_boundary:
    - <what will NOT be changed>
```

The agent then waits for a durable or conversational authorization such as:

```text
APPROVE
APPLY
APPROVE THIS BATCH
```

Approval is bounded to the previewed mutation batch. A materially different change requires a new preview and approval.

### MATERIAL_CHANGES_ONLY

The agent may perform trivial/local/reversible edits within the frozen task without a separate approval round. Material changes still require the same preview + explicit approval.

Material normally includes public contracts, architecture boundaries, dependencies, persistence/data, security, CI/CD, infrastructure, production behavior, external providers, secrets/identity, destructive actions, or meaningful scope expansion.

### BOUNDED_AUTONOMY

The agent may mutate only inside a previously approved frozen task and explicit path/resource boundary. It must still STOP and request approval before scope, strategy, risk, environment, authority, or public-contract expansion.

## Read-only discovery

The following normally do not require mutation approval:

- reading repository files and current project state;
- `git status`, diff/log/branch inspection;
- dependency/graph/search queries;
- reading CI/test configuration;
- non-mutating cloud/runtime queries;
- planning, drafting and review.

If a supposedly read-only tool can produce side effects, treat it as mutation-capable.

## Approval is not a substitute for task governance

This policy controls mutation authority. It does not replace:

- DRAFT/REVIEW/FREEZE requirements;
- environment permissions;
- production/destructive authorization;
- security/data controls;
- verification/closure evidence.

A task can therefore require both an approved task contract and a separate mutation approval.

## Batch changes to avoid approval spam

Under `STRICT_PREVIEW`, group tightly related edits into one bounded batch when they share one purpose, one verification plan, and one rollback boundary. Do not ask separately for every line or file unless the operator explicitly requests per-file authorization.

Recommended sequence:

```text
READ / DISCOVER
→ CURRENT STATE
→ PROPOSED STATE
→ CHANGE PREVIEW
→ OPERATOR APPROVAL
→ MUTATE ONLY APPROVED BOUNDARY
→ VERIFY
→ REPORT ACTUAL RESULT / DELTA
```

## Mid-task discovery

If implementation reveals a material difference from the approved preview:

```text
STOP
→ report discovered state
→ explain why the old preview is no longer sufficient
→ present a revised preview
→ obtain new approval
```

Never use an earlier broad approval as unlimited authority for newly discovered work.
