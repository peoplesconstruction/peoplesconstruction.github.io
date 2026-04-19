# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Business website for **BCCA Peoples Construction LTD**, a Vancouver-area landscaping and construction company (est. 2009). Hosted on GitHub Pages at peoplesconstruction.github.io.

## Development Commands

```bash
# Install dependencies
bundle install

# Serve locally with live reload
bundle exec jekyll serve

# Build for production
bundle exec jekyll build
```

No tests, linting, or build pipeline — this is a static Jekyll site deployed automatically by GitHub Pages on push to `main`.

## Architecture

**Static site generator:** Jekyll via the `github-pages` gem. No custom plugins (GitHub Pages restriction).

**Bilingual structure (English/Chinese):** Every page exists in both `/en/` and `/zh/` with mirrored file names. Pages link to their counterpart via front matter fields `zh_pair` / `en_pair`, which power `<link rel="alternate" hreflang="...">` tags and the language switcher in the header. The root `index.html` redirects to `/en/`.

**Layouts and includes:**
- `_layouts/default.html` — base layout with SEO schema markup (English only), Google Fonts, and shared CSS/JS
- `_layouts/page.html` — extends default, adds page title/description header
- `_includes/header.html` — nav with language-conditional links; active state set by `page.nav` front matter
- `_includes/footer.html`

**Data-driven content (`_data/`):**
- `services_en.yml` / `services_zh.yml` — service categories, descriptions, and line items
- `gallery_en.yml` / `gallery_zh.yml` — photo gallery entries (src, alt, caption) used on portfolio and home pages
- `contact.yml` — shared contact info (phone numbers differ by language)

**Static assets:**
- `assets/css/main.css` — single stylesheet, CSS custom properties for theming (green palette: `--color-primary: #2d5a3d`)
- `assets/js/main.js` — minimal JS: mobile nav toggle, header scroll shrink
- `assets/images/` — organized by page (home/, services/, contact/, gallery/)
- `photos/` — source photos (raw JPGs), not served directly

**Key front matter fields for pages:** `layout`, `title`, `description`, `lang` (en/zh), `nav` (home/services/portfolio/about/contact), `zh_pair`/`en_pair` (path to language counterpart).

## Content Conventions

- When adding a new page, create both `/en/` and `/zh/` versions with matching `zh_pair`/`en_pair` front matter
- Gallery photos are referenced in `_data/gallery_*.yml`; images go in `assets/images/gallery/`
- Services are data-driven — edit `_data/services_en.yml` and `_data/services_zh.yml`, not the HTML templates
- The site uses emoji icons on the home page service cards (hardcoded in `en/index.html` and `zh/index.html`)
