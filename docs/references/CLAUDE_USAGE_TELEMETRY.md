# Claude Code Usage Telemetry Sources

**Checked:** 2026-09-12

This note records why Agentic Flow supports optional Claude Code quota snapshots and which parts are stable vs implementation-dependent.

## Anthropic / Claude Code evidence

Official Claude Code repository issue (Aug 20, 2026):

- https://github.com/anthropics/claude-code/issues/88111
- reports that statusLine stdin includes `rate_limits.five_hour` and `seven_day` and discusses additional per-model weekly windows;
- also references `cachedUsageUtilization` in `~/.claude.json`.

Earlier official Claude Code repository requests document the historical gap and the meaning of the displayed usage windows:

- https://github.com/anthropics/claude-code/issues/34301
- https://github.com/anthropics/claude-code/issues/23078
- https://github.com/anthropics/claude-code/issues/34497

These show that `/status` / `/usage` expose current session/5-hour and weekly utilization and that the data comes from Claude Code rate-limit telemetry.

## Stability classification

```text
/status or /usage displayed utilization       product behavior
statusLine rate_limits fields                 preferred programmatic source when present
~/.claude.json cachedUsageUtilization         implementation-dependent fallback
transcript scraping                           not required / not recommended for quota snapshot
```

Anthropic's public documentation does not currently define `~/.claude.json cachedUsageUtilization` as a stable external API contract. Consumers must tolerate absence/schema changes and report `UNAVAILABLE` rather than invent values.

## Flow consequence

Agentic Flow normalizes observed values and records source/freshness. It does not treat quota telemetry as engineering evidence, and low quota never authorizes reducing required verification quality.
