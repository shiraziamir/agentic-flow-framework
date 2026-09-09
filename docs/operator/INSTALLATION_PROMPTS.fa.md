# Promptهای عملی برای نصب و Adoption

**این فایل مخصوص اپراتور است و نباید داخل Context روزمره Agent preload شود.**  
**نسخه:** 1.0  
**به‌روزرسانی:** 2026-09-09T11:30:00Z

## پروژه جدید یا Repository بدون کار فعال

```text
Agentic Flow در مسیر `.agentic-flow/` Extract شده است.
فایل `.agentic-flow/docs/agent/START_HERE.md` را بخوان و Framework را برای این Repository adopt کن.
فعلاً Product Work را شروع نکن.
اول Instructionهای موجود پروژه، Build/Test/Deploy structure و نیازهای Project Profile را بررسی کن.
فقط حداقل Vendor Adapter لازم را بساز و Adoption Receipt بده.
```

## Adoption وسط کار برنامه‌نویسی

```text
Agentic Flow در حالی وارد شده که Coding از قبل در حال انجام است.
فایل `.agentic-flow/docs/agent/MIDSTREAM_ADOPTION.md` را بخوان.
تا قبل از ثبت Adoption Snapshot، Product Changeهای فعلی را Reset، دور نریز، ادامه نده یا بی‌صدا Amend نکن.
برای کار قبلی به‌صورت Retroactive ادعای Review یا Authorization این Framework نکن.
Remaining Work، Project Profile/Gap و Verificationهای لازم را reconcile کن و Next Authorization را گزارش بده.
```

## پروژه Mature که CI/CD و Monitoring دارد

```text
Agentic Flow را به‌عنوان Operating/Control Layer adopt کن، نه Replacement Technology Stack.
اگر CI/CD، Observability، Security، Task Tracking و Architecture فعلی semantics لازم را دارند، آنها را حفظ و به Framework map کن.
Shadow System نساز.
Conflict واقعی و Gap واقعی را از Requirementهایی که قبلاً برآورده شده‌اند جدا گزارش کن.
```

## پروژه Production-bound

```text
بعد از Adoption، Production Profile موجود را با کوچک‌ترین Profile Set لازم بررسی کن.
تا زمانی که Requirementهای Tier/Environment با Receipt فعلی ثابت نشده‌اند، عبارت `production ready` را استفاده نکن.
برای Backup/Restore، Observability، Security، Delivery، Troubleshooting و Resilience که Missing یا Unverified هستند Operational Gap بساز.
همه Gapها را خودکار Implement نکن؛ آنها را بر اساس Risk اولویت‌بندی کن و برای تغییرات لازم Authorization بگیر.
```
