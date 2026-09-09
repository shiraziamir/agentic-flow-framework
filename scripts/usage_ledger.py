#!/usr/bin/env python3
"""Append and report privacy-safe agent usage events.

No provider SDK required. Feed observable provider/harness counters; unknown values stay null.
The script never stores prompts, responses, reasoning, or transcripts.
"""
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

DEFAULT = Path('.agentic/usage/events.jsonl')
ALLOWED_ROLES = {
    'ORCHESTRATOR', 'CHEAP_READONLY', 'EXECUTION_TIER',
    'JUDGMENT_TIER', 'INDEPENDENT_REVIEWER'
}


def read_events(path: Path):
    if not path.exists():
        return []
    out = []
    for line in path.read_text(encoding='utf-8').splitlines():
        try:
            out.append(json.loads(line))
        except (ValueError, TypeError):
            continue
    return out


def record(args):
    if args.role not in ALLOWED_ROLES:
        raise SystemExit(f'unknown role: {args.role}')
    rec = {
        'schema_version': '1.0',
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'task_id': args.task_id,
        'phase': args.phase,
        'agent_role': args.role,
        'provider': args.provider,
        'model': args.model,
        'source': args.source,
        'usage': {
            'input_tokens': args.input_tokens,
            'cache_read_input_tokens': args.cache_read_tokens,
            'cache_creation_input_tokens': args.cache_creation_tokens,
            'output_tokens': args.output_tokens,
            'total_context_tokens': args.context_tokens,
            'estimated_cost_usd': args.cost_usd,
        },
        'operations': {'tool_calls': args.tool_calls, 'child_agents': args.child_agents},
        'waste_flags': args.waste_flag or [],
        'note': args.note,
        'evidence_refs': args.evidence_ref or [],
    }
    args.log.parent.mkdir(parents=True, exist_ok=True)
    with args.log.open('a', encoding='utf-8') as fh:
        fh.write(json.dumps(rec, ensure_ascii=False) + '\n')
    print(json.dumps(rec, indent=2, ensure_ascii=False))


def report(args):
    events = read_events(args.log)
    if args.task_id:
        events = [e for e in events if e.get('task_id') == args.task_id]
    totals = defaultdict(float)
    by_role = defaultdict(lambda: defaultdict(float))
    flags = defaultdict(int)
    for e in events:
        usage = e.get('usage') or {}
        role = e.get('agent_role') or 'UNKNOWN'
        for key in ('input_tokens', 'cache_read_input_tokens', 'cache_creation_input_tokens', 'output_tokens', 'estimated_cost_usd'):
            val = usage.get(key)
            if isinstance(val, (int, float)):
                totals[key] += val
                by_role[role][key] += val
        for flag in e.get('waste_flags') or []:
            flags[flag] += 1
    print(f'events: {len(events)}')
    print('totals:')
    for key, value in sorted(totals.items()):
        print(f'  {key}: {value:g}')
    print('by_role:')
    for role in sorted(by_role):
        print(f'  {role}:')
        for key, value in sorted(by_role[role].items()):
            print(f'    {key}: {value:g}')
    print('waste_flags:')
    if flags:
        for flag, count in sorted(flags.items(), key=lambda x: (-x[1], x[0])):
            print(f'  {flag}: {count}')
    else:
        print('  none recorded')
    print('\nCaveat: totals cover only instrumented events; missing telemetry is unknown, not zero.')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--log', type=Path, default=DEFAULT)
    sub = ap.add_subparsers(dest='cmd', required=True)

    p = sub.add_parser('record')
    p.add_argument('--task-id')
    p.add_argument('--phase', required=True)
    p.add_argument('--role', required=True)
    p.add_argument('--provider', required=True)
    p.add_argument('--model')
    p.add_argument('--source', default='UNKNOWN')
    p.add_argument('--input-tokens', type=int)
    p.add_argument('--cache-read-tokens', type=int)
    p.add_argument('--cache-creation-tokens', type=int)
    p.add_argument('--output-tokens', type=int)
    p.add_argument('--context-tokens', type=int)
    p.add_argument('--cost-usd', type=float)
    p.add_argument('--tool-calls', type=int)
    p.add_argument('--child-agents', type=int)
    p.add_argument('--waste-flag', action='append')
    p.add_argument('--evidence-ref', action='append')
    p.add_argument('--note')
    p.set_defaults(func=record)

    p = sub.add_parser('report')
    p.add_argument('--task-id')
    p.set_defaults(func=report)

    args = ap.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()
