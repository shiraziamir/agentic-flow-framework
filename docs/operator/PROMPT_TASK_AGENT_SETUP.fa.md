# بهترین روش‌های Prompt، Task و Agent Setup

**راهنمای مخصوص اپراتور**  
**نسخه:** 1.0  
**به‌روزرسانی:** 2026-09-09T11:30:00Z

## Prompt نویسی

Prompt باید مستقیم، دقیق و قابل‌سنجش باشد. Constraintهای مهم، Permission و Output مورد انتظار را روشن بنویسید. متن‌های خارجی، Log، فایل کاربر و داده‌ی Provider را با Heading، Tag یا Code Fence از Instruction جدا کنید.

نمونه‌ی بهتر:

```text
Goal: duplicate payment on provider timeout را اصلاح کن.
Constraints: schema change ممنوع؛ production mutation ممنوع.
Evidence: focused test + mutation/path proof + integration receipt.
Stop if: retry semantics با فرض Task فرق داشت.
Output: changed paths, exact tests, remaining unknowns.
```

Promptهای مبهم مانند `fix it`، `make it production ready` یا `check everything` بهتر است ابتدا Agent را مجبور به Draft Task محدود و قابل‌Review کنند.

اگر Format یا رفتار مورد انتظار ممکن است اشتباه فهمیده شود، Example بدهید. به‌جای اضافه‌کردن Ruleهای کلی و طولانی، Prompt را بر اساس Failure واقعی اصلاح کنید. از Agent Chain-of-Thought خصوصی نخواهید؛ Rationale کوتاه، Assumption، Check، Receipt و Unknown کافی است.

## Task نویسی

یک Task مهم باید مشخص کند: چه چیزی واقعاً مشاهده شده، Outcome مطلوب چیست، چه چیزی فقط Hypothesis است، کدام Path/Module قابل Edit یا Reference است، چه Surfaceهای فنی/Production درگیرند، در Closure چه Claimهایی گفته می‌شود، Receipt هر Claim چیست، چه Environmentی لازم است، چه Checkهایی عمداً خارج Scope هستند، و Agent در چه شرایطی باید `STOP` یا Escalate کند.

`Definition of Done` را قبل از `APPLY` بنویسید و تا حد امکان آن را بر اساس رفتار قابل مشاهده تعریف کنید، نه فقط «کلاس X ساخته شود». اگر Fact در دسترس نیست، `UNKNOWN` را حفظ کنید.

## استراتژی تست

برای Claimهای مهم تا حد امکان Test Design قبل از Implementation انجام شود، ولی `strict TDD` برای هر تغییر اجباری نیست. کوچک‌ترین Test Layerی را انتخاب کنید که Claim را مستقیماً ثابت می‌کند. Regression/Safety Test مهم بهتر است در صورت نیاز با `mutation/path proof` نشان دهد که واقعاً می‌تواند Defect را بگیرد.

## Agent Setup

Instruction دائمی Agent باید Map باشد، نه Manual. Build/Lint/Test commandهای پروژه، Source of Truth، Boundaryهای مهم، Permissionها و Pointerهای Lazy به Profile/Skill کافی هستند. Operator docs، Research، Task History و Checklistهای طولانی را وارد Context دائمی نکنید.

Instructionهای Hierarchical یا Subtree-specific فقط وقتی بسازید که واقعاً آن بخش پروژه Rule متفاوت دارد.

## Subagent و Model Routing

اول ابزار deterministic. برای Discovery و Log Reduction محدود که خروجی قابل‌چک دارد از Subagent ارزان Read-only استفاده کنید. برای Implementation محلی مدل استاندارد و برای Architecture/Security/Ambiguity/High-risk Closure مدل قوی‌تر یا Reviewer مستقل استفاده کنید. بین Agentها Evidence Packet کوچک منتقل کنید، نه Transcript کامل.

## Setup وسط کار

اگر Framework یا Agent جدید وسط Coding وارد شد، اول `HEAD`، Branch، Dirty Paths، Task فعلی، Testهای قبلی و Environment Mutationهای فعال Snapshot شوند. کار قبلی را به‌دروغ «Reviewed by framework» اعلام نکنید. Remaining Work را reconcile کنید؛ پروژه را کورکورانه از صفر شروع نکنید.

## منابع

این توصیه‌ها با Guidance رسمی فعلی OpenAI، Anthropic، Google Gemini و OpenCode هم‌راستا هستند: Instruction روشن و مشخص، Structure ثابت، Example در صورت نیاز، Context hierarchical/modular و Skillهای on-demand. لینک‌ها و کاربرد هر منبع در `docs/references/PRIMARY_SOURCES.md` ثبت شده‌اند.
