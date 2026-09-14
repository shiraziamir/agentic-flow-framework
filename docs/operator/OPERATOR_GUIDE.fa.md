# راهنمای اپراتور — Agentic Flow

**Runbook اصلی اپراتور. Agent نباید این فایل را به‌صورت دائمی preload کند مگر اینکه Task اپراتوری به آن نیاز داشته باشد.**  
**نسخه فریم‌ورک:** 1.10  
**به‌روزرسانی:** 2026-09-14

این سند توضیح واحد و عملیاتی Agentic Flow برای اپراتور است: نقش‌ها چگونه با هم کار می‌کنند، مدل مراقب و مدل اجراکننده چه تفاوتی دارند، چه Guardrailهایی فعال‌اند، چه چیزی دست انسان می‌ماند و سیستم در چه شرایطی باید Alert بدهد یا متوقف شود. Authority نهایی همچنان در `ARCHITECTURE.md` و Schemaهاست؛ این فایل روش استفاده از آن‌ها را توضیح می‌دهد.

## ۱. مدل کنترل در یک نگاه

```text
PRODUCT OWNER / OPERATOR
WHY / WHAT / priority / business trade-offs / accepted risk / production authority
        │
        ├── greenfield یا معماری نامطمئن ──► PROJECT ARCHITECT (read-only)
        │                                      │
        │                                      ▼
        │                           architecture options + eval contract
        │                                      │
        ▼                                      ▼
DESIGNER / TASK ARCHITECT ──► MANAGER / REVIEWER ──► EXECUTOR
طراحی Task به‌صورت read-only      freeze + authority       اجرای محدود
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
                                               برای HIGH-risk در صورت نیاز
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
| Operator / Product Owner | هدف، اولویت، trade-off، ریسک، Production authority | اختیار انسانی | فقط تصمیم صریح انسان |
| Project Architect | تبدیل Product Intent به constraint، eval و گزینه معماری | read-only | ممنوع |
| Designer / Task Architect | تبدیل هدف محدود به Task Contract | read-only | ممنوع |
| Manager / Reviewer | freeze کردن Task، کنترل authority، بررسی diff و receipt | read/review | پیش‌فرض ممنوع |
| Executor | اجرای HOW داخل مرزهای freeze‌شده | bounded write | فقط با مجوز جداگانه Owner |
| Cold / Adversarial Reviewer | پیدا کردن فرض غلط و defect قبل از Manager | read-only | ممنوع |
| Independent Judge | closure مستقل برای HIGH-risk | read-only | ممنوع |

اسم متفاوت مدل به‌تنهایی استقلال ایجاد نمی‌کند. استقلال واقعی تا جای ممکن باید در چهار بعد باشد:

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

### VIBE_PROTOTYPE

فعال‌سازی:

```yaml
project_mode:
  mode: VIBE_PROTOTYPE
```

وقتی سؤال اصلی این است که «آیا ایده کار می‌کند؟» یا «کاربر این تجربه را دوست دارد؟» از این Mode استفاده کنید. سرعت یادگیری اولویت دارد؛ معماری می‌تواند provisional و بخشی از کد sacrificial باشد.

```text
VIBE_PROTOTYPE != PRODUCTION BASELINE
```

این Mode مجوز Production readiness، استفاده از داده حساس یا Production mutation نمی‌دهد. عبور به `PRODUCT_BUILD` نیازمند re-baseline، Architecture Checkpoint و دسته‌بندی کد prototype است:

```text
REUSE_AS_IS | REUSE_AFTER_REVIEW | REWRITE | DISCARD
```

### PRODUCT_BUILD

برای ساخت Product baseline. Product constraint، quality/eval contract و تصمیم‌های معماری باربر باید قبل از رشد وسیع featureها به‌اندازه کافی روشن باشند.

### MAINTENANCE

برای پروژه‌ای که baseline معتبر دارد. اگر boundary مهم عوض شد یا Swamp Guard drift ساختاری دید، دوباره به Architecture Discovery برگردید.

## ۴. شروع پروژه از صفر

ایده نباید مستقیم به Executor داده شود.

```text
PRODUCT INTENT
→ PRODUCT BRIEF
→ QUALITY / EVAL CONTRACT
→ ARCHITECTURE DISCOVERY
→ 2–3 MINIMAL OPTIONS در صورت نیاز
→ LOAD-BEARING DECISIONS
→ WALKING SKELETON
→ ARCHITECTURE CHECKPOINT
→ PRODUCT BASELINE
→ NORMAL TASK FLOW
```

اپراتور باید سؤال‌های محصول را جواب بدهد، نه اینکه نقش Senior Architect بازی کند: کاربر کیست، چه outcomeی می‌خواهد، رفتار غیرقابل قبول چیست، privacy/freshness/latency/cost چقدر مهم است و trade-off تجاری چیست.

Project Architect شکل سیستم را کشف می‌کند و نباید زود وارد coding شود. چیزهای سخت‌تغییر را freeze می‌کنیم؛ انتخاب‌های ارزان‌تغییر را تا زمانی که evidence نداریم باز نگه می‌داریم.

برای AI/RAG، tuning جدی روی chunking، embedding، top-k، reranking، prompt یا vector vendor قبل از eval baseline نماینده ممنوع است.

راهنمای canonical: `docs/agent/PROJECT_INCEPTION_ARCHITECTURE.md`  
Prompt: `prompts/operator/PROJECT_ARCHITECT.md`

## ۵. Task Hierarchy — جلوگیری از گم‌شدن هدف اصلی

هر workstream فقط یک هدف durable اصلی دارد:

```text
PRIMARY_TASK = هدف فعلی اصلی
SIDE_TASK    = کار کمکی محدود
INTERRUPT    = وقفه فوری و محدود
```

قانون:

```text
RECENCY IS NOT PRIORITY.
CONVERSATIONAL MOMENTUM CANNOT PROMOTE A SIDE TASK.
```

هر `SIDE_TASK` باید `primary_task_ref`، success condition محدود، scope/budget، return condition و promotion authority داشته باشد. بعد از اتمام، نتیجه ثبت می‌شود و Flow به Primary Task برمی‌گردد.

طولانی‌شدن بحث، خطای تازه یا چند prompt پشت‌سرهم، promotion محسوب نمی‌شود. Promotion فقط با تصمیم صریح Manager/Operator انجام می‌شود.

اگر Side Task بیش از حد round بخورد، معماری unrelated بسازد یا تبدیل به هدف de-facto شود، Agent باید اعلام کند:

```text
SIDE_TASK DRIFT
Recommended action: CLOSE | DEFER | PROMOTE_PROPOSAL
```

برای `INTERRUPT` ابتدا Primary Task و resume state دقیق checkpoint می‌شود؛ بعد کار فوری انجام می‌شود و سپس یا resume می‌کنیم یا صریحاً reprioritize می‌کنیم.

## ۶. Lifecycle معمول Task

Risk و نوع کار دو چیز متفاوت هستند:

```text
risk.level = LOW | MEDIUM | HIGH
work_kind  = IMPLEMENTATION | REMEDIATION | EVIDENCE_ONLY
```

Flow پیش‌فرض:

```text
LOW
execute → focused test → compact self-review → report

MEDIUM
short preflight → execute → cold review → one bounded remediation → Manager review

HIGH
frozen contract
→ failure-surface preflight
→ explicit apply authority
→ bounded execution
→ adversarial review
→ Manager consolidated findings
→ one remediation round by default
→ read-only Independent Judge when required
→ Operator production/business decision
```

Round دوم remediation فقط با finding جدید و مادی قابل توجیه است. remediation تکراری خودش Swamp signal است.

## ۷. Authorityها عمداً از هم جدا هستند

یک «انجامش بده» نباید همه مجوزها تلقی شود:

```text
TASK AUTHORITY
MUTATION AUTHORITY
ENVIRONMENT AUTHORITY
EXTERNAL-SIDE-EFFECT AUTHORITY
PRODUCTION AUTHORITY
```

مثال:

- Task approved != Mutation approved در `STRICT_PREVIEW`؛
- مجوز تست != مجوز تماس با paid provider واقعی؛
- staging read != production mutation؛
- Judge PASS != مجوز deploy.

برای adoption اولیه، `STRICT_PREVIEW` پیش‌فرض مناسب است. Editهای مرتبط را batch کنید؛ permission spam برای هر خط/فایل نسازید.

## ۸. Swamp Guard — مراقبت دائمی از باتلاق

Swamp Guard در checkpointهای مادی و قبل از گسترش معماری/tooling اجرا می‌شود:

```text
CLEAR | WATCH | ALERT | STOP_REBASELINE
```

Signalهای مهم:

- redesign/remediation تکراری در یک subsystem؛
- framework/datastore/abstraction جدید بدون نیاز محصول یا failure boundary؛
- چند mechanism برای یک responsibility؛
- AI/RAG tuning بدون eval؛
- رشد feature قبل از vertical slice واقعی؛
- تصمیم معماری فقط در chat؛
- ابهام در source-of-truth یا state ownership؛
- workaround موقت که دائمی شده؛
- prototype که بی‌صدا production expectation گرفته؛
- complexity که سریع‌تر از value اثبات‌شده رشد می‌کند؛
- `SIDE_TASK` که توجه را از `PRIMARY_TASK` می‌دزدد.

Alert باید این شکل را داشته باشد:

```text
SWAMP ALERT: <WATCH|ALERT|STOP_REBASELINE>
Signal: ...
Evidence: ...
Why it matters: ...
Recommended action: ...
Continue allowed: YES|NO
Authority needed: <none|Manager|Operator>
```

`STOP_REBASELINE` یعنی patch محلی را ادامه ندهید؛ state/evidence را حفظ کنید، به Architecture Discovery برگردید، simplify/measure/decide کنید و بعد از baseline منسجم ادامه دهید.

## ۹. مدل مراقب و روند Review

Executor نباید کار material خودش را close کند.

برای MEDIUM/HIGH، در صورت policy، Cold/Adversarial Reviewer قبل از Manager exact diff را بررسی می‌کند. Manager ترجیحاً این ترتیب را دنبال می‌کند:

```text
frozen contract
→ exact base/head / diff
→ surrounding source
→ raw tests / CI / receipts
→ gaps / omitted checks
→ Executor narrative last
```

Manager findingها را تا جای ممکن یکجا می‌دهد و برای اصلاحات same-task یک remediation window محدود صادر می‌کند.

برای HIGH-risk، Independent Judge به‌صورت read-only claimها را دوباره در برابر source/diff/receipt بررسی می‌کند. Judge حق edit، ضعیف‌کردن Task، provider call یا production mutation ندارد.

این یعنی «مدل مراقب» فقط یک مدل قوی‌تر نیست؛ باید authority و context و evidence آن هم از Executor جدا باشد.

## ۱۰. قوانین Evidence

Claim نباید از Receipt خودش بزرگ‌تر باشد:

```text
unit PASS          != integration proven
mock PASS          != real boundary proven
HTTP 200           != persistence proven
CI green           != deployed behavior proven
backup configured  != restore proven
reviewer PASS      != runtime evidence
three models PASS  != three independent engineers
```

پایین‌ترین Environment مجاز را استفاده کنید که changed path واقعی را exercise کند. اگر چنین محیطی وجود ندارد، نتیجه `UNVERIFIED` یا `BLOCKED` است؛ claim را ضعیف نکنید.

## ۱۱. Handoff مبتنی بر Repository

اپراتور نباید message bus بین مدل‌ها و sessionها باشد.

Session جدید باید بتواند از artifactهای durable این موارد را بازیابی کند:

```text
project mode / architecture baseline
PRIMARY_TASK
active SIDE_TASK / INTERRUPT
suspended/resume state
exact repository base/head
frozen task contract
review findings
remediation window
receipts / gaps
Swamp Guard state
closure state
next authority decision
```

قبل از clear/تعویض session، state durable را checkpoint کنید. تازگی conversation حق ندارد priority پروژه را عوض کند.

## ۱۲. Production Control

قبل از هر Production mutation این موارد باید وجود داشته باشند:

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

اگر rollback امن نیست، forward recovery، backup/checkpoint، blast-radius control و STOP condition لازم است. Independent Judge همچنان read-only می‌ماند.

## ۱۳. Workspace Safety و External Effects

Dirty work با ownership نامعلوم state محافظت‌شده است. `reset/restore/clean` مخرب را صرفاً برای راحتی Agent استفاده نکنید.

Provider call واقعی، paid API، ارسال پیام، deployment و destructive data action authority جدا می‌خواهند. نیاز تست به معنی مجوز side effect واقعی نیست.

## ۱۴. Routing مدل و هزینه

Framework vendor-neutral است:

```text
Project Architect → reasoning قوی‌تر وقتی ambiguity معماری بالاست
Executor          → task-adequate / cost-efficient
Manager           → judgment قوی‌تر در صورت نیاز
Independent Judge → high reasoning + separate context
```

کاهش هزینه هیچ‌وقت evidence/acceptance bar را پایین نمی‌آورد.

## ۱۵. اپراتور باید چه چیزهایی را دائماً چک کند؟

در checkpointهای مهم بررسی کنید:

- Project Mode هنوز درست است؟
- `PRIMARY_TASK` هنوز صریح است و Side Task جایش را نگرفته؟
- Side Taskها محدود و return conditionها رعایت شده‌اند؟
- Swamp Alertها واقعاً بررسی شده‌اند یا نادیده گرفته شده‌اند؟
- Architecture/Eval baseline با واقعیت محصول هم‌خوان است؟
- HEAD بررسی‌شده همان candidate فعلی است؟
- Receiptها current هستند و Claim بیش‌ازحد بزرگ نشده؟
- Temporary override منقضی باقی نمانده؟
- Restore/Recovery evidence کافی و تازه است؟
- Production authority به Reviewer/Judge نشت نکرده؟
- Governance خودش باعث round-trip بی‌فایده نشده؟

## ۱۶. Quick Start اپراتور

```text
1. README.md را بخوان.
2. .agentic/PROJECT_PROFILE.yaml را ایجاد/تأیید کن.
3. VIBE_PROTOTYPE | PRODUCT_BUILD | MAINTENANCE را انتخاب کن.
4. اگر greenfield/architecture نامطمئن است: Project Architect / Project Inception.
5. یک PRIMARY_TASK ثبت کن.
6. برای Task material از Designer استفاده کن.
7. Manager contract را freeze و authority محدود می‌دهد.
8. Executor اجرا و تست می‌کند.
9. Cold review → Manager findings → یک remediation round.
10. برای HIGH-risk در صورت نیاز Independent Judge.
11. Operator درباره production/business risk تصمیم می‌گیرد.
12. Repository state را به session بعد منتقل می‌کند.
```

## ۱۷. مراجع canonical

- `ARCHITECTURE.md` — invariantهای اصلی.
- `schemas/PROJECT_PROFILE_CONFIG.md` — Project Mode، Swamp Guard، Task Focus و authority defaults.
- `schemas/TASK_CONTRACT.md` — Primary/Side/Interrupt، scope، claim و authority.
- `docs/agent/PROJECT_INCEPTION_ARCHITECTURE.md` — greenfield/vibe/product inception.
- `docs/agent/TASK_WORKFLOW_DRAFT_REVIEW_APPLY_VERIFY.md` — lifecycle Task.
- `schemas/MUTATION_APPROVAL_POLICY.md` — apply/remediation authority.
- `docs/operator/DESIGNER_MANAGER_SETUP.md` — setup نقش‌ها و permissionها.
- `prompts/operator/PROJECT_ARCHITECT.md` — Prompt معماری.
- `prompts/operator/TASK_DESIGNER.md` — Prompt Designer.
- `prompts/operator/MANAGER_REVIEWER.md` — Prompt Manager.
- `prompts/operator/INDEPENDENT_JUDGE.md` — Prompt Judge read-only.
- `production/DELIVERY.md` — rollback/recovery production.

Operator Guide روش استفاده را توضیح می‌دهد؛ canonical policy را override نمی‌کند.