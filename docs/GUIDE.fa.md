<div dir="rtl" align="right">
<h1>راهنمای جامع فارسی Agentic Flow</h1>
<p><strong>نسخه فریم‌ورک: 1.11</strong><br><strong>به‌روزرسانی: 2026-09-14</strong></p>

<p>این فایل راهنمای مفهومی و مسیر یادگیری فارسی است. برای اجرای روزمره و جزئیات نقش‌ها/Guardrailها از <code>docs/operator/OPERATOR_GUIDE.fa.md</code> استفاده کنید. Authority نهایی در <code>ARCHITECTURE.md</code> و Schemaهاست.</p>

<h2>۱. مسئله‌ای که Flow حل می‌کند</h2>
<p>Coding Agent می‌تواند خیلی سریع کد تولید کند، اما «کد نوشته شد» با «رفتار درست و قابل اتکا اثبات شد» یکسان نیست. Agentic Flow سرعت را نگه می‌دارد و در عین حال Product Intent، Architecture، Priority، Authority، Evidence و Production Safety را از هم جدا می‌کند.</p>

<pre dir="ltr" style="text-align:left"><code>1. What exactly is authorized?
2. What actually changed?
3. What evidence really proves it?
4. What remains unproven?
5. If it is wrong, how do we stop or recover?</code></pre>

<h2>۲. مسیر اصلی پروژه</h2>
<pre dir="ltr" style="text-align:left"><code>PRODUCT INTENT
→ PRODUCT / EVAL CONSTRAINTS
→ ARCHITECTURE DISCOVERY
→ SYSTEM TRUTH / DATA AUTHORITY MAP
→ WALKING SKELETON
→ PRIMARY TASK
→ BOUNDED IMPLEMENTATION
→ LOCAL LENS + SYSTEM LENS
→ REVIEW / REMEDIATION
→ INDEPENDENT CLOSURE when justified
→ OPERATOR PRODUCTION AUTHORITY
→ ROLLBACK / RECOVERY READY</code></pre>

<p>اصل مرکزی:</p>
<blockquote><p>Quality requirements ثابت می‌ماند؛ Ceremony بر اساس Risk تغییر می‌کند.</p></blockquote>

<h2>۳. Presetها؛ برای شروع لازم نیست ده‌ها تنظیم را دستی بچینید</h2>
<pre dir="ltr" style="text-align:left"><code>VIBE_FAST
PRODUCT_STANDARD
HIGH_ASSURANCE</code></pre>

<ul>
<li><code>VIBE_FAST</code>: برای آزمایش، امکان‌سنجی و یادگیری سریع؛ کد می‌تواند sacrificial باشد ولی Production claim ندارد.</li>
<li><code>PRODUCT_STANDARD</code>: انتخاب عادی برای محصول قابل نگهداری.</li>
<li><code>HIGH_ASSURANCE</code>: برای پول، Identity، Privacy، Tenant Isolation، Durability حساس، عملیات destructive/regulated یا رفتار پرریسک.</li>
</ul>

<p>Phase پروژه جداست:</p>
<pre dir="ltr" style="text-align:left"><code>VIBE_PROTOTYPE | PRODUCT_BUILD | MAINTENANCE</code></pre>

<pre dir="ltr" style="text-align:left"><code>VIBE_PROTOTYPE != PRODUCTION BASELINE</code></pre>

<h2>۴. وقتی فقط به‌عنوان Product Owner می‌دانید چه می‌خواهید</h2>
<p>لازم نیست خودتان Database، Vector Store یا Framework انتخاب کنید. شما باید Outcome و Trade-off را مشخص کنید: کاربر کیست، جواب خوب/بد چیست، Privacy/Freshness/Latency/Cost چقدر مهم است، چه چیزی Audit‌پذیر باشد و در Failure چه رفتاری قابل قبول است.</p>

<pre dir="ltr" style="text-align:left"><code>PRODUCT BRIEF
→ QUALITY / EVAL CONTRACT
→ ARCHITECTURE DISCOVERY
→ SYSTEM TRUTH MAP
→ CURRENT SCALE BOUNDARY
→ 2–3 MINIMAL OPTIONS when useful
→ WALKING SKELETON
→ ARCHITECTURE CHECKPOINT</code></pre>

<p>برای RAG/Search/AI، قبل از tuning جدی باید Eval Baseline نماینده داشته باشیم. Vector Vendor، Chunk Size، Embedding، Top-K، Reranker یا Prompt صرفاً از روی عادت Agent انتخاب و Freeze نمی‌شوند.</p>

<h2>۵. Dual-Lens: درست بودن Local کافی نیست</h2>
<pre dir="ltr" style="text-align:left"><code>LOCAL LENS
Does the changed behavior work correctly?

SYSTEM LENS
What truth does the whole system claim after this change?</code></pre>

<p>System Lens به ابعادی مثل این نگاه می‌کند:</p>
<pre dir="ltr" style="text-align:left"><code>WRITE · READ · AGGREGATE · CACHE · RESTART · FAILURE · RECOVERY
ADMIN · METRIC · TENANT_ISOLATION · SCALE · PRIVACY · COST</code></pre>

<p>اما Flow عمداً از Checklist Theater جلوگیری می‌کند:</p>
<ul>
<li>LOW و واقعاً Local: خلاصه کوتاه System Impact؛ ۱۳ خانه مکانیکی پر نمی‌شود.</li>
<li>MEDIUM/HIGH: ابعاد مرتبط صریح ثبت می‌شوند.</li>
<li>Money/Privacy/Identity/Tenant/Durability/Recovery/Destructive/Production: ابعاد affected همیشه صریح‌اند.</li>
</ul>

<h2>۶. System Truth Map</h2>
<p>برای Product Build و سیستم‌های Stateful/Cost/Privacy/Tenant-sensitive یک Map کوچک نگه می‌داریم:</p>
<pre dir="ltr" style="text-align:left"><code>.agentic/SYSTEM_TRUTH_MAP.yaml</code></pre>

<p>Template: <code>templates/SYSTEM_TRUTH_MAP.example.yaml</code></p>

<p>این Map مشخص می‌کند چه چیزی authoritative است، چه چیزهایی cache/projection هستند، چه چیزی بعد از Restart می‌ماند، Failure چه می‌کند، Recovery چگونه است، Tenant Isolation چگونه enforce می‌شود و مرز Scale فعلی چیست.</p>

<blockquote><p>Cache، Projection، Summary یا Metric صرفاً چون خواندنش راحت است منبع حقیقت نمی‌شود.</p></blockquote>

<h2>۷. Primary Task نباید توسط Side Task بلعیده شود</h2>
<pre dir="ltr" style="text-align:left"><code>PRIMARY_TASK = هدف durable اصلی
SIDE_TASK    = کار کمکی محدود
INTERRUPT    = وقفه فوری و محدود</code></pre>

<pre dir="ltr" style="text-align:left"><code>RECENCY IS NOT PRIORITY.
CONVERSATIONAL MOMENTUM CANNOT PROMOTE A SIDE TASK.</code></pre>

<p>Side Task باید Primary Ref، Success Condition، Budget/Scope و Return Condition داشته باشد. Promotion فقط با تصمیم صریح Manager/Operator انجام می‌شود.</p>

<h2>۸. Swamp Guard</h2>
<pre dir="ltr" style="text-align:left"><code>CLEAR | WATCH | ALERT | STOP_REBASELINE</code></pre>

<p>Signalها شامل Architecture Churn، Remediation تکراری، Framework/Datastore/Abstraction بی‌دلیل، چند Mechanism برای یک Responsibility، AI/RAG tuning بدون Eval، Feature Growth قبل از Vertical Slice، Source-of-Truth مبهم، Prototype-to-Production Drift، Side-task Drift و System-Lens Risk حل‌نشده است.</p>

<pre dir="ltr" style="text-align:left"><code>STOP_REBASELINE
→ preserve state/evidence
→ architecture discovery
→ simplify / measure / decide
→ resume from coherent baseline</code></pre>

<p>خود Agentic Flow هم تحت Swamp Guard است: وقتی Policy زیاد می‌شود، قبل از افزودن مفهوم جدید باید Simplify و Validate کنیم.</p>

<h2>۹. Risk و Workflow</h2>
<pre dir="ltr" style="text-align:left"><code>LOW
execute → focused test → compact diff review → compact system-impact summary

MEDIUM
short preflight → execute → Dual-Lens → cold review
→ one remediation → Manager review

HIGH
frozen contract → failure/System-Lens preflight → explicit authority
→ bounded execution → adversarial review → Manager findings
→ one remediation by default → read-only Independent Judge
→ Operator production/business decision</code></pre>

<p>Round دوم Remediation فقط با New Material Finding توجیه دارد.</p>

<h2>۱۰. مدل اجراکننده و مدل مراقب</h2>
<p>Executor می‌تواند مدل cost-efficient و مناسب Task باشد. Manager/Judge در موارد سخت می‌توانند reasoning قوی‌تر داشته باشند. ولی مدل متفاوت به‌تنهایی evidence مستقل نمی‌سازد.</p>

<pre dir="ltr" style="text-align:left"><code>MULTI-MODEL AGREEMENT
!=
INDEPENDENT BEHAVIORAL EVIDENCE</code></pre>

<p>Independent Closure تا جای ممکن چهار جدایی دارد:</p>
<pre dir="ltr" style="text-align:left"><code>IMPLEMENTATION
CONTEXT
AUTHORITY
EVIDENCE</code></pre>

<p>Independent Judge پیش‌فرض Read-only است و Production را mutate نمی‌کند.</p>

<h2>۱۱. Evidence و Test</h2>
<pre dir="ltr" style="text-align:left"><code>unit PASS          != user flow proven
HTTP 200           != persistence
CI green           != deployed artifact
backup configured  != restore proven
reviewer PASS      != runtime evidence</code></pre>

<p>برای Testهای باربر، Mutation/Path Proof وقتی عملی است انجام می‌شود: رفتار هدف در Copy ایزوله خراب می‌شود و تست باید قرمز شود. Workspace ناشناخته اپراتور با Git destructive command قربانی Mutation Testing نمی‌شود.</p>

<h2>۱۲. Cross-System Audit</h2>
<p>اولویت Trigger:</p>
<pre dir="ltr" style="text-align:left"><code>EVENT
> RISK / AUTHORITY CHANGE
> TASK-COUNT REMINDER</code></pre>

<p>Release واقعی، Incident مادی یا تغییر مهم Security/Data/Authority/Recovery می‌تواند فوراً Audit را trigger کند. عدد ۵ تا ۸ Material Task فقط Reminder است.</p>

<h2>۱۳. Production</h2>
<pre dir="ltr" style="text-align:left"><code>NO ROLLBACK / RECOVERY PLAN
→ NOT EXECUTION-READY FOR PRODUCTION MUTATION</code></pre>

<p>قبل از هر Production Mutation باید Target/Artifact/Change Identity، Health Signal، Abort Condition، Rollback یا Forward Recovery، State/Data Constraints، Recovery Owner و Post-change Verification مشخص باشد.</p>

<p>اگر Rollback ممکن نیست، Forward Recovery، Backup/Checkpoint و Blast-radius Control لازم است. PASS مدل مراقب مجوز Production نیست.</p>

<h2>۱۴. Human نباید Message Bus باشد</h2>
<pre dir="ltr" style="text-align:left"><code>Human transports authority.
Repository transports engineering state.</code></pre>

<p>Project Mode/Preset، System Truth Map، Primary Task، Exact Refs، Findings، Remediation State، Receipts/Gaps، Swamp State و Next Authority Decision باید در Repository قابل بازیابی باشند.</p>

<h2>۱۵. مسیر مطالعه</h2>
<pre dir="ltr" style="text-align:left"><code>برای فهم سریع:
README.md
→ docs/GETTING_STARTED.md

برای اپراتور:
docs/operator/OPERATOR_GUIDE.fa.md

برای Agent:
docs/agent/START_HERE.md

برای Greenfield:
docs/agent/PROJECT_INCEPTION_ARCHITECTURE.md

برای Task Material:
docs/agent/TASK_WORKFLOW_DRAFT_REVIEW_APPLY_VERIFY.md

Authority نهایی:
ARCHITECTURE.md</code></pre>

<blockquote><p>هدف Agentic Flow حداکثر کردن Process نیست؛ هدف کمترین Processی است که Product Intent، System Truth، Evidence و Authority را در Risk فعلی منسجم نگه دارد.</p></blockquote>
</div>
