# Bootstrap prompt — generic coding agent

**Version:** 1.7  
**Updated:** 2026-09-09T11:30:00Z

Use after cloning the framework or extracting the Agent Bundle into a target repository.

```text
Adopt Agentic Flow as this repository's agent operating/control layer. Do not start unrelated product work during bootstrap.

1. Read `docs/agent/START_HERE.md`, then canonical `ARCHITECTURE.md` and `VERSION`.
2. Determine adoption mode:
   - NEW/IDLE;
   - EXISTING MATURE;
   - MIDSTREAM ACTIVE CODING.
3. If any product work is already active/dirty, read `docs/agent/MIDSTREAM_ADOPTION.md` and capture the adoption snapshot before further mutation. Preserve existing valid edits; do not retroactively claim framework review/authorization.
4. Inspect existing agent instructions, build/lint/test/deploy commands, repository/dependency graph, current branch/task, runtime environments, data stores, CI/CD, observability, security, task/history stores and provider/harness capabilities.
5. Reuse existing mechanisms that already satisfy framework semantics. Do not create shadow CI, task stores, observability or policy files merely to match example filenames.
6. Locate or propose `.agentic/PROJECT_PROFILE.yaml` using `schemas/PROJECT_PROFILE_CONFIG.md` and `templates/PROJECT_PROFILE.example.yaml`. Derive it from real project evidence; missing controls are gaps, not PASS.
7. Read router files only:
   - `verification/00_INDEX.md`;
   - `production/00_INDEX.md`;
   - `skills/00_INDEX.md`.
   Load detailed profiles/Skills lazily only when triggered.
8. Generate/update the minimum vendor/harness adapter needed here. It must point to canonical sources, current project profile and task workflow; it must not copy the whole framework into permanent context.
9. Preserve HIGH/MEDIUM/EVIDENCE_ONLY governance and material lifecycle:
   DRAFT_TASK -> REVIEW_DRAFT -> required freeze/authorization -> APPLY_TASK -> VERIFY_AND_REPORT -> required independent closure.
10. Preserve claim/receipt rules, project baseline vs temporary override, environment authorization, production-gap honesty and hot-state/cold-history separation.
11. Use the lowest environment capable of proving a claim. Agent environment requests are not authority; production mutation follows explicit project authorization.
12. Configure semantic roles from actual harness capabilities. Cheap/read-only workers may perform bounded mechanically checkable discovery; stronger models are reserved for ambiguity/judgment.
13. Keep `docs/operator/`, `docs/references/`, `docs/architecture/`, research and cold history out of normal coding-agent context.
14. If a required harness feature does not exist, report the limitation/gap instead of pretending it exists.
15. After writing adapters/profile pointers, validate a fresh session can discover:
   - source of truth + framework version;
   - current work/task/profile;
   - build/lint/test/affected-project commands;
   - verification and production routers;
   - DRAFT/REVIEW/APPLY/VERIFY workflow;
   - environment/permission policy;
   - current production/open-gap entrypoints;
   without loading operator docs or the entire framework shelf.
16. Return an adoption receipt conforming to `docs/agent/ADOPTION_RECEIPT_SCHEMA.md` and STOP before product work unless the next authorization explicitly permits it.
```