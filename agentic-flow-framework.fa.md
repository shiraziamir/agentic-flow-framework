# راهنمای فارسی Agentic Flow Framework

**نسخه راهنمای خواندنی:** 1.8
**به‌روزرسانی:** `2026-09-13`
**منبع قطعی:** `ARCHITECTURE.md`

این فایل برای انسان است. اگر با `ARCHITECTURE.md` اختلاف داشت، معماری Canonical ملاک است.

راهنمای فارسی جامع، مستقل و دارای چینش RTL/LTR خوانا در [`docs/GUIDE.fa.md`](docs/GUIDE.fa.md) قرار دارد.

## این Framework چه مسئله‌ای را حل می‌کند؟

Agentic Flow بین هدف Task، Implementation، Evidence، وضعیت عملیاتی پروژه و Authority تفاوت روشن می‌گذارد تا Agent نتواند یک Narrative مطمئن را به‌جای واقعیت پروژه قرار دهد.

```text
Project Baseline
→ Bounded Task
→ Review Verification Design
→ Authorized Implementation
→ Receipts / Reality Report
→ Independent Judgment when required
→ Durable Checkpoint
```

اصول اصلی:

- حافظه پروژه Durable باشد، Context کاری قابل تعویض و کوچک بماند؛
- Claim از Receipt قوی‌تر نباشد؛
- Production Readiness با Profile و Gapهای واقعی تعریف شود، نه Badge؛
- Baseline پروژه از Exception موقت جدا باشد؛
- مستندات اپراتور و Context روزمره Agent از هم جدا باشند.

## نصب به‌صورت ZIP قابل‌حمل

از Repository اصلی:

```bash
python3 scripts/build_agent_bundle.py
```

فایل زیر ساخته می‌شود:

```text
dist/agentic-flow-agent-bundle.zip
```

آن را داخل پروژه مقصد با نام پیشنهادی زیر Extract کنید:

```text
.agentic-flow/
```

سپس Agent فقط از اینجا شروع کند:

```text
.agentic-flow/START_HERE.md
```

اگر Coding از قبل در حال انجام است، Agent باید `docs/agent/MIDSTREAM_ADOPTION.md` را بخواند، وضعیت واقعی `HEAD`، Branch، Dirty Paths، Task، Testهای قبلی و Environment Mutationها را Snapshot کند و کار معتبر موجود را دور نریزد. کار قبلی نباید به‌صورت Retroactive «Reviewed/Authorized by framework» اعلام شود.

Bundle پیش‌فرض `docs/operator/`، Research، Referenceهای خارجی و Cold History را وارد Context روزمره Agent نمی‌کند.

## Project Profile

پروژه معمولاً یک Baseline کوچک دارد:

```text
.agentic/PROJECT_PROFILE.yaml
```

این فایل مشخص می‌کند چه چیزی **باید** درست باشد: Test Policy، Readiness Tier، Permissionهای Environment، Backup/Observability/Security expectations و Pattern Policy. این فایل به‌تنهایی ثابت نمی‌کند واقعیت فعلی همان است.

اگر یک Control موقتاً خاموش یا Suppress شود، از `TEMPORARY_OVERRIDE` با Owner، دلیل، Expiry، Risk، Compensating Control و Restore Verification استفاده می‌شود؛ Baseline بی‌صدا عوض نمی‌شود.

## چرخه Task مهم

```text
REQUEST
→ DRAFT
→ REVIEW
→ FREEZE / APPLY AUTHORIZATION در صورت نیاز
→ APPLY
→ VERIFY + REALITY REPORT
→ Independent Closure در صورت نیاز
```

قبل از Implementation باید `Definition of Done` قابل مشاهده، Surfaceهای فنی/Production، Claimهای Closure، حداقل Receipt هر Claim، Test/Environment لازم و شرایط `STOP` مشخص باشند.

## Test و Environment

برای Claimهای مهم، Test Design قبل از Implementation انجام می‌شود؛ ولی `strict TDD` برای هر تغییر کوچک یا Exploratory اجباری نیست.

برای Regression/Safety Test مهم، در صورت نیاز باید نشان داده شود که Test واقعاً می‌تواند Defect را پیدا کند:

```text
GREEN
→ Controlled Defect / Mutation
→ Expected RED
→ Restore
→ GREEN
```

Environmentها به‌ترتیب قدرت و ریسک:

```text
LOCAL / HERMETIC
→ EPHEMERAL TEST
→ SHARED TEST
→ STAGING / PRODUCTION-LIKE
→ CONTROLLED CANARY / PRODUCTION READ
→ PRODUCTION MUTATION
```

Agent باید پایین‌ترین Environmentی را انتخاب کند که Claim را ثابت می‌کند. درخواست Environment به معنی Authorization نیست.

## Production Engineering

Profileهای Production شامل Build/Deploy/Rollback، Security، Metrics/Logs/Traces/SLO، Backup/PITR/Restore، Troubleshooting، AI-safe Log Analysis، Resilience/Chaos و معماری قابل تغییر هستند.

اندازه Repository با سطح Assurance یکی نیست. یک Service کوچک Payment/Auth ممکن است `HIGH_ASSURANCE` باشد.

چند قاعده مهم:

```text
backup enabled  != recoverability
CI green        != deployment
scanner green   != secure
metrics exist   != useful observability
reviewer PASS   != missing runtime receipt
```

برای داده مهم، Restore همان Receipt اصلی Recoverability است.

## Log و AI

Logهایی که وارد LLM می‌شوند Untrusted Data هستند. User Input، Provider Error یا متن خارجی داخل Log نمی‌تواند Instruction یا Permission ایجاد کند. Log باید تا حد ممکن Structured، Redacted و Bounded باشد و Query/Time Window/Raw Source Ref حفظ شود.

## Patternها

Adapter، Repository، Strategy، Circuit Breaker، Saga و Patternهای مشابه باید یک مشکل واقعی مانند Volatile Dependency، Failure Boundary، Public Contract یا Testability را حل کنند.

Pattern کوچک و Local می‌تواند داخل Strategy تاییدشده انتخاب شود. Pattern بزرگ Cross-module یا Public باید با Problem، Alternative ساده‌تر، Benefit، Cost و Verification Impact پیشنهاد شود و متناسب با Risk Review شود.

## جداسازی مستندات

- `docs/agent/` — برای Adoption/Bootstrap Agent؛
- `docs/operator/` — برای انسان: نصب، Prompt، Task و Governance؛
- `docs/architecture/` — توضیح چرایی و معماری؛
- `docs/references/` و `research/` — منابع خارجی و تحقیق تاریخ‌دار.

Agent برنامه‌نویس نباید مستندات Operator و Research را به‌صورت دائمی preload کند.

## مسیرهای شروع

Agent: `docs/agent/START_HERE.md`
اپراتور: `docs/operator/OPERATOR_GUIDE.fa.md`
بهترین روش‌های Prompt/Task/Agent Setup: `docs/operator/PROMPT_TASK_AGENT_SETUP.fa.md`
چرایی و معماری: `docs/architecture/WHY_AND_HOW.md`
تمام منابع: `docs/references/PRIMARY_SOURCES.md`
