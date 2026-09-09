# Portable Agent Bundle

Build the drop-in ZIP from a framework checkout:

```bash
python3 scripts/build_agent_bundle.py
python3 scripts/test_build_agent_bundle.py
```

Default ZIP:

```text
dist/agentic-flow-agent-bundle.zip
```

Extract into a target project as `.agentic-flow/`, then instruct the coding agent to read:

```text
.agentic-flow/docs/agent/START_HERE.md
```

For an active/mid-task session, use:

```text
.agentic-flow/docs/agent/MIDSTREAM_ADOPTION.md
```

The bundle intentionally excludes operator-only documentation, external research, reader HTML and cold project history. Its manifest contains SHA-256 hashes of bundled files.
