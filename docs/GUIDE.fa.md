<div dir="rtl" align="right">
<h1 id="راهنمای-جامع-فارسی-agentic-flow">راهنمای جامع فارسی Agentic
Flow</h1>
<p><strong>نسخه فریم‌ورک: 1.8</strong> <strong>به‌روزرسانی:
2026-09-13</strong> <strong>وضعیت: فریم‌ورک عملیاتی مبتنی بر شواهد، در
حال اعتبارسنجی</strong></p>
<p>این سند راهنمای مستقل فارسی برای فهمیدن، راه‌اندازی و استفاده از
Agentic Flow است. برای شروع لازم نیست همه فایل‌های ریپو را بخوانید.</p>
<blockquote>
<p>مسئله اصلی تولید سریع کد نیست؛ مسئله این است که بدانیم دقیقاً چه چیزی
مجاز بوده، چه چیزی تغییر کرده، کدام رفتار واقعاً اجرا شده، شواهد چه
ادعایی را ثابت می‌کنند و چه چیزهایی هنوز نامعلوم‌اند.</p>
</blockquote>
<h2 id="۱-این-ریپو-چرا-وجود-دارد">۱. این ریپو چرا وجود دارد؟</h2>
<p>در استفاده معمول از coding agent، یک گفت‌وگو ممکن است هم‌زمان نقش
نیازمندی، برنامه، مجوز، گزارش اجرا و مدرک تکمیل را بازی کند. نتیجه
می‌تواند یک حالت ظاهراً کامل اما نادرست باشد:</p>
<ul>
<li>عامل بدون اعلام دامنه کار را بزرگ‌تر می‌کند؛</li>
<li>یک unit test یا mock سبز به‌عنوان اثبات integration واقعی گزارش
می‌شود؛</li>
<li>همان عامل task را تعریف، پیاده‌سازی، تأیید و بسته‌شدن آن را اعلام
می‌کند؛</li>
<li>وجود کد یا سبز بودن CI با اجرا، deployment یا production readiness
اشتباه گرفته می‌شود؛</li>
<li>تصمیم‌ها داخل تاریخچه چت می‌مانند؛</li>
<li>عبارت «انجام شد» unknownها و operational gapها را پنهان می‌کند.</li>
</ul>
<p>Agentic Flow بخش پایدار کار را وارد خود ریپو می‌کند: profile پروژه،
task contract منجمد، mutation policy، receiptهای قابل ردیابی، gapهای
صریح و تصمیم review. گفت‌وگو فقط context موقت کار است.</p>
<h2 id="۲-ایده-مرکزی">۲. ایده مرکزی</h2>
<pre dir="ltr" style="text-align:left" class="text"><code>WHAT SHOULD BE TRUE   → project profile + frozen task
WHAT MAY CHANGE NOW   → mutation approval
WHERE ACTION MAY RUN  → environment authority
WHAT WAS DONE         → exact diff / commit / artifact
WHAT WAS OBSERVED     → claim-bound receipts
WHAT IS UNKNOWN       → explicit unknowns / gaps
WHO DECIDES           → operator / manager</code></pre>
<p>قاعده اصلی این است:</p>
<blockquote>
<p>دامنه هر ادعا نباید از receipt فعلی که مستقیماً آن را ثابت می‌کند
بزرگ‌تر باشد.</p>
</blockquote>
<p>وجود یک migration در source فقط وجود آن فایل را ثابت می‌کند. اجرای
موفق migration روی database واقعی چیز دیگری است. deployment نیز بدون
هویت artifact و environment و live check ثابت نمی‌شود.</p>
<h2 id="۳-مقایسه-با-روش-معمول">۳. مقایسه با روش معمول</h2>
<table>
<thead>
<tr>
<th>Agentic Flow</th>
<th>روش معمول</th>
</tr>
</thead>
<tbody>
<tr>
<td>source of truth در repository و ref مشخص است</td>
<td>چت عملاً source of truth می‌شود</td>
</tr>
<tr>
<td>Designer، Manager و Executor جدا هستند</td>
<td>یک عامل معمولاً همه نقش‌ها را دارد</td>
</tr>
<tr>
<td>task، mutation و environment authority جدا هستند</td>
<td>«انجامش بده» ممکن است همه چیز تلقی شود</td>
</tr>
<tr>
<td>هر claim به minimum receipt وصل می‌شود</td>
<td>«tests passed» علامت کلی completion است</td>
</tr>
<tr>
<td>mock فقط boundary مدل‌شده را ثابت می‌کند</td>
<td>mock ممکن است جای integration واقعی بنشیند</td>
</tr>
<tr>
<td>unknown و gap حذف نمی‌شوند</td>
<td>summary خوش‌بینانه آن‌ها را پنهان می‌کند</td>
</tr>
<tr>
<td>handoff با state فشرده یا context packet انجام می‌شود</td>
<td>ادامه کار به replay چت وابسته است</td>
</tr>
</tbody>
</table>
<p>این روش برای هر تغییر کوچک لازم نیست سنگین باشد. ارزش اصلی آن در
کارهای material، چندعاملی، دارای database، provider، security،
deployment یا هزینه بالای false-complete است.</p>
<h2 id="۴-نقشها-و-جدایی-اختیار">۴. نقش‌ها و جدایی اختیار</h2>
<h3 id="designer--task-architect">Designer / Task Architect</h3>
<p>Designer با دسترسی read-only، intent اپراتور و واقعیت ریپو را به دو
خروجی تبدیل می‌کند:</p>
<ol type="1">
<li>Frozen Contract Proposal شامل WHAT، success، scope، acceptance و
STOP condition؛</li>
<li>Engineering Advisory شامل راهنمای HOW که به شواهد موجود محدود
است.</li>
</ol>
<p>Designer کد محصول را تغییر نمی‌دهد، task خودش را approve نمی‌کند و کد
Executor را merge نمی‌کند.</p>
<h3 id="manager--reviewer">Manager / Reviewer</h3>
<p>Manager مسئول کیفیت task و authority است. او proposal را با intent و
source واقعی مقایسه می‌کند، در صورت مجاز بودن task را freeze می‌کند،
preview تغییر را بررسی می‌کند و پس از اجرا خود commit یا PR و receiptهای
خام را می‌بیند. summary عامل جای diff واقعی را نمی‌گیرد.</p>
<h3 id="executor">Executor</h3>
<p>Executor HOW را در مرز frozen task انتخاب می‌کند، پیش از mutation
طراحی اجرایی کوتاه می‌دهد، روی branch محدود کار می‌کند، changed path را در
محیط مناسب اجرا می‌کند و receipt می‌سازد. Executor نمی‌تواند material
closure را به‌تنهایی تأیید کند یا scope را بدون amendment گسترش دهد.</p>
<pre dir="ltr" style="text-align:left" class="text"><code>Operator intent
→ Designer: contract proposal + advisory
→ Manager: review + freeze + bounded authorization
→ Executor: preflight + implementation + tests + commit/PR
→ Manager: exact diff/commit + raw receipt review
→ authorized merge / closure decision</code></pre>
<p>اگر هر سه session از یک credential نامحدود استفاده کنند، جدایی نقش
فقط procedural است و security boundary واقعی ایجاد نمی‌کند. برای کار
material، identity و permission جدا، protected branch، PR و required
checks بهتر است.</p>
<h2 id="۵-واژگان-advisory">۵. واژگان advisory</h2>
<ul>
<li><strong>MUST</strong>: فقط invariant منجمدشده، owner constraint یا
واقعیت مشاهده‌شده ریپو؛</li>
<li><strong>SHOULD</strong>: پیشنهاد evidence-backed که Executor می‌تواند
با دلیل، جایگزین کوچک‌تر و سازگار انتخاب کند؛</li>
<li><strong>INVESTIGATE</strong>: سؤال یا واقعیتی که پیش از mutation
باید روشن شود؛</li>
<li><strong>AVOID</strong>: failure mode، معماری ناسازگار، test ضعیف یا
خطر محتمل.</li>
</ul>
<p>پیشنهاد یک مدل نباید فقط به دلیل لحن قاطع به MUST تبدیل شود.</p>
<h2 id="۶-دسترسی-مستقیم-git-و-جداسازی-branchpr">۶. دسترسی مستقیم Git و
جداسازی branch/PR</h2>
<p>برای کار medium یا high-risk:</p>
<ul>
<li>Designer ریپو، branch و commit مشخص را مستقیم و read-only بررسی
می‌کند؛</li>
<li>Executor فقط روی task branch محدود commit می‌زند؛</li>
<li>Manager ابتدا frozen contract، سپس advisory، diff واقعی، source
اطراف تغییر و raw receipts را می‌بیند؛</li>
<li>Manager commit SHA یا PR head بررسی‌شده را ثبت می‌کند؛</li>
<li>هر commit جدید پس از approve، review قبلی را برای head جدید stale
می‌کند؛</li>
<li>merge فقط با authority تعریف‌شده پروژه انجام می‌شود.</li>
</ul>
<pre dir="ltr" style="text-align:left" class="text"><code>protected default branch
→ isolated executor branch
→ pull request
→ required CI/checks
→ manager reviews exact head SHA
→ authorized merge decision</code></pre>
<h2 id="۷-جایگزین-context-packet">۷. جایگزین Context Packet</h2>
<p>اگر Designer یا Manager دسترسی مستقیم Git ندارد، context packet محدود
تهیه کنید. packet باید repository، branch، commit، dirty-state، فایل‌ها و
excerptهای مرتبط، profile/task pointers، diff لازم، entrypoint تست،
receiptها، environment identity، omissionها، unknownها و زمان تازگی را
داشته باشد.</p>
<p>Context packet مدرک است، نه authority. برای approve کردن کد
high-risk، packet ناقص جای source/diff مستقیم را نمی‌گیرد. قرارداد کامل
در مسیر زیر است:</p>
<pre dir="ltr" style="text-align:left" class="text"><code>docs/operator/CONTEXT_PACKET.md</code></pre>
<h2 id="۸-محیط-اجرای-لازم">۸. محیط اجرای لازم</h2>
<p>عامل باید حداقل به محیطی دسترسی داشته باشد که بتواند behavior
تغییرکرده را واقعاً exercise کند. توانایی ویرایش کد یا اجرای mock
به‌تنهایی execution readiness نیست.</p>
<pre dir="ltr" style="text-align:left" class="text"><code>LOCAL / HERMETIC
→ EPHEMERAL TEST
→ SHARED TEST
→ STAGING / PRODUCTION-LIKE
→ CONTROLLED PRODUCTION READ / CANARY
→ PRODUCTION MUTATION</code></pre>
<p>پایین‌ترین محیط <strong>کافی</strong> را استفاده کنید، نه قوی‌ترین محیط
را. برای تغییر رفتار غیرمستندی، baseline معمول LOCAL_REAL یا
EPHEMERAL_TEST است، البته وقتی dependencyهای مؤثر را واقعاً اجرا
می‌کند.</p>
<table>
<thead>
<tr>
<th>حداقل receipt معنادار</th>
<th>claim</th>
</tr>
</thead>
<tbody>
<tr>
<td>focused test می‌تواند کافی باشد</td>
<td>pure function یا parser محلی</td>
</tr>
<tr>
<td>application واقعی و database disposable</td>
<td>transaction یا persistence</td>
</tr>
<tr>
<td>migration engine واقعی و داده representative</td>
<td>migration</td>
</tr>
<tr>
<td>contract test و در صورت نیاز sandbox مجاز</td>
<td>provider یا API boundary</td>
</tr>
<tr>
<td>application در حال اجرا و boundaryهای لازم</td>
<td>user workflow</td>
</tr>
<tr>
<td>environment و artifact دقیق و live check</td>
<td>deployment در محیط X</td>
</tr>
</tbody>
</table>
<pre dir="ltr" style="text-align:left" class="text"><code>Claim:
PostgreSQL transaction rollback is correct.

Adequate receipt:
real application path
+ disposable PostgreSQL
+ forced failure
+ query showing neither row persisted

Insufficient alone:
mocked connection PASS</code></pre>
<p>Mock برای unit-level feedback مفید است، اما فقط interaction مدل‌شده را
ثابت می‌کند. mock-only closure نباید ادعای integration، persistence،
migration، end-user، deployment یا production را ببندد.</p>
<p>اگر محیط کافی در authority فعلی موجود نیست:</p>
<ol type="1">
<li>claim را UNVERIFIED یا BLOCKED ثبت کنید؛</li>
<li>environment request محدود با دلیل، resource، duration، cleanup و
risk بسازید؛</li>
<li>برای محیط یا authority مناسب تصمیم بگیرید؛</li>
<li>claim قوی را با receipt ضعیف‌تر حفظ نکنید.</li>
</ol>
<p>درخواست محیط، مجوز استفاده از آن نیست.</p>
<h2 id="۹-چهار-مرز-مستقل">۹. چهار مرز مستقل</h2>
<table>
<thead>
<tr>
<th>سؤال</th>
<th>مرز</th>
</tr>
</thead>
<tbody>
<tr>
<td>چه outcome و scopeای تصویب شده؟</td>
<td>task authority</td>
</tr>
<tr>
<td>در این batch چه فایل یا resourceای تغییر می‌کند؟</td>
<td>mutation authority</td>
</tr>
<tr>
<td>عمل در کدام محیط و با چه سطحی مجاز است؟</td>
<td>environment authority</td>
</tr>
<tr>
<td>چه مشاهده‌ای claim را ثابت می‌کند؟</td>
<td>closure evidence</td>
</tr>
</tbody>
</table>
<p>STRICT_PREVIEW یعنی پیش از هر mutation batch، Executor باید current
state، proposed state، فایل‌ها و resourceهای متأثر، impact، planned
checks، recovery و out-of-scope را بگوید و برای APPROVE یا APPLY صبر
کند. freeze شدن task، مجوز نامحدود mutation یا production نیست.</p>
<h2 id="۱۰-شروع-پنجدقیقهای">۱۰. شروع پنج‌دقیقه‌ای</h2>
<h3 id="گام-اول-چیدمان">گام اول: چیدمان</h3>
<pre dir="ltr" style="text-align:left" class="text"><code>workspace/
├── agentic-flow-framework/
└── my-project/</code></pre>
<p>برای assurance بالاتر، framework را به commit یا tag بررسی‌شده pin
کنید.</p>
<h3 id="گام-دوم-شروع-read-only">گام دوم: شروع read-only</h3>
<p>به coding agent بگویید ابتدا فایل‌های زیر را بخواند و پروژه را بدون
تغییر inspect کند:</p>
<pre dir="ltr" style="text-align:left" class="text"><code>docs/agent/START_HERE.md
ARCHITECTURE.md</code></pre>
<p>اگر کار از قبل در جریان است، MIDSTREAM_ADOPTION باید branch، HEAD،
dirty paths، task جاری، تست‌های اجراشده و environment mutationها را ثبت و
حفظ کند.</p>
<h3 id="گام-سوم-profile-پروژه">گام سوم: profile پروژه</h3>
<p>از template موجود، فایل profile را در پروژه مقصد ایجاد کنید:</p>
<pre dir="ltr" style="text-align:left" class="text"><code>source: templates/PROJECT_PROFILE.example.yaml
target: my-project/.agentic/PROJECT_PROFILE.yaml</code></pre>
<p>در profile، surfaceها، readiness tier، test layerها، execution
readiness، environment permissionها، mutation policy و requirementهای
operation/security را تعیین کنید. profile هدف را تعریف می‌کند؛ اثبات
وضعیت runtime نیست.</p>
<h3 id="گام-چهارم-designer-و-manager">گام چهارم: Designer و Manager</h3>
<p>برای task material دو session جدا باز کنید:</p>
<pre dir="ltr" style="text-align:left" class="text"><code>prompts/operator/TASK_DESIGNER.md
prompts/operator/MANAGER_REVIEWER.md</code></pre>
<p>Designer proposal می‌دهد؛ Manager آن را بررسی و فقط در صورت داشتن
authority freeze می‌کند.</p>
<h3 id="گام-پنجم-اجرا-و-review">گام پنجم: اجرا و review</h3>
<p>Executor روی branch جدا preflight می‌دهد، پس از approval لازم تغییر
می‌دهد، changed path را در محیط کافی اجرا می‌کند و receiptها را به ref و
environment دقیق وصل می‌کند. Manager commit یا PR واقعی را review می‌کند.
نمونه کامل در این مسیر است:</p>
<pre dir="ltr" style="text-align:left" class="text"><code>docs/examples/END_TO_END_TASK.md</code></pre>
<h2 id="۱۱-prompt-اولیه-designer">۱۱. prompt اولیه Designer</h2>
<pre dir="ltr" style="text-align:left" class="text"><code>You are the TASK DESIGNER / TASK ARCHITECT.
You are not the Executor or approving Manager.

Framework: &lt;path&gt;
Repository: &lt;path or owner/name&gt;
Operator intent: &lt;request&gt;

Inspect the identified repository ref read-only.
Do not implement, commit product code, approve, or merge.
Produce:
A) FROZEN CONTRACT PROPOSAL
B) ENGINEERING ADVISORY using MUST/SHOULD/INVESTIGATE/AVOID

Bind every material recommendation to repository evidence.
Define claims, minimum receipts, required real boundaries and the lowest
adequate environment. Mark mock-only limitations and UNKNOWN facts.
Require an Executor implementation-design preflight.
Return a proposal only.</code></pre>
<p>نسخه کامل و آماده کپی در prompts/operator/TASK_DESIGNER.md است.</p>
<h2 id="۱۲-prompt-اولیه-manager">۱۲. prompt اولیه Manager</h2>
<pre dir="ltr" style="text-align:left" class="text"><code>You are the MANAGER / REVIEWER.
You are not the implementation Executor.

Inspect repository evidence directly when available.
Review and freeze the task only when authorized.
Keep task, mutation and environment authority separate.
Reject claims whose planned receipts cannot establish them.
For behavior changes, require a real changed-path execution environment;
mock-only evidence cannot close integration-or-stronger claims.

When a commit/PR exists, review:
frozen contract → advisory → exact diff/head → surrounding source
→ raw tests/environment receipts → Executor summary last.

Return APPROVE, REQUEST CHANGES, BLOCKED/MORE EVIDENCE REQUIRED,
or AMENDMENT REQUIRED, and name the exact reviewed ref.</code></pre>
<p>نسخه کامل در prompts/operator/MANAGER_REVIEWER.md است.</p>
<h2 id="۱۳-نمونه-گردش-کار">۱۳. نمونه گردش کار</h2>
<p>فرض کنید order و audit باید در یک transaction ذخیره شوند:</p>
<ol type="1">
<li>Designer کشف می‌کند تست‌های فعلی repositoryها را mock می‌کنند و
ownership اتصال نامعلوم است.</li>
<li>contract می‌گوید در خطای audit هیچ‌کدام از rowها نباید persist
شود.</li>
<li>minimum receipt، application واقعی همراه PostgreSQL disposable و
query بعد از forced failure است.</li>
<li>Manager task را روی commit مشخص freeze می‌کند، اما mutation هنوز
جداگانه نیاز به approval دارد.</li>
<li>Executor کوچک‌ترین design سازگار را پیشنهاد می‌دهد و فایل‌های دقیق را
در preview می‌آورد.</li>
<li>بعد از approval، روی task branch پیاده‌سازی و integration test واقعی
اجرا می‌شود.</li>
<li>Manager base/head واقعی PR و receipt خام را می‌بیند.</li>
<li>closure فقط همان رفتار مشاهده‌شده را بیان می‌کند و staging و
production را not tested نگه می‌دارد.</li>
</ol>
<h2 id="۱۴-منابع-و-میزان-اتکا">۱۴. منابع و میزان اتکا</h2>
<p>این فریم‌ورک از منابع اولیه برای اجزای مختلف استفاده می‌کند:</p>
<ul>
<li>راهنمای OpenAI، Anthropic و Google برای prompt و context روشن؛</li>
<li>Playwright و Pact برای verification نزدیک به behavior و
boundary؛</li>
<li>Microsoft Well-Architected و Google SRE برای layered testing و محیط
متناسب با risk؛</li>
<li>GitHub برای protected branch و محدودیت معنای green checks؛</li>
<li>OWASP، NIST، SLSA و GitHub dependency review برای security و supply
chain؛</li>
<li>Prometheus، OpenTelemetry، Google SRE و مستندات databaseها برای
observability و recovery.</li>
</ul>
<p>نقشه خلاصه در docs/WHY_AGENTIC_FLOW.md و فهرست کامل لینک‌ها در
docs/references/PRIMARY_SOURCES.md است. این منابع practiceهای جزئی را
پشتیبانی می‌کنند؛ ثابت نمی‌کنند Agentic Flow به‌عنوان سیستم کامل از همه
روش‌ها بهتر است.</p>
<h2 id="۱۵-وضعیت-اعتبارسنجی-و-محدودیتها">۱۵. وضعیت اعتبارسنجی و
محدودیت‌ها</h2>
<p>موارد زیر به‌صورت deterministic در ریپو تست می‌شوند:</p>
<ul>
<li>lintهای verification و production readiness روی fixtureهای
موجود؛</li>
<li>normalization محدود usage telemetry؛</li>
<li>ساخت bundle، manifest، hash و boundary فایل‌ها؛</li>
<li>topology و واژگان ضروری onboarding.</li>
</ul>
<p>موارد زیر هنوز اثبات نشده‌اند:</p>
<ul>
<li>کاهش اندازه‌گیری‌شده false-complete در پروژه‌های واقعی؛</li>
<li>بهبود قطعی defect rate، lead time یا هزینه؛</li>
<li>portability کامل برای همه مدل‌ها و harnessها؛</li>
<li>production readiness هر پروژه adopter.</li>
</ul>
<p>همچنین schemaهای Markdown همه‌جا machine-enforced نیستند؛ جدایی نقش
بدون permission و identity جدا procedural است؛ context packet ممکن است
ناقص یا stale باشد؛ و انتخاب minimum receipt هنوز به judgment نیاز دارد.
جزئیات در docs/VALIDATION_STATUS.md است.</p>
<h2 id="۱۶-تستهای-خود-ریپو">۱۶. تست‌های خود ریپو</h2>
<div class="sourceCode" id="cb14"><pre
class="sourceCode bash"><code class="sourceCode bash"><span id="cb14-1"><a href="#cb14-1" aria-hidden="true" tabindex="-1"></a><span class="ex">python3</span> <span class="at">-m</span> unittest discover <span class="at">-s</span> scripts <span class="at">-p</span> <span class="st">&#39;test_*.py&#39;</span></span>
<span id="cb14-2"><a href="#cb14-2" aria-hidden="true" tabindex="-1"></a><span class="ex">python3</span> scripts/test_docs_onboarding.py</span>
<span id="cb14-3"><a href="#cb14-3" aria-hidden="true" tabindex="-1"></a><span class="ex">python3</span> scripts/build_agent_bundle.py</span></code></pre></div>
<p>PASS این تست‌ها فقط invariantهای خود repository و bundle را در
checkout مشخص ثابت می‌کند؛ نه موفقیت framework در یک پروژه واقعی.</p>
<h2 id="۱۷-ترتیب-مطالعه-پیشنهادی">۱۷. ترتیب مطالعه پیشنهادی</h2>
<ol type="1">
<li>README.md</li>
<li>docs/GETTING_STARTED.md</li>
<li>همین راهنمای فارسی</li>
<li>docs/examples/END_TO_END_TASK.md</li>
<li>docs/operator/DESIGNER_MANAGER_SETUP.md</li>
<li>ARCHITECTURE.md برای policy canonical</li>
<li>فقط schema و verification یا production profile مرتبط با task
جاری</li>
</ol>
<p>برای coding agent، entrypoint همیشه docs/agent/START_HERE.md است؛
operator docs نباید به context دائمی همه agentها تبدیل شوند.</p>
<h2 id="۱۸-خلاصه-عملی">۱۸. خلاصه عملی</h2>
<ul>
<li>ابتدا WHY و claim را روشن کنید.</li>
<li>profile را هدف بدانید، نه evidence.</li>
<li>Designer پیشنهاد می‌دهد؛ Manager authority و review را نگه می‌دارد؛
Executor اجرا می‌کند.</li>
<li>task approval، mutation approval و environment permission یکی
نیستند.</li>
<li>برای changed behavior محیطی لازم است که real path را exercise
کند.</li>
<li>mock فقط claim محدود خودش را می‌بندد.</li>
<li>Manager commit یا PR واقعی را می‌بیند.</li>
<li>unknown، skipped check و operational gap را پنهان نکنید.</li>
<li>production یا destructive action بدون authority صریح مجاز نیست.</li>
<li>هر claim را فقط تا قدرت receipt آن بیان کنید.</li>
</ul>

</div>
