#!/usr/bin/env python3
"""Lint Agentic Flow task/evidence/status artifacts for mechanical truth errors.

JSON works with the Python standard library. YAML is supported when PyYAML is
installed. This linter intentionally checks only deterministic invariants; it
cannot decide whether a test is semantically sufficient for a real-world claim.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

GLOBAL_WORDS = re.compile(
    r"\b(all|none|no\s+regressions?|no\s+security\s+issues?|secure|fully\s+tested|only|nothing\s+else)\b",
    re.IGNORECASE,
)

RUNG = {
    "IDENTITY": 1,
    "STATIC": 2,
    "BUILD": 3,
    "FOCUSED_TEST": 4,
    "PATH_PROOF": 5,
    "INTEGRATION_CONTRACT": 6,
    "LIVE_BEHAVIOR": 7,
    "DEPLOYED_ARTIFACT": 8,
    "EXHAUSTIVE_BOUNDED_NEGATIVE": 9,
}

REF_BOUND_TYPES = {
    "BUILD",
    "FOCUSED_TEST",
    "PATH_PROOF",
    "INTEGRATION_CONTRACT",
    "LIVE_BEHAVIOR",
    "DEPLOYED_ARTIFACT",
}


def load_doc(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".json":
        value = json.loads(text)
    elif path.suffix.lower() in {".yaml", ".yml"}:
        try:
            import yaml  # type: ignore
        except ImportError as exc:
            raise RuntimeError(
                f"{path}: YAML input requires PyYAML; use JSON or install PyYAML"
            ) from exc
        value = yaml.safe_load(text)
    else:
        try:
            value = json.loads(text)
        except json.JSONDecodeError as exc:
            raise RuntimeError(
                f"{path}: unsupported format; use .json or .yaml/.yml"
            ) from exc
    if not isinstance(value, dict):
        raise RuntimeError(f"{path}: root must be an object/mapping")
    return value


def lint_task(doc: dict[str, Any]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    classification = doc.get("classification")
    if not isinstance(classification, dict):
        errors.append("task: missing classification mapping")
    else:
        profiles = classification.get("verification_profiles") or []
        if "GENERAL" not in profiles:
            errors.append("task: verification_profiles must include GENERAL")
        if not classification.get("primary_surface"):
            errors.append("task: missing classification.primary_surface")

    claims = doc.get("planned_claims") or []
    if not claims:
        warnings.append("task: no planned_claims; closure may become narrative-driven")
    for i, claim in enumerate(claims):
        if not isinstance(claim, dict):
            errors.append(f"task: planned_claims[{i}] must be a mapping")
            continue
        if not claim.get("statement"):
            errors.append(f"task: planned_claims[{i}] missing statement")
        if not claim.get("minimum_receipt"):
            errors.append(f"task: planned_claims[{i}] missing minimum_receipt")

    if not doc.get("definition_of_done"):
        errors.append("task: missing definition_of_done")
    if not doc.get("stop_conditions"):
        warnings.append("task: no stop_conditions")
    return errors, warnings


def lint_packet(doc: dict[str, Any]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    identity = doc.get("identity") or {}
    head_ref = identity.get("head_ref") if isinstance(identity, dict) else None
    if not head_ref:
        errors.append("packet: identity.head_ref missing")

    evidence_list = doc.get("evidence") or []
    evidence: dict[str, dict[str, Any]] = {}
    for i, item in enumerate(evidence_list):
        if not isinstance(item, dict):
            errors.append(f"packet: evidence[{i}] must be a mapping")
            continue
        eid = item.get("id")
        if not eid:
            errors.append(f"packet: evidence[{i}] missing id")
            continue
        if eid in evidence:
            errors.append(f"packet: duplicate evidence id {eid}")
        evidence[eid] = item

        etype = item.get("type")
        if etype in REF_BOUND_TYPES and head_ref:
            eref = item.get("repository_ref")
            if not eref:
                warnings.append(f"packet: {eid} ({etype}) missing repository_ref")
            elif eref != head_ref:
                errors.append(
                    f"packet: {eid} ({etype}) repository_ref {eref!r} != head_ref {head_ref!r}; possible stale evidence"
                )
        if etype in REF_BOUND_TYPES and not item.get("observed_at"):
            warnings.append(f"packet: {eid} ({etype}) missing observed_at")

    claims = doc.get("claims") or []
    for i, claim in enumerate(claims):
        if not isinstance(claim, dict):
            errors.append(f"packet: claims[{i}] must be a mapping")
            continue
        cid = claim.get("id", f"claims[{i}]")
        statement = str(claim.get("statement") or "")
        status = claim.get("verification_status")
        truth = claim.get("truth_class")
        refs = claim.get("evidence_refs") or []

        if status == "VERIFIED" and not refs:
            errors.append(f"packet: {cid} VERIFIED with no evidence_refs")
        if truth == "UNKNOWN" and status == "VERIFIED":
            errors.append(f"packet: {cid} cannot be UNKNOWN and VERIFIED")
        if truth == "CONTRADICTED" and status not in {"CONTRADICTED", "UNVERIFIED"}:
            errors.append(f"packet: {cid} truth CONTRADICTED but status {status!r}")

        actual_types: list[str] = []
        for ref in refs:
            if ref not in evidence:
                errors.append(f"packet: {cid} references missing evidence {ref}")
                continue
            actual_types.append(str(evidence[ref].get("type") or ""))

        minimum = claim.get("minimum_receipt")
        if status == "VERIFIED" and minimum in RUNG:
            strengths = [RUNG[t] for t in actual_types if t in RUNG]
            if not strengths or max(strengths) < RUNG[minimum]:
                errors.append(
                    f"packet: {cid} VERIFIED but strongest receipt {actual_types or 'NONE'} is below minimum {minimum}"
                )

        if status == "VERIFIED" and GLOBAL_WORDS.search(statement):
            if "EXHAUSTIVE_BOUNDED_NEGATIVE" not in actual_types:
                errors.append(
                    f"packet: {cid} uses global/negative wording without EXHAUSTIVE_BOUNDED_NEGATIVE receipt"
                )

    dod = doc.get("dod_matrix") or []
    for i, row in enumerate(dod):
        if not isinstance(row, dict):
            errors.append(f"packet: dod_matrix[{i}] must be a mapping")
            continue
        if row.get("status") == "PASS" and not row.get("evidence_refs"):
            errors.append(f"packet: DoD {row.get('dod_id', i)} PASS with no evidence_refs")

    return errors, warnings


def lint_status(doc: dict[str, Any]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    if not doc.get("repository_ref"):
        errors.append("report: repository_ref missing")
    claims = doc.get("claims") or []
    for i, claim in enumerate(claims):
        if not isinstance(claim, dict):
            errors.append(f"report: claims[{i}] must be a mapping")
            continue
        cid = claim.get("claim_id", i)
        if claim.get("verification_status") == "VERIFIED" and not claim.get("evidence_refs"):
            errors.append(f"report: claim {cid} VERIFIED with no evidence_refs")
        if claim.get("truth_class") == "UNKNOWN" and claim.get("verification_status") == "VERIFIED":
            errors.append(f"report: claim {cid} cannot be UNKNOWN and VERIFIED")
        if GLOBAL_WORDS.search(str(claim.get("statement") or "")):
            warnings.append(
                f"report: claim {cid} contains global/negative wording; verify finite universe in evidence packet"
            )
    if "checks" not in doc:
        warnings.append("report: checks section missing")
    return errors, warnings


def classify(doc: dict[str, Any]) -> str:
    if "identity" in doc and "evidence" in doc and "dod_matrix" in doc:
        return "packet"
    if "planned_claims" in doc or "definition_of_done" in doc:
        return "task"
    if "report_id" in doc or ("claims" in doc and "checks" in doc):
        return "status"
    return "unknown"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="+", type=Path)
    parser.add_argument("--strict", action="store_true", help="treat warnings as failures")
    args = parser.parse_args()

    total_errors = 0
    total_warnings = 0
    for path in args.files:
        try:
            doc = load_doc(path)
        except Exception as exc:
            print(f"ERROR {exc}", file=sys.stderr)
            total_errors += 1
            continue

        kind = classify(doc)
        if kind == "task":
            errors, warnings = lint_task(doc)
        elif kind == "packet":
            errors, warnings = lint_packet(doc)
        elif kind == "status":
            errors, warnings = lint_status(doc)
        else:
            errors, warnings = [f"{path}: could not identify artifact type"], []

        print(f"{path}: {kind} — {len(errors)} error(s), {len(warnings)} warning(s)")
        for msg in errors:
            print(f"  ERROR: {msg}")
        for msg in warnings:
            print(f"  WARN:  {msg}")
        total_errors += len(errors)
        total_warnings += len(warnings)

    if total_errors or (args.strict and total_warnings):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
