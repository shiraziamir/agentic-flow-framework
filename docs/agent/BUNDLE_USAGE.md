# Agent Bundle Usage

**Agent-facing routing document.**

Build from a framework checkout:

```bash
python3 scripts/test_build_agent_bundle.py
python3 scripts/build_agent_bundle.py
```

Default output:

```text
dist/agentic-flow-agent-bundle.zip
```

## Installation

Extract the `agentic-flow/` directory from the ZIP into the target repository as:

```text
.agentic-flow/
```

Then the coding agent starts at:

```text
.agentic-flow/START_HERE.md
```

The root `README.md` is for the human/operator and explains exactly where to copy the bundle and what initial prompt to send.

## Distribution contents vs. agent context

The ZIP is a **distribution package**, not an instruction to preload every file.

It contains:

- canonical policy and runtime schemas/profiles/skills/prompts;
- agent-facing adoption/workflow/token guidance;
- separate operator guides, including Python-tool usage;
- architecture explanation;
- primary-source/reference documentation;
- `BEST_PRACTICES_USED.en.txt`;
- integrity manifest and root entrypoints.

The coding agent normally loads only `START_HERE.md` plus the files it routes to. `docs/operator/`, `docs/architecture/` and `docs/references/` remain cold unless the task explicitly needs them.

Research notes, reader HTML and cold project/history artifacts remain outside the default portable bundle.

## Active coding

If work is already in progress, `START_HERE.md` routes to:

```text
docs/agent/MIDSTREAM_ADOPTION.md
```

before further product mutation.

## Integrity

The ZIP contains `BUNDLE_MANIFEST.json` with framework version, source paths, SHA-256 hashes and byte counts. GitHub Actions rebuilds the bundle from a clean checkout and verifies required files, manifest hashes and distribution boundaries before publishing the release artifact.
