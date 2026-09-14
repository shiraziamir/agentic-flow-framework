# راهنمای اپراتور — Agentic Flow

**Runbook اصلی اپراتور. Agent نباید این فایل را دائماً preload کند مگر Task اپراتوری به آن نیاز داشته باشد.**  
**نسخه فریم‌ورک:** 1.10  
**به‌روزرسانی:** 2026-09-14

این سند توضیح عملیاتی واحد برای اپراتور است: چه نقشی چه کاری می‌کند، مدل اجراکننده و مدل مراقب چگونه جدا می‌شوند، چه Guardrailهایی فعال‌اند، `Dual-Lens` چطور جلوی «درست بودن محلی ولی غلط شدن کل سیستم» را می‌گیرد، و انسان کجا باید تصمیم واقعی بگیرد. Authority نهایی همچنان در `ARCHITECTURE.md` و Schemaهاست.

## ۱. مدل کنترل در یک نگاه

```text
PRODUCT OWNER / OPERATOR
WHY / WHAT / priority / business trade-offs / accepted risk / production authority
        │
        ├── greenfield یا معماری نامطمئن ──► PROJECT ARCHITECT (read-only)
        │                                      │
        │                                      ▼
        │                    architecture + System Truth Map + eval contract
        │                                      │
        ▼                                      ▼
DESIGNER / TASK ARCHITECT ──► MANAGER / REVIEWER ──► EXECUTOR
طراحی Task به‌صورت read-only      freeze + authority       اجرای محدود
                                                             │
                                                             ▼
                                                   LOCAL + SYSTEM LENS
                                                             │
                                                             ▼
                                                  COLD / ADVERSARIAL REVIEW
                                                             │
                                                             ▼
                                                  MANAGER CONSOLIDATED REVIEW
                                                             │
                                                    bounded remediation
                                                             │
                                                             ▼
                                               INDEPENDENT JUDGE (read-only)
                                                             │
                                                             ▼
                                                     OPERATOR decision
                                               merge / production / business risk
```

اصل مرکزی:

```text
Human transports authority and priority.
Repository transports engineering state.
```

## ۲. نقش‌ها و حدود اختیار

| نقش | مسئولیت اصلی | Mutation پیش‌فرض | Production mutation |
|---|---|---:|---:|
| Operator / Product Owner | هدف، اولویت، trade-off، ریسک و Production authority | اختیار انسانی | فقط تصمیم صریح انسان |
| Project Architect | تبدیل Product Intent به constraint، eval، System Truth Map و گزینه معماری | read-only | ممنوع |
| Designer / Task Architect | تبدیل هدف محدود به Task Contract | read-only | ممنوع |
| Manager / Reviewer | freeze کردن Task، کنترل authority، بررسی diff/receipt/System Lens | read/review | پیش‌فرض ممنوع |
| Executor | اجرای HOW داخل مرزهای freeze‌شده | bounded write | فقط با مجوز جداگانه Owner |
| Cold / Adversarial Reviewer | پیدا کردن defect و فرض غلط قبل از Manager | read-only | ممنوع |
| Independent Judge | closure مستقل برای HIGH-risk | read-only | ممنوع |

مدل متفاوت به‌تنهایی استقلال ایجاد نمی‌کند. استقلال واقعی تا جای ممکن باید در این چهار بعد باشد:

```text
IMPLEMENTATION
CONTEXT
AUTHORITY
EVIDENCE
```

و:

```text
MULTI-MODEL AGREEMENT != INDEPENDENT BEHAVIORAL EVIDENCE
```

## ۳. Modeهای پروژه

### `VIBE_PROTOTYPE`

فعال‌سازی:

```yaml
project_mode:
  mode: VIBE_PROTOTYPE
```

وقتی سؤال اصلی این است که «آیا ایده کار می‌کند؟» یا «کاربر این تجربه را دوست دارد؟» استفاده می‌شود. سرعت یادگیری اولویت دارد و بخشی از کد می‌تواند sacrificial باشد.

```text
VIBE_PROTOTYPE != PRODUCTION BASELINE
```

این Mode مجوز Production readiness، داده حساس یا Production mutation نمی‌دهد. عبور به `PRODUCT_BUILD` نیازمند re-baseline، Architecture Checkpoint و دسته‌بندی کد Prototype است:

```text
REUSE_AS_IS | REUSE_AFTER_REVIEW | REWRITE | DISCARD
```

### `PRODUCT_BUILD`

برای ساخت Product baseline. Product constraint، quality/eval contract، `System Truth Map` و تصمیم‌های معماری باربر باید قبل از رشد وسیع featureها روشن باشند.

### `MAINTENANCE`

برای پروژه‌ای با baseline معتبر. اگر boundary مهم عوض شد یا Swamp Guard drift ساختاری دید، دوباره به Architecture Discovery برگردید.

## ۴. شروع پروژه از صفر

ایده نباید مستقیم به Executor داده شود:

```text
PRODUCT INTENT
→ PRODUCT BRIEF
→ QUALITY / EVAL CONTRACT
→ ARCHITECTURE DISCOVERY
→ SYSTEM TRUTH / DATA AUTHORITY MAP
→ CURRENT SCALE BOUNDARY
→ 2–3 MINIMAL OPTIONS
→ LOAD-BEARING DECISIONS
→ WALKING SKELETON
→ ARCHITECTURE CHECKPOINT
→ PRODUCT BASELINE
→ NORMAL TASK FLOW
```

اپراتور سؤال محصول را جواب می‌دهد، نه سؤال تخصصی دیتابیس یا framework: کاربر کیست، outcome چیست، رفتار غیرقابل قبول چیست، privacy/freshness/latency/cost چقدر مهم است و چه trade-off تجاری قابل قبول است.

برای AI/RAG، tuning جدی روی chunking، embedding، top-k، reranking، prompt یا vector vendor قبل از eval baseline نماینده ممنوع است.

راهنما: `docs/agent/PROJECT_INCEPTION_ARCHITECTURE.md`  
نقشه سیستم: `schemas/SYSTEM_TRUTH_MAP.md`  
Prompt: `prompts/operator/PROJECT_ARCHITECT.md`

## ۵. Dual-Lens — هر تغییر با دو نگاه

هر تغییر material باید هم‌زمان با دو لنز دیده شود:

```text
LOCAL LENS
آیا خود تغییر درست پیاده‌سازی شده است؟

SYSTEM LENS
بعد از این تغییر، کل سیستم چه حقیقتی را ادعا می‌کند؟
```

### Local Lens

حداقل بررسی می‌کند:

- call path واقعی؛
- business invariant؛
- failure semantics؛
- resource/cleanup behavior؛
- تست هدفمند و regression مرتبط؛
- mutation/path proof برای تست‌های باربر.

### System Lens

پروژه یک `System Truth Map` کوچک نگه می‌دارد که شامل اجزا، trust boundaryها، منبع authoritative داده، cache/projectionها، رفتار restart/failure/recovery، tenant isolation و مرز مقیاس فعلی است.

برای هر Task material این ماتریس مرور می‌شود:

```text
WRITE
READ
AGGREGATE
CACHE
RESTART
FAILURE
RECOVERY
ADMIN
METRIC
TENANT_ISOLATION
SCALE
PRIVACY
COST
```

برای هر سطر فقط یکی از این وضعیت‌ها مجاز است:

```text
UNAFFECTED
VERIFIED
CHANGED_AND_TESTED
OPEN_RISK
NOT_APPLICABLE
```

قواعد مهم:

- `UNAFFECTED` نتیجه بررسی است، نه مقدار پیش‌فرض.
- cache، projection، summary یا metric صرفاً چون خواندنش راحت است authoritative نمی‌شود.
- `OPEN_RISK` باید تا زمان resolve/accept/defer/escalate شدن قابل مشاهده بماند.
- اگر authority، trust boundary، recovery rule یا scale boundary مادی عوض شد، `System Truth Map` باید update شود.
- سبز بودن یک تابع، claim سراسری سیستم را ثابت نمی‌کند.

## ۶. System Truth Map و Data Authority

برای پروژه‌های stateful، cost-sensitive، privacy-sensitive، tenant-aware یا Production-oriented، این نقشه باید پاسخ دهد:

```text
Entry points
Trust boundaries
Databases
Caches
Queues
External providers
Background workers
Admin operations
Metrics / alerts
Deployment / rollback / recovery
```

و برای داده باربر:

```text
Data name
Authoritative source
Derived/cached copies
Writer / readers
TTL/freshness
Maximum size/bound
Privacy class
Restart behavior
Failure behavior
Recovery procedure
Tenant isolation
```

مثلاً اگر «هزینه Provider» حقیقت مالی سیستم است، باید معلوم باشد authority آن PostgreSQL ledger است یا چیز دیگر؛ Redis projection نباید بی‌صدا authority شود.

## ۷. Threat/Failure review کوچک

هدف سند صدصفحه‌ای نیست. در شروع پروژه یا تغییر boundary باربر این سؤال‌ها مرور می‌شوند:

```text
What can leak?
What can be counted twice?
What can be silently lost?
What survives restart?
What becomes stale?
What can grow without a bound?
What happens under concurrency?
What happens when a dependency lies or partially fails?
What can one tenant do to another?
What can cause unexpected provider spend?
What can an administrator safely do later?
```

فقط risk و decision مادی ثبت می‌شود و به invariant، تست، STOP condition یا architecture boundary تبدیل می‌شود.

## ۸. Audit دوره‌ای سراسری

درست بودن تک‌تک Taskها تضمین نمی‌کند رابطه اجزا بعد از چند تغییر هنوز درست باشد.

Trigger پیشنهادی و قابل تنظیم:

```text
هر حدود 5–8 Task مادی (پیش‌فرض نمونه: 6)
قبل از Demo deployment مهم
قبل از release واقعی به مشتری
بعد از incident مادی
قبل/بعد از تغییر مهم data authority یا trust boundary
```

Audit روی این محورهاست:

```text
FINANCIAL TRUTH
PRIVACY TRUTH
IDENTITY / AUTHORIZATION
TENANT ISOLATION
RESTART SURVIVAL
BACKUP / RESTORE
OBSERVABILITY TRUTH
CAPACITY BOUNDS
EXTERNAL-PROVIDER FAILURE / SPEND
ADMIN RECOVERY
```

این مرحله full code review دوباره نیست؛ هدفش پیدا کردن drift بین اجزاست.

## ۹. Task Hierarchy — جلوگیری از گم‌شدن هدف اصلی

هر workstream فقط یک هدف durable اصلی دارد:

```text
PRIMARY_TASK = هدف اصلی فعلی
SIDE_TASK    = کار کمکی محدود
INTERRUPT    = وقفه فوری و محدود
```

قانون:

```text
RECENCY IS NOT PRIORITY.
CONVERSATIONAL MOMENTUM CANNOT PROMOTE A SIDE TASK.
```

هر `SIDE_TASK` باید `primary_task_ref`، success condition محدود، scope/budget، return condition و promotion authority داشته باشد. بعد از پایان، نتیجه ثبت می‌شود و Flow به Primary Task برمی‌گردد.

Promotion فقط با تصمیم صریح Manager/Operator انجام می‌شود. طولانی‌شدن بحث یا چند prompt پشت‌سرهم promotion نیست.

اگر Side Task بیش از حد round بخورد، معماری unrelated بسازد یا هدف de-facto شود:

```text
SIDE_TASK DRIFT
Recommended action: CLOSE | DEFER | PROMOTE_PROPOSAL
```

برای `INTERRUPT` ابتدا Primary Task و resume state دقیق checkpoint می‌شود.

## ۱۰. Lifecycle معمول Task

Risk و نوع کار جدا هستند:

```text
risk.level = LOW | MEDIUM | HIGH
work_kind  = IMPLEMENTATION | REMEDIATION | EVIDENCE_ONLY
```

Flow پیش‌فرض:

```text
LOW
execute → focused test → compact review

MEDIUM
short preflight → execute → Dual-Lens → cold review → one remediation → Manager review

HIGH
frozen contract
→ failure/System-Lens preflight
→ explicit apply authority
→ bounded execution
→ adversarial review
→ Manager consolidated findings
→ one remediation by default
→ read-only Independent Judge
→ Operator production/business decision
```

Round دوم remediation فقط با finding جدید و مادی قابل توجیه است.

## ۱۱. Task Contract باید چه چیزی داشته باشد؟

برای Task مادی حداقل:

```text
Goal
Invariants
Allowed mutation surface
Failure semantics
Acceptance tests
STOP conditions
```

برای MEDIUM/HIGH، الگوریتم یا pseudocode پیشنهادی مفید است تا reasoning قبل از edit دیده شود؛ اما تا وقتی owner آن را invariant نکرده، implementation script محسوب نمی‌شود.

Task Contract همچنین Local Lens و System Lens را ثبت می‌کند.

## ۱۲. تست رفتاری و Mutation Proof

فقط تست تابع کافی نیست وقتی claim کسب‌وکاری بزرگ‌تر است. سناریوهای واقعی متناسب با feature بررسی شوند: success، fallback/escalation، retry، partial external side effect، source-of-truth unavailable، restart/rebuild، boundary زمانی، admin recovery، cross-tenant و concurrency.

برای تست باربر، نشان دهید تست defect هدف را می‌گیرد. نمونه mutationها:

```text
remove tenant dimension from cache key
turn database/authority failure into zero or empty success
double-count aggregate data
remove lock / cleanup / readiness condition
skip rebuild after restart
```

Mutation فقط در محیط موقت/ایزوله انجام می‌شود. برای برگرداندن فایل از `git reset --hard` یا `git checkout --` استفاده نکنید؛ bytes نسخه اصلی را حفظ و restore را verify کنید.

## ۱۳. Authorityها عمداً جدا هستند

```text
TASK AUTHORITY
MUTATION AUTHORITY
ENVIRONMENT AUTHORITY
EXTERNAL-SIDE-EFFECT AUTHORITY
PRODUCTION AUTHORITY
```

Task approved به معنی source mutation، provider call یا production deploy نیست. برای adoption اولیه `STRICT_PREVIEW` مناسب است؛ editهای مرتبط را batch کنید تا approval spam ایجاد نشود.

## ۱۴. Swamp Guard

```text
CLEAR | WATCH | ALERT | STOP_REBASELINE
```

Signalهای مهم:

- redesign/remediation تکراری؛
- framework/datastore/abstraction بدون نیاز واقعی؛
- چند mechanism برای یک responsibility؛
- AI/RAG tuning بدون eval؛
- feature growth قبل از vertical slice واقعی؛
- تصمیم معماری فقط در chat؛
- source-of-truth مبهم؛
- workaround موقت که دائمی شده؛
- prototype با expectation production؛
- `SIDE_TASK` که توجه را از `PRIMARY_TASK` می‌دزدد؛
- System-Lens `OPEN_RISK`های تکراری؛
- cache/projection که بی‌تصمیم رسمی تبدیل به business authority شده است.

Alert:

```text
SWAMP ALERT: <WATCH|ALERT|STOP_REBASELINE>
Signal: ...
Evidence: ...
Why it matters: ...
Recommended action: ...
Continue allowed: YES|NO
Authority needed: <none|Manager|Operator>
```

## ۱۵. مدل مراقب و روند Review

Executor نباید کار material خودش را close کند.

برای MEDIUM/HIGH، Cold/Adversarial Reviewer قبل از Manager exact diff را بررسی می‌کند. Manager ترجیحاً این ترتیب را دنبال می‌کند:

```text
frozen contract
→ System Truth Map / engineering advisory
→ exact base/head / diff
→ surrounding source
→ raw tests / CI / receipts
→ Dual-Lens matrix / OPEN_RISKs
→ Executor narrative last
```

Manager findingها را یکجا می‌دهد و same-task fixها را داخل remediation window محدود می‌کند.

برای HIGH-risk، Independent Judge read-only است و source/diff/receipt را مستقل می‌سنجد. Judge حق edit، provider call یا production mutation ندارد.

## ۱۶. Evidence

```text
unit PASS          != integration proven
mock PASS          != real boundary proven
HTTP 200           != persistence proven
CI green           != deployed behavior proven
backup configured  != restore proven
reviewer PASS      != runtime evidence
three models PASS  != three independent engineers
```

پایین‌ترین Environment مجاز را استفاده کنید که changed path واقعی را exercise کند. اگر وجود ندارد نتیجه `UNVERIFIED` یا `BLOCKED` است.

## ۱۷. Handoff مبتنی بر Repository

اپراتور نباید message bus باشد. Session جدید باید از repo بتواند این موارد را پیدا کند:

```text
project mode / architecture baseline
System Truth Map ref/version
PRIMARY_TASK
active SIDE_TASK / INTERRUPT
resume state
exact base/head
frozen task contract
review findings
remediation window
receipts / gaps
System-Lens OPEN_RISKs
cross-system audit state
Swamp Guard state
closure state
next authority decision
```

## ۱۸. Production Control

قبل از هر Production mutation:

```text
exact target and change identity
success / health signals
abort condition
rollback OR explicit forward-recovery path
stateful/data rollback constraints
recovery authority/owner
post-change verification
```

```text
NO ROLLBACK / RECOVERY PLAN
→ NOT EXECUTION-READY FOR PRODUCTION MUTATION
```

اگر rollback امن نیست، forward recovery، backup/checkpoint، blast-radius control و STOP condition لازم است. Independent Judge read-only می‌ماند.

## ۱۹. Workspace Safety و External Effects

Dirty work با ownership نامعلوم state محافظت‌شده است. `reset/restore/clean` مخرب را صرفاً برای راحتی Agent استفاده نکنید.

Provider call واقعی، paid API، ارسال پیام، deployment و destructive data action authority جدا می‌خواهند.

## ۲۰. Routing مدل و هزینه

```text
Project Architect → reasoning قوی‌تر وقتی ambiguity معماری بالاست
Executor          → task-adequate / cost-efficient
Manager           → judgment قوی‌تر در صورت نیاز
Independent Judge → high reasoning + separate context
```

کاهش هزینه evidence/acceptance bar را پایین نمی‌آورد.

## ۲۱. اپراتور چه چیزهایی را دائماً چک کند؟

- Project Mode هنوز درست است؟
- `PRIMARY_TASK` هنوز صریح است؟
- Side Taskها محدودند؟
- Swamp Alert نادیده گرفته نشده؟
- `System Truth Map` هنوز با implementation باربر هم‌خوان است؟
- `OPEN_RISK`های System Lens جمع نشده‌اند؟
- Cross-System Audit عقب نیفتاده؟
- Architecture/Eval baseline هنوز واقعی است؟
- HEAD بررسی‌شده همان candidate است؟
- Receiptها current هستند و Claim بیش‌ازحد بزرگ نشده؟
- Restore/Recovery evidence کافی است؟
- Production authority به Reviewer/Judge نشت نکرده؟
- Governance خودش round-trip بی‌فایده نساخته؟

## ۲۲. Quick Start اپراتور

```text
1. README.md را بخوان.
2. .agentic/PROJECT_PROFILE.yaml را ایجاد/تأیید کن.
3. VIBE_PROTOTYPE | PRODUCT_BUILD | MAINTENANCE را انتخاب کن.
4. برای greenfield: Project Architect / Project Inception.
5. System Truth Map + Data Authority + Scale Boundary را بساز/تأیید کن.
6. یک PRIMARY_TASK ثبت کن.
7. Designer برای Task material، Contract + Dual-Lens preflight می‌دهد.
8. Manager freeze و authority محدود می‌دهد.
9. Executor اجرا و تست می‌کند.
10. Local Lens + System Lens → Cold review → Manager findings → یک remediation.
11. HIGH-risk → Independent Judge در صورت نیاز.
12. Cross-System Audit را در triggerهای پروژه اجرا کن.
13. Operator درباره production/business risk تصمیم می‌گیرد.
14. Repository state را به session بعد منتقل می‌کند.
```

## ۲۳. مراجع canonical

- `ARCHITECTURE.md` — invariantهای اصلی.
- `schemas/PROJECT_PROFILE_CONFIG.md` — Mode، Dual-Lens، Swamp Guard و authority defaults.
- `schemas/SYSTEM_TRUTH_MAP.md` — component/data authority/recovery/scale map.
- `schemas/TASK_CONTRACT.md` — Task focus، Dual-Lens، scope، claim و authority.
- `docs/agent/PROJECT_INCEPTION_ARCHITECTURE.md` — Project Inception.
- `docs/agent/TASK_WORKFLOW_DRAFT_REVIEW_APPLY_VERIFY.md` — lifecycle Task.
- `schemas/MUTATION_APPROVAL_POLICY.md` — apply/remediation authority.
- `docs/operator/DESIGNER_MANAGER_SETUP.md` — setup نقش‌ها و permissionها.
- `prompts/operator/PROJECT_ARCHITECT.md` — Prompt معماری.
- `prompts/operator/TASK_DESIGNER.md` — Prompt Designer.
- `prompts/operator/MANAGER_REVIEWER.md` — Prompt Manager.
- `prompts/operator/INDEPENDENT_JUDGE.md` — Prompt Judge read-only.
- `production/DELIVERY.md` — rollback/recovery production.

Operator Guide روش استفاده را توضیح می‌دهد و canonical policy را override نمی‌کند.