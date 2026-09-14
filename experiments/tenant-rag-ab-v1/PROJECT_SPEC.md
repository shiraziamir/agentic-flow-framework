# TenantRAG Mini — Shared Project Specification

Both experiment arms receive this specification unchanged.

## Product goal

Build a small multi-tenant document Q&A service for early SaaS tenants. A tenant can ingest text documents and ask questions. The service retrieves relevant document chunks and uses a provider abstraction to generate a deterministic answer with citations.

The project is deliberately local-first and testable without paid/network AI services.

## Required stack

- Python 3.12+
- FastAPI
- SQLite as durable local database
- pytest
- no required external cloud service
- no required model download

Additional dependencies are allowed when justified, but keep the implementation small and reproducible.

## Core concepts

### Tenant

Every business object belongs to one `tenant_id`. No tenant may read, retrieve, delete, mutate, aggregate, or administer another tenant's data through normal tenant-scoped APIs.

### Document

A document has:

```text
document_id
tenant_id
version
text
created_at / updated_at
```

The implementation may normalize/chunk text internally.

### Retrieval

Retrieval must be deterministic and offline. A simple lexical/BM25/TF-IDF/token-overlap implementation is acceptable. The evaluator cares about deterministic relevance behavior, not a particular retrieval library.

Default `top_k = 3`.

### Answer provider

Use a provider interface/adapter. The default test provider is deterministic and local; it must expose enough instrumentation to know when an actual provider attempt occurred.

A query response should contain an answer, citations with document/version/chunk provenance, and whether the result was cached. Exact additional fields are implementation-defined.

### Cost

A provider attempt can have a configurable simulated monetary cost. Cost is business truth, not merely telemetry. Later queue items define exact accounting semantics.

## API shape

Exact route naming may evolve through the queue, but normal tenant-facing operations must support ingest/create document, query/answer, update/version document, delete document, and tenant cost/budget status. Admin/health/metrics/recovery operations are introduced later.

Tenant identity may be represented by path/header as long as it is consistent, validated, and testable.

## Non-goals

Do not build a frontend, real authentication/OIDC, real external LLM calls, a vector database, Kubernetes/Terraform, or distributed multi-region behavior.

## Current target scale

```text
20 early tenants
<= 2,000 documents per tenant
<= 10 MB text per tenant for this experiment
<= 20 concurrent local requests in evaluator stress cases
single service instance
single SQLite database
```

Not claimed: 10,000 concurrent users, multi-region availability, unbounded document sizes, or zero-downtime distributed migrations.

## Global product invariants

1. Tenant isolation is never optional.
2. Durable business truth must survive application restart.
3. Cached/derived state must not silently become authoritative state.
4. A delete must eventually make deleted content unavailable to retrieval and answers.
5. Unknown/unavailable authoritative financial state must never be represented as a real numeric zero.
6. Real/simulated provider attempts must be distinguishable from cache hits.
7. No hidden real network/paid provider calls are necessary for success.
8. The service should fail clearly rather than fabricate success when a required durable dependency is unavailable.
9. The final repository must be runnable and testable by another engineer from documented commands.

## Repository expectations

By freeze keep at minimum: README setup/run/test commands, application source, tests, SQLite schema/migration/bootstrap, Dockerfile, example configuration, and backup/restore or recovery instructions introduced by the queue. Arm B may contain additional `.agentic/` control/evidence artifacts because those are part of Agentic Flow.

## Environment constraint

The implementation must be testable locally without secrets. Optional integrations must use controlled local substitutes in tests.
