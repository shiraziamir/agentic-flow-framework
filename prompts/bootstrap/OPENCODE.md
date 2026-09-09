# Bootstrap prompt — OpenCode

```text
Bootstrap OpenCode from this framework.

Read ARCHITECTURE.md, schemas/, and skills/00_INDEX.md. Inspect existing AGENTS.md, opencode.json/jsonc, .opencode/skills, .agents/skills and .claude/skills.

Create/update:
- concise AGENTS.md mapping to canonical authority;
- skill discovery using canonical SKILL.md directories, preferring one source of skill bodies rather than duplicated copies;
- per-agent model/permission settings for cheap read-only discovery, standard execution, and read-only supervision when supported;
- explicit skill permissions: reviewer should not load mutation-oriented tooling unnecessarily.

Use lazy references. Do not preload all skill bodies. Preserve adapter-vs-authority separation and report any precedence conflicts among skill sources.
```
