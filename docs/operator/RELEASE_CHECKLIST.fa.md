# چک‌لیست Release برای اپراتور

قبل از اینکه Release Framework را کامل اعلام کنید:

- `VERSION`، `ARCHITECTURE.md`، `README.md`، Reader Docs و `CHANGELOG.md` یک نسخه را نشان دهند.
- مستندات Agent و Operator از هم جدا بمانند.
- `docs/references/PRIMARY_SOURCES.md` منابع جدید استفاده‌شده را داشته باشد.
- Self-testهای `verification_lint`، `production_readiness_lint` و `build_agent_bundle` پاس شوند.
- `build_agent_bundle.py` یک ZIP بسازد که Manifest آن با Hash فایل‌ها سازگار باشد و Operator/Research/History را وارد Bundle نکند.
- Prompt نصب تازه و Prompt Midstream Adoption وجود داشته باشند.
- Bootstrap Adapterها به آخرین معماری Canonical اشاره کنند و Policy طولانی را Duplicate نکنند.
- آخرین `main` به‌عنوان Release Receipt ثبت شود.
