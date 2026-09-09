# Agent Bundle Usage

**Agent-facing document**  
**Version:** 1.0  
**Updated:** 2026-09-09T11:30:00Z

A framework checkout can build a portable ZIP with:

```bash
python3 scripts/build_agent_bundle.py
```

Default output:

```text
dist/agentic-flow-agent-bundle.zip
```

Extract it into the target repository, preferably as:

```text
.agentic-flow/
```

Then read:

```text
.agentic-flow/docs/agent/START_HERE.md
```

The bundle deliberately excludes `docs/operator/`, `research/`, reader HTML, and cold project history. Those are useful for humans/audits but should not become normal coding-agent context.

The ZIP contains `BUNDLE_MANIFEST.json` with SHA-256 hashes for bundled files. Verify hashes when the bundle crosses trust boundaries.
