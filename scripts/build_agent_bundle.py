#!/usr/bin/env python3
"""Build the portable Agentic Flow drop-in bundle.

The bundle intentionally excludes operator docs, research, reader HTML, retrospectives,
and repository history so a target coding agent receives only canonical/agent-facing
runtime material. Run from the framework repository root.
"""
from __future__ import annotations
import argparse, hashlib, json, zipfile
from pathlib import Path

INCLUDE_FILES = {"VERSION", "ARCHITECTURE.md"}
INCLUDE_PREFIXES = (
    "docs/agent/", "schemas/", "verification/", "production/", "skills/",
    "prompts/bootstrap/", "prompts/workflow/", "prompts/supervisor/", "templates/",
)
INCLUDE_SCRIPTS = {
    "scripts/verification_lint.py", "scripts/production_readiness_lint.py",
    "scripts/usage_ledger.py",
}
EXCLUDE_PARTS = {"__pycache__", ".DS_Store"}


def selected(root: Path) -> list[Path]:
    files=[]
    for p in root.rglob("*"):
        if not p.is_file(): continue
        rel=p.relative_to(root).as_posix()
        if any(x in p.parts for x in EXCLUDE_PARTS): continue
        if rel in INCLUDE_FILES or rel in INCLUDE_SCRIPTS or any(rel.startswith(x) for x in INCLUDE_PREFIXES):
            files.append(p)
    return sorted(files, key=lambda p: p.relative_to(root).as_posix())


def build(root: Path, output: Path) -> dict:
    files=selected(root)
    manifest={"format":1,"files":[]}
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output,"w",compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for p in files:
            rel=p.relative_to(root).as_posix()
            data=p.read_bytes()
            manifest["files"].append({"path":rel,"sha256":hashlib.sha256(data).hexdigest(),"bytes":len(data)})
            info=zipfile.ZipInfo(f"agentic-flow/{rel}", date_time=(2026,9,9,0,0,0))
            info.compress_type=zipfile.ZIP_DEFLATED
            info.external_attr=0o100644 << 16
            z.writestr(info,data)
        payload=json.dumps(manifest,indent=2,sort_keys=True).encode()
        info=zipfile.ZipInfo("agentic-flow/BUNDLE_MANIFEST.json", date_time=(2026,9,9,0,0,0))
        info.compress_type=zipfile.ZIP_DEFLATED
        z.writestr(info,payload)
    return manifest


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--root",type=Path,default=Path(".")); ap.add_argument("--output",type=Path,default=Path("dist/agentic-flow-agent-bundle.zip")); a=ap.parse_args()
    m=build(a.root.resolve(),a.output.resolve())
    print(f"built {a.output} with {len(m['files'])} files")

if __name__=="__main__": main()
