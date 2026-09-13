<div dir="rtl" align="right">
<h1>راهنمای جامع فارسی Agentic Flow</h1>
<p><strong>نسخه فریم‌ورک: 1.9</strong><br><strong>به‌روزرسانی: 2026-09-13</strong></p>
<p>Agentic Flow یک روش repository-first و vendor-neutral برای کار با coding agentها است. هدف آن کندکردن agent یا ساختن bureaucracy نیست؛ هدف این است که سرعت تولید کد با مرزهای روشن اختیار، تست واقعی، review مستقل، شواهد قابل اتکا و rollback قابل اجرا همراه شود.</p>

<h2>۱. پنج سؤال اصلی</h2>
<p>اگر در یک پروژه agentic نتوانید سریع به این پنج سؤال جواب بدهید، احتمال false-complete شدن کار زیاد است:</p>
<pre dir="ltr" style="text-align:left" class="text"><code>1. What exactly is authorized?
2. What actually changed?
3. What evidence really proves it?
4. What remains unproven?
5. If it is wrong, how do we stop or recover?</code></pre>

<h2>۲. این ریپو چه مشکلی را حل می‌کند؟</h2>
<p>coding agent می‌تواند خیلی سریع کد تولید کند، اما «کد نوشته شد» با «رفتار درست و قابل اتکا اثبات شد» یکسان نیست. شکست‌های مهم معمولاً از scope drift، تست مثبت کاذب، نبود محیط واقعی، provider call غیرمجاز، review سطحی، از دست رفتن dirty work، production بدون rollback و وابستگی به حافظه یک session می‌آیند.</p>
<pre dir="ltr" style="text-align:left" class="text"><code>WHAT SHOULD BE TRUE   → task/profile
WHAT MAY CHANGE NOW   → mutation authority
WHERE IT MAY RUN      → environment authority
WHAT REALLY CHANGED   → exact diff / commit
WHAT WAS OBSERVED     → receipts
WHAT IS UNKNOWN       → explicit gaps
WHO DECIDES           → operator / delegated manager</code></pre>
<p>اصل بنیادی این است که engineering state باید در repository بماند و chat فقط working context موقت باشد.</p>

<h2>۳. برای شروع چه بخوانم؟</h2>
<p>لازم نیست کل repository را بخوانید. برای انسان معمولاً همین چهار فایل کافی است:</p>
<pre dir="ltr" style="text-align:left" class="text"><code>1. README.md
2. docs/GETTING_STARTED.md
3. docs/agent/TASK_WORKFLOW_DRAFT_REVIEW_APPLY_VERIFY.md
4. docs/GUIDE.fa.md</code></pre>
<p>برای Executor نیز نقطه شروع عادی <code>docs/agent/START_HERE.md</code> به‌همراه task/profile فعلی است. schemaها و production/verification profileها فقط وقتی load می‌شوند که task آن‌ها را trigger کند.</p>

<h2>۴. اصل مرکزی</h2>
<blockquote><p>Quality requirements ثابت می‌ماند؛ ceremony بر اساس risk تغییر می‌کند.</p></blockquote>
<pre dir="ltr" style="text-align:left" class="text"><code>LOW
execute → focused test → compact review

MEDIUM
short preflight → execute → cold review → one remediation → Manager review

HIGH
frozen contract → failure-surface preflight → bounded execution
→ adversarial review → Manager consolidated review
→ one remediation by default → read-only Independent Judge</code></pre>
<p>HIGH به معنی اجازه‌گرفتن برای هر خط نیست؛ یعنی boundary قوی‌تر، evidence قوی‌تر و autonomy محدود داخل همان boundary.</p>

<h2>۵. نقش‌ها</h2>
<h3>Designer / Task Architect</h3>
<p>Designer به‌صورت read-only شروع می‌کند، intent اپراتور را به contract قابل مشاهده و Engineering Advisory تبدیل می‌کند و نباید implementation را انجام دهد یا task خودش را approve کند.</p>
<h3>Manager / Reviewer</h3>
<p>Manager کیفیت task، authority، exact diff و receipts را review می‌کند، findingها را یکجا می‌دهد و در صورت امن بودن یک remediation window محدود صادر می‌کند.</p>
<h3>Executor</h3>
<p>Executor HOW را انتخاب می‌کند، implementation را انجام می‌دهد، changed path را در محیط کافی اجرا می‌کند و evidence تولید می‌کند. او نمی‌تواند material closure را خودش تأیید کند.</p>
<h3>Independent Judge</h3>
<p>Judge برای HIGH-risk یا هرجایی که policy مستقل‌بودن closure را می‌خواهد استفاده می‌شود. پیش‌فرض او read-only است: source/diff/CI/receipt را می‌بیند ولی کد، task، provider یا production را تغییر نمی‌دهد.</p>
<pre dir="ltr" style="text-align:left" class="text"><code>Operator intent
→ Designer
→ Manager
→ Executor
→ Cold Reviewer
→ Manager consolidated findings
→ One bounded remediation
→ Independent Judge (HIGH, read-only)
→ Operator production/business authority</code></pre>

<h2>۶. توافق چند مدل، evidence مستقل نیست</h2>
<p>ممکن است سه مدل مختلف همگی یک assumption غلط یا test oracle ضعیف را بپذیرند. بنابراین تعداد مدل‌های موافق به‌تنهایی claim را قوی‌تر نمی‌کند.</p>
<pre dir="ltr" style="text-align:left" class="text"><code>MULTI-MODEL AGREEMENT
!=
INDEPENDENT BEHAVIORAL EVIDENCE</code></pre>
<p>اگر سه مدل بگویند PASS ولی PostgreSQL واقعی، migration واقعی یا runtime واقعی بررسی نشده باشد، integration/production claim همچنان اثبات نشده است.</p>

<h2>۷. استقلال واقعی review چه معنی دارد؟</h2>
<p>Independent closure بهتر است چهار نوع جدایی را داشته باشد:</p>
<pre dir="ltr" style="text-align:left" class="text"><code>IMPLEMENTATION INDEPENDENCE
Judge did not materially implement the change

CONTEXT INDEPENDENCE
Judge reads task + exact diff + receipts, not only summaries

AUTHORITY INDEPENDENCE
Executor cannot self-approve / self-merge / self-close

EVIDENCE INDEPENDENCE
Judge inspects raw receipts/runtime evidence</code></pre>
<p>استفاده از model/provider متفاوت defense-in-depth خوبی است، اما جای این چهار مورد را نمی‌گیرد و evidence class را ارتقا نمی‌دهد.</p>

<h2>۸. Model routing و کنترل هزینه</h2>
<p>فریم‌ورک به Sonnet، Opus، ChatGPT یا vendor خاصی وابسته نیست. پروژه می‌تواند roleها را بر اساس capability و هزینه route کند.</p>
<pre dir="ltr" style="text-align:left" class="text"><code>Executor          → task-adequate / cost-efficient
Manager           → stronger reasoning when justified
Independent Judge → high reasoning + separate context</code></pre>
<p>هزینه کمتر هرگز اجازه کاهش acceptance criteria یا evidence requirement را نمی‌دهد. اگر مدل ارزان‌تر برای claim کافی نیست، capability را بالا ببرید یا claim را UNVERIFIED نگه دارید.</p>

<h2>۹. قبل از coding: Failure Surface Matrix</h2>
<p>برای material task قبل از اولین edit فقط happy path را نبینید. baseline زیر را بررسی کنید و triggerهای اضافی را فقط وقتی مرتبط‌اند اضافه کنید:</p>
<pre dir="ltr" style="text-align:left" class="text"><code>NORMAL PATH
BOUNDARY / INVALID INPUT
DEPENDENCY OR I/O FAILURE
CLEANUP / ROLLBACK FAILURE
OBSERVABILITY / HEALTH PROPAGATION
TEST-ORACLE FALSIFICATION

WHEN APPLICABLE:
THREAD / PROCESS CONCURRENCY
CRASH / RESTART
DURABILITY / PARTIAL WRITE
PERMISSION / IDENTITY
EXTERNAL PROVIDER
MIGRATION / SCHEMA
CACHE / CONSISTENCY</code></pre>
<p>هدف این است که findingهای مهم قبل از coding دیده شوند و remediation به چندین round تبدیل نشود.</p>

<h2>۱۰. Controlled Remediation Window</h2>
<p>بعد از Manager review، findingهای همان task نباید برای هر fix یک authorization جدید بسازند. هدف عادی یک remediation تجمیع‌شده است.</p>
<pre dir="ltr" style="text-align:left" class="text"><code>implementation
→ adversarial review
→ Manager consolidated findings
→ ONE bounded remediation
→ final review</code></pre>
<p>پیش‌فرض پیشنهادی <code>default_max_iterations: 1</code> است. round دوم فقط وقتی مجاز است که <strong>new material finding</strong> پیدا شده باشد و از maximum configured عبور نکند.</p>
<pre dir="ltr" style="text-align:left" class="text"><code>round 2 without new material finding
→ STOP / MANAGER REVIEW

Remediation autonomy != scope autonomy</code></pre>
<p>provider جدید، migration، public API، security boundary، dependency، production action یا فایل خارج از scope پنجره را باطل می‌کند.</p>

<h2>۱۱. محیط تست واقعی</h2>
<p>Executor فقط وقتی برای یک claim execution-ready است که بتواند changed path واقعی را در پایین‌ترین محیط کافی اجرا کند.</p>
<pre dir="ltr" style="text-align:left" class="text"><code>LOCAL / HERMETIC
→ LOCAL_REAL
→ EPHEMERAL TEST
→ SHARED TEST
→ STAGING / PRODUCTION-LIKE
→ CONTROLLED PRODUCTION READ
→ PRODUCTION MUTATION</code></pre>
<p>Mock می‌تواند unit/model claim را ثابت کند، اما به‌تنهایی persistence، migration، integration، deployment یا production را ثابت نمی‌کند.</p>

<h2>۱۲. Receipt کوتاه، evidence کامل</h2>
<p>Evidence نباید به گزارش صدها خطی تبدیل شود. raw log/artifact جدا نگهداری می‌شود و receipt فقط index فشرده است.</p>
<pre dir="ltr" style="text-align:left" class="text"><code>claim: C4
environment: ephemeral-postgres-17
command: pytest tests/integration/test_commit_uncertainty.py
result: PASS 7/7
artifact_ref: artifacts/T125/integration-03.log
proves: commit uncertainty classification
does_not_prove: production provider behavior</code></pre>

<h2>۱۳. Human نباید message bus باشد</h2>
<p>اپراتور باید authority و تصمیم واقعی را منتقل کند، نه اینکه برای همیشه گزارش agentها را copy/paste کند.</p>
<pre dir="ltr" style="text-align:left" class="text"><code>Human transports authority.
Repository transports engineering state.</code></pre>
<p>task، exact head، findings، remediation state، receipts، gaps و next authority decision باید به‌صورت durable در repository قابل بازیابی باشند.</p>
<pre dir="ltr" style="text-align:left" class="text"><code>checkpoint durable state
→ session may be cleared/replaced
→ fresh session reads current repo/task state
→ continue without replaying old chat</code></pre>
<p>دستورهایی مثل <code>/clear</code> vendor-specific هستند و canonical policy نیستند؛ اصل مهم session-reset-safe بودن بعد از checkpoint است.</p>

<h2>۱۴. حفاظت از workspace</h2>
<p>dirty work نامعلوم state محافظت‌شده است. ownership نامعلوم یعنی preserve، نه discard.</p>
<pre dir="ltr" style="text-align:left" class="sourceCode bash"><code>git status
git diff
# inspect ownership before destructive operations
# avoid blind: git reset --hard / git clean -fd / git checkout --</code></pre>

<h2>۱۵. Provider Call و External Side Effects</h2>
<p>مجوز تست با مجوز تماس provider واقعی، paid API، ارسال پیام یا deployment یکی نیست.</p>
<pre dir="ltr" style="text-align:left" class="text"><code>test authority
!= external-provider-call authority
!= production mutation authority</code></pre>

<h2>۱۶. Git و PR</h2>
<p>برای material work، exact commit و PR باید source of review باشند، نه summary Executor.</p>
<pre dir="ltr" style="text-align:left" class="text"><code>protected main
→ isolated Executor branch
→ PR + CI
→ Manager exact diff review
→ one bounded remediation
→ Independent Judge when required
→ authorized merge</code></pre>
<p>اگر بعد از review commit جدید push شود، review قبلی برای head جدید stale است مگر policy صریحاً خلاف آن را تعریف کرده باشد.</p>

<h2>۱۷. Production mode</h2>
<p>فعال‌شدن production mode به معنی blanket permission نیست. هر production mutation باید قبل از اجرا rollback یا explicit forward-recovery readiness داشته باشد.</p>
<pre dir="ltr" style="text-align:left" class="text"><code>target environment
exact artifact/config/change identity
success + health signals
abort condition
rollback OR forward-recovery path
stateful/data constraints
recovery owner/authority
post-change verification</code></pre>
<p>اگر rollback واقعاً unsafe یا impossible است، forward recovery، backup/checkpoint، blast-radius control و STOP condition لازم است.</p>
<pre dir="ltr" style="text-align:left" class="text"><code>Judge PASS
!= production mutation authority

Independent Judge production mutation: DENIED by default</code></pre>

<h2>۱۸. دسترسی پیشنهادی roleها</h2>
<table>
<tr><th>Role</th><th>Source</th><th>Production read</th><th>Production mutation</th></tr>
<tr><td>Designer</td><td>Read-only</td><td>معمولاً Denied</td><td>Denied</td></tr>
<tr><td>Executor</td><td>Bounded write</td><td>Owner approval</td><td>Owner approval</td></tr>
<tr><td>Manager</td><td>Read/review</td><td>Owner approval</td><td>معمولاً Denied</td></tr>
<tr><td>Independent Judge</td><td>Read-only</td><td>Owner approval</td><td>Denied</td></tr>
</table>
<p>اگر همه roleها یک credential نامحدود داشته باشند، separation فقط procedural است و security boundary واقعی نیست.</p>

<h2>۱۹. Flow metrics</h2>
<p>برای اینکه بفهمیم کندی از quality cost است یا agent defect یا governance friction، metricهای سبک نگه دارید:</p>
<pre dir="ltr" style="text-align:left" class="text"><code>first_pass_review_passed
remediation_iterations
manager_review_rounds
authorization_round_trips
unplanned_scope_escalations
environment_blocked
agent_safety_incidents
task_cycle_time (optional)</code></pre>
<p>این metricها برای بهبود process هستند، نه امتیازدادن به افراد.</p>

<h2>۲۰. راه‌اندازی عملی</h2>
<ol>
<li>framework را کنار project clone یا به commit/tag بررسی‌شده pin کنید.</li>
<li>Executor را از <code>docs/agent/START_HERE.md</code> شروع کنید.</li>
<li><code>.agentic/PROJECT_PROFILE.yaml</code> را از template بسازید.</li>
<li>برای شروع <code>STRICT_PREVIEW</code> را انتخاب کنید و editهای مرتبط را batch کنید.</li>
<li>برای material task، Designer contract/advisory را بسازد.</li>
<li>Manager task، environment، authority و evidence plan را review کند.</li>
<li>Executor در branch جدا implement و test کند.</li>
<li>cold/adversarial review قبل از Manager نهایی انجام شود.</li>
<li>Manager findingها را یکجا بدهد و معمولاً یک remediation round صادر کند.</li>
<li>برای HIGH-risk، Independent Judge در context جدا و read-only closure را بررسی کند.</li>
<li>Operator فقط تصمیم‌های واقعی مثل production، risk acceptance و business priority را approve کند.</li>
</ol>

<h2>۲۱. جمع‌بندی</h2>
<p>Agentic Flow قرار نیست تعداد مدل‌ها را زیاد کند و بعد از «اجماع» نتیجه بگیرد سیستم درست است. هدف این است که role، authority، evidence و runtime reality از هم جدا بمانند.</p>
<blockquote><p>مدل‌های بیشتر می‌توانند review coverage را بهتر کنند؛ فقط evidence واقعی می‌تواند claim را قوی‌تر کند.</p></blockquote>
<blockquote><p>Human authority را حمل می‌کند؛ repository engineering state را.</p></blockquote>
<blockquote><p>برای production: هیچ mutation بدون rollback یا forward-recovery readiness.</p></blockquote>
<p>اگر تازه وارد repo شده‌اید، README را بخوانید، سپس Getting Started را اجرا کنید و فقط اسنادی را load کنید که task فعلی trigger می‌کند.</p>
</div>
