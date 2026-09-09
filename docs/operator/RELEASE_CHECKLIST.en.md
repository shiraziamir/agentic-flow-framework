# Operator Release Checklist

Before calling a framework release complete:

- `VERSION`, `ARCHITECTURE.md`, `README.md`, reader docs and `CHANGELOG.md` agree on the release version.
- Agent-facing and operator-facing documentation remain separated.
- `docs/references/PRIMARY_SOURCES.md` includes newly used external sources.
- `scripts/test_verification_lint.py`, `scripts/test_production_readiness_lint.py`, and `scripts/test_build_agent_bundle.py` pass.
- `scripts/build_agent_bundle.py` produces a ZIP whose manifest hashes match its contents and excludes operator/research/history files.
- A fresh-install prompt and a midstream-adoption prompt are present.
- Bootstrap adapters point to the latest canonical architecture and do not duplicate long policy.
- Final repository `main` ref is recorded as the release receipt.
