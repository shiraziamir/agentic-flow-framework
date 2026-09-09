# Bootstrap prompt — Claude Code

```text
Bootstrap Claude Code from this framework.

Canonical authority: ARCHITECTURE.md, schemas/, skills/. Generated Claude files must remain adapters.

Read ARCHITECTURE.md and skills/00_INDEX.md first. Then inspect existing CLAUDE.md, .claude/agents, .claude/skills, settings and hooks.

Create/update:
- a SHORT CLAUDE.md that maps to canonical authority, repo commands and local gotchas;
- Claude-compatible skills from the canonical skills, preferably by exposing or synchronizing SKILL.md directories rather than duplicating prose;
- a cheap/read-only discovery subagent only if explicitly configured with an available cheap model (do not assume built-in Explore is always Haiku);
- a standard executor definition if useful;
- an independent reviewer/supervisor with read-only tools;
- deterministic hooks only for rules that must always fire and can be checked exactly.

Do not make the supervisor edit the work it reviews.
Do not encode model names as authority; map semantic roles to current available models.
Do not copy all skills into CLAUDE.md.
Validate fresh-session discovery and report generated files plus any unsupported feature.
```
