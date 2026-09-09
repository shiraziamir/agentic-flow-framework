# Research note — bootstrap, skills and independent supervision

Date: 2026-09-09

This note records primary evidence used for the v1.2 bootstrap/supervision update. It is research, not policy authority.

## 1. Short maps beat giant permanent instruction files

OpenAI's Harness Engineering report describes an internal agent-first codebase where a large `AGENTS.md` accumulated too much guidance, crowded out useful task/code context, became stale, and was replaced by a short map into structured repository documentation.

Source:
- https://openai.com/index/harness-engineering/

Framework implication: root adapters should point to canonical documents and skills rather than duplicate them.

## 2. Skills should be discovered lazily

OpenCode documents `SKILL.md`-based reusable behavior loaded on demand. The model sees skill identifiers/descriptions and loads the full body only when needed. It supports project skill sources under `.opencode/skills`, `.claude/skills`, and `.agents/skills` with explicit precedence and permissions.

Sources:
- https://opencode.ai/docs/skills
- https://opencode.ai/docs/rules

Framework implication: keep one canonical portable skill body and avoid unnecessary copies across vendor directories.

## 3. Vendor adapters need precedence discipline

OpenCode explicitly documents rule precedence between project `AGENTS.md`, Claude-compatible files and global rules. Multiple instruction sources can therefore drift or shadow one another.

Source:
- https://opencode.ai/docs/rules

Framework implication: generated adapters must be declared non-authoritative and bootstrap should report precedence conflicts.

## 4. Separate child contexts are useful context firebreaks

Claude Code documents subagents as separate contexts and supports model selection in subagent definitions. Anthropic's cost guidance recommends cheaper models for simpler subagent work while reserving stronger models for harder reasoning. Current Claude Code behavior must be checked by version rather than assumed from historical defaults.

Sources:
- https://code.claude.com/docs/en/sub-agents
- https://code.claude.com/docs/en/costs

Framework implication: cheap/read-only discovery is a semantic role; configure the actual model explicitly when cost behavior matters.

## 5. Gemini context files are hierarchical project adapters

Gemini CLI documents project context through `GEMINI.md` files and hierarchical/import behavior. Capacity-management features do not replace repository-visible durable state.

Source:
- https://google-gemini.github.io/gemini-cli/docs/cli/gemini-md.html

Framework implication: `GEMINI.md` should be a concise adapter pointing at canonical authority rather than a copied framework manual.

## 6. Supervisor independence is architectural, not a model label

The framework distinguishes direct-access supervision from evidence-only supervision because the available proof differs materially.

Direct-access review can independently inspect source/diff/tests and attempt falsification. Evidence-only review cannot verify hidden repository facts and therefore requires an explicit packet and an `UNVERIFIED_FROM_PACKET` state.

This design is also consistent with Yara's learned rule that author/executor/judge collapse creates easy-task and self-closure failure modes. The supervisor should be a separate human, model, session, or harness role and should remain read-only during the review pass when independence is part of the assurance argument.

## 7. Skill telemetry interpretation

Yara's own `SKILL_ACTIVATION_TRACE.md` states that observed rule conformance or positive outcome does not establish that loading the skill caused the behavior. Its historical telemetry also contains canonical-ID fragmentation (`name` vs `name.md`) and the event log is not a complete denominator for uninstrumented project tasks.

Framework implication:
- use frequency as routing evidence, not as a deletion rule;
- keep broadly useful skills CORE/COMMON;
- keep rare safety procedures RISK_TRIGGERED/cold;
- use controlled skill-present vs skill-neutralized fixtures for causal promotion claims.
