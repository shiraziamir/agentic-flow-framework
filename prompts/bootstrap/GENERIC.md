# Bootstrap prompt — generic coding agent

Use this after cloning Agentic Flow Framework into a project or making it available as a reference.

```text
You are bootstrapping this repository's agent operating layer.

1. Read, in order:
   - ARCHITECTURE.md
   - schemas/TASK_CONTRACT.md
   - schemas/EVIDENCE_PACKET.md
   - skills/00_INDEX.md
2. Inspect the target project's existing agent instruction surfaces and build/test mechanics. Do not overwrite working project-specific rules blindly.
3. Generate or update the minimum vendor-specific adapter files needed by your current agent/harness.
4. Adapters are NON-AUTHORITATIVE. They must point to the canonical files above and must not invent policy that conflicts with them.
5. Keep always-on instructions concise. Do not copy ARCHITECTURE.md or every skill body into the adapter. Expose skills lazily/on demand where the harness supports it.
6. Configure semantic roles (ORCHESTRATOR / EXECUTION_TIER / JUDGMENT_TIER / INDEPENDENT_REVIEWER) using capabilities actually available in this environment.
7. If the harness lacks a feature, document the limitation and preserve the conceptual lifecycle using files/prompts instead of pretending the feature exists.
8. Before writing, report the adapter plan and any conflicts with existing files.
9. After writing, verify that a fresh session can discover:
   - source of truth;
   - skill index;
   - task-contract workflow;
   - supervisor workflow;
   - build/test commands;
   without loading the entire framework into permanent context.
10. Return changed paths and a concise validation receipt.
```
