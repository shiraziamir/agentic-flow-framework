# Shared Product Queue — 12 Fixed Prompts

Use this queue unchanged for both experiment arms. Release prompts strictly in order. Best mode is one prompt at a time. Do not repair or rewrite earlier prompts after seeing implementation results.

Each prompt is the complete operator message for that queue item. After finishing an item, commit with prefix `QNN` and record metrics before moving on.

## Q01 — Build the first working vertical slice

Build the first usable version of TenantRAG Mini from `PROJECT_SPEC.md`.

I want a FastAPI service where a tenant can ingest a text document, ask a question, retrieve the top relevant chunks using a deterministic offline retrieval method, and get a deterministic answer plus citations.

Use a local deterministic answer provider behind an interface so we can replace or instrument it later. Add focused tests for the happy path and obvious invalid input. Document how to install, run, and test the service.

Keep the implementation small. Do not add production infrastructure or features that have not been requested.

Done when another engineer can clone the repo, run the tests, start the API, ingest a document, query it, and see citations.

## Q02 — Make business state survive restart

The prototype now needs durable local state.

Move document/chunk state that matters to the product into SQLite. A fresh application instance using the same database file must still be able to query documents ingested before restart.

Add an appropriate small schema/bootstrap/migration mechanism and a test that creates data, tears down/recreates the application/runtime boundary, and proves the data is still usable. Do not change external product behavior unnecessarily.

## Q03 — Enforce tenant isolation and real deletion

We are preparing for multiple early tenants.

Make tenant isolation explicit and test it. Tenant A must never retrieve, inspect, delete, update, aggregate, or otherwise receive Tenant B's data through tenant-facing behavior.

Add document deletion. After deletion, its content must no longer appear in retrieval or answers for that tenant.

Add negative tests, not only happy paths. Keep the public API coherent.

## Q04 — Add a query cache without changing truth

Queries are starting to repeat. Add a bounded in-process query-result cache with configurable TTL.

Requirements: entries are tenant-scoped; a hit does not invoke the answer provider; ingest/update/delete that can change an answer prevents stale results; cache memory is bounded; restart may lose cache but not durable business state.

Expose enough instrumentation to prove provider call vs cache hit. Test hit, miss, expiration, tenant separation, and invalidation. Do not introduce Redis or another external service.

## Q05 — Add tenant budgets and authoritative provider cost

Add a monthly per-tenant provider budget.

Each actual answer-provider attempt has configurable simulated cost. The authoritative record of spend must be durable in SQLite.

Required behavior: each real provider attempt contributes to spend exactly once; cache hits cost zero; a tenant cannot begin a new paid attempt when doing so would exceed budget; expose current monthly budget/spend; if authoritative spend cannot be read reliably, do not substitute `0.0` or pretend budget is healthy; all behavior remains tenant-scoped.

Add tests around budget boundaries and cache hits.

## Q06 — Small operational detour: cache reset and counters

Small operational request before we continue product work.

Add an admin operation that resets/rebuilds derived query-cache state for one tenant without deleting durable documents or authoritative spend ledger.

Also expose simple process-local counters for at least query requests, provider attempts, and cache hits.

Keep this change deliberately small. Do not redesign unrelated architecture just because this admin endpoint exists. Add focused tests proving cache reset does not reset durable documents or financial truth.

## Q07 — Add document versioning and trustworthy provenance

We need document edits.

Add document update/versioning. When a document changes, the next version becomes current and stale cached answers must not survive the update.

Every answer citation must identify enough provenance to know which document version and chunk produced it.

Updating records a newer version rather than silently rewriting provenance; new queries use current version; old versions may remain for history but not normal retrieval; deletion still prevents retrieval; tenant isolation remains intact.

Test update → cache invalidation → new answer/citation provenance.

## Q08 — Make provider failure and retry semantics financially correct

The answer provider can fail transiently now.

Add controlled retry behavior: at most 2 provider attempts total per query request. The deterministic test provider must be configurable to fail/succeed in a known sequence.

Every cost-bearing provider attempt that starts must be recorded exactly once even if the overall query ultimately fails. Retries must not disappear from spend. If authoritative cost/budget state is unavailable, block new paid attempts. An already valid cached answer may still be served without provider call. Never report unknown spend as zero.

Return clear errors for exhausted retries or unavailable authoritative financial state. Add behavioral tests including “provider attempt costs money, then request fails”.

## Q09 — Handle duplicate/concurrent work safely

Clients retry requests.

Add idempotency for document ingestion/update. Reusing the same idempotency key for the same tenant and same operation must not create duplicate durable document/version state.

Harden for the experiment's local concurrency target: concurrent duplicate ingestion must not create multiple logical copies; provider-attempt accounting must not double-count or lose attempts; budget enforcement must not allow obvious overspend due to concurrent stale reads; SQLite transaction/locking behavior should be intentional and tested.

Keep the solution appropriate for one process and one SQLite DB; do not build distributed locking.

## Q10 — Add recovery behavior, backup/restore, and safe admin repair

We need to know what survives failure.

Add documented/testable recovery behavior: process restart continues from durable state; losing in-memory cache is safe; admin can clear/rebuild derived state without changing authoritative documents, versions, or spend; provide a simple SQLite backup and restore procedure; add at least one automated restore/readback test or equivalent deterministic recovery test.

The goal is not enterprise backup tooling. The goal is proving that “backup exists” differs from “restore works”.

## Q11 — Prepare a realistic release candidate

Prepare the service to be run by another engineer as a release candidate.

Add `/healthz` for process liveness; `/readyz` that reflects whether required durable state can support normal requests; a lightweight metrics endpoint or documented machine-readable metrics output; environment-based config with example; Dockerfile; clear database initialization/migration commands; and a short production-like runbook covering startup, backup, restore, expected health signals, abort condition, and rollback or forward-recovery for bad deployment/config/database change.

Do not claim Kubernetes/cloud readiness. This is a small single-instance service. Run the meaningful full test suite at the end.

## Q12 — Freeze candidate: harden, do not add features

This is the final product prompt before freeze.

Do not add new product features. Treat the repository as a release candidate and perform one bounded hardening pass.

Review the complete implementation, tests, and operational path for material defects in requested behavior. Pay particular attention to tenant isolation; authoritative vs derived state; cost/budget accounting; cache invalidation; restart/restore; provider failure/retry; concurrency/idempotency; admin operations; health/readiness truth; and unnecessary complexity/scope growth.

Fix only material defects inside existing requirements. Run appropriate final tests and produce a concise release report stating what changed, what was actually tested, what remains unverified, and how to recover from a bad release.

After this item is committed, STOP. The repository is frozen for evaluator comparison.
