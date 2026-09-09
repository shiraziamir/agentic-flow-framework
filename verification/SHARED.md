# Verification Profile — SHARED / PUBLIC CONTRACT

**Version:** 1.0  
**Updated:** 2026-09-09T10:04:00Z

Use for shared libraries, types, schemas, utilities and public contracts consumed by multiple modules/services/clients.

## Core checks

1. identify affected consumers mechanically where possible (project/import/dependency graph);
2. build/typecheck/package the changed shared surface;
3. run focused tests for the shared implementation;
4. build/test affected consumers, not only the producer;
5. verify backward/forward compatibility according to the frozen contract;
6. when API/message/schema behavior changes, run contract verification through actual consumer/provider boundary code where practical;
7. verify generated declarations/schema/artifacts are synchronized;
8. verify forbidden dependency/layer edges remain forbidden.

## Receipt rules

- Producer tests alone do not prove consumer compatibility.
- Type compatibility does not prove runtime serialization/protocol compatibility.
- Contract tests should exercise real consumer boundary/client code rather than hand-constructed requests when feasible.

## Shared blind spots

- one consumer discovered manually while other dependents are missed;
- source package passes but built/published artifact differs;
- default/optional/null semantics change silently;
- enum/discriminator/serialization change breaks older consumer;
- import path/package export changes break runtime despite local source resolution;
- circular/layering dependency introduced;
- schema generated file stale;
- contract over-constrained by tests that assert irrelevant provider details;
- contract under-tests a consumer branch it actually depends on.

For TypeScript repositories, project references or a build-system project graph can provide mechanical dependency evidence and reduce whole-repo guessing.
