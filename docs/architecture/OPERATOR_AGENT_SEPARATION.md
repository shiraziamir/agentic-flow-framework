# Operator / Agent Documentation Separation

Agentic Flow deliberately separates human/operator education from coding-agent runtime instructions.

## Agent-facing

`docs/agent/` contains only adoption/bootstrap material that a coding agent may need. Canonical operational policy remains in root/schema/router/skill/prompt files.

## Operator-facing

`docs/operator/` contains installation examples, prompting/task-writing guidance and explanations for humans. These files are excluded from the default Agent Bundle and should not be copied into `AGENTS.md`, `CLAUDE.md`, `GEMINI.md` or other permanent coding-agent prompts.

## References/research

`docs/references/` and `research/` preserve provenance and dated external evidence. They are cold and loaded only when current research/provenance is necessary.

This separation reduces token/context cost, prevents duplicate policy authority, and keeps human-readable explanation from becoming unintended agent instructions.
