# BCCA People Construction Website Design

## Overview

Brochure-style website for BCCA People Construction, a Vancouver landscaping & construction company established in 2009. Hosted on GitHub Pages using Jekyll. Bilingual (English/Chinese) with strong local SEO.

## Architecture

**Platform:** Jekyll on GitHub Pages (native build support, no CI needed)

**Bilingual structure:** Separate page sets per language with a language switcher in the nav.

```
/en/index.html        /zh/index.html
/en/services.html     /zh/services.html
/en/portfolio.html    /zh/portfolio.html
/en/about.html        /zh/about.html
/en/contact.html      /zh/contact.html
```

- Root `index.html` redirects to `/en/`
- `hreflang` tags link English and Chinese versions
- `_data/` YAML files store service lists and project data per language

**Repo structure:**

```
_layouts/           -> default.html, page.html, project.html
_includes/          -> header.html, footer.html, lang-switcher.html
_data/              -> services_en.yml, services_zh.yml, projects.yml
assets/
  css/              -> main.css
  js/               -> main.js (mobile nav, etc.)
  images/
    portfolio/      -> project photos (placeholders initially)
    home/           -> hero/banner images
en/                 -> English pages
zh/                 -> Chinese pages
_config.yml         -> Jekyll configuration
```

## Pages

### Home
- Full-width hero: project photo background, styled "BCCA People Construction" text, tagline "Quality Landscaping & Construction Since 2009", CTA "View Our Work"
- Services overview: 4-6 icon cards linking to Services page
- Featured projects: 3 project cards from portfolio
- Trust bar: "Serving Vancouver & Lower Mainland", years in business, projects completed
- Footer: contact info, quick links, "Free Consultation" callout

### Services
Organized by category with photo alongside each:

**Landscaping & Garden Design:** Landscape design & installation, garden bed creation & planting, sod installation & lawn care, tree & shrub planting, irrigation & sprinkler systems, drainage solutions, yard grading & leveling, seasonal planting & maintenance

**Hardscaping & Masonry:** Paving stone / interlock driveways, natural stone patios, retaining walls, garden walls & borders, walkways & pathways, steps & staircases, curbing & edging

**Outdoor Living:** Custom deck building (wood & composite), pergolas & gazebos, outdoor kitchens & BBQ areas, fire pits & fireplaces, patio covers & shade structures, hot tub surrounds, outdoor lighting & landscape lighting

**Fencing & Privacy:** Wood fencing, vinyl & composite fencing, gates & entries, privacy screens, lattice & trellis work

**Exterior & Property:** Driveway sealing & repair, concrete work, excavation & demolition, snow removal, pressure washing, property maintenance, and more...

### Portfolio / Projects
- Grid of project cards (cover photo, title, short description)
- Click-through to detail pages with multiple photos, description, services used, before/after
- Projects stored in `_data/projects.yml` for easy adding

### About Us
- Company story (est. 2009, Vancouver-based)
- Experience and background
- Why choose BCCA
- Team photo placeholder

### Contact
- Phone, email, WeChat QR code
- Business address / service area
- Embedded Google Map
- Business hours

## Visual Design

**Style:** Clean & modern

- **Colors:** White/light gray backgrounds, dark charcoal text, muted green or blue accent
- **Typography:** Sans-serif Google Font pairing (e.g., Inter or Montserrat), bold headings, regular body
- **Layout:** Generous whitespace, max-width content container, full-bleed hero images
- **Responsive:** Mobile-first CSS, hamburger nav on small screens, stacked layouts on mobile
- **Brand:** Styled text only (no logo file)

## SEO

- Semantic HTML5 elements
- Per-page `<title>` and `<meta description>`, localized per language
- `hreflang` tags linking language versions
- LocalBusiness structured data (JSON-LD)
- Alt text on all images
- Target keywords: "Vancouver landscaping contractor", "landscaping company Vancouver BC", service-specific terms, Chinese equivalents

## Placeholder Images

- Colored placeholder `.jpg` files for each section
- Organized in `assets/images/` with clear naming (e.g., `portfolio/project-1-cover.jpg`, `home/hero.jpg`)
- Easy to swap with real photos later
