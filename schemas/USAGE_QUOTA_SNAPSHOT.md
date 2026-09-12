# Usage Quota Snapshot

**Schema version:** 1.0  
**Updated:** 2026-09-12

Use this optional schema when an agent harness exposes observable subscription/rate-limit utilization. It is operational telemetry, not a task-completion receipt.

```yaml
usage_quota:
  provider: <provider>
  harness: <harness>
  source: <exact source identifier>
  observed_at: <time or epoch>
  source_age_seconds: <integer|null>
  stale: <true|false|unknown>
  session:
    window: <name>
    used_percent: <number|null>
    remaining_percent: <number|null>
    resets_at: <time|null>
  weekly:
    window: <name>
    used_percent: <number|null>
    remaining_percent: <number|null>
    resets_at: <time|null>
```

## Rules

1. Never fabricate quota values. Missing telemetry is `UNAVAILABLE`, not zero.
2. `remaining_percent` may be derived as `100 - observed used_percent`; label the source of the used value.
3. Preserve source freshness. A stale cache may still be useful for notification but must be marked stale.
4. Prefer provider/harness-supported telemetry over private implementation caches.
5. A local cache path that is not a documented public contract is a fallback and may break after updates.
6. Do not read/store credentials, prompts, responses, chain-of-thought, or full transcripts to obtain quota values.
7. Quota telemetry may influence routing/scheduling recommendations, but may not silently lower the task acceptance/evidence bar.
8. Reports and notifications should make clear whether percentages are **used** or **remaining**.

## Claude Code source preference

For current Claude Code integrations, prefer:

```text
1. statusLine payload rate_limits.five_hour / rate_limits.seven_day when present
2. ~/.claude.json cachedUsageUtilization as a best-effort local fallback
3. UNAVAILABLE
```

The cache path is intentionally classified as implementation-dependent. Flow consumers must tolerate its absence or schema change.
