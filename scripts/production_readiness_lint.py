#!/usr/bin/env python3
"""Lint Agentic Flow production profiles/gaps for deterministic contradictions.

JSON uses only the Python standard library. YAML works when PyYAML is installed.
This tool validates structural/invariant truth only; it cannot prove runtime
readiness, backup restore success, security, observability quality or SLO health.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

SCALES = {"SMALL", "MEDIUM", "LARGE"}
TIERS = {"BASIC", "STANDARD", "HIGH_ASSURANCE"}
GAP_STATES = {"NOT_IMPLEMENTED", "PARTIAL", "UNVERIFIED", "BLOCKED", "ACCEPTED_RISK", "CLOSED"}


def load_doc(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".json":
        value = json.loads(text)
    elif path.suffix.lower() in {".yaml", ".yml"}:
        try:
            import yaml  # type: ignore
        except ImportError as exc:
            raise RuntimeError(f"{path}: YAML requires PyYAML; use JSON or install PyYAML") from exc
        value = yaml.safe_load(text)
    else:
        try:
            value = json.loads(text)
        except json.JSONDecodeError as exc:
            raise RuntimeError(f"{path}: use .json or .yaml/.yml") from exc
    if not isinstance(value, dict):
        raise RuntimeError(f"{path}: root must be an object/mapping")
    return value


def present(value: Any) -> bool:
    return value not in (None, "", "NONE", "NOT_DEFINED", "UNKNOWN")


def lint_profile(doc: dict[str, Any]) -> tuple[list[str], list[str]]:
    e: list[str] = []
    w: list[str] = []
    scale = doc.get("codebase_scale")
    tier = doc.get("readiness_tier")
    if scale not in SCALES:
        e.append(f"profile: invalid/missing codebase_scale {scale!r}")
    if tier not in TIERS:
        e.append(f"profile: invalid/missing readiness_tier {tier!r}")

    ctx = doc.get("business_context") or {}
    recovery = doc.get("recovery") or {}
    obs = doc.get("observability") or {}
    sec = doc.get("security") or {}
    res = doc.get("resilience") or {}

    stateful = bool(ctx.get("stateful"))
    data_criticality = ctx.get("durable_data_criticality")
    user_facing = bool(ctx.get("user_facing"))

    if stateful and data_criticality == "HIGH":
        if recovery.get("backup_required") is not True:
            e.append("profile: stateful HIGH-criticality data requires backup_required=true")
        if recovery.get("restore_test_required") is not True:
            e.append("profile: stateful HIGH-criticality data requires restore_test_required=true")
        if not present(recovery.get("rpo")):
            e.append("profile: HIGH-criticality durable data requires defined RPO")
        if not present(recovery.get("rto")):
            e.append("profile: HIGH-criticality durable data requires defined RTO")

    if tier in {"STANDARD", "HIGH_ASSURANCE"}:
        if obs.get("metrics_required") is not True:
            e.append(f"profile: {tier} requires metrics_required=true")
        if obs.get("logs_required") is not True:
            e.append(f"profile: {tier} requires logs_required=true")
        if sec.get("vulnerability_management_required") is not True:
            e.append(f"profile: {tier} requires vulnerability_management_required=true")

    if tier == "HIGH_ASSURANCE":
        if user_facing and obs.get("slo_required") is not True:
            e.append("profile: user-facing HIGH_ASSURANCE requires slo_required=true")
        if res.get("failure_mode_analysis_required") is not True:
            e.append("profile: HIGH_ASSURANCE requires failure_mode_analysis_required=true")
        if res.get("recovery_drill_required") is not True:
            e.append("profile: HIGH_ASSURANCE requires recovery_drill_required=true")
        if sec.get("threat_model_required") is not True:
            e.append("profile: HIGH_ASSURANCE requires threat_model_required=true")

    if doc.get("runtime", {}).get("environments") is None:
        w.append("profile: runtime.environments missing")
    if not doc.get("required_profiles"):
        w.append("profile: required_profiles empty; readiness routing may be underspecified")
    return e, w


def lint_gap(doc: dict[str, Any]) -> tuple[list[str], list[str]]:
    e: list[str] = []
    w: list[str] = []
    if not doc.get("gap_id"):
        e.append("gap: missing gap_id")
    state = doc.get("state")
    if state not in GAP_STATES:
        e.append(f"gap: invalid/missing state {state!r}")
    if not doc.get("area"):
        e.append("gap: missing area")
    if not doc.get("requirement"):
        e.append("gap: missing requirement")
    reality = doc.get("reality") or {}
    if not reality.get("observed"):
        e.append("gap: missing reality.observed")
    if state != "CLOSED" and not reality.get("missing_receipt"):
        w.append("gap: open gap has no missing_receipt definition")
    if state == "ACCEPTED_RISK":
        if not present(doc.get("accepted_by")):
            e.append("gap: ACCEPTED_RISK requires accepted_by")
        if not present(doc.get("owner")):
            e.append("gap: ACCEPTED_RISK requires owner")
        if not present(doc.get("acceptance_expiry")):
            w.append("gap: ACCEPTED_RISK has no acceptance_expiry/review point")
    if state != "CLOSED" and not present(doc.get("owner")):
        w.append("gap: open material gap has no assigned owner")
    if state == "CLOSED" and not reality.get("evidence_refs"):
        e.append("gap: CLOSED requires evidence_refs")
    return e, w


def classify(doc: dict[str, Any]) -> str:
    if "codebase_scale" in doc or "readiness_tier" in doc:
        return "profile"
    if "gap_id" in doc or ("requirement" in doc and "state" in doc):
        return "gap"
    return "unknown"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="+", type=Path)
    parser.add_argument("--strict", action="store_true", help="treat warnings as failures")
    args = parser.parse_args()
    total_e = 0
    total_w = 0
    for path in args.files:
        try:
            doc = load_doc(path)
            kind = classify(doc)
            if kind == "profile":
                errors, warnings = lint_profile(doc)
            elif kind == "gap":
                errors, warnings = lint_gap(doc)
            else:
                errors, warnings = [f"{path}: could not identify artifact type"], []
        except Exception as exc:
            errors, warnings, kind = [str(exc)], [], "error"
        print(f"{path}: {kind} — {len(errors)} error(s), {len(warnings)} warning(s)")
        for msg in errors:
            print(f"  ERROR: {msg}")
        for msg in warnings:
            print(f"  WARN:  {msg}")
        total_e += len(errors)
        total_w += len(warnings)
    return 1 if total_e or (args.strict and total_w) else 0


if __name__ == "__main__":
    raise SystemExit(main())
