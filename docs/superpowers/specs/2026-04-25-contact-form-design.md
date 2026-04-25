# Contact form design

**Status:** Approved 2026-04-25
**Author:** Yunfei (Kevin) Wang
**Affected pages:** `/en/contact/`, `/zh/contact/`

## Goal

Add a short, embedded contact form to the contact page so prospective customers can reach out without picking up the phone or composing an email. Each form submission should fire a Google Ads conversion using the existing `AW-18062849405` tag, and notify the business by email.

## Non-goals

- Replacing or hiding the existing phone / email / WeChat contact cards. The form is additive.
- Building a custom form backend. We use Google Forms because the team is comfortable with it and submissions land in a Google Sheet automatically.
- Tracking offline conversions via the Google Ads API (Path B from the design discussion). Reserved for later if ad spend grows.

## Approach summary

- One Google Form per language (EN, ZH) — the team builds these directly in Google Forms and styles them to match the brand green (`#2d5a3d`).
- Each form is embedded as an iframe on its corresponding contact page, in the right column of the existing `.contact-grid`.
- Conversion tracking uses the **iframe-reload heuristic**: after the initial render, any subsequent `load` event on the iframe is treated as a successful submission, and we fire a third gtag conversion (`gtag_report_conversion_form`).
- Email notifications start with the built-in Google Forms "notify on new response" toggle. Upgrade to a Google Apps Script if richer notifications are needed later.

## Form questions

Both forms have the same nine questions, in this order. Required fields are marked with `*`.

| # | EN label | ZH label | Type | Required |
|---|---|---|---|---|
| 1 | Name | 姓名 | Short answer | * |
| 2 | How should we reach you? *(check all you'd like us to try)* | 您希望我们如何联系您？*（可多选）* | Checkboxes | * |
| 3 | Phone number | 电话 | Short answer |  |
| 4 | Email | 电子邮件 | Short answer |  |
| 5 | WeChat ID | 微信号 | Short answer |  |
| 6 | Property location *(city or neighborhood)* | 项目所在地 *（城市或社区）* | Short answer | * |
| 7 | Service(s) needed | 所需服务 | Checkboxes | * |
| 8 | When do you need this done? | 希望何时完成？ | Multiple choice | * |
| 9 | Project details | 项目详情 | Paragraph |  |

### Q2 — How should we reach you?

EN options (in order): Phone call, Text message, Email, WeChat
ZH options (in order): 微信, 电话, 短信, 电子邮件

The ZH form puts WeChat first because it's the primary channel for many Chinese-speaking customers.

### Q2 description (helper text covering Q3–Q5)

Q2's description field (shown directly under the question, above the contact fields) should read:

- EN: *"Please fill in at least one contact method below — phone, email, or WeChat. We'll reach out using your preferred channel(s)."*
- ZH: *"请至少填写以下任一联系方式——电话、电子邮件或微信。我们会通过您偏好的方式与您联系。"*

This is enforced socially, not technically. Google Forms cannot natively require "at least one of these fields." If the team finds people submitting with no contact info, revisit (e.g., make Q3 a required free-text field with the prompt "phone, email, or WeChat ID — whichever you prefer").

### Q7 — Service(s) needed

Checkboxes mirroring the existing 5 service categories:

EN:
- Landscaping & Garden Design
- Hardscaping & Masonry (paving, retaining walls, walkways)
- Outdoor Living (decks, pergolas, lighting)
- Fencing & Privacy
- Exterior & Property (concrete, excavation, pressure washing)
- Not sure / something else

ZH:
- 园艺与花园设计
- 硬质景观与砖石工程（铺路、挡土墙、走道）
- 户外生活空间（露台、凉亭、照明）
- 围栏与隐私
- 外部与物业（混凝土、挖掘、高压清洗）
- 不确定 / 其他

### Q8 — Timeline

Multiple choice (single select):

EN:
- ASAP / urgent
- Within 1 month
- 1–3 months
- 3–6 months
- Just exploring / flexible

ZH:
- 越快越好
- 1 个月内
- 1–3 个月
- 3–6 个月
- 暂在了解中 / 时间灵活

### Q9 — Project details

Paragraph, optional. Helper text:

- EN: *"Most customers leave this blank — we'll follow up by phone or WeChat to get the details. If you'd like a faster written quote, share what you can here: scope, approximate dimensions, materials, photos (paste links), or anything specific you want us to know."*
- ZH: *"大多数客户可以留空——我们会通过电话或微信跟进了解详情。如果您希望尽快收到书面报价，可在此处提供更多信息：项目范围、大致尺寸、材料、照片链接，或其他您希望我们了解的内容。"*

## Embed on contact pages

The current contact page (`en/contact.html`, `zh/contact.html`) uses `.contact-grid`, a two-column grid where only the left column is populated. The form fills the right column.

**Layout:**
- Section heading above the iframe: *"Request a Free Estimate"* / *"申请免费报价"*
- iframe attributes: `width="100%"`, `height="900"`, `frameborder="0"`, with an `id` for the load-event handler (e.g. `id="contact-form-iframe"`).
- The existing `.contact-grid` rule already collapses to a single column on mobile, so no responsive changes needed.
- Form theme color in Google Forms: `#2d5a3d` (matches `--color-primary`).

## Conversion tracking (Path A — iframe-reload heuristic)

### Why this works

When a user submits a Google Form embedded in an iframe, the iframe reloads to display the "Your response has been recorded" confirmation page. The parent page can listen for the iframe's `load` event. The first `load` is the initial render (ignore); any subsequent `load` is treated as a successful submission.

This is heuristic — it could miscount if a user manually reloads the iframe — but in practice such reloads are rare. The only false negative is a user who closes the tab before the iframe finishes reloading, which is also rare given how fast Google Forms responds.

The conversion fires from the parent page using the existing gtag setup, so the GCLID stored in `_gcl_aw` from the original ad click is automatically attributed.

### Setup steps (Google Ads side)

1. In Google Ads → Tools → Conversions → New conversion action → Website.
2. Category: **Submit lead form**. Name: e.g. "Contact form submission". Value: `1.0 CAD` to match the existing two conversions.
3. Use the same `AW-18062849405` tag (already on the site).
4. Copy the `send_to` ID Google Ads provides (looks like `AW-18062849405/XXXXXXXXX`). This goes into the new `gtag_report_conversion_form` function.

### Code changes

**`_layouts/default.html`** — add a third conversion-reporting function alongside the existing two:

```js
function gtag_report_conversion_form() {
  gtag('event', 'conversion', {
    'send_to': 'AW-18062849405/REPLACE_WITH_FORM_CONVERSION_ID',
    'value': 1.0,
    'currency': 'CAD'
  });
}
```

No `event_callback` redirect is needed — the user stays on the contact page; only the iframe content changes.

**Contact pages** — both `en/contact.html` and `zh/contact.html` get an inline script after the iframe:

```js
(function() {
  var iframe = document.getElementById('contact-form-iframe');
  if (!iframe) return;
  var loadCount = 0;
  iframe.addEventListener('load', function() {
    loadCount++;
    if (loadCount > 1) {
      gtag_report_conversion_form();
    }
  });
})();
```

Self-contained, runs once per page load, no global state.

## Email notifications

**Default (recommended to start):** in Google Forms → Responses tab → ⋮ menu → "Get email notifications for new responses". Sends a bare notification to `bccapeoplesconstruction@gmail.com` (the form owner). User clicks through to read the response.

**Upgrade path** (defer until needed): a ~10-line Google Apps Script `onFormSubmit` trigger that emails the actual answers inline. One script per form (EN, ZH). Not in scope for this spec; revisit if click-through fatigue becomes a problem.

## Implementation walkthrough

The team builds the Google Forms; the implementer (Claude or developer) wires up the embed + conversion tracking on the website.

**Team does** (one-time setup):
1. Create the EN Google Form using the questions above.
2. Apply the brand green theme (`#2d5a3d`).
3. Enable response notifications.
4. Get the embed iframe code (Send → `< >` icon → copy).
5. Repeat for the ZH form.
6. In Google Ads, create the new "Contact form submission" conversion action and copy the `send_to` ID.
7. Hand off both iframe URLs and the conversion ID to the implementer.

**Implementer does:**
1. Add `gtag_report_conversion_form` to `_layouts/default.html` with the conversion ID.
2. In `en/contact.html`, add the section heading, the iframe, and the load-event script. The iframe goes inside the existing `.contact-grid`, after the left column's closing `</div>`.
3. Repeat in `zh/contact.html` with the ZH iframe URL.
4. Test locally with `bundle exec jekyll serve`. Submit a test response on each form, verify it lands in the Google Sheet, verify the conversion fires (Google Ads conversion debugger or Google Tag Assistant).

## Open questions / future work

- If "at least one contact method" enforcement turns out to matter, switch Q3 to a required free-text field (Path 2 from the design discussion).
- If response-notification click-through becomes annoying, add the Apps Script email upgrade.
- If ad spend grows, revisit Path B (offline conversion import) for higher-fidelity attribution.
