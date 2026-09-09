#!/usr/bin/env python3
"""Self-tests for production_readiness_lint.py using in-memory artifacts."""

from production_readiness_lint import lint_gap, lint_profile


def assert_ok(errors, label):
    assert not errors, f"{label}: unexpected errors: {errors}"


def assert_has(errors, fragment, label):
    assert any(fragment in e for e in errors), f"{label}: expected {fragment!r}; got {errors}"


def main() -> int:
    good = {
        "codebase_scale": "MEDIUM",
        "readiness_tier": "STANDARD",
        "business_context": {"stateful": True, "durable_data_criticality": "HIGH", "user_facing": True},
        "runtime": {"environments": ["dev", "production"]},
        "recovery": {"backup_required": True, "restore_test_required": True, "rpo": "15m", "rto": "2h"},
        "observability": {"metrics_required": True, "logs_required": True, "traces_required": True, "slo_required": True},
        "security": {"vulnerability_management_required": True, "threat_model_required": True},
        "resilience": {"failure_mode_analysis_required": True, "recovery_drill_required": True},
        "required_profiles": ["DELIVERY", "OBSERVABILITY", "SECURITY_FIRST", "DATA_DURABILITY"],
    }
    e, _ = lint_profile(good)
    assert_ok(e, "good profile")

    bad_backup = {**good, "recovery": {"backup_required": False, "restore_test_required": False, "rpo": "NOT_DEFINED", "rto": "NOT_DEFINED"}}
    e, _ = lint_profile(bad_backup)
    assert_has(e, "backup_required=true", "backup")
    assert_has(e, "restore_test_required=true", "restore")
    assert_has(e, "defined RPO", "rpo")
    assert_has(e, "defined RTO", "rto")

    high = {**good, "readiness_tier": "HIGH_ASSURANCE", "observability": {**good["observability"], "slo_required": False}, "security": {"vulnerability_management_required": True, "threat_model_required": False}, "resilience": {"failure_mode_analysis_required": False, "recovery_drill_required": False}}
    e, _ = lint_profile(high)
    assert_has(e, "slo_required=true", "slo")
    assert_has(e, "failure_mode_analysis_required=true", "fma")
    assert_has(e, "recovery_drill_required=true", "drill")
    assert_has(e, "threat_model_required=true", "threat")

    accepted = {"gap_id": "G1", "area": "SECURITY", "requirement": "x", "state": "ACCEPTED_RISK", "reality": {"observed": "missing", "missing_receipt": "test"}, "owner": "team", "accepted_by": "DEC-1", "acceptance_expiry": "2026-12-01"}
    e, _ = lint_gap(accepted)
    assert_ok(e, "accepted risk")

    invalid_accept = {**accepted, "accepted_by": "NONE", "owner": "UNASSIGNED"}
    e, _ = lint_gap(invalid_accept)
    assert_has(e, "accepted_by", "risk authority")
    assert_has(e, "requires owner", "risk owner")

    closed = {"gap_id": "G2", "area": "DELIVERY", "requirement": "rollback", "state": "CLOSED", "reality": {"observed": "implemented", "evidence_refs": []}, "owner": "team"}
    e, _ = lint_gap(closed)
    assert_has(e, "CLOSED requires evidence_refs", "gap close receipt")

    print("production_readiness_lint self-tests: 6 scenarios PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
