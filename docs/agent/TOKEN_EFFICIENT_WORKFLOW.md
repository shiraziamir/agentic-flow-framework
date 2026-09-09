# Token-Efficient Agent Workflow

**Agent-facing practical guide.** Use this when work is long, multi-agent, repository-wide, log-heavy, or cost-sensitive.

## Goal

Reduce token/context waste **without weakening acceptance quality**.

The primary rule is:

> Use deterministic tools for deterministic facts, small context for bounded work, and stronger model judgment only where ambiguity remains.

## Recommended workflow

```text
1. Read current task / profile pointers
2. Identify the affected surface
3. Use deterministic discovery first
4. Load only relevant files/profiles/skills
5. Delegate bounded read-only discovery when useful
6. Implement a bounded change
7. Run focused verification
8. Escalate only unresolved ambiguity/evidence conflicts
9. Hand off compact receipts, not transcripts
10. Store durable checkpoint; release cold context
```

## 1. Start from a small working set

Normal context should usually contain:

```text
ARCHITECTURE map
current task / amendment / classification
current project/profile/gap/override pointers
relevant source files
selected verification profiles
selected production profiles
0–3 triggered skills
current receipts / unresolved facts
```

Do not preload all operator docs, research, completed tasks, incidents, judgments, profiles, skills, or logs.

## 2. Deterministic first

Prefer these before asking a model to rediscover the same facts:

```text
grep / ripgrep
AST / dependency graph
linters
schema validators
test selectors
repository queries
JSON/YAML parsing
digests / file identity
CI status / deployment identity
bounded log queries
```

The Python helpers shipped with this framework are examples of deterministic checks. See `docs/operator/USING_PYTHON_TOOLS.en.md` for operator usage.

## 3. Read only the affected repository surface

Start from the task and dependency/consumer evidence. Expand only when the current evidence says another module or boundary is relevant.

Avoid whole-repository scans solely because the task is uncertain. Use a targeted discovery pass first.

## 4. Keep large telemetry out of model context

For logs/metrics/traces:

```text
query
→ filter
→ deduplicate
→ group episodes
→ preserve counts/time window/source
→ send bounded evidence packet to the model
```

Do not paste megabytes of raw logs when a deterministic reducer can isolate the relevant events.

## 5. Use cheaper/read-only workers for mechanical discovery

When the harness supports multiple agents/models, a cheaper read-only worker can handle:

- file/module inventory;
- repetitive classification;
- log reduction;
- independent partitions of a search space;
- locating references/consumers;
- mechanical documentation comparison.

The result must remain mechanically checkable. Do not give a cheap discovery worker mutation authority by default.

## 6. Escalate for judgment, not volume

Use stronger reasoning when there is:

- ambiguous root cause;
- conflicting evidence;
- security/authz/data impact;
- major public contract or architecture change;
- production/recovery risk;
- repeated failed attempts without a discriminating hypothesis;
- closure requiring independent judgment.

Do not escalate merely because there are many files.

## 7. Compact handoffs

A child-agent or session handoff should contain:

```text
what was checked
relevant paths / refs
observed facts
receipts
what was ruled out
remaining unknowns
recommended next discriminating action
```

Do not transfer full transcripts or chain-of-thought.

## 8. Avoid repeat-reading stable information

Promote stable findings into durable indexes/checkpoints rather than rereading the same large files after every reset.

Read cold history only when the current task needs regression, provenance, audit, incident, architecture-history or retrospective evidence.

## 9. Watch for token-waste patterns

Emit `TOKEN_WASTE_WARNING` when a material pattern appears, such as:

- unjustified whole-repo scan;
- repeated large-file rereads;
- full completed-task/history preload for ordinary work;
- raw-log dump instead of bounded query;
- expensive model doing mostly mechanical discovery;
- multiple agents searching the same surface with high overlap;
- more than two failed loops without new evidence;
- unnecessary always-loaded tools/docs;
- soft/hard budget breach.

Recommended warning shape:

```text
TOKEN_WASTE_WARNING
reason: <observable pattern>
current evidence: <what shows the waste>
smaller/cheaper alternative: <specific action>
quality guard: <why acceptance quality is unchanged>
operator decision needed: yes|no
```

## 10. Never trade away the evidence bar silently

These are **not** token optimizations:

```text
skip required integration test to save tokens
replace real boundary with mock to finish faster
downgrade HIGH risk to avoid review
accept scanner/config presence as runtime proof
omit restore/deployment evidence because it is expensive
```

If a cost/time constraint requires lowering the acceptance bar, make that an explicit operator decision and report the resulting gap/unknown.

## Practical rule of thumb

```text
mechanical fact       → script/query/tool
bounded discovery     → cheap/read-only worker when useful
implementation        → standard execution tier
architecture/security/root cause/closure ambiguity → stronger judgment tier
```

The cheapest workflow is the one that reaches adequate evidence with the fewest repeated loops—not the one that merely emits the fewest tokens in the first attempt.
