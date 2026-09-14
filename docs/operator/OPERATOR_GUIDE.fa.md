# راهنمای اپراتور — Agentic Flow

**Runbook اصلی اپراتور. Coding Agent نباید این فایل را دائماً preload کند مگر Task اپراتوری به آن نیاز داشته باشد.**  
**نسخه فریم‌ورک:** 1.11  
**به‌روزرسانی:** 2026-09-14

این سند توضیح عملیاتی واحد برای اپراتور است: چه نقشی چه کاری می‌کند، مدل اجراکننده و مدل مراقب چگونه جدا می‌شوند، چه Guardrailهایی فعال‌اند، `Dual-Lens` چطور جلوی «درست بودن محلی ولی غلط شدن کل سیستم» را می‌گیرد، و انسان کجا باید تصمیم واقعی بگیرد. Authority نهایی همچنان در `ARCHITECTURE.md` و Schemaهاست.

## ۱. مدل کنترل در یک نگاه

```text
PRODUCT OWNER / OPERATOR
WHY / WHAT / priority / business trade-offs / accepted risk / production authority
        │
        ├── greenfield / معماری نامطمئن ──► PROJECT ARCHITECT (read-only)
        │                                      │
        │                    product constraints + eval + System Truth Map
        │                                      │
        ▼                                      ▼
DESIGNER / TASK ARCHITECT ──► MANAGER / REVIEWER ──► EXECUTOR
Task design به‌صورت read-only      freeze + authority       اجرای محدود
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
                                                    one bounded remediation
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

## ۲. با Preset شروع کنید، نه با یک دیوار تنظیمات

Phase پروژه و Operating Preset دو مفهوم جدا هستند:

```text
Project phase:
VIBE_PROTOTYPE | PRODUCT_BUILD | MAINTENANCE

Operating preset:
VIBE_FAST | PRODUCT_STANDARD | HIGH_ASSURANCE
```

| Preset | کاربرد | رفتار پیش‌فرض |
|---|---|---|
| `VIBE_FAST` | آزمایش disposable، امکان‌سنجی، UX learning | سریع، review فشرده، sacrificial code مجاز، بدون production claim |
| `PRODUCT_STANDARD` | محصول قابل نگهداری معمولی | Project Inception در صورت نیاز، Dual-Lens risk-adaptive، تست واقعی کافی، remediation محدود |
| `HIGH_ASSURANCE` | پول، identity، privacy، tenant isolation، durability حساس، عملیات destructive/regulated | evidence قوی‌تر و independent closure هرجا توجیه دارد |

لازم نیست تمام optionهای Schema را داخل هر پروژه copy کنید. از Preset شروع کنید و فقط تفاوت واقعی پروژه را در `.agentic/PROJECT_PROFILE.yaml` override کنید.

## ۳. Vibe Mode پشتیبانی می‌شود، ولی محصور است

```text
VIBE_PROTOTYPE != PRODUCTION BASELINE
```

در Vibe Mode سرعت یادگیری اولویت دارد. معماری می‌تواند موقت و بخشی از کد sacrificial باشد. اما این Mode مجوز داده حساس، production readiness یا production mutation نمی‌دهد.

برای عبور به `PRODUCT_BUILD` باید re-baseline شود و کد Prototype صریحاً دسته‌بندی شود:

```text
REUSE_AS_IS | REUSE_AFTER_REVIEW | REWRITE | DISCARD
```

## ۴. پروژه Greenfield: ایده مستقیم به کدنویسی نمی‌رود

```text
PRODUCT INTENT
→ PRODUCT BRIEF
→ QUALITY / EVAL CONTRACT
→ ARCHITECTURE DISCOVERY
→ SYSTEM TRUTH / DATA AUTHORITY MAP
→ CURRENT SCALE BOUNDARY
→ MINIMAL OPTIONS when useful
→ WALKING SKELETON
→ ARCHITECTURE CHECKPOINT
→ PRODUCT BASELINE
```

Product Owner outcome و trade-off را مشخص می‌کند: کاربر کیست، success/failure چیست، privacy/freshness/latency/cost چقدر مهم است و چه ریسکی قابل قبول است. Project Architect کوچک‌ترین شکل سیستم را پیشنهاد می‌دهد.

برای AI/RAG/Search، tuning جدی قبل از eval baseline نماینده انجام نمی‌شود.

فایل‌های اصلی:

```text
docs/agent/PROJECT_INCEPTION_ARCHITECTURE.md
prompts/operator/PROJECT_ARCHITECT.md
schemas/SYSTEM_TRUTH_MAP.md
templates/SYSTEM_TRUTH_MAP.example.yaml
```

## ۵. نقش‌ها و حدود اختیار

| نقش | مسئولیت اصلی | Mutation پیش‌فرض | Production mutation |
|---|---|---:|---:|
| Operator / Product Owner | هدف، اولویت، trade-off، ریسک، production authority | اختیار انسانی | تصمیم صریح انسان |
| Project Architect | constraint، eval، System Truth Map، گزینه معماری | read-only | ممنوع |
| Designer / Task Architect | Task Contract و advisory | read-only | ممنوع |
| Manager / Reviewer | freeze Task، review exact diff/evidence، authority محدود | read/review | پیش‌فرض ممنوع |
| Executor | اجرای HOW داخل boundary تصویب‌شده | bounded write | فقط با مجوز جداگانه Owner |
| Cold / Adversarial Reviewer | کشف defect/فرض غلط قبل از Manager | read-only | ممنوع |
| Independent Judge | closure برای HIGH-risk یا policy-required | read-only | ممنوع |

مدل متفاوت به‌تنهایی independence نیست. استقلال واقعی تا جای ممکن این چهار بعد را جدا می‌کند:

```text
IMPLEMENTATION
CONTEXT
AUTHORITY
EVIDENCE
```

```text
MULTI-MODEL AGREEMENT != INDEPENDENT BEHAVIORAL EVIDENCE
```

## ۶. Task Focus — موضوع فعلی گفتگو مساوی اولویت پروژه نیست

```text
PRIMARY_TASK = هدف durable اصلی
SIDE_TASK    = کار کمکی محدود
INTERRUPT    = وقفه فوری و محدود
```

```text
RECENCY IS NOT PRIORITY.
CONVERSATIONAL MOMENTUM CANNOT PROMOTE A SIDE TASK.
```

Side Task باید reference به Primary، success condition محدود، budget/scope و return condition داشته باشد. بعد از پایان، Flow به Primary برمی‌گردد.

Promotion فقط با تصمیم صریح Manager/Operator انجام می‌شود. اگر Side Task در حال بلعیدن پروژه باشد، Agent باید `SIDE_TASK DRIFT` اعلام کند و `CLOSE | DEFER | PROMOTE_PROPOSAL` پیشنهاد دهد.

برای `INTERRUPT` ابتدا Primary Task و resume state دقیق checkpoint می‌شود.

## ۷. Dual-Lens بدون Checklist Theater

```text
LOCAL LENS
آیا رفتار تغییرکرده درست کار می‌کند؟

SYSTEM LENS
بعد از این تغییر، سیستم چه حقیقتی را ادعا می‌کند؟
```

ابعاد System Lens:

```text
WRITE · READ · AGGREGATE · CACHE · RESTART · FAILURE · RECOVERY
ADMIN · METRIC · TENANT_ISOLATION · SCALE · PRIVACY · COST
```

وضعیت‌ها:

```text
UNAFFECTED | VERIFIED | CHANGED_AND_TESTED | OPEN_RISK | NOT_APPLICABLE
```

قاعده risk-adaptive:

- `LOW` و واقعاً local → یک خلاصه کوتاه از system impact؛ ۱۳ خانه را مکانیکی پر نکنید.
- `MEDIUM/HIGH` → ابعاد مرتبط صریح ثبت شوند.
- هر Risk Level که به **پول، privacy، identity، tenant isolation، durability/recovery، state destructive یا production semantics** دست می‌زند → ابعاد affected صریح ثبت شوند.

`UNAFFECTED` نتیجه بررسی است، نه filler. `OPEN_RISK` باید visible بماند. Cache/projection/metric بی‌صدا authority نمی‌شود.

## ۸. System Truth Map

برای `PRODUCT_BUILD` و سیستم‌های stateful/cost/privacy/tenant-sensitive نگه دارید:

```text
.agentic/SYSTEM_TRUTH_MAP.yaml
```

این artifact فقط حقیقت‌های باربر را نگه می‌دارد:

```text
entry points / trust boundaries
DB / cache / queue / provider / worker
admin / observability / deployment / recovery
authoritative data + derived copies
writers / readers
freshness / size / privacy bounds
restart / failure / recovery behavior
tenant isolation
current scale target / ceiling / safety limit / scale trigger
```

این Map مدل سیستم است، نه runtime proof. Claimهای runtime همچنان receipt می‌خواهند.

## ۹. Threat/Failure Mini-Review

در Project Inception یا تغییر boundary باربر به‌طور کوتاه بپرسید:

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

فقط risk و decision مادی ثبت شود. هدف ساختن سند امنیتی صدصفحه‌ای نیست.

## ۱۰. Lifecycle تسک بر اساس Risk

```text
LOW
execute → focused test → compact diff review → compact system-impact summary

MEDIUM
short preflight → execute → Dual-Lens → cold review
→ one remediation → Manager review

HIGH
frozen contract → failure/System-Lens preflight → explicit authority
→ bounded execution → adversarial review → Manager findings
→ one remediation by default → read-only Independent Judge
→ Operator production/business decision
```

Round دوم remediation فقط با **new material finding** توجیه دارد و باید داخل boundary قبلی بماند.

## ۱۱. تست و Evidence

برای business behavior مادی فقط helper return را تست نکنید. بسته به feature سناریوهای واقعی مانند success، fallback، retry، external side-effect سپس failure، source-of-truth unavailable، restart/rebuild، time boundary، admin recovery، cross-tenant و concurrency/duplicate-work را بررسی کنید.

برای تست‌های load-bearing، mutation/path proof وقتی عملی است استفاده شود: رفتار هدف را در یک copy ایزوله عمداً خراب کنید و ثابت کنید تست قرمز می‌شود.

برای این کار از destructive Git reset/restore/clean روی workspace نامعلوم اپراتور استفاده نکنید.

```text
unit PASS          != user flow proven
HTTP 200           != persistence
CI green           != deployed artifact
backup configured  != restore proven
reviewer PASS      != runtime evidence
```

## ۱۲. Swamp Guard

```text
CLEAR | WATCH | ALERT | STOP_REBASELINE
```

Signalهای رایج: architecture churn، remediation تکراری، tool/abstraction بدون نیاز، چند mechanism برای یک responsibility، AI/RAG tuning بدون eval، feature growth قبل از vertical slice، تصمیم معماری فقط در chat، ambiguity در source-of-truth، prototype-to-production drift، side-task attention drift، System-Lens risk حل‌نشده و رشد complexity سریع‌تر از value اثبات‌شده.

حالت شدید:

```text
STOP_REBASELINE
→ preserve state/evidence
→ architecture discovery
→ simplify / measure / decide
→ resume from coherent baseline
```

خود Framework هم تحت همین قانون است: وقتی controls زیاد می‌شوند، قبل از افزودن مفهوم جدید باید simplify و validate کنیم.

## ۱۳. Cross-System Audit

اولویت Trigger:

```text
EVENT
> RISK / AUTHORITY CHANGE
> TASK-COUNT REMINDER
```

Release واقعی به مشتری، incident مادی یا تغییر مهم security/data/authority/recovery می‌تواند فوراً Audit را trigger کند. عدد `5–8 material tasks` فقط reminder است.

محورهای Audit می‌تواند شامل financial truth، privacy، identity/authorization، tenant isolation، restart survival، backup/restore، observability truth، capacity bounds، provider failure/spend و admin recovery باشد.

## ۱۴. Production Control

Production mutation یک Authority مستقل است. قبل از **هر** Production change باید این موارد مشخص باشند:

```text
exact target environment
exact artifact/config/change identity
expected health/success signal
abort condition
rollback OR forward-recovery path
state/data constraints
recovery owner/authority
post-change verification
```

```text
NO ROLLBACK / RECOVERY PLAN
→ NOT EXECUTION-READY FOR PRODUCTION MUTATION
```

اگر rollback unsafe یا impossible است، forward recovery، backup/checkpoint، blast-radius control و STOP condition لازم است. PASS مدل مراقب یا Manager مجوز Production نیست.

## ۱۵. انسان نباید Message Bus باشد

Repository باید durable نگه دارد:

```text
project mode / preset
System Truth Map
PRIMARY / active task
exact refs
findings
remediation state
receipts / gaps
Swamp state
next authority decision
```

انسان عمدتاً باید authority واقعی را حمل کند:

```text
approve / reject
change priority
accept risk
choose business trade-off
authorize production
```

Session جدید باید بتواند بدون replay کردن chat قبلی از روی repo ادامه دهد.

## ۱۶. Checklist روزانه اپراتور

قبل از material work:

```text
1. PRIMARY_TASK چیست؟
2. Project Mode و Preset چیست؟
3. Architecture/System Truth baseline کافی است؟
4. Risk و allowed mutation surface چیست؟
5. کدام evidence/environment موفقیت را ثابت می‌کند؟
6. کدام System-Lens dimensions ممکن است حساس باشند؟
7. چه external/production authority جداگانه لازم است؟
```

در Closure:

```text
چه چیزی تغییر کرد؟
چه چیزی آن را ثابت می‌کند؟
چه چیزی هنوز ثابت نشده؟
کدام System Truth تغییر کرد؟
چه risk جدید/باز باقی مانده؟
چه provider/environment mutation رخ داد؟
چطور stop/recover می‌کنیم؟
Next authorized action چیست؟
```

## ۱۷. مسیرهای عمیق‌تر

```text
Canonical policy          ARCHITECTURE.md
Project profile/presets   schemas/PROJECT_PROFILE_CONFIG.md
Project inception         docs/agent/PROJECT_INCEPTION_ARCHITECTURE.md
System Truth              schemas/SYSTEM_TRUTH_MAP.md
Task workflow             docs/agent/TASK_WORKFLOW_DRAFT_REVIEW_APPLY_VERIFY.md
Mutation authority        schemas/MUTATION_APPROVAL_POLICY.md
Role setup                docs/operator/DESIGNER_MANAGER_SETUP.md
Independent Judge         prompts/operator/INDEPENDENT_JUDGE.md
Production rollback       production/DELIVERY.md
Validation limits         docs/VALIDATION_STATUS.md
```

هدف «حداکثر Process» نیست. هدف **کمترین Processی است که Product Intent، System Truth، Evidence و Authority را در Risk فعلی منسجم نگه دارد**.
