# راهنمای اپراتور — Agentic Flow

**این فایل مخصوص اپراتور است و Agent نباید آن را به‌صورت دائمی preload کند.**  
**نسخه:** 1.7  
**به‌روزرسانی:** 2026-09-09

## هدف

این چارچوب باید کنترل ریسک را بالا ببرد، بدون اینکه هر کار کوچک را به مراسم اداری تبدیل کند. اپراتور صاحب تصمیم‌های مربوط به ریسک کسب‌وکار، مجوز Production، پذیرش ریسک و تغییرات معماری مهم است. Agent داخل این مرزها کار می‌کند و باید واقعیت، Receipt و Gap را گزارش کند؛ نه اینکه ابهام را با جمله‌های مطمئن پنهان کند.

## نصب به‌صورت Drop-in

Artifact قابل‌حمل خودش یک `README.md` در Root دارد. پوشه‌ی `agentic-flow/` داخل ZIP را در Repository مقصد به این شکل Extract کنید:

```text
.agentic-flow/
```

سپس این Prompt را به Agent بدهید:

```text
Read .agentic-flow/START_HERE.md and adopt Agentic Flow for this repository.
Do not start or change product work until adoption validation is complete.
```

اگر Agent از قبل وسط کار برنامه‌نویسی است:

```text
Read .agentic-flow/docs/agent/MIDSTREAM_ADOPTION.md.
Adopt the framework without discarding current edits or fabricating prior review/authorization.
Return the adoption snapshot and conflicts before continuing product mutation.
```

## Baseline پروژه

یک فایل زیر ایجاد کنید:

```text
.agentic/PROJECT_PROFILE.yaml
```

از `templates/PROJECT_PROFILE.example.yaml` شروع کنید. این فایل باید کوچک بماند و فقط سطح مورد انتظار پروژه را مشخص کند؛ مانند `readiness tier`، سیاست Test، سطح دسترسی Agent به Environmentها، Backup/Metric/Restore requirementها و سیاست Patternها. تاریخچه Taskها و متن‌های طولانی نباید در این فایل قرار بگیرند.

## Workflow تسک

برای تغییرهای مهم Agent را مستقیم به Coding نفرستید. Workflow عادی:

```text
DRAFT
→ REVIEW
→ FREEZE / APPLY AUTHORIZATION در صورت نیاز
→ APPLY
→ VERIFY + REPORT
→ Independent Closure در صورت نیاز
```

راهنمای عملی Agent:

```text
docs/agent/TASK_WORKFLOW_DRAFT_REVIEW_APPLY_VERIFY.md
```

Promptهای اجرایی در `prompts/workflow/` هستند. شدت Governance باید متناسب با Risk باشد؛ تغییر کوچک نباید مجبور به تشریفات High-risk شود.

## ابزارهای deterministic با Python

راهنمای کامل دستورها:

```text
docs/operator/USING_PYTHON_TOOLS.fa.md
```

نسخه انگلیسی:

```text
docs/operator/USING_PYTHON_TOOLS.en.md
```

بررسی معمول Framework قبل از Release:

```bash
python3 scripts/test_verification_lint.py
python3 scripts/test_production_readiness_lint.py
python3 scripts/test_build_agent_bundle.py
python3 scripts/build_agent_bundle.py
```

هدف هر Script:

```text
verification_lint.py
  پیدا کردن تناقض مکانیکی در Task / Evidence / Status

production_readiness_lint.py
  پیدا کردن تناقض مکانیکی در Production Profile / Gap

build_agent_bundle.py
  ساخت ZIP قابل‌حمل و Manifest

usage_ledger.py
  ثبت و گزارش Counterهای واقعی Usage/Token در صورت وجود Telemetry
```

PASS شدن Linter به معنی درست بودن Runtime، Security، Deployment، Monitoring یا Restore نیست. Script فقط چیزی را که قانون deterministic دارد بررسی می‌کند؛ Claim واقعی همچنان Receipt واقعی لازم دارد.

## تصمیم‌هایی که بهتر است صریحاً دست اپراتور بمانند

موارد زیر معمولاً باید مجوز Human/Owner داشته باشند:

- تغییر Production یا عملیات مخرب روی داده؛
- پذیرش Gap مهم Security/Data/Recovery؛
- پایین‌آوردن دائمی Requirementهای Backup/Observability/Security؛
- تغییر Pattern معماری در چند Module یا Public Contract؛
- تغییر Task فریز‌شده‌ی High-risk؛
- قبول‌کردن Acceptance Gate خراب.

## Exception موقت

اگر مثلاً یک Metric پرهزینه شده یا یک Control باید چند ساعت/روز خاموش شود، Baseline را بی‌صدا تغییر ندهید. از `schemas/TEMPORARY_OVERRIDE.md` استفاده کنید و `owner`، علت، `expiry`، ریسک ایجادشده، `compensating control` و روش اثبات Restore را ثبت کنید. Override منقضی‌شده نباید بی‌صدا باقی بماند.

## Environment برای Agent

Agent باید پایین‌ترین Environmentی را استفاده کند که Claim را واقعاً ثابت می‌کند. اگر ممکن است Environmentهای Ephemeral/Disposable برای Integration و E2E بسازید. دسترسی Shared Staging و Production باید Policy و Permission مشخص داشته باشد. درخواست Agent برای Environment به معنی مجوز نیست.

## Review

برای کار عادی، یک Session/Model سرد و جدا می‌تواند Closure Review انجام دهد. برای Security، Persistence، Public Contract، Production Semantics یا معماری مهم، Reviewer مستقل قوی‌تر یا Human استفاده کنید. اگر ممکن است Reviewer ابتدا Task، Diff و Receipt خام را ببیند و Report Agent را بعداً بخواند تا Anchoring کمتر شود.

## کنترل Token و Context

راهنمای عملی:

```text
docs/agent/TOKEN_EFFICIENT_WORKFLOW.md
```

فایل‌های Operator، Research و History را داخل Context دائمی Agent قرار ندهید. مدل قوی را برای Judgment و Ambiguity نگه دارید؛ کارهای Inventory، Log Reduction و Discovery قابل‌چک را می‌توان با ابزار deterministic یا Subagent ارزان Read-only انجام داد.

صرفه‌جویی Token مجوز پایین‌آوردن Evidence Bar نیست.

## بررسی‌های دوره‌ای اپراتور

به‌صورت دوره‌ای این موارد ارزش بررسی دارند:

- Project Profile و Gapها؛
- Overrideهای منقضی‌شده؛
- تازگی Restore Test؛
- مالکیت SLO/Alert؛
- Dependency/Security posture؛
- گزارش مصرف Token/Cost در صورت وجود Telemetry؛
- Retrospective برای اینکه Governance بیش از حد سنگین یا بیش از حد ضعیف نشده باشد.

`project-retrospective` و `project-storytelling` فقط در صورت نیاز Load شوند و بخشی از Context روزمره Agent نباشند.
