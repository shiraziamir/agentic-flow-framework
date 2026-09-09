#!/usr/bin/env python3
"""Regression tests for scripts/verification_lint.py."""

from __future__ import annotations

import unittest

import verification_lint as vl


class VerificationLintTests(unittest.TestCase):
    def test_good_live_packet_passes(self) -> None:
        doc = {
            "identity": {"head_ref": "abc"},
            "claims": [
                {
                    "id": "C1",
                    "statement": "frontend checkout works in testenv X",
                    "truth_class": "OBSERVED",
                    "verification_status": "VERIFIED",
                    "minimum_receipt": "LIVE_BEHAVIOR",
                    "evidence_refs": ["E1"],
                }
            ],
            "evidence": [
                {
                    "id": "E1",
                    "type": "LIVE_BEHAVIOR",
                    "repository_ref": "abc",
                    "observed_at": "2026-09-09T10:00:00Z",
                }
            ],
            "dod_matrix": [{"dod_id": "D1", "status": "PASS", "evidence_refs": ["E1"]}],
        }
        errors, warnings = vl.lint_packet(doc)
        self.assertEqual(errors, [])
        self.assertEqual(warnings, [])

    def test_stale_receipt_is_error(self) -> None:
        doc = {
            "identity": {"head_ref": "new"},
            "claims": [],
            "evidence": [
                {
                    "id": "E1",
                    "type": "FOCUSED_TEST",
                    "repository_ref": "old",
                    "observed_at": "2026-09-09T10:00:00Z",
                }
            ],
            "dod_matrix": [],
        }
        errors, _ = vl.lint_packet(doc)
        self.assertTrue(any("possible stale evidence" in message for message in errors))

    def test_receipt_below_frozen_minimum_is_error(self) -> None:
        doc = {
            "identity": {"head_ref": "abc"},
            "claims": [
                {
                    "id": "C1",
                    "statement": "frontend flow works",
                    "truth_class": "OBSERVED",
                    "verification_status": "VERIFIED",
                    "minimum_receipt": "LIVE_BEHAVIOR",
                    "evidence_refs": ["E1"],
                }
            ],
            "evidence": [
                {
                    "id": "E1",
                    "type": "FOCUSED_TEST",
                    "repository_ref": "abc",
                    "observed_at": "2026-09-09T10:00:00Z",
                }
            ],
            "dod_matrix": [],
        }
        errors, _ = vl.lint_packet(doc)
        self.assertTrue(any("below minimum LIVE_BEHAVIOR" in message for message in errors))

    def test_global_verified_claim_requires_exhaustive_receipt(self) -> None:
        doc = {
            "identity": {"head_ref": "abc"},
            "claims": [
                {
                    "id": "C1",
                    "statement": "no regressions",
                    "truth_class": "OBSERVED",
                    "verification_status": "VERIFIED",
                    "minimum_receipt": "FOCUSED_TEST",
                    "evidence_refs": ["E1"],
                }
            ],
            "evidence": [
                {
                    "id": "E1",
                    "type": "FOCUSED_TEST",
                    "repository_ref": "abc",
                    "observed_at": "2026-09-09T10:00:00Z",
                }
            ],
            "dod_matrix": [],
        }
        errors, _ = vl.lint_packet(doc)
        self.assertTrue(any("global/negative wording" in message for message in errors))

    def test_dod_pass_requires_receipt(self) -> None:
        doc = {
            "identity": {"head_ref": "abc"},
            "claims": [],
            "evidence": [],
            "dod_matrix": [{"dod_id": "D1", "status": "PASS", "evidence_refs": []}],
        }
        errors, _ = vl.lint_packet(doc)
        self.assertIn("packet: DoD D1 PASS with no evidence_refs", errors)

    def test_unknown_cannot_be_verified(self) -> None:
        doc = {
            "identity": {"head_ref": "abc"},
            "claims": [
                {
                    "id": "C1",
                    "statement": "production behavior is correct",
                    "truth_class": "UNKNOWN",
                    "verification_status": "VERIFIED",
                    "minimum_receipt": "DEPLOYED_ARTIFACT",
                    "evidence_refs": ["E1"],
                }
            ],
            "evidence": [
                {
                    "id": "E1",
                    "type": "DEPLOYED_ARTIFACT",
                    "repository_ref": "abc",
                    "observed_at": "2026-09-09T10:00:00Z",
                }
            ],
            "dod_matrix": [],
        }
        errors, _ = vl.lint_packet(doc)
        self.assertIn("packet: C1 cannot be UNKNOWN and VERIFIED", errors)


if __name__ == "__main__":
    unittest.main()
