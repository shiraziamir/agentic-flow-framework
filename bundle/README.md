# Portable Agent Bundle

Build and self-test the drop-in ZIP:

```bash
python3 scripts/test_build_agent_bundle.py
python3 scripts/build_agent_bundle.py
```

Default ZIP:

```text
dist/agentic-flow-agent-bundle.zip
```

Extract into a target project as `.agentic-flow/`. The generated ZIP provides:

```text
.agentic-flow/START_HERE.md
.agentic-flow/INSTALL_PROMPT.txt
.agentic-flow/BUNDLE_MANIFEST.json
```

For active/mid-task coding, `START_HERE.md` routes the agent to `docs/agent/MIDSTREAM_ADOPTION.md` before further mutation.

The bundle intentionally excludes operator-only documentation, external reference/research material, reader HTML and cold project history. The manifest records framework version plus SHA-256 hashes/byte counts for bundled source files.
