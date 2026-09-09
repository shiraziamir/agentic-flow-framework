# Research note — DevOps-friendly, security-first production engineering

**Date:** 2026-09-09  
**Framework target:** v1.6  
**Status:** research/evidence, not policy authority

Canonical policy lives in `ARCHITECTURE.md`. This note records the primary/current sources used for v1.6.

## 1. Google SRE: measure user-facing reliability

Google SRE's monitoring guidance emphasizes symptom vs cause, black-box plus white-box monitoring, and the four golden signals: latency, traffic, errors and saturation. The SRE Workbook recommends alerting from SLIs/SLOs and error budgets so pages correspond to meaningful user-impact reliability consumption.

Sources:
- https://sre.google/sre-book/monitoring-distributed-systems/
- https://sre.google/workbook/alerting-on-slos/

Framework implication: production observability starts with user/service outcomes and actionable alerts, then drills into causes. Metrics/logs/traces are receipts, not monitoring theater.

## 2. Google DORA: DevOps performance is throughput + stability

DORA/Google's Four Keys measure deployment frequency, lead time for changes, change failure rate and time to restore service. Deployment frequency/lead time measure delivery throughput; change failure/time-to-restore measure stability. These are system-level outcome measures, not proof that any particular pipeline/tool is good.

Sources:
- https://cloud.google.com/blog/products/devops-sre/using-the-four-keys-to-measure-your-devops-performance
- https://cloud.google.com/resources/state-of-devops

Framework implication: a DevOps-friendly project should make delivery events reconstructible enough to measure improvement where valuable, without gaming metrics or ranking individuals.

## 3. Microsoft Well-Architected: reliability, security and operations are joint design concerns

Microsoft's current Azure Well-Architected guidance evaluates workloads through Reliability, Security, Cost Optimization, Operational Excellence and Performance Efficiency. Current safe-deployment guidance emphasizes small/incremental quality-gated changes, progressive exposure, health models, failure detection and stopping/recovering when gates fail. Mission-critical guidance recommends rehearsing recovery, practicing failure, security monitoring/incident response, threat testing and continuous validation. IaC supports predictable/repeatable deployment and drift control.

Sources:
- https://learn.microsoft.com/en-us/azure/well-architected/what-is-well-architected-framework
- https://learn.microsoft.com/en-us/azure/well-architected/operational-excellence/safe-deployments
- https://learn.microsoft.com/en-us/azure/well-architected/operational-excellence/principles
- https://learn.microsoft.com/en-us/azure/well-architected/mission-critical/mission-critical-design-principles
- https://learn.microsoft.com/en-us/azure/well-architected/mission-critical/mission-critical-deployment-testing
- https://learn.microsoft.com/en-us/azure/architecture/patterns/deployment-stamp

Framework implication: readiness must scale by business/risk/complexity; operations and recovery are design inputs, not post-release chores. Progressive exposure without meaningful health/abort gates is ceremony.

## 4. Netflix / Chaos Engineering: controlled experiments, not random destruction

The Principles of Chaos Engineering define a measurable steady state, a hypothesis that it persists, introduction of real-world failure variables and attempts to disprove the hypothesis. Netflix's Chaos Monkey experience intentionally terminated production instances because server failures were inevitable and teams needed services resilient to them. Netflix also emphasizes automated unit/integration/smoke/canary validation before production.

Sources:
- https://principlesofchaos.org/
- https://medium.com/netflix-techblog/chaos-engineering-upgraded-878d341f15fa
- https://netflixtechblog.medium.com/tips-for-high-availability-be0472f2599c

Framework implication: production chaos is maturity-gated and requires observability, recovery, bounded blast radius and abort controls. Small/low-risk projects are not required to run Chaos Monkey.

## 5. OWASP + NIST + CISA: security belongs inside the SDLC

OWASP ASVS supplies versioned application-security verification requirements. OWASP SAMM is risk-driven and technology/process agnostic, designed to measure and improve the full secure-development lifecycle. NIST SP 800-218 SSDF 1.1 is the current final SSDF; NIST published SSDF 1.2 as a draft in December 2025, so v1.6 treats 1.1 as the final baseline unless a project explicitly evaluates the draft. CISA Secure by Design emphasizes taking ownership of customer security outcomes, transparency/accountability and secure-by-default products.

Sources:
- https://owasp.org/www-project-application-security-verification-standard/
- https://owasp.org/www-project-samm/
- https://csrc.nist.gov/pubs/sp/800/218/final
- https://csrc.nist.gov/projects/ssdf/publications
- https://www.cisa.gov/news-events/news/applying-secure-design-thinking-events-news
- https://www.cisa.gov/sites/default/files/2023-06/principles_approaches_for_security-by-design-default_508c.pdf

Framework implication: security posture is scoped evidence plus explicit gaps; `secure` is not a badge inferred from functional tests or scanner output.

## 6. SLSA: artifact provenance is incremental

SLSA v1.2 is the current approved specification. Its Build track increases assurance from L1 provenance exists, to L2 signed provenance from a hosted build platform, to L3 hardened builds.

Sources:
- https://slsa.dev/spec/v1.2/build-track-basics
- https://slsa.dev/spec/v1.2/tracks

Framework implication: projects select a provenance target proportional to supply-chain risk. Never claim a SLSA level from the existence of CI alone.

## 7. Prometheus + OpenTelemetry: observable systems need disciplined telemetry

Prometheus recommends bounded label cardinality, labels rather than procedurally generated metric names, consistent units, and symptom-oriented actionable alerting. OpenTelemetry's stable log data model includes timestamps, severity, resource, attributes and TraceId/SpanId and describes correlating logs with traces/resources.

Sources:
- https://prometheus.io/docs/practices/instrumentation/
- https://prometheus.io/docs/practices/naming/
- https://prometheus.io/docs/practices/alerting/
- https://opentelemetry.io/docs/specs/otel/logs/data-model/
- https://opentelemetry.io/docs/specs/otel/logs/

Framework implication: metrics/logs/traces should be correlated and cost-aware; user IDs/emails are not Prometheus labels; raw logs are not the only debugging substrate.

## 8. Kubernetes: logs need a lifecycle beyond pods/nodes

Kubernetes documentation states application logs are important for debugging/monitoring but container runtime logging alone is not a complete solution. Cluster-level logging requires storage/lifecycle independent of nodes, pods and containers. Kubernetes observability documentation treats metrics, logs and traces as the three primary signals.

Sources:
- https://kubernetes.io/docs/concepts/cluster-administration/logging/
- https://kubernetes.io/docs/concepts/cluster-administration/observability/

Framework implication: a Kubernetes project that loses logs with pod/node lifecycle has an explicit operability gap when incident retention is required.

## 9. Database recovery: backup is incomplete until restore is proven

PostgreSQL documents SQL dump, filesystem backup and continuous WAL archiving/PITR as different approaches; PITR requires base backup plus necessary WAL. MySQL point-in-time recovery uses a full backup plus subsequent binary logs.

Sources:
- https://www.postgresql.org/docs/current/backup.html
- https://www.postgresql.org/docs/current/continuous-archiving.html
- https://dev.mysql.com/doc/refman/26.7/en/point-in-time-recovery-binlog.html

Framework implication: RPO/RTO choose the method; `backup enabled` is not recoverability evidence. Restore drills measure actual recovery.

## 10. AI-assisted log analysis creates new trust/privacy boundaries

OWASP Logging guidance recommends not directly logging access tokens, passwords, encryption keys, database connection strings and sensitive PII and discusses protecting logs against unauthorized access/modification. OWASP LLM01:2025 identifies indirect prompt injection in external content and recommends content segregation, least privilege and approval for high-risk actions. OpenTelemetry provides trace/resource fields that allow deterministic correlation before LLM reasoning.

Sources:
- https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html
- https://genai.owasp.org/llmrisk/llm01-prompt-injection/
- https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html
- https://opentelemetry.io/docs/specs/otel/logs/data-model/

Framework implication: logs are untrusted data, not instructions. AI log analysis should use bounded/redacted packets, read-only discovery, exact query/time-window provenance and normal authorization for remediation.

## 11. Evolvable architecture: isolate volatile semantics and failure domains

Microsoft's Anti-Corruption Layer pattern recommends an adapter/facade between systems with different semantics so outside/legacy dependencies do not constrain internal design. Microsoft's architectural principles describe dependency inversion as a path to loosely coupled, testable, modular and maintainable applications. Reliability patterns include circuit breaker, retry, bulkhead, idempotent consumer, health endpoint, rate limiting and saga, but each pattern addresses a specific failure mode and adds complexity.

Sources:
- https://learn.microsoft.com/en-us/azure/architecture/patterns/anti-corruption-layer
- https://learn.microsoft.com/th-th/dotnet/architecture/modern-web-apps-azure/architectural-principles
- https://learn.microsoft.com/en-us/azure/well-architected/reliability/design-patterns
- https://learn.microsoft.com/en-us/azure/architecture/best-practices/transient-faults

Framework implication: adapters/DI/patterns are conditional tools protecting real change/failure boundaries, not mandatory layers for every small codebase.

## 12. v1.6 design conclusions

The framework separates:

```text
codebase scale      SMALL | MEDIUM | LARGE
readiness tier      BASIC | STANDARD | HIGH_ASSURANCE
```

Risk overrides size. Production readiness is assessed across build/delivery, observability, data durability, troubleshooting, security/supply chain, resilience and code evolvability. Missing or unverified requirements become durable operational gaps instead of being hidden by a broad `production-ready` claim.