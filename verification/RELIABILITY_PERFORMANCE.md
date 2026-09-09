# Verification Annex — RELIABILITY / PERFORMANCE

**Version:** 1.0  
**Updated:** 2026-09-09T10:04:00Z

Use for performance, concurrency, cache/state, external providers, retries/timeouts, observability or other failure-under-load/partial-failure behavior.

## Core checks

1. define the measurable claim and comparable baseline before testing;
2. identify environment, dataset/workload, concurrency, duration/sample count and relevant configuration;
3. repeat measurements enough to expose variance rather than relying on one lucky run;
4. exercise timeout/retry/cancellation/partial failure when those semantics changed;
5. exercise concurrency/shared-state behavior when races/ordering matter;
6. verify cache actually includes or bypasses the changed path according to the claim;
7. verify external-provider failure/fallback semantics without assuming provider availability;
8. inspect logs/metrics/traces when the task claims operational improvement or absence of hidden failures;
9. distinguish throughput/latency/resource/error-rate dimensions rather than collapsing them into `faster`;
10. state measurement uncertainty and validity boundary.

## Receipt rules

- One timing sample is not a reliable performance claim.
- A cache hit can hide the changed implementation path.
- Repeated retries can hide an unstable failure while increasing latency/cost/side effects.
- `no errors in logs` is only bounded by the queried time range, source and filter.
- External-provider success during one smoke does not prove resilience to timeout/rate-limit/partial response.

## Blind spots

- baseline and treatment use different environment/config/data;
- warm cache vs cold cache mismatch;
- percentile tail regression hidden by average;
- retry storm/duplicate side effect;
- race only appears under parallel execution;
- observability query misses another service/namespace/time range;
- fallback silently returns stale/incomplete data;
- rate-limit/quota/cost impact omitted;
- benchmark includes startup/build time in one side but not the other;
- improvement is within run-to-run noise.
