# Generated adapters

Files such as `CLAUDE.md`, tool-specific agent definitions, OpenCode config and `GEMINI.md` belong to the **target project**, not necessarily this framework repo.

Generate them with `prompts/bootstrap/*`.

They are adapters, not source of truth. If an adapter conflicts with `ARCHITECTURE.md`, fix/amend the canonical architecture or regenerate the adapter; do not silently fork policy in the adapter.

Preferred adapter properties:

- short permanent context;
- explicit pointer to canonical authority;
- lazy/on-demand skill discovery;
- vendor-specific permissions/hooks/model configuration only;
- reproducible generation from the current framework version.
