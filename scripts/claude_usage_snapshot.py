#!/usr/bin/env python3
"""Normalize observable Claude Code usage-limit telemetry.

Preferred input is a Claude Code statusLine JSON payload on stdin/file when it
contains rate_limits.five_hour / seven_day. Fallback is ~/.claude.json's
cachedUsageUtilization cache. Missing or unrecognized data stays unavailable.
No prompts, responses, credentials, or transcripts are read or stored.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path
from typing import Any


def _num(value: Any) -> float | None:
    if isinstance(value, (int, float)):
        return float(value)
    try:
        if value is not None and str(value).strip() != "":
            return float(value)
    except (TypeError, ValueError):
        pass
    return None


def _pct_from_obj(obj: Any) -> float | None:
    if not isinstance(obj, dict):
        return None
    for key in ("percent", "used_percentage", "percentage"):
        value = _num(obj.get(key))
        if value is not None:
            return value
    util = _num(obj.get("utilization"))
    if util is not None:
        return util * 100.0 if 0 <= util <= 1 else util
    return None


def _reset_from_obj(obj: Any) -> Any:
    if not isinstance(obj, dict):
        return None
    for key in ("resets_at", "resetsAt", "reset_at", "resetAt"):
        if obj.get(key) not in (None, ""):
            return obj.get(key)
    return None


def _window(kind: str, obj: Any) -> dict[str, Any]:
    used = _pct_from_obj(obj)
    if used is not None:
        used = max(0.0, min(100.0, used))
        remaining = max(0.0, min(100.0, 100.0 - used))
    else:
        remaining = None
    return {
        "kind": kind,
        "used_percent": used,
        "remaining_percent": remaining,
        "resets_at": _reset_from_obj(obj),
    }


def from_statusline(payload: dict[str, Any]) -> dict[str, Any] | None:
    limits = payload.get("rate_limits") or payload.get("rateLimits")
    if not isinstance(limits, dict):
        return None
    five = limits.get("five_hour") or limits.get("fiveHour") or limits.get("session")
    seven = limits.get("seven_day") or limits.get("sevenDay") or limits.get("weekly_all")
    if not isinstance(five, dict) and not isinstance(seven, dict):
        return None
    return {
        "schema_version": "1.0",
        "provider": "anthropic",
        "harness": "claude-code",
        "source": "CLAUDE_STATUSLINE_RATE_LIMITS",
        "observed_at_unix": int(time.time()),
        "source_age_seconds": 0,
        "session": _window("session_5h", five or {}),
        "weekly": _window("weekly_7d_all", seven or {}),
    }


def from_cache(payload: dict[str, Any]) -> dict[str, Any] | None:
    cached = payload.get("cachedUsageUtilization")
    if not isinstance(cached, dict):
        return None
    util = cached.get("utilization")
    if not isinstance(util, dict):
        return None
    limits = util.get("limits")
    if not isinstance(limits, list):
        return None
    by_kind = {item.get("kind"): item for item in limits if isinstance(item, dict)}
    session = by_kind.get("session")
    weekly = by_kind.get("weekly_all")
    if not isinstance(session, dict) and not isinstance(weekly, dict):
        return None
    fetched_ms = _num(cached.get("fetchedAtMs"))
    age = None
    if fetched_ms is not None:
        age = max(0, int(time.time() - fetched_ms / 1000.0))
    return {
        "schema_version": "1.0",
        "provider": "anthropic",
        "harness": "claude-code",
        "source": "CLAUDE_JSON_CACHED_USAGE_UTILIZATION",
        "observed_at_unix": int(time.time()),
        "source_age_seconds": age,
        "session": _window("session_5h", session or {}),
        "weekly": _window("weekly_7d_all", weekly or {}),
    }


def unavailable(reason: str) -> dict[str, Any]:
    return {
        "schema_version": "1.0",
        "provider": "anthropic",
        "harness": "claude-code",
        "source": "UNAVAILABLE",
        "observed_at_unix": int(time.time()),
        "source_age_seconds": None,
        "session": _window("session_5h", {}),
        "weekly": _window("weekly_7d_all", {}),
        "reason": reason,
    }


def load_json(path: Path | None) -> dict[str, Any] | None:
    try:
        if path is None:
            if sys.stdin.isatty():
                return None
            raw = sys.stdin.read()
        else:
            raw = path.read_text(encoding="utf-8")
        value = json.loads(raw)
        return value if isinstance(value, dict) else None
    except (OSError, json.JSONDecodeError):
        return None


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--statusline-json", type=Path)
    ap.add_argument("--claude-json", type=Path, default=Path.home() / ".claude.json")
    ap.add_argument("--max-cache-age", type=int, default=900,
                    help="seconds; stale cache is reported but not fabricated")
    args = ap.parse_args()

    status_payload = load_json(args.statusline_json)
    result = from_statusline(status_payload or {}) if status_payload else None

    if result is None and args.claude_json.exists():
        cache_payload = load_json(args.claude_json)
        result = from_cache(cache_payload or {}) if cache_payload else None
        if result and result.get("source_age_seconds") is not None:
            result["stale"] = result["source_age_seconds"] > args.max_cache_age

    if result is None:
        result = unavailable("no recognized Claude Code rate-limit telemetry")

    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
