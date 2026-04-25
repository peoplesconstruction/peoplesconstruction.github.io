# Contact form implementation plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a bilingual embedded Google Form to the contact page that fires a Google Ads conversion on submission.

**Architecture:** One Google Form per language, embedded as an iframe in the right column of the existing `.contact-grid`. Conversion tracking detects successful submissions by listening for the iframe's `load` event after the initial render. Form responses land in a Google Sheet and trigger an email notification to the business.

**Tech Stack:** Jekyll (static site, GitHub Pages), Google Forms (embed), Google Ads gtag (conversion tracking).

**Spec:** `docs/superpowers/specs/2026-04-25-contact-form-design.md`

**Note on testing:** This site has no automated test suite (per `CLAUDE.md`). Verification is manual — local Jekyll preview, real form submissions, and the Google Ads conversion debugger / Tag Assistant.

---

## Task 1: Build the English Google Form

**Owner:** Yunfei (Kevin) — done in the Google Forms web UI at https://forms.google.com.

**Output of this task:** A live Google Form whose embed URL will be pasted into Task 5.

- [ ] **Step 1: Create a new blank form**

  Go to https://forms.google.com → "Blank form".
  Title: `Request a Free Estimate — BCCA Peoples Construction`
  Description: `Tell us a bit about your project and we'll be in touch shortly.`

- [ ] **Step 2: Apply the brand theme**

  Click the palette icon (top right) → "Customize theme".
  Set "Color" → custom → hex `#2d5a3d`.
  Background color: leave default (light).
  Header image: optional — can upload a banner from `assets/images/` if desired, otherwise skip.

- [ ] **Step 3: Add Q1 — Name**

  Question: `Name`
  Type: Short answer
  Toggle: "Required" ON

- [ ] **Step 4: Add Q2 — How should we reach you?**

  Click `+` to add a new question.
  Question: `How should we reach you?`
  Description (click ⋮ on the question → "Show" → "Description"): `Please fill in at least one contact method below — phone, email, or WeChat. We'll reach out using your preferred channel(s).`
  Type: Checkboxes
  Options (in this order):
    - `Phone call`
    - `Text message`
    - `Email`
    - `WeChat`
  Toggle: "Required" ON

- [ ] **Step 5: Add Q3 — Phone number**

  Question: `Phone number`
  Type: Short answer
  Required: OFF

- [ ] **Step 6: Add Q4 — Email**

  Question: `Email`
  Type: Short answer
  Required: OFF

  Optional: click ⋮ → Response validation → Text → Email — but this rejects submissions where the email field is empty too, so leave OFF unless you want to enforce email format only when filled.

- [ ] **Step 7: Add Q5 — WeChat ID**

  Question: `WeChat ID`
  Type: Short answer
  Required: OFF

- [ ] **Step 8: Add Q6 — Property location**

  Question: `Property location (city or neighborhood)`
  Type: Short answer
  Required: ON

- [ ] **Step 9: Add Q7 — Service(s) needed**

  Question: `Service(s) needed`
  Type: Checkboxes
  Options:
    - `Landscaping & Garden Design`
    - `Hardscaping & Masonry (paving, retaining walls, walkways)`
    - `Outdoor Living (decks, pergolas, lighting)`
    - `Fencing & Privacy`
    - `Exterior & Property (concrete, excavation, pressure washing)`
    - `Not sure / something else`
  Required: ON

- [ ] **Step 10: Add Q8 — Timeline**

  Question: `When do you need this done?`
  Type: Multiple choice (single select)
  Options:
    - `ASAP / urgent`
    - `Within 1 month`
    - `1–3 months`
    - `3–6 months`
    - `Just exploring / flexible`
  Required: ON

- [ ] **Step 11: Add Q9 — Project details**

  Question: `Project details`
  Description: `Most customers leave this blank — we'll follow up by phone or WeChat to get the details. If you'd like a faster written quote, share what you can here: scope, approximate dimensions, materials, photos (paste links), or anything specific you want us to know.`
  Type: Paragraph
  Required: OFF

- [ ] **Step 12: Configure the response destination**

  Click the `Responses` tab.
  Click the green Sheets icon → "Create a new spreadsheet" → name it `Contact Form Responses (EN)`.
  This binds form submissions to a Google Sheet.

- [ ] **Step 13: Enable email notifications**

  Still on the `Responses` tab, click the `⋮` (three-dot) menu → "Get email notifications for new responses".
  This sends a notification to `bccapeoplesconstruction@gmail.com` (the form owner) on every submission.

- [ ] **Step 14: Get the embed URL**

  Click `Send` (top right) → click the `< >` (embed) icon.
  Copy the `src` URL from the iframe HTML — it looks like `https://docs.google.com/forms/d/e/<FORM_ID>/viewform?embedded=true`.

  **Save this URL** — it goes into Task 5, Step 2 as `EN_FORM_EMBED_URL`.

- [ ] **Step 15: Manual smoke test**

  Open the form's "live" URL (Send → link icon → copy → paste in a new tab). Submit a fake response (name: "Test", check Phone, fill 555-0100, fill location "Test", check any service, pick any timeline, leave details blank).

  Verify:
  - The response appears in the linked Google Sheet within ~5 seconds.
  - You receive an email notification at `bccapeoplesconstruction@gmail.com`.

  Delete the test row from the sheet afterward.

---

## Task 2: Build the Chinese Google Form

**Owner:** Yunfei (Kevin) — done in Google Forms.

Same structure as Task 1 but with all Chinese labels and `WeChat` first in Q2.

- [ ] **Step 1: Create a new blank form**

  Title: `申请免费报价 — BCCA Peoples Construction`
  Description: `请告诉我们您的项目情况，我们将尽快与您联系。`

- [ ] **Step 2: Apply the brand theme**

  Same as Task 1 Step 2 — color `#2d5a3d`.

- [ ] **Step 3: Add Q1 — 姓名**

  Question: `姓名`
  Type: Short answer
  Required: ON

- [ ] **Step 4: Add Q2 — 您希望我们如何联系您？**

  Question: `您希望我们如何联系您？（可多选）`
  Description: `请至少填写以下任一联系方式——电话、电子邮件或微信。我们会通过您偏好的方式与您联系。`
  Type: Checkboxes
  Options (in this order — WeChat first):
    - `微信`
    - `电话`
    - `短信`
    - `电子邮件`
  Required: ON

- [ ] **Step 5: Add Q3 — 电话**

  Question: `电话`
  Type: Short answer
  Required: OFF

- [ ] **Step 6: Add Q4 — 电子邮件**

  Question: `电子邮件`
  Type: Short answer
  Required: OFF

- [ ] **Step 7: Add Q5 — 微信号**

  Question: `微信号`
  Type: Short answer
  Required: OFF

- [ ] **Step 8: Add Q6 — 项目所在地**

  Question: `项目所在地（城市或社区）`
  Type: Short answer
  Required: ON

- [ ] **Step 9: Add Q7 — 所需服务**

  Question: `所需服务`
  Type: Checkboxes
  Options:
    - `园艺与花园设计`
    - `硬质景观与砖石工程（铺路、挡土墙、走道）`
    - `户外生活空间（露台、凉亭、照明）`
    - `围栏与隐私`
    - `外部与物业（混凝土、挖掘、高压清洗）`
    - `不确定 / 其他`
  Required: ON

- [ ] **Step 10: Add Q8 — 希望何时完成？**

  Question: `希望何时完成？`
  Type: Multiple choice
  Options:
    - `越快越好`
    - `1 个月内`
    - `1–3 个月`
    - `3–6 个月`
    - `暂在了解中 / 时间灵活`
  Required: ON

- [ ] **Step 11: Add Q9 — 项目详情**

  Question: `项目详情`
  Description: `大多数客户可以留空——我们会通过电话或微信跟进了解详情。如果您希望尽快收到书面报价，可在此处提供更多信息：项目范围、大致尺寸、材料、照片链接，或其他您希望我们了解的内容。`
  Type: Paragraph
  Required: OFF

- [ ] **Step 12: Bind to a Google Sheet**

  Responses tab → green Sheets icon → "Create a new spreadsheet" → name it `Contact Form Responses (ZH)`.

- [ ] **Step 13: Enable email notifications**

  Responses tab → ⋮ menu → "Get email notifications for new responses".

- [ ] **Step 14: Get the embed URL**

  Send → `< >` icon → copy the iframe `src` URL.

  **Save this URL** — it goes into Task 6, Step 2 as `ZH_FORM_EMBED_URL`.

- [ ] **Step 15: Manual smoke test**

  Submit a fake response on the live URL. Verify it lands in the ZH spreadsheet and triggers an email. Delete the test row afterward.

---

## Task 3: Create the Google Ads conversion action

**Owner:** Yunfei (Kevin) — done in the Google Ads web UI at https://ads.google.com.

**Output:** A `send_to` ID that gets pasted into Task 4.

- [ ] **Step 1: Open the Conversions page**

  Google Ads → Tools (wrench icon, top right) → Measurement → Conversions.

- [ ] **Step 2: Create a new conversion action**

  Click `+ New conversion action` → choose `Website`.

  Enter the website URL: `https://peoplesconstruction.github.io` → Scan.

- [ ] **Step 3: Configure the conversion action**

  Click `+ Add a conversion action manually` (skip the auto-detected ones).

  Settings:
  - **Goal and action optimization:** Submit lead form → Primary
  - **Conversion name:** `Contact form submission`
  - **Value:** `Use the same value for each conversion` → `1.00 CAD`
  - **Count:** `One` (one conversion per click — same as your existing phone/email actions)
  - **Click-through conversion window:** 30 days (default)
  - **View-through conversion window:** 1 day (default)
  - **Attribution model:** Data-driven (default)

  Click `Done` → `Save and continue`.

- [ ] **Step 4: Get the conversion tag snippet**

  On the next page, choose `Use Google tag` (since the site already has the gtag).

  Click `See event snippet`. You'll see code like:

  ```js
  gtag('event', 'conversion', {
    'send_to': 'AW-18062849405/XXXXXXXXX',
    'value': 1.0,
    'currency': 'CAD'
  });
  ```

  **Copy the full `send_to` value** (e.g. `AW-18062849405/XXXXXXXXX`).
  **Save it** — it goes into Task 4, Step 1 as `FORM_CONVERSION_SEND_TO`.

  Click `Done`.

---

## Task 4: Add the gtag conversion-reporting function

**Files:**
- Modify: `_layouts/default.html` (around lines 19–52, after the existing email conversion function)

- [ ] **Step 1: Add the new function**

  In `_layouts/default.html`, find the closing `</script>` of the email conversion block (around line 52). Add this new block immediately after it, before the hreflang `{% if %}` block:

  ```html
  <!-- Event snippet for Form submission conversion page -->
  <script>
  function gtag_report_conversion_form() {
    gtag('event', 'conversion', {
        'send_to': 'FORM_CONVERSION_SEND_TO',
        'value': 1.0,
        'currency': 'CAD'
    });
  }
  </script>
  ```

  Replace `FORM_CONVERSION_SEND_TO` with the value you saved in Task 3, Step 4 (e.g. `AW-18062849405/abcDEFghi123`).

- [ ] **Step 2: Verify the file builds**

  Run: `bundle exec jekyll build`
  Expected: completes with no errors. (If `bundle` isn't installed, run `bundle install` first.)

- [ ] **Step 3: Commit**

  ```bash
  git add _layouts/default.html
  git commit -m "Add gtag conversion function for contact form submissions."
  ```

---

## Task 5: Embed the English form

**Files:**
- Modify: `en/contact.html`
- Modify: `assets/css/main.css` (one new rule)

- [ ] **Step 1: Add CSS for the form column**

  In `assets/css/main.css`, find the `.map-container` rule (around line 573) and add this new rule directly after it:

  ```css
  .contact-form-section h2 {
    margin-bottom: 16px;
  }

  .contact-form-iframe {
    width: 100%;
    height: 900px;
    border: 0;
    border-radius: 8px;
  }
  ```

- [ ] **Step 2: Add the form to en/contact.html**

  In `en/contact.html`, find the closing `</div>` of the left column (the one immediately before `</div>` closing `.contact-grid`, around line 51 — the one right after the "Service Area" `contact-info-item` block).

  Insert this new sibling `<div>` between that closing `</div>` and the `.contact-grid` closing `</div>`:

  ```html
      <div class="contact-form-section">
        <h2>Request a Free Estimate</h2>
        <p>Fill out the form and we'll be in touch shortly.</p>
        <iframe id="contact-form-iframe"
                class="contact-form-iframe"
                src="EN_FORM_EMBED_URL"
                title="Request a Free Estimate"
                loading="lazy">Loading…</iframe>
      </div>

      <script>
        (function() {
          var iframe = document.getElementById('contact-form-iframe');
          if (!iframe) return;
          var loadCount = 0;
          iframe.addEventListener('load', function() {
            loadCount++;
            if (loadCount > 1 && typeof gtag_report_conversion_form === 'function') {
              gtag_report_conversion_form();
            }
          });
        })();
      </script>
  ```

  Replace `EN_FORM_EMBED_URL` with the URL you saved in Task 1, Step 14.

- [ ] **Step 3: Verify the page builds and renders**

  Run: `bundle exec jekyll serve`
  Open: `http://localhost:4000/en/contact/`
  Expected: contact info on the left, embedded Google Form on the right (single column on mobile widths). The form heading reads "Request a Free Estimate".

- [ ] **Step 4: Test conversion firing locally**

  Install the Google Tag Assistant Chrome extension (https://tagassistant.google.com) if you haven't.

  In Tag Assistant, add the URL `http://localhost:4000/en/contact/` and click "Connect". Submit the form with test data. After the iframe reloads to "Your response has been recorded", check Tag Assistant — you should see the conversion event fire with `send_to: AW-18062849405/<your-id>`.

  Delete the test row from the EN response sheet.

- [ ] **Step 5: Commit**

  ```bash
  git add en/contact.html assets/css/main.css
  git commit -m "Embed contact form on English contact page."
  ```

---

## Task 6: Embed the Chinese form

**Files:**
- Modify: `zh/contact.html`

(CSS from Task 5 already covers the ZH page.)

- [ ] **Step 1: Add the form to zh/contact.html**

  In `zh/contact.html`, find the closing `</div>` of the left column (around line 51, after the "服务区域" `contact-info-item`).

  Insert this between that closing `</div>` and the `.contact-grid` closing `</div>`:

  ```html
      <div class="contact-form-section">
        <h2>申请免费报价</h2>
        <p>填写下方表格，我们将尽快与您联系。</p>
        <iframe id="contact-form-iframe"
                class="contact-form-iframe"
                src="ZH_FORM_EMBED_URL"
                title="申请免费报价"
                loading="lazy">加载中…</iframe>
      </div>

      <script>
        (function() {
          var iframe = document.getElementById('contact-form-iframe');
          if (!iframe) return;
          var loadCount = 0;
          iframe.addEventListener('load', function() {
            loadCount++;
            if (loadCount > 1 && typeof gtag_report_conversion_form === 'function') {
              gtag_report_conversion_form();
            }
          });
        })();
      </script>
  ```

  Replace `ZH_FORM_EMBED_URL` with the URL you saved in Task 2, Step 14.

- [ ] **Step 2: Verify the page renders**

  With `bundle exec jekyll serve` still running, open: `http://localhost:4000/zh/contact/`
  Expected: same layout as the EN page but with the Chinese form embedded and the heading "申请免费报价".

- [ ] **Step 3: Test conversion firing locally**

  In Tag Assistant, connect to `http://localhost:4000/zh/contact/`. Submit the ZH form with test data. Verify the conversion event fires.

  Delete the test row from the ZH response sheet.

- [ ] **Step 4: Commit**

  ```bash
  git add zh/contact.html
  git commit -m "Embed contact form on Chinese contact page."
  ```

---

## Task 7: Production verification

After the changes are deployed (GitHub Pages auto-deploys on push to `main`).

- [ ] **Step 1: Push the branch and merge**

  ```bash
  git push -u origin contact-form-spec
  ```

  Open a pull request on GitHub from `contact-form-spec` into `main`. Review the diff, then merge. (Ask user before merging if unsure.)

- [ ] **Step 2: Wait for GitHub Pages to deploy**

  GitHub Actions / Pages typically deploys within 1–2 minutes. Check Settings → Pages → "Last deployed" timestamp.

- [ ] **Step 3: Submit one real test entry on the live site**

  Visit `https://peoplesconstruction.github.io/en/contact/`. Submit a real-looking entry (use your own contact info, label the project description "TEST — please ignore"). Verify:
    - The response appears in the EN Google Sheet.
    - The email notification arrives at `bccapeoplesconstruction@gmail.com`.

  Repeat on `https://peoplesconstruction.github.io/zh/contact/` for the ZH form.

- [ ] **Step 4: Verify conversion in Google Ads**

  Google Ads → Tools → Conversions → click on `Contact form submission`.

  Within 3–24 hours, the "Conversions" count should increment by 2 (one for each test submission). If it doesn't appear after 24 hours, check the Tag Assistant captures from Task 5 Step 4 / Task 6 Step 3 to confirm the snippet is firing.

- [ ] **Step 5: Clean up test data**

  Delete the two test rows from the EN and ZH spreadsheets.

---

## Summary of files changed

- `_layouts/default.html` — added `gtag_report_conversion_form` function
- `en/contact.html` — added form section and load-event tracker
- `zh/contact.html` — added form section and load-event tracker
- `assets/css/main.css` — added `.contact-form-section` and `.contact-form-iframe` rules

## Summary of external setup (done by user)

- One EN Google Form + linked sheet + email notifications
- One ZH Google Form + linked sheet + email notifications
- One new Google Ads conversion action ("Contact form submission")
