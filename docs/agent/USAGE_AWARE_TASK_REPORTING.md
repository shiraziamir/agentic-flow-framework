# Usage-Aware Task Reporting

**Agent-facing optional capability. Load only when the current harness exposes trustworthy quota telemetry or the operator asks for it.**

## Goal

After a material task/turn, append a compact usage snapshot so the operator can see whether another expensive task should continue now, switch model/tier, or wait for reset.

Quota reporting is advisory. It must never replace engineering evidence or silently reduce verification quality.

## Report shape

When telemetry is available:

```text
Usage
- session: 15% used / 85% remaining
- weekly: 23% used / 77% remaining
- source: CLAUDE_STATUSLINE_RATE_LIMITS
- freshness: live/current event
```

When only a local cache is available:

```text
Usage
- session: 15% used / 85% remaining
- weekly: 23% used / 77% remaining
- source: CLAUDE_JSON_CACHED_USAGE_UTILIZATION
- cache age: 118s
```

When unavailable:

```text
Usage
- session: unavailable
- weekly: unavailable
- source: UNAVAILABLE
```

Never write `0% used` or `100% remaining` merely because telemetry is missing.

## Claude Code

Normalize observable telemetry with:

```bash
python3 <framework>/scripts/claude_usage_snapshot.py
```

If a statusLine JSON payload is available, pipe/pass that payload so the helper can prefer `rate_limits` telemetry. Otherwise the helper best-effort reads `~/.claude.json` and labels that source explicitly.

The normalized schema is `schemas/USAGE_QUOTA_SNAPSHOT.md`.

## End-of-task behavior

If the project/operator enables quota reporting, a material completion/status message should end with one compact quota section. Do not repeatedly query or print quota during every minor tool call.

Recommended cadence:

```text
material task completion
material checkpoint / handoff
before starting a known high-cost task when remaining quota is low
operator notification (Telegram/Slack/etc.)
```

## Routing guidance

Quota may inform an explicit recommendation such as:

```text
weekly remaining 8% -> recommend deferring non-urgent broad exploration
session remaining 5% -> checkpoint durable state before another large task
```

But it must not cause:

```text
skip required tests
weaken closure claims
avoid a required security check
silently switch to a weaker model for a judgment task
```

If a routing change affects quality/risk, report the tradeoff and obtain the normal authorization when required.
