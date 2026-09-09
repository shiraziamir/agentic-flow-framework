# Production Profile — Security First

**Version:** 1.0  
**Updated:** 2026-09-09T10:40:00Z

Goal: make security part of design, implementation, delivery and operations instead of a final scan.

## Framework references

Use these as references, not badges:

- OWASP ASVS for verifiable application security requirements;
- OWASP SAMM for risk-driven secure-development maturity;
- NIST SSDF for secure software development practices integrated into the SDLC;
- CISA Secure by Design for ownership of customer security outcomes, secure defaults and transparency;
- SLSA for software build provenance/supply-chain integrity.

A claim such as `OWASP compliant`, `secure by design` or `SLSA L2` requires versioned scoped evidence. Functional green tests are not a security assessment.

## Security throughout the lifecycle

### Design

- classify data and trust boundaries;
- identify internet/public/admin/tenant boundaries;
- threat model high-risk flows and privileged actions;
- choose secure defaults and minimize required customer/operator hardening;
- identify dependency/provider/supply-chain trust;
- avoid unnecessary privileges, exposed endpoints and persistent secrets.

### Development

- validate inputs at trust boundaries;
- encode output/context safely;
- use centralized, well-tested authn/authz mechanisms;
- enforce authorization server-side at object/tenant/action level;
- use parameterized database access and safe serializers/parsers;
- handle secrets via secret stores/identity, not source/config history;
- fail closed for security-sensitive checks;
- avoid leaking sensitive details in errors/logs;
- use memory-safe languages/safer APIs where practical and material to threat model.

### CI / supply chain

- dependency and license review;
- vulnerability scanning appropriate to ecosystem;
- secret scanning;
- SAST/linters where signal is useful;
- container/IaC/Kubernetes scanning when those surfaces exist;
- SBOM where required by profile/ecosystem/customer needs;
- provenance and immutable artifact identity according to chosen SLSA target;
- protected signing/deployment credentials with least privilege.

### Runtime

- least privilege identities/RBAC;
- network exposure limited to need;
- TLS and certificate lifecycle managed;
- secure headers/cookies/session settings for web applications;
- audit/security event logging without secrets;
- rate/abuse controls where relevant;
- vulnerability/patch ownership and response SLA;
- backups protected as sensitive assets;
- incident response and break-glass access defined for material systems.

## BASIC

- no secrets committed;
- dependency ownership/update path;
- authn/authz negative tests for protected flows;
- input/security-boundary checks appropriate to application;
- least-privilege production identity where platform supports it;
- security findings/gaps explicit.

## STANDARD

Additionally:

- documented threat/security boundary review for exposed/privileged flows;
- automated secret/dependency/vulnerability checks;
- scoped ASVS/secure-coding requirements for relevant application type;
- SBOM if material to supply-chain/customer operations;
- patch/vulnerability triage ownership and deadlines;
- production security/audit telemetry and incident path;
- tenant/ownership/object-level authorization tests when multi-tenant;
- infrastructure/container/Kubernetes hardening checks when present.

## HIGH_ASSURANCE

Additionally, where applicable:

- formal threat model and abuse cases kept current with architecture;
- independent security review/penetration testing for critical releases/boundaries;
- stronger SLSA/provenance target and verification;
- security regression suite mapped to versioned requirements;
- privileged admin/break-glass actions strongly audited;
- key/secret rotation and compromise recovery rehearsed;
- vulnerability disclosure/response process where product exposure warrants it;
- customer-security-impacting gaps require explicit risk acceptance and expiry.

## Security-first pattern selection

Patterns are chosen to reduce risk, not to decorate architecture. Examples:

- adapter/anti-corruption layer isolates untrusted/external semantics;
- circuit breaker/bulkhead limits cascading dependency failure;
- explicit dependency injection reduces hidden privileged/global dependencies;
- separate command/read/admin interfaces can narrow authorization surfaces;
- centralized policy enforcement avoids divergent one-off checks.

## Gaps

Never hide:

- security scanning not implemented;
- threat model absent where required;
- authz tested only for positive path;
- high/critical known vulnerability accepted without owner/expiry;
- secrets/PII present in logs;
- mutable/untraceable production artifact;
- dependency/SBOM/provenance coverage incomplete;
- admin or automation identity is overprivileged;
- backup copies have weaker access controls than live data;
- production security monitoring or incident ownership undefined.