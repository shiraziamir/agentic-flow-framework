---
name: blind-spot-audit
description: Perform a cold, read-only falsification pass for common sources of false confidence after evidence exists and before medium/high-risk closure.
metadata:
  class: COMMON
  authority: portable-agentic-flow
---

# Blind-Spot Audit

**Updated:** 2026-09-09T10:04:00Z

## USE WHEN

- HIGH-risk closure;
- MEDIUM-risk closure where evidence is non-trivial;
- report makes broad/global claims;
- previous task/review found false-complete states;
- reviewer suspects tests may not exercise the real changed path.

Do not use as ritual on tiny EVIDENCE_ONLY edits.

## COLD REVIEW ORDER

To reduce anchoring, prefer:

1. frozen task/DoD + change classification;
2. actual base/head diff and identity;
3. raw/bounded receipts and verification profile;
4. independently chosen falsifying checks;
5. only then compare with executor narrative/status report.

## CHECKLIST

Challenge at least the applicable categories:

- **Identity:** wrong/stale commit, dirty tree, wrong artifact/image/config/environment.
- **Scope:** unexpected file/consumer/surface omitted from classification.
- **Path:** passing test/cache/mock/fallback bypasses the changed code.
- **Method:** proxy check substituted for exact acceptance gate; baseline not comparable.
- **Frontend:** user-visible/error/loading/permission/browser console/network path omitted.
- **Backend:** authz/validation/error/retry/transaction/provider boundary omitted.
- **Shared:** affected consumer/public contract/package/generated schema omitted.
- **Data:** existing-data migration/rollback/idempotency/write-read behavior omitted.
- **Infra/CI:** skipped stage/check, wrong target, mutable tag/artifact mismatch, no real trigger/deploy receipt.
- **Security:** positive path tested without relevant negative/tenant/ownership path.
- **Reliability:** flaky retry, race, cache, timeout, fallback, tail latency or log-query boundary hidden.
- **Reporting:** `all/none/no regression/secure/production-ready` wording exceeds finite verification boundary.
- **Judgment:** model/human reviewer opinion is being used as evidence for a behavior it did not observe.

## OUTPUT

```text
PASS | FAIL | INCONCLUSIVE
blind spots checked
falsifying checks performed
findings
claims that must be narrowed/reclassified
missing/stale evidence
recommended disposition
```

## MUTATION AUTHORITY

NONE. Do not repair the reviewed work in the same pass.
