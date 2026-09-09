# Midstream Adoption — Existing Active Coding Session

**Agent-facing document**  
**Version:** 1.0  
**Updated:** 2026-09-09T11:30:00Z

Use when Agentic Flow is introduced after coding has already started. The goal is to adopt governance/evidence/context controls **without discarding, rewriting, or pretending to re-authorize existing work**.

## STOP before new mutation

Do not immediately refactor the current work to match the framework.

First record an adoption snapshot:

```yaml
adoption_snapshot:
  repository_ref: <HEAD>
  branch: <branch>
  dirty_paths: []
  existing_task_or_issue: <ref|NONE>
  observed_goal: <bounded summary>
  work_already_done: []
  tests_already_run: []
  known_failures: []
  current_environment_mutations: []
  existing_agent_instruction_files: []
  unresolved_scope: []
```

Do not claim pre-adoption work was reviewed, authorized, or verified under this framework unless durable evidence actually shows that.

## Reconcile instead of restart

1. Read `ARCHITECTURE.md` and the project’s existing instruction files.
2. Locate/create the project profile without silently changing current runtime requirements.
3. Classify the **remaining** work and the already-changed paths.
4. Create a task/amendment that clearly distinguishes:
   - work observed before adoption;
   - remaining intended work;
   - verification still required;
   - production/operational gaps discovered during adoption.
5. If current edits violate a safety boundary, STOP and request owner/supervisor disposition rather than automatically reverting them.
6. If current edits are compatible, preserve them and continue from the current state after the appropriate review/authorization.

## Verification

Existing green tests are receipts only for the ref/environment where they actually ran. If the framework introduces stronger required claims/receipts, mark the difference `UNVERIFIED` and run the missing checks where authorized; do not rewrite history.

For load-bearing tests created before adoption, use mutation/path proof only when risk/claim importance justifies it.

## Adapter generation

Generate concise vendor adapters only after identifying existing `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, OpenCode rules, hooks, permissions, and task stores. Prefer linking/importing canonical files over duplicating them. Operator documentation must not become always-on agent context.

## Output

Return:
- adoption snapshot ref;
- conflicts between existing rules and framework rules;
- project-profile status/gaps;
- task/amendment needed to continue;
- adapter files changed;
- verification that no existing product work was silently discarded or falsely reclassified.
