# راهنمای اپراتور — استفاده از ابزارهای Python

**این فایل برای اپراتور است. Agent فقط زمانی آن را Load کند که Task واقعاً به این ابزارها نیاز داشته باشد.**

اسکریپت‌های داخل `scripts/` برای بررسی‌های deterministic و ساخت/اعتبارسنجی Bundle هستند. هدف این است که چیزهایی که با قانون دقیق قابل بررسی‌اند با Script انجام شوند، نه با مصرف Token و قضاوت مدل.

این اسکریپت‌ها به‌تنهایی ثابت نمی‌کنند که برنامه Secure، Production-ready، Recoverable یا درست Deploy شده است. برای چنین Claimهایی همچنان Receipt واقعی Runtime/Test/Security/Recovery لازم است.

## پیش‌نیاز

Python 3.11 یا جدیدتر پیشنهاد می‌شود. CI فعلی این ابزارها را با Python 3.13 بررسی می‌کند.

ورودی JSON فقط به Python standard library نیاز دارد. برای YAML در Linterها باید `PyYAML` نصب باشد.

## 1. بررسی Task / Evidence / Status

Script:

```text
scripts/verification_lint.py
```

این Script تناقض‌های مکانیکی را پیدا می‌کند؛ برای مثال:

- Claim با وضعیت `VERIFIED` ولی بدون Evidence؛
- Receipt مربوط به Repository Ref قدیمی؛
- Receipt ضعیف‌تر از حداقل Receipt فریز‌شده‌ی Task؛
- ترکیب `UNKNOWN` و `VERIFIED`؛
- DoD با وضعیت PASS ولی بدون Evidence؛
- Claim کلی مانند `no regressions` بدون Receipt مناسب و bounded.

اجرا:

```bash
python3 scripts/verification_lint.py path/to/file.json
```

چند فایل:

```bash
python3 scripts/verification_lint.py file1.json file2.json file3.json
```

تبدیل Warning به Failure:

```bash
python3 scripts/verification_lint.py --strict file.json
```

تست خود Checker:

```bash
python3 scripts/test_verification_lint.py
```

این Linter نمی‌تواند تشخیص دهد که یک Test از نظر معنایی واقعاً کافی است یا UI/Runtime/Security واقعاً درست کار می‌کند.

## 2. بررسی Production Profile و Gap

Script:

```text
scripts/production_readiness_lint.py
```

نمونه تناقض‌هایی که می‌گیرد:

- دیتای High-criticality بدون Requirement مشخص Backup/Restore/RPO/RTO؛
- `STANDARD` یا `HIGH_ASSURANCE` بدون Metrics/Logs/Vulnerability-management لازم؛
- سرویس User-facing با `HIGH_ASSURANCE` ولی بدون SLO Requirement؛
- `HIGH_ASSURANCE` بدون Failure-mode analysis، Recovery drill یا Threat model؛
- `ACCEPTED_RISK` بدون Owner یا Accepting authority؛
- Gap با وضعیت `CLOSED` بدون Evidence.

اجرا:

```bash
python3 scripts/production_readiness_lint.py .agentic/production/PROFILE.yaml
```

Profile همراه Gapها:

```bash
python3 scripts/production_readiness_lint.py \
  .agentic/production/PROFILE.yaml \
  .agentic/production/gaps/*.yaml
```

تست خود Checker:

```bash
python3 scripts/test_production_readiness_lint.py
```

این Script ثابت نمی‌کند Backup واقعاً Restore می‌شود، SLO سالم است، Monitoring مفید است یا Production واقعاً Ready است.

## 3. ساخت Agent Bundle

Script:

```text
scripts/build_agent_bundle.py
```

از Root Repository اجرا کنید:

```bash
python3 scripts/build_agent_bundle.py
```

خروجی پیش‌فرض:

```text
dist/agentic-flow-agent-bundle.zip
```

خروجی با نام دلخواه:

```bash
python3 scripts/build_agent_bundle.py \
  --output dist/my-agentic-flow-bundle.zip
```

تست Builder:

```bash
python3 scripts/test_build_agent_bundle.py
```

Builder فایل‌های Distribution را جمع می‌کند، Root entrypointها را می‌سازد و در `BUNDLE_MANIFEST.json` مسیر فایل، SHA-256 و Byte count را ثبت می‌کند.

GitHub Action یک مرحله قوی‌تر هم دارد: Bundle را از یک Checkout تمیز و واقعی Repository می‌سازد و سپس Manifest، Hash و Boundaryها را دوباره Verify می‌کند.

## 4. ثبت Usage/Token در صورت وجود داده واقعی

Script:

```text
scripts/usage_ledger.py
```

فقط زمانی استفاده شود که Provider/Harness عدد واقعی Token/Cost را ارائه می‌کند. مقدارها را حدس نزنید.

نمونه ثبت:

```bash
python3 scripts/usage_ledger.py record \
  --task-id TASK-123 \
  --phase APPLY \
  --role EXECUTION_TIER \
  --provider example-provider \
  --model example-model \
  --input-tokens 1200 \
  --output-tokens 300 \
  --tool-calls 4
```

گزارش:

```bash
python3 scripts/usage_ledger.py report
```

گزارش یک Task:

```bash
python3 scripts/usage_ledger.py report --task-id TASK-123
```

مسیر پیش‌فرض:

```text
.agentic/usage/events.jsonl
```

این Ledger نباید Prompt، Response، Chain-of-thought یا Transcript را ذخیره کند.

## 5. بررسی پیشنهادی قبل از Release

```bash
python3 -m py_compile \
  scripts/verification_lint.py \
  scripts/production_readiness_lint.py \
  scripts/usage_ledger.py \
  scripts/build_agent_bundle.py

python3 scripts/test_verification_lint.py
python3 scripts/test_production_readiness_lint.py
python3 scripts/test_build_agent_bundle.py
python3 scripts/build_agent_bundle.py
```

بعد اجازه دهید GitHub Actions همان کار را روی Checkout تمیز تکرار کند و Artifact واقعی را بسازد.

## 6. چه زمانی Script و چه زمانی Agent؟

برای سؤال deterministic از Script/Tool استفاده کنید:

```text
آیا Field لازم وجود دارد؟
آیا Hashها یکسان‌اند؟
آیا Version marker درست است؟
آیا VERIFIED claim بدون Evidence داریم؟
آیا Bundle فایل لازم را دارد؟
```

برای سؤال judgment-heavy از Agent/Human استفاده کنید:

```text
آیا این Test رفتار واقعی مشتری را کافی ثابت می‌کند؟
آیا این Architecture مناسب است؟
Root cause محتمل چیست؟
آیا Risk امنیتی قابل قبول است؟
آیا Restore drill واقعاً RPO/RTO را ثابت می‌کند؟
```

قاعده‌ی عملی:

```text
Deterministic truth → Script / Tool
Ambiguity / Judgment → Agent / Human
```
