#!/usr/bin/env python3
from claude_usage_snapshot import from_cache, from_statusline, unavailable


def main() -> None:
    status = from_statusline({
        "rate_limits": {
            "five_hour": {"utilization": 0.15, "resets_at": 111},
            "seven_day": {"utilization": 0.23, "resets_at": 222},
        }
    })
    assert status is not None
    assert status["source"] == "CLAUDE_STATUSLINE_RATE_LIMITS"
    assert status["session"]["used_percent"] == 15.0
    assert status["session"]["remaining_percent"] == 85.0
    assert status["weekly"]["used_percent"] == 23.0
    assert status["weekly"]["remaining_percent"] == 77.0

    cache = from_cache({
        "cachedUsageUtilization": {
            "fetchedAtMs": 0,
            "utilization": {
                "limits": [
                    {"kind": "session", "percent": 15},
                    {"kind": "weekly_all", "percent": 23},
                ]
            },
        }
    })
    assert cache is not None
    assert cache["source"] == "CLAUDE_JSON_CACHED_USAGE_UTILIZATION"
    assert cache["session"]["used_percent"] == 15.0
    assert cache["weekly"]["remaining_percent"] == 77.0

    missing = unavailable("x")
    assert missing["source"] == "UNAVAILABLE"
    assert missing["session"]["remaining_percent"] is None
    assert missing["weekly"]["remaining_percent"] is None

    print("claude_usage_snapshot self-tests: 3 scenarios PASS")


if __name__ == "__main__":
    main()
