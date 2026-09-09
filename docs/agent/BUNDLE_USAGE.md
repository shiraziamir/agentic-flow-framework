# Agent Bundle Usage

**Agent-facing document**  
**Version:** 1.7  
**Updated:** 2026-09-09T11:30:00Z

Build the portable ZIP from a framework checkout:

```bash
python3 scripts/build_agent_bundle.py
python3 scripts/test_build_agent_bundle.py
```

Default output:

```text
dist/agentic-flow-agent-bundle.zip
```

Extract the archive into the target repository, preferably as:

```text
.agentic-flow/
```

The ZIP exposes a root entrypoint:

```text
.agentic-flow/START_HERE.md
```

and a one-line operator handoff:

```text
.agentic-flow/INSTALL_PROMPT.txt
```

The canonical copy also remains under `docs/agent/START_HERE.md`. If coding is already in progress, follow `docs/agent/MIDSTREAM_ADOPTION.md` before further product mutation.

The bundle deliberately excludes `docs/operator/`, `docs/references/`, `docs/architecture/`, `research/`, reader HTML and cold project history. Those remain available in the full source repository but should not become normal coding-agent context.

`BUNDLE_MANIFEST.json` records the framework version plus SHA-256 hash and byte count for each bundled source file. Verify hashes when the bundle crosses trust boundaries.
