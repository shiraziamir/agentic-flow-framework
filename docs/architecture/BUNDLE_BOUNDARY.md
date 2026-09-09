# Portable Bundle Boundary

The portable Agent Bundle is a **self-contained distribution package**. Distribution contents and coding-agent working context are intentionally different concepts.

## Included in the distribution

The bundle includes:

- canonical `ARCHITECTURE.md` and `VERSION`;
- schemas, verification profiles, production profiles and skills;
- bootstrap/workflow/supervisor prompts and templates;
- deterministic helper scripts;
- `docs/agent/` adoption and execution guidance;
- `docs/operator/` human installation/operation guides;
- `docs/architecture/` explanations;
- `docs/references/PRIMARY_SOURCES.md`;
- root `README.md`, `START_HERE.md`, `INSTALL_PROMPT.txt`, `PRIMARY_SOURCES.md` and `BEST_PRACTICES_USED.en.txt` convenience files;
- `BUNDLE_MANIFEST.json` with source-file hashes and byte counts.

## Excluded from the default distribution

The bundle still excludes material that is useful for repository research/history but not required for portable operation:

```text
research/
reader HTML views
retrospectives/
stories/
cold project history
repository .git history
```

## Agent preload boundary

The fact that operator/reference documents are physically present in the ZIP does **not** authorize or require the coding agent to preload them.

Normal coding-agent context starts at `START_HERE.md` and is limited to the current task/project state, relevant source, selected verification/production profiles and triggered skills.

These remain cold unless explicitly needed:

```text
docs/operator/
docs/architecture/
docs/references/
PRIMARY_SOURCES.md
BEST_PRACTICES_USED.en.txt
```

## Why this design

A portable artifact should be usable offline by both a human operator and a coding agent without requiring a second repository checkout merely to find installation instructions, architecture rationale or source provenance. At the same time, packaging documentation should not turn into permanent model context.

Therefore:

```text
Distribution completeness != Agent context size
```

The ZIP is complete enough to operate and audit; the agent's loaded context stays intentionally small and task-driven.
