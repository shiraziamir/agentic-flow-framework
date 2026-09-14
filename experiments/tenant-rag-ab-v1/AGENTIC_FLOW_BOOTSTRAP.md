# Arm B Bootstrap — Agentic Flow 1.11

You are implementing TenantRAG Mini using Agentic Flow Framework 1.11.

Use the same `PROJECT_SPEC.md` and currently released queue item as Arm A. Product requirements must not be strengthened, weakened, or rewritten merely because the framework exists.

Adopt Agentic Flow before product mutation with:

```yaml
operating_preset: PRODUCT_STANDARD
project_mode:
  mode: PRODUCT_BUILD
```

Use `STRICT_PREVIEW` unless current canonical policy gives a narrower safe path. Create only triggered framework artifacts; do not preload the whole framework.

This project is stateful, tenant-scoped, cost-sensitive and release-oriented, so a System Truth Map is applicable. Update it as architecture evolves; do not treat it as runtime proof.

Prefer the same base model/provider/harness used for Arm A. Role separation may use fresh contexts because that is part of the treatment, but do not silently upgrade models.

Use risk-adaptive ceremony: LOW/local work stays compact; MEDIUM/HIGH gets deeper preflight/review; money, tenant isolation, durability/recovery, destructive state and production semantics receive explicit System-Lens treatment; one bounded remediation round is default; Independent Judge only when policy/risk requires it. Do not create approval spam or checklist theater.

For each queue item: recover durable state; classify the work and preserve the primary objective; apply the current Agentic Flow workflow proportionately; implement and verify; perform required Local/System Lens review; close/remediate within authorized scope; commit with prefix `QNN`; append factual metrics to `RUN_RECORD.md`; checkpoint state; then continue only to the next item.

Q06 is intentionally a small operational detour. Keep it bounded and do not let it replace the product objective.

Do not inspect evaluator-only material or future queue items when prompts are released one at a time.

After Q12 closure and commit, stop all mutation and record the frozen HEAD. No post-freeze repair is allowed before comparison.
