# Primary Sources and Engineering References

**Version:** 1.2  
**Updated:** 2026-09-14  
**Purpose:** human/reference index; not always-on agent context.

This file records the main external sources used to design Agentic Flow Framework. Canonical framework policy lives in `ARCHITECTURE.md`; these links are evidence/research inputs, not independent authority. Time-sensitive vendor behavior must be rechecked when it affects a decision.

## Agent harness, context, prompting and skills

| Organization | Source | Used for |
|---|---|---|
| OpenAI | https://openai.com/index/harness-engineering/ | repository-first agent harnesses, concise instruction maps, versioned plans/docs, deterministic enforcement, agent-legible runtime evidence |
| OpenAI | https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api | clear/specific instructions, delimiters, explicit formats/examples |
| OpenAI | https://help.openai.com/en/articles/10032626 | iterative prompt refinement and clear prompt design |
| Anthropic | https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices | clarity, structured prompts, examples, agentic autonomy/safety, avoiding over-eager coding/test gaming |
| Anthropic | https://platform.claude.com/docs/en/agents-and-tools/tool-use/manage-tool-context | tool/context bloat, lazy tool loading, context editing, batching/programmatic tool use |
| Anthropic | https://platform.claude.com/docs/en/manage-claude/usage-cost-api | observable token/cache/usage accounting |
| Claude Code | https://github.com/anthropics/claude-code/issues/88111 | current status-line `rate_limits.five_hour` / `seven_day` behavior and presence of `cachedUsageUtilization`; used only as time-sensitive harness evidence, not as a stable API guarantee |
| Claude Code | https://github.com/anthropics/claude-code/issues/34301 | historical/current-session and weekly usage telemetry semantics and rate-limit source context |
| Claude Code | https://github.com/anthropics/claude-code/issues/23078 | `/status`/`/usage` account-quota visibility and historical programmatic-access gap |
| Anthropic | https://platform.claude.com/docs/en/test-and-evaluate/develop-tests | measurable success criteria, evaluation design and edge cases |
| Anthropic | https://platform.claude.com/docs/en/managed-agents/define-outcomes | independent/outcome grading in separate context |
| Google | https://ai.google.dev/gemini-api/docs/prompting-strategies | precise/direct prompts, consistent structure, critical instruction placement, long-context structuring |
| Gemini CLI | https://google-gemini.github.io/gemini-cli/docs/cli/gemini-md.html | hierarchical project context files and modular imports |
| OpenCode | https://opencode.ai/docs/rules | concise committed `AGENTS.md`, modular/lazy references and precedence |
| OpenCode | https://opencode.ai/docs/skills | on-demand `SKILL.md` discovery/loading |

For the stability classification of Claude Code quota sources, see `docs/references/CLAUDE_USAGE_TELEMETRY.md`.

## Verification, frontend, contracts and code boundaries

| Organization | Source | Used for |
|---|---|---|
| Playwright | https://playwright.dev/docs/best-practices | user-visible frontend verification rather than implementation-detail-only tests |
| Pact | https://docs.pact.io/consumer | consumer contract tests exercising the real client boundary |
| TypeScript | https://www.typescriptlang.org/docs/handbook/project-references | logical project boundaries and affected/dependency structure |
| Microsoft | https://learn.microsoft.com/en-us/azure/architecture/patterns/anti-corruption-layer | adapters/anti-corruption layers around volatile/legacy external semantics |
| Microsoft | https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/architectural-principles | dependency inversion, modular/testable design principles |
| Microsoft | https://learn.microsoft.com/en-us/azure/well-architected/reliability/design-patterns | reliability patterns selected for specific failure modes |
| Martin Fowler | https://martinfowler.com/bliki/MutationTesting.html | mutation testing as a way to prove tests detect meaningful defects; selective/manual mutation for load-bearing tests |

## System modeling, threat review and business-logic safety

| Organization | Source | Used for |
|---|---|---|
| OWASP | https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html | early system modeling, data flows, trust boundaries, threat identification, review/validation |
| OWASP | https://cheatsheetseries.owasp.org/cheatsheets/Secure_Code_Review_Cheat_Sheet.html | data-flow review, trust zones, transaction integrity, race conditions, resource limits and rollback/error-path review |
| OWASP | https://cheatsheetseries.owasp.org/cheatsheets/Business_Logic_Security_Cheat_Sheet.html | business-process threat questions: ordering, repeats, concurrent actors, value-producing operations and abuse cases |
| OWASP | https://cheatsheetseries.owasp.org/cheatsheets/Secure_Coding_with_AI_Cheat_Sheet.html | trust boundaries and least-privilege considerations for agentic coding environments |

## DevOps, delivery and testing

| Organization | Source | Used for |
|---|---|---|
| Google Cloud / DORA | https://cloud.google.com/blog/products/devops-sre/using-the-four-keys-to-measure-your-devops-performance | deployment frequency, lead time, change failure rate, time to restore service |
| Google Cloud / DORA | https://cloud.google.com/resources/state-of-devops | software delivery performance research context |
| Microsoft | https://learn.microsoft.com/en-us/azure/well-architected/operational-excellence/safe-deployments | progressive exposure, health gates, rollout abort/rollback and safe deployment |
| Microsoft | https://learn.microsoft.com/en-us/azure/well-architected/operational-excellence/testing | layered continuous testing, production-like/ephemeral environments, testing proportionate to risk |
| Microsoft | https://learn.microsoft.com/en-us/azure/well-architected/mission-critical/mission-critical-deployment-testing | mission-critical staging/deployment testing and production-like validation |
| Google SRE | https://sre.google/sre-book/testing-reliability/ | testing reliability across layers, non-hermetic production/configuration checks and detecting integrated-path mismatches |
| Google SRE | https://sre.google/workbook/canarying-releases/ | canarying and closing the gap between test environments and real production traffic |
| GitHub | https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches | required checks can be successful/skipped/neutral; green gate is not proof every test ran |

## Observability, SRE, logs and metrics

| Organization | Source | Used for |
|---|---|---|
| Google SRE | https://sre.google/sre-book/monitoring-distributed-systems/ | symptom/cause distinction and four golden signals: latency, traffic, errors, saturation |
| Google SRE | https://sre.google/workbook/alerting-on-slos/ | SLI/SLO/error-budget alerting |
| Google SRE | https://sre.google/workbook/monitoring/ | testing monitoring/alert behavior and validating that operational signals actually fire as expected |
| Prometheus | https://prometheus.io/docs/practices/instrumentation/ | instrumentation and metric design |
| Prometheus | https://prometheus.io/docs/practices/naming/ | metric naming/units/labels |
| Prometheus | https://prometheus.io/docs/practices/alerting/ | actionable symptom-oriented alerts |
| OpenTelemetry | https://opentelemetry.io/docs/specs/otel/logs/data-model/ | structured log model, timestamps/severity/resource/TraceId/SpanId |
| OpenTelemetry | https://opentelemetry.io/docs/specs/otel/logs/ | logs/traces correlation model |
| Kubernetes | https://kubernetes.io/docs/concepts/cluster-administration/logging/ | cluster-level logging lifecycle beyond pod/node lifetime |
| Kubernetes | https://kubernetes.io/docs/concepts/cluster-administration/observability/ | metrics/logs/traces as primary observability signals |

## Database durability, caching and recovery

| Organization | Source | Used for |
|---|---|---|
| PostgreSQL | https://www.postgresql.org/docs/current/backup.html | backup approaches and restore requirements |
| PostgreSQL | https://www.postgresql.org/docs/current/continuous-archiving.html | WAL archiving and point-in-time recovery |
| MySQL | https://dev.mysql.com/doc/refman/8.4/en/point-in-time-recovery-binlog.html | full backup plus binary logs for PITR |
| Microsoft | https://learn.microsoft.com/en-us/azure/well-architected/reliability/ | reliability/recovery design and rehearsal principles |
| Microsoft | https://learn.microsoft.com/en-us/azure/architecture/patterns/cache-aside | cache-aside semantics, origin/source relationship, staleness and failure fallback considerations |

## Secure development and supply chain

| Organization | Source | Used for |
|---|---|---|
| OWASP | https://owasp.org/www-project-application-security-verification-standard/ | versioned application-security verification requirements |
| OWASP | https://owasp.org/www-project-samm/ | risk-driven secure-development maturity across the SDLC |
| OWASP | https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html | sensitive-data/log hygiene, integrity/access considerations |
| OWASP GenAI | https://genai.owasp.org/llmrisk/llm01-prompt-injection/ | indirect prompt injection from external/log content, segregation and least privilege |
| NIST | https://csrc.nist.gov/pubs/sp/800/218/final | SSDF 1.1 final secure-software-development framework |
| NIST | https://csrc.nist.gov/projects/ssdf/publications | SSDF publication/version status; 1.2 draft tracked separately from final baseline |
| CISA | https://www.cisa.gov/securebydesign | secure-by-design/default principles and ownership of customer security outcomes |
| SLSA | https://slsa.dev/spec/v1.2/build-track-basics | SLSA v1.2 build provenance assurance levels |
| GitHub | https://docs.github.com/en/code-security/concepts/supply-chain-security/dependency-review | direct/transitive dependency, vulnerability and license review |
| GitHub | https://docs.github.com/en/pull-requests/how-tos/review-pull-requests/reviewing-dependency-changes-in-a-pull-request | dependency-review limitations and manifest/source-diff review |

## Resilience and chaos engineering

| Organization | Source | Used for |
|---|---|---|
| Principles of Chaos | https://principlesofchaos.org/ | steady state, hypothesis, real-world failures, bounded experiments and falsification |
| Netflix | https://medium.com/netflix-techblog/chaos-engineering-upgraded-878d341f15fa | Netflix chaos engineering evolution and controlled resilience testing |
| Netflix | https://netflixtechblog.medium.com/tips-for-high-availability-be0472f2599c | availability/recovery engineering context |

## Microsoft Well-Architected / operational maturity

| Source | Used for |
|---|---|
| https://learn.microsoft.com/en-us/azure/well-architected/what-is-well-architected-framework | reliability/security/operational excellence/performance/cost as joint workload concerns |
| https://learn.microsoft.com/en-us/azure/well-architected/operational-excellence/principles | operational-excellence design principles |
| https://learn.microsoft.com/en-us/azure/well-architected/mission-critical/mission-critical-design-principles | recovery rehearsal, failure practice and mission-critical operational design |

## Research notes inside this repository

Dated interpretation/evidence notes are under `research/`, including context/model routing, bootstrap/supervision, adaptive governance/token efficiency, execution retrospective, verification blind spots, production engineering, and project profiles/testing/environments/patterns. These notes may summarize or interpret the links above; when they disagree with canonical policy, `ARCHITECTURE.md` wins.