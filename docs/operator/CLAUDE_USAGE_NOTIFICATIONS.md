# Claude Code Usage Notifications

**Operator guide.** Use when you want completion notifications (Telegram, Slack, email, etc.) to include Claude Code session/weekly quota.

## What is confirmed

Claude Code displays account usage windows such as the current 5-hour/session utilization and current 7-day/all-models utilization. Current Claude Code builds may expose these windows to status-line integrations as `rate_limits.five_hour` and `rate_limits.seven_day`.

A second practical source observed in current builds is:

```text
~/.claude.json
  cachedUsageUtilization.utilization.limits
```

with entries such as:

```text
kind=session
kind=weekly_all
```

This local cache is useful but is not treated by Agentic Flow as a stable public API. It is fallback telemetry and may change.

## Recommended source order

```text
Claude Code statusLine rate_limits
→ ~/.claude.json cachedUsageUtilization
→ UNAVAILABLE
```

Use:

```bash
python3 <framework>/scripts/claude_usage_snapshot.py
```

Example normalized output:

```json
{
  "source": "CLAUDE_JSON_CACHED_USAGE_UTILIZATION",
  "source_age_seconds": 118,
  "session": {
    "used_percent": 15.0,
    "remaining_percent": 85.0
  },
  "weekly": {
    "used_percent": 23.0,
    "remaining_percent": 77.0
  }
}
```

## Telegram / notification pattern

Keep provider extraction separate from transport. Your Telegram hook should consume normalized values rather than duplicate Claude-specific parsing everywhere.

Example concept:

```bash
SNAPSHOT="$(python3 /path/to/agentic-flow-framework/scripts/claude_usage_snapshot.py)"
SESSION_USED="$(printf '%s' "$SNAPSHOT" | jq -r '.session.used_percent // "?"')"
SESSION_LEFT="$(printf '%s' "$SNAPSHOT" | jq -r '.session.remaining_percent // "?"')"
WEEKLY_USED="$(printf '%s' "$SNAPSHOT" | jq -r '.weekly.used_percent // "?"')"
WEEKLY_LEFT="$(printf '%s' "$SNAPSHOT" | jq -r '.weekly.remaining_percent // "?"')"
SOURCE="$(printf '%s' "$SNAPSHOT" | jq -r '.source')"

USAGE_TEXT="session ${SESSION_USED}% used / ${SESSION_LEFT}% left; weekly ${WEEKLY_USED}% used / ${WEEKLY_LEFT}% left; source=${SOURCE}"
```

If values are unavailable, send `usage unavailable`; do not substitute zero.

## Recommended completion notification

```text
Claude Code finished TASK-123 in project-x.
Result: PASS (focused tests 12/12).
Usage: session 15% used / 85% left; weekly 23% used / 77% left.
Source: Claude statusLine rate limits.
```

For a stale cache:

```text
Usage: session 15% used / 85% left; weekly 23% used / 77% left (cache age 8m, stale).
```

## Hook security

- never print or persist bot tokens/API credentials in logs;
- keep transport credentials outside project source;
- quota extraction does not require transcript content;
- prefer Stop/status-line hooks that always fail open (`exit 0`) so notification failure cannot block agent completion;
- do not send source code, prompts, responses, secrets, or raw transcripts merely to report quota.

## Operational recommendation

Use quota as an operator signal, not an autonomous quality downgrade. Low remaining quota can trigger a checkpoint, notification, or recommendation to defer broad exploration. Required tests, security checks and evidence remain required.
