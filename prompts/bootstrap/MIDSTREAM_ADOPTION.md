# Bootstrap prompt — Midstream Adoption

**Version:** 1.0  
**Updated:** 2026-09-09T11:30:00Z

```text
Adopt Agentic Flow while preserving the current active coding state.

Do not mutate product code until the adoption snapshot is complete.

Read `docs/agent/MIDSTREAM_ADOPTION.md` and follow it exactly.

Required snapshot:
- repository HEAD/branch;
- dirty paths;
- current issue/task if known;
- observed goal;
- work already done;
- tests already run and their refs/environments;
- known failures;
- active runtime/environment mutations;
- existing agent instruction files;
- unresolved scope.

Then reconcile the remaining work with the framework. Do not discard valid edits, retroactively claim framework review/authorization, or silently widen scope.

Return the adoption snapshot, conflicts, remaining task/amendment, project-profile/gap state, adapter changes and the next authorization required.
```
