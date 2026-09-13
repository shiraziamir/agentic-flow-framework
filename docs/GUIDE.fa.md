<div dir="rtl" align="right">
<h1>راهنمای جامع فارسی Agentic Flow</h1>
<p><strong>نسخه فریم‌ورک: 1.9</strong><br><strong>به‌روزرسانی: 2026-09-13</strong></p>
<p>این سند برای کسی نوشته شده که برای اولین بار وارد این ریپو می‌شود و می‌خواهد بدون خواندن ده‌ها فایل بفهمد این سیستم چرا ساخته شده، چگونه باید آن را راه‌اندازی کند و چطور کیفیت را بدون کندکردن بی‌دلیل جریان کار حفظ کند.</p>

<h2>۱. این ریپو چه مشکلی را حل می‌کند؟</h2>
<p>coding agent می‌تواند خیلی سریع کد تولید کند، اما سرعت تایپ کد با قابلیت اعتماد سیستم یکسان نیست. شکست‌های مهم معمولاً از جنس scope drift، تست مثبت کاذب، نبود محیط واقعی، ادعای بزرگ‌تر از شواهد، دسترسی بیش از حد، از دست رفتن کار ذخیره‌نشده، provider call غیرمجاز و reviewهای پراکنده هستند.</p>
<p>Agentic Flow تلاش می‌کند این مشکلات را با یک روش repository-first حل کند: چیزی که باید پایدار بماند در ریپو ثبت می‌شود و چت فقط context موقت است.</p>
<pre dir="ltr" style="text-align:left" class="text"><code>WHAT SHOULD BE TRUE   → project/task contract
WHAT MAY CHANGE NOW   → mutation authority
WHERE IT MAY RUN      → environment authority
WHAT REALLY CHANGED   → exact diff / commit
WHAT WAS OBSERVED     → receipts
WHAT IS UNKNOWN       → explicit gaps
WHO DECIDES           → operator / manager</code></pre>

<h2>۲. برای شروع فقط چه چیزهایی را بخوانم؟</h2>
<p>لازم نیست کل repository را بخوانید. مسیر پیشنهادی برای انسان فقط چهار فایل است:</p>
<pre dir="ltr" style="text-align:left" class="text"><code>1. README.md
2. docs/GETTING_STARTED.md
3. docs/agent/TASK_WORKFLOW_DRAFT_REVIEW_APPLY_VERIFY.md
4. docs/GUIDE.fa.md</code></pre>
<p>برای Executor معمولاً فقط <code>docs/agent/START_HERE.md</code> و task/profile فعلی لازم است. schema و production profile و verification profile فقط وقتی باید load شوند که task واقعاً به آن‌ها نیاز داشته باشد.</p>

<h2>۳. تفاوت با استفاده معمول از coding agent</h2>
<table>
<tr><th>Agentic Flow</th><th>روش معمول</th></tr>
<tr><td>repository source of truth است</td><td>چت source of truth می‌شود</td></tr>
<tr><td>Designer، Manager و Executor از هم جدا هستند</td><td>یک agent همه نقش‌ها را انجام می‌دهد</td></tr>
<tr><td>task، mutation، environment و external effect authority جدا هستند</td><td>یک «انجامش بده» ممکن است همه مجوزها تلقی شود</td></tr>
<tr><td>claim با receipt محدود می‌شود</td><td>tests passed ممکن است معادل done فرض شود</td></tr>
<tr><td>review می‌تواند consolidated باشد</td><td>findingها یکی‌یکی round-trip می‌سازند</td></tr>
<tr><td>remediation داخل پنجره کنترل‌شده انجام می‌شود</td><td>برای هر اصلاح authorization جدید گرفته می‌شود</td></tr>
</table>

<h2>۴. اصل مرکزی نسخه جدید</h2>
<blockquote><p>Quality requirements ثابت می‌ماند؛ ceremony بر اساس risk تغییر می‌کند.</p></blockquote>
<p>هدف کاهش کیفیت یا حذف review نیست. هدف کم‌کردن تعداد رفت‌وبرگشت‌های غیرضروری، گزارش‌های تکراری و permission gateهای ریز است.</p>
<pre dir="ltr" style="text-align:left" class="text"><code>LOW
execute → focused test → compact self-review → report

MEDIUM
short preflight → execute → cold review → bounded remediation → Manager review

HIGH
frozen contract → failure-surface preflight → explicit initial authorization
→ execute → adversarial review → Manager consolidated review
→ controlled remediation → final/independent closure</code></pre>

<h2>۵. نقش‌ها</h2>
<h3>Designer / Task Architect</h3>
<p>Designer read-only شروع می‌کند. او intent اپراتور را به contract قابل اجرا و Engineering Advisory تبدیل می‌کند. Designer نباید implementation را کورکورانه تحمیل کند.</p>
<h3>Manager / Reviewer</h3>
<p>Manager task را review/freeze می‌کند، authority را کنترل می‌کند، exact diff یا PR head را می‌بیند، findingها را consolidated می‌کند و در صورت امن بودن remediation window صادر می‌کند.</p>
<h3>Executor</h3>
<p>Executor HOW را انتخاب می‌کند، اما WHAT و success و scope را تغییر نمی‌دهد. او باید changed path را در محیط مناسب اجرا کند و نمی‌تواند material closure را خودش تأیید کند.</p>
<pre dir="ltr" style="text-align:left" class="text"><code>Operator intent
→ Designer: contract + advisory
→ Manager: freeze + bounded authority
→ Executor: implementation + test
→ cold/adversarial review
→ Manager: consolidated review
→ remediation window when safe
→ closure</code></pre>

<h2>۶. قبل از coding: Failure Surface Matrix</h2>
<p>یکی از علل remediationهای پیاپی این است که agent فقط happy path را می‌بیند و failureها در reviewهای بعدی آشکار می‌شوند. برای taskهای material، قبل از اولین edit حداقل این موارد بررسی می‌شوند:</p>
<pre dir="ltr" style="text-align:left" class="text"><code>NORMAL PATH
BOUNDARY / INVALID INPUT
DEPENDENCY OR I/O FAILURE
CLEANUP / ROLLBACK FAILURE
OBSERVABILITY / HEALTH PROPAGATION
TEST-ORACLE FALSIFICATION</code></pre>
<p>فقط در صورت مرتبط بودن موارد زیر نیز اضافه می‌شوند:</p>
<pre dir="ltr" style="text-align:left" class="text"><code>THREAD CONCURRENCY
PROCESS CONCURRENCY
CRASH / RESTART
DURABILITY / PARTIAL WRITE
PERMISSION / IDENTITY
EXTERNAL PROVIDER
MIGRATION / SCHEMA
CACHE / CONSISTENCY</code></pre>
<p>هدف این نیست که همه taskها را سنگین کنیم. یک تغییر ساده parser نباید مجبور به crash/restart test شود، اما یک task persistence یا concurrency باید این failure surface را جدی بگیرد.</p>

<h2>۷. Engineering Advisory</h2>
<p>راهنمای HOW باید evidence-constrained باشد. چهار tag اصلی داریم:</p>
<pre dir="ltr" style="text-align:left" class="text"><code>[MUST]        frozen invariant / owner constraint
[SHOULD]      evidence-backed recommendation
[INVESTIGATE] fact to establish before mutation
[AVOID]       likely failure/design/test trap</code></pre>
<p>پیشنهاد مدل به‌تنهایی authority نیست. اگر repository evidence نشان دهد راه کوچک‌تر و منسجم‌تری وجود دارد، Executor می‌تواند آن را انتخاب کند و دلیل را گزارش کند.</p>

<h2>۸. Controlled Remediation Window</h2>
<p>برای taskهای MEDIUM/HIGH، بعد از یک review جامع لازم نیست برای هر finding کوچک authorization جدید صادر شود. Manager می‌تواند یک پنجره اصلاح محدود بدهد:</p>
<pre dir="ltr" style="text-align:left" class="text"><code>remediation_window:
  review_ref: REVIEW-125-1
  finding_ids: [R1, R2, R3]
  max_iterations: 2
  allowed_files_or_resources:
    - src/logstore/**
    - tests/logstore/**
  owner_review_required_before_closure: true</code></pre>
<p>عدد دو یک default عملی است، نه قانون علمی. اگر در remediation نیاز به database جدید، migration جدید، provider جدید، public API، security boundary، production action، dependency جدید یا فایل خارج از scope پیدا شود، پنجره فوراً باطل می‌شود.</p>
<pre dir="ltr" style="text-align:left" class="text"><code>Remediation autonomy != scope autonomy</code></pre>

<h2>۹. محیط تست واقعی</h2>
<p>Executor فقط وقتی execution-ready است که بتواند رفتار تغییرکرده را در پایین‌ترین محیط کافی exercise کند. mock-only closure فقط claimهای unit/model را می‌بندد.</p>
<pre dir="ltr" style="text-align:left" class="text"><code>LOCAL / HERMETIC
→ LOCAL_REAL
→ EPHEMERAL TEST
→ SHARED TEST
→ STAGING / PRODUCTION-LIKE
→ CONTROLLED PRODUCTION READ
→ PRODUCTION MUTATION</code></pre>
<p>اگر claim درباره PostgreSQL transaction، migration، persistence یا concurrency واقعی است، mock به‌تنهایی کافی نیست. اگر محیط لازم وجود ندارد، claim باید UNVERIFIED یا BLOCKED بماند؛ requirement نباید ضعیف شود.</p>

<h2>۱۰. Cold / Adversarial Review قبل از Manager</h2>
<p>Manager نباید اولین کسی باشد که obvious defectها را پیدا می‌کند. برای MEDIUM/HIGH بهتر است یک reviewer سرد یا context جدا exact diff را بررسی کند.</p>
<pre dir="ltr" style="text-align:left" class="text"><code>implementation
→ focused tests
→ cold/adversarial review
→ executor fixes bounded findings
→ Manager review</code></pre>
<p>موارد مهم review شامل false-positive test، swallowed exception، cleanup failure، connection leak، duplicate state authority، concurrency gap، health propagation gap و scope drift هستند.</p>

<h2>۱۱. Receipt کوتاه، evidence کامل</h2>
<p>شواهد باید قوی باشند، اما گزارش نباید صدها خط تکراری شود. log خام و artifact جدا نگهداری می‌شود و receipt فقط index فشرده است.</p>
<pre dir="ltr" style="text-align:left" class="text"><code>claim: C4
environment: ephemeral-postgres-17
command: pytest tests/integration/test_commit_uncertainty.py
result: PASS 7/7
artifact_ref: artifacts/T125/integration-03.log
proves: commit uncertainty classification
does_not_prove: production provider behavior</code></pre>

<h2>۱۲. حفاظت از workspace</h2>
<p>کار commit‌نشده state محافظت‌شده است. ownership نامعلوم یعنی preserve، نه discard. دستورهای destructive باید با دقت و authority مناسب اجرا شوند.</p>
<pre dir="ltr" style="text-align:left" class="sourceCode bash"><code>git status
git diff
# inspect ownership before any destructive action
# avoid blind: git reset --hard / git clean -fd / git checkout --</code></pre>
<p>اگر agent مطمئن نیست تغییر متعلق به خودش است، باید آن را نگه دارد یا checkpoint امن بسازد.</p>

<h2>۱۳. Provider Call و External Side Effects</h2>
<p>مجوز اجرای تست به معنی مجوز تماس با provider واقعی، paid API، ارسال پیام، deployment یا تغییر سیستم خارجی نیست.</p>
<pre dir="ltr" style="text-align:left" class="text"><code>test authority
!= external-provider-call authority
!= production mutation authority</code></pre>
<p>پیش‌فرض مناسب برای provider واقعی: DENIED یا EXPLICIT_AUTHORITY_REQUIRED.</p>

<h2>۱۴. Git و PR</h2>
<p>برای کار material بهترین حالت این است که Designer و Manager به repository دسترسی مستقیم داشته باشند اما permission و role آن‌ها محدود و روشن باشد.</p>
<pre dir="ltr" style="text-align:left" class="text"><code>protected main
→ isolated Executor branch
→ PR
→ CI/checks
→ Manager reviews exact head SHA
→ remediation if bounded
→ final review
→ authorized merge</code></pre>
<p>summary عامل جای exact diff را نمی‌گیرد. هر commit جدید بعد از review باید head مورد بررسی را تازه کند.</p>

<h2>۱۵. اندازه‌گیری خود Flow</h2>
<p>اگر throughput کند شود باید بدانیم زمان در کجا مصرف شده است: quality cost، agent defect، governance friction یا environment friction.</p>
<pre dir="ltr" style="text-align:left" class="text"><code>first_pass_review_passed
remediation_iterations
manager_review_rounds
authorization_round_trips
unplanned_scope_escalations
environment_blocked
agent_safety_incidents
task_cycle_time (optional)</code></pre>
<p>این metricها برای بهبود process هستند، نه امتیازدادن به افراد.</p>

<h2>۱۶. چه زمانی Flow سبک یا سنگین باشد؟</h2>
<p>برای typo، rename یا docs کوچک full ceremony لازم نیست. برای persistence، auth، concurrency، migration، CI/CD، provider، production behavior یا تغییر چندماژولی controls قوی‌تر منطقی است.</p>
<pre dir="ltr" style="text-align:left" class="text"><code>LOW    → fewer gates
MEDIUM → bounded design/review/remediation
HIGH   → strong boundaries + strong evidence + bounded autonomy</code></pre>

<h2>۱۷. مسیر پیشنهادی راه‌اندازی</h2>
<ol>
<li>فریم‌ورک را کنار project clone یا به commit/tag بررسی‌شده pin کنید.</li>
<li>Executor را با <code>docs/agent/START_HERE.md</code> شروع کنید.</li>
<li>profile پروژه را از template بسازید.</li>
<li>برای اولین adoption از STRICT_PREVIEW استفاده کنید ولی تغییرات مرتبط را batch کنید.</li>
<li>برای taskهای material، Designer contract/advisory را آماده کند.</li>
<li>Manager scope، risk، environment و evidence plan را review کند.</li>
<li>Executor در branch جدا implement و test کند.</li>
<li>cold/adversarial review قبل از Manager انجام شود.</li>
<li>Manager findingها را یکجا بدهد و در صورت امن بودن remediation window صادر کند.</li>
<li>closure فقط بر اساس exact diff و receiptهای فعلی انجام شود.</li>
</ol>

<h2>۱۸. جمع‌بندی</h2>
<p>Agentic Flow قرار نیست coding agent را کند کند یا bureaucracy بسازد. هدف آن این است که سرعت تولید کد با مرزهای روشن، محیط تست واقعی، review منسجم و evidence قابل اتکا همراه شود.</p>
<blockquote><p>هدف نسخه جدید: gate کمتر، boundary قوی‌تر، preflight بهتر، review تجمیع‌شده، remediation محدود و گزارش کوتاه‌تر؛ بدون کاهش quality bar.</p></blockquote>
<p>اگر تازه وارد repo شده‌اید، به جای خواندن همه چیز از README و Getting Started شروع کنید و فقط فایل‌هایی را باز کنید که task فعلی trigger می‌کند.</p>
</div>
