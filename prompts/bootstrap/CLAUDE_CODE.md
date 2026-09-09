# Bootstrap prompt — Claude Code

**Version:** 1.1  
**Updated:** 2026-09-09

```text
Bootstrap Claude Code from this framework.

First apply every rule in prompts/bootstrap/GENERIC.md. The following are Claude-specific additions only.

Canonical authority: ARCHITECTURE.md, schemas/, skills/. Generated Claude files remain adapters and must identify the canonical architecture version.

Inspect existing CLAUDE.md, .claude/agents, .claude/skills, settings and hooks.

Create/update only as justified:
- a SHORT CLAUDE.md that maps to canonical authority, repo commands and local gotchas;
- Claude-compatible skills by exposing/synchronizing canonical SKILL.md directories rather than duplicating prose;
- a cheap/read-only discovery subagent only when explicitly configured with an available cheap model; do not assume the built-in Explore model is fixed;
- a standard executor definition if useful;
- an independent reviewer/supervisor with read-only tools;
- deterministic hooks only for rules that must always fire and can be checked exactly;
- usage capture when the Claude/API/harness surface actually exposes counters; otherwise mark telemetry unavailable/unknown.

Use lazy/deferred tool discovery where the available Claude surface supports it, keep large tool results/logs out of standing context, and preserve hot-state/cold-history separation.

Do not make the supervisor edit the work it reviews. Do not encode model names as authority. Do not copy all skills/history into CLAUDE.md.

Validate fresh-session discovery, adaptive governance, TOKEN_WASTE_WARNING behavior for long work, and report generated files plus unsupported features.
```
