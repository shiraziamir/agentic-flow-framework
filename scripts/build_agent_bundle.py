#!/usr/bin/env python3
"""Build the portable Agentic Flow distribution bundle.

The ZIP is self-contained for both a coding agent and a human operator, while
START_HERE.md keeps the coding-agent working context small. Deeper research,
reader HTML, retrospectives, stories and repository history remain excluded.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import zipfile
from pathlib import Path

INCLUDE_FILES = {
    "VERSION",
    "ARCHITECTURE.md",
    "bundle/README.md",
    "bundle/BEST_PRACTICES_USED.en.txt",
}
INCLUDE_PREFIXES = (
    "docs/",
    "schemas/",
    "verification/",
    "production/",
    "skills/",
    "prompts/bootstrap/",
    "prompts/workflow/",
    "prompts/supervisor/",
    "templates/",
)
INCLUDE_SCRIPTS = {
    "scripts/verification_lint.py",
    "scripts/test_verification_lint.py",
    "scripts/production_readiness_lint.py",
    "scripts/test_production_readiness_lint.py",
    "scripts/build_agent_bundle.py",
    "scripts/test_build_agent_bundle.py",
    "scripts/usage_ledger.py",
    "scripts/claude_usage_snapshot.py",
    "scripts/test_claude_usage_snapshot.py",
    "scripts/test_docs_onboarding.py",
}
EXCLUDE_PARTS = {"__pycache__", ".DS_Store"}
ZIP_TIME = (2026, 9, 9, 0, 0, 0)


def selected(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(root).as_posix()
        if any(part in EXCLUDE_PARTS for part in path.parts):
            continue
        if (
            rel in INCLUDE_FILES
            or rel in INCLUDE_SCRIPTS
            or any(rel.startswith(prefix) for prefix in INCLUDE_PREFIXES)
        ):
            files.append(path)
    return sorted(files, key=lambda p: p.relative_to(root).as_posix())


def _write(zf: zipfile.ZipFile, name: str, data: bytes) -> None:
    info = zipfile.ZipInfo(name, date_time=ZIP_TIME)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o100644 << 16
    zf.writestr(info, data)


def build(root: Path, output: Path) -> dict:
    files = selected(root)
    version = (root / "VERSION").read_text(encoding="utf-8").strip()
    manifest = {
        "format": 1,
        "framework_version": version,
        "entrypoint": "START_HERE.md",
        "operator_entrypoint": "README.md",
        "files": [],
    }
    output.parent.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for path in files:
            rel = path.relative_to(root).as_posix()
            data = path.read_bytes()
            manifest["files"].append(
                {
                    "path": rel,
                    "sha256": hashlib.sha256(data).hexdigest(),
                    "bytes": len(data),
                }
            )
            _write(zf, f"agentic-flow/{rel}", data)

        start_here = (root / "docs/agent/START_HERE.md").read_bytes()
        operator_readme = (root / "bundle/README.md").read_bytes()
        best_practices = (root / "bundle/BEST_PRACTICES_USED.en.txt").read_bytes()
        primary_sources = (root / "docs/references/PRIMARY_SOURCES.md").read_bytes()
        install_prompt = (
            "Read .agentic-flow/START_HERE.md and adopt Agentic Flow for this repository. "
            "Inspect the project read-only first. Use STRICT_PREVIEW mutation approval unless "
            "the existing project profile explicitly says otherwise. Before each mutation batch, "
            "report current state, proposed state, affected files/resources, impact, planned checks, "
            "rollback/recovery when relevant, and out-of-scope boundaries; then wait for explicit "
            "APPROVE/APPLY. If coding is already in progress, follow MIDSTREAM_ADOPTION before "
            "further mutation and preserve current edits.\n"
        ).encode("utf-8")

        _write(zf, "agentic-flow/README.md", operator_readme)
        _write(zf, "agentic-flow/START_HERE.md", start_here)
        _write(zf, "agentic-flow/INSTALL_PROMPT.txt", install_prompt)
        _write(zf, "agentic-flow/BEST_PRACTICES_USED.en.txt", best_practices)
        _write(zf, "agentic-flow/PRIMARY_SOURCES.md", primary_sources)
        _write(
            zf,
            "agentic-flow/BUNDLE_MANIFEST.json",
            json.dumps(manifest, indent=2, sort_keys=True).encode("utf-8"),
        )

    return manifest


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("dist/agentic-flow-agent-bundle.zip"),
    )
    args = parser.parse_args()

    manifest = build(args.root.resolve(), args.output.resolve())
    print(
        f"built {args.output} for Agentic Flow {manifest['framework_version']} "
        f"with {len(manifest['files'])} source files"
    )


if __name__ == "__main__":
    main()
