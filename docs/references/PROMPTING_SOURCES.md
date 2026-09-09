# Prompting / Agent-Setup Source Notes

**Updated:** 2026-09-09T11:30:00Z

Current prompt/agent-setup guidance was rechecked against:

- OpenAI prompt engineering best practices: https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api
- OpenAI ChatGPT prompting best practices: https://help.openai.com/en/articles/10032626
- Anthropic prompting best practices: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- Google Gemini prompt design strategies: https://ai.google.dev/gemini-api/docs/prompting-strategies
- Gemini CLI hierarchical context files: https://google-gemini.github.io/gemini-cli/docs/cli/gemini-md.html
- OpenCode project rules: https://opencode.ai/docs/rules
- OpenCode Agent Skills: https://opencode.ai/docs/skills

Shared conclusions used by this framework: clear/direct instructions, explicit constraints/output formats, structured separation of instructions from context/data, examples when semantics are ambiguous, iterative refinement based on observed failures, concise project instruction maps, hierarchical/modular context, and on-demand reusable skills rather than permanent prompt inflation.
