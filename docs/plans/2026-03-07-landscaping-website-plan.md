# BCCA People Construction Website Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a bilingual (English/Chinese) Jekyll website for BCCA People Construction, a Vancouver landscaping contractor, hosted on GitHub Pages.

**Architecture:** Jekyll static site with separate page sets per language (`/en/`, `/zh/`), shared layouts/includes, YAML data files for services and projects, and mobile-first responsive CSS. Root redirects to `/en/`.

**Tech Stack:** Jekyll, HTML5, CSS3, vanilla JavaScript, GitHub Pages

---

### Task 1: Jekyll Project Setup

**Files:**
- Create: `Gemfile`
- Create: `_config.yml`
- Create: `.gitignore`

**Step 1: Create Gemfile**

```ruby
source "https://rubygems.org"

gem "github-pages", group: :jekyll_plugins
```

**Step 2: Create `_config.yml`**

```yaml
title: BCCA People Construction
description: "Quality Landscaping & Construction Since 2009 - Serving Vancouver & Lower Mainland"
url: "https://peoplesconstruction.github.io"
baseurl: ""

permalink: pretty

defaults:
  - scope:
      path: "en"
    values:
      lang: "en"
      lang_name: "English"
  - scope:
      path: "zh"
    values:
      lang: "zh"
      lang_name: "中文"

exclude:
  - Gemfile
  - Gemfile.lock
  - README.md
  - docs/
  - .Rhistory
```

**Step 3: Create `.gitignore`**

```
_site/
.sass-cache/
.jekyll-cache/
.jekyll-metadata
Gemfile.lock
.bundle/
vendor/
.Rhistory
.DS_Store
```

**Step 4: Create directory structure**

```bash
mkdir -p _layouts _includes _data assets/css assets/js assets/images/home assets/images/portfolio assets/images/services assets/images/about en zh
```

**Step 5: Verify Jekyll builds**

Run: `bundle install && bundle exec jekyll build`
Expected: Build succeeds (may warn about empty site)

**Step 6: Commit**

```bash
git add Gemfile _config.yml .gitignore
git commit -m "feat: initialize Jekyll project with config and Gemfile"
```

---

### Task 2: Generate Placeholder Images

**Files:**
- Create: `scripts/generate_placeholders.py`
- Create: 15+ placeholder `.jpg` files in `assets/images/`

**Step 1: Create placeholder generation script**

This script uses Python's Pillow library to generate colored placeholder images with text labels. If Pillow is not installed, run `pip install Pillow` first.

```python
#!/usr/bin/env python3
"""Generate placeholder images for BCCA People Construction website."""

from PIL import Image, ImageDraw, ImageFont
import os

def create_placeholder(path, width, height, color, text):
    """Create a colored placeholder image with centered text."""
    img = Image.new('RGB', (width, height), color)
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 28)
    except (OSError, IOError):
        font = ImageFont.load_default()
    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    x = (width - tw) // 2
    y = (height - th) // 2
    draw.text((x, y), text, fill="white", font=font)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    img.save(path, "JPEG", quality=80)
    print(f"Created: {path}")

base = "assets/images"

# Home page
create_placeholder(f"{base}/home/hero.jpg", 1920, 800, "#2d5a3d", "Hero Image")

# Service category photos
categories = ["landscaping", "hardscaping", "outdoor-living", "fencing", "exterior"]
colors = ["#3a7d44", "#6b705c", "#4a6741", "#5a7247", "#4e6e58"]
for cat, col in zip(categories, colors):
    create_placeholder(f"{base}/services/{cat}.jpg", 800, 600, col, cat.replace("-", " ").title())

# Portfolio project photos (6 projects, cover + 2 detail each)
project_colors = ["#3a5a40", "#588157", "#4a7c59", "#2d6a4f", "#40916c", "#52b788"]
for i in range(1, 7):
    create_placeholder(f"{base}/portfolio/project-{i}-cover.jpg", 800, 600, project_colors[i-1], f"Project {i}")
    create_placeholder(f"{base}/portfolio/project-{i}-before.jpg", 800, 600, "#8b8b8b", f"Project {i} Before")
    create_placeholder(f"{base}/portfolio/project-{i}-after.jpg", 800, 600, project_colors[i-1], f"Project {i} After")

# About page
create_placeholder(f"{base}/about/team.jpg", 800, 600, "#4a6741", "Team Photo")

# WeChat QR placeholder
create_placeholder(f"{base}/contact/wechat-qr.jpg", 300, 300, "#07c160", "WeChat QR")

print("All placeholders generated!")
```

**Step 2: Run the script**

Run: `cd /Users/yunfe/Documents/GitHub/peoplesconstruction.github.io && python3 scripts/generate_placeholders.py`
Expected: All images created in `assets/images/`

**Step 3: Verify images exist**

Run: `find assets/images -name "*.jpg" | sort`
Expected: ~25 placeholder images listed

**Step 4: Commit**

```bash
git add scripts/generate_placeholders.py assets/images/
git commit -m "feat: add placeholder images and generation script"
```

---

### Task 3: Data Files

**Files:**
- Create: `_data/services_en.yml`
- Create: `_data/services_zh.yml`
- Create: `_data/projects_en.yml`
- Create: `_data/projects_zh.yml`
- Create: `_data/contact.yml`

**Step 1: Create `_data/services_en.yml`**

```yaml
- category: "Landscaping & Garden Design"
  image: "/assets/images/services/landscaping.jpg"
  description: "Transform your outdoor space with professional landscape design and installation services."
  items:
    - "Landscape design & installation"
    - "Garden bed creation & planting"
    - "Sod installation & lawn care"
    - "Tree & shrub planting"
    - "Irrigation & sprinkler systems"
    - "Drainage solutions"
    - "Yard grading & leveling"
    - "Seasonal planting & maintenance"

- category: "Hardscaping & Masonry"
  image: "/assets/images/services/hardscaping.jpg"
  description: "Durable, beautiful hardscape features built with quality materials and expert craftsmanship."
  items:
    - "Paving stone & interlock driveways"
    - "Natural stone patios"
    - "Retaining walls"
    - "Garden walls & borders"
    - "Walkways & pathways"
    - "Steps & staircases"
    - "Curbing & edging"

- category: "Outdoor Living"
  image: "/assets/images/services/outdoor-living.jpg"
  description: "Create the perfect outdoor living space for entertaining, relaxing, and enjoying nature."
  items:
    - "Custom deck building (wood & composite)"
    - "Pergolas & gazebos"
    - "Outdoor kitchens & BBQ areas"
    - "Fire pits & fireplaces"
    - "Patio covers & shade structures"
    - "Hot tub surrounds"
    - "Outdoor lighting & landscape lighting"

- category: "Fencing & Privacy"
  image: "/assets/images/services/fencing.jpg"
  description: "Enhance your property's security and curb appeal with professionally installed fencing."
  items:
    - "Wood fencing"
    - "Vinyl & composite fencing"
    - "Gates & entries"
    - "Privacy screens"
    - "Lattice & trellis work"

- category: "Exterior & Property"
  image: "/assets/images/services/exterior.jpg"
  description: "Complete exterior and property services to keep your property looking its best year-round."
  items:
    - "Driveway sealing & repair"
    - "Concrete work (sidewalks, pads, foundations)"
    - "Excavation & demolition"
    - "Snow removal (seasonal)"
    - "Pressure washing"
    - "Property maintenance"
    - "And more..."
```

**Step 2: Create `_data/services_zh.yml`**

```yaml
- category: "园林绿化设计"
  image: "/assets/images/services/landscaping.jpg"
  description: "专业的园林设计与施工服务，打造您理想的户外空间。"
  items:
    - "景观设计与施工"
    - "花坛建造与种植"
    - "草皮铺设与草坪养护"
    - "乔木与灌木种植"
    - "灌溉与喷淋系统"
    - "排水解决方案"
    - "场地平整"
    - "季节性种植与养护"

- category: "硬质景观与砌筑"
  image: "/assets/images/services/hardscaping.jpg"
  description: "采用优质材料和精湛工艺，打造耐久美观的硬质景观。"
  items:
    - "铺路石与联锁砖车道"
    - "天然石材露台"
    - "挡土墙"
    - "花园墙与边界"
    - "人行道与小径"
    - "台阶与楼梯"
    - "路缘与镶边"

- category: "户外生活空间"
  image: "/assets/images/services/outdoor-living.jpg"
  description: "打造完美的户外生活空间，享受娱乐、休闲与自然。"
  items:
    - "定制木甲板（实木与复合材料）"
    - "凉亭与花架"
    - "户外厨房与烧烤区"
    - "火坑与壁炉"
    - "露台遮阳棚"
    - "热水浴缸围护"
    - "户外照明与景观照明"

- category: "围栏与隐私"
  image: "/assets/images/services/fencing.jpg"
  description: "专业安装围栏，提升物业安全性和美观度。"
  items:
    - "木围栏"
    - "乙烯基与复合材料围栏"
    - "大门与入口"
    - "隐私屏风"
    - "格子架与棚架"

- category: "外部与物业服务"
  image: "/assets/images/services/exterior.jpg"
  description: "全方位的外部和物业服务，让您的物业全年保持最佳状态。"
  items:
    - "车道密封与修补"
    - "混凝土工程（人行道、垫层、地基）"
    - "挖掘与拆除"
    - "除雪服务（季节性）"
    - "高压清洗"
    - "物业维护"
    - "更多服务..."
```

**Step 3: Create `_data/projects_en.yml`**

```yaml
- id: "backyard-transformation"
  title: "Complete Backyard Transformation"
  description: "A full backyard renovation including new patio, retaining wall, and garden beds."
  cover: "/assets/images/portfolio/project-1-cover.jpg"
  images:
    - src: "/assets/images/portfolio/project-1-before.jpg"
      alt: "Backyard before renovation"
      caption: "Before"
    - src: "/assets/images/portfolio/project-1-after.jpg"
      alt: "Backyard after renovation"
      caption: "After"
  services:
    - "Landscape design & installation"
    - "Natural stone patios"
    - "Retaining walls"

- id: "front-yard-paving"
  title: "Front Yard Paving & Landscaping"
  description: "New interlock driveway and front garden with irrigation system."
  cover: "/assets/images/portfolio/project-2-cover.jpg"
  images:
    - src: "/assets/images/portfolio/project-2-before.jpg"
      alt: "Front yard before paving"
      caption: "Before"
    - src: "/assets/images/portfolio/project-2-after.jpg"
      alt: "Front yard after paving"
      caption: "After"
  services:
    - "Paving stone & interlock driveways"
    - "Garden bed creation & planting"
    - "Irrigation & sprinkler systems"

- id: "outdoor-living-deck"
  title: "Custom Deck & Outdoor Kitchen"
  description: "Multi-level composite deck with built-in BBQ area and pergola."
  cover: "/assets/images/portfolio/project-3-cover.jpg"
  images:
    - src: "/assets/images/portfolio/project-3-before.jpg"
      alt: "Yard before deck construction"
      caption: "Before"
    - src: "/assets/images/portfolio/project-3-after.jpg"
      alt: "Completed deck and outdoor kitchen"
      caption: "After"
  services:
    - "Custom deck building (wood & composite)"
    - "Outdoor kitchens & BBQ areas"
    - "Pergolas & gazebos"

- id: "garden-retaining-wall"
  title: "Terraced Garden with Retaining Walls"
  description: "Multi-tier retaining wall system with integrated garden beds and lighting."
  cover: "/assets/images/portfolio/project-4-cover.jpg"
  images:
    - src: "/assets/images/portfolio/project-4-before.jpg"
      alt: "Sloped yard before retaining walls"
      caption: "Before"
    - src: "/assets/images/portfolio/project-4-after.jpg"
      alt: "Terraced garden with retaining walls"
      caption: "After"
  services:
    - "Retaining walls"
    - "Garden bed creation & planting"
    - "Outdoor lighting & landscape lighting"

- id: "cedar-fence-privacy"
  title: "Cedar Fence & Privacy Screen"
  description: "Full property cedar fencing with custom gate and privacy screening."
  cover: "/assets/images/portfolio/project-5-cover.jpg"
  images:
    - src: "/assets/images/portfolio/project-5-before.jpg"
      alt: "Property before fencing"
      caption: "Before"
    - src: "/assets/images/portfolio/project-5-after.jpg"
      alt: "Completed cedar fence"
      caption: "After"
  services:
    - "Wood fencing"
    - "Gates & entries"
    - "Privacy screens"

- id: "complete-exterior"
  title: "Complete Exterior Renovation"
  description: "Driveway replacement, walkway installation, and landscape lighting."
  cover: "/assets/images/portfolio/project-6-cover.jpg"
  images:
    - src: "/assets/images/portfolio/project-6-before.jpg"
      alt: "Exterior before renovation"
      caption: "Before"
    - src: "/assets/images/portfolio/project-6-after.jpg"
      alt: "Completed exterior renovation"
      caption: "After"
  services:
    - "Paving stone & interlock driveways"
    - "Walkways & pathways"
    - "Outdoor lighting & landscape lighting"
```

**Step 4: Create `_data/projects_zh.yml`**

```yaml
- id: "backyard-transformation"
  title: "后院全面改造"
  description: "后院全面翻新，包括新露台、挡土墙和花坛。"
  cover: "/assets/images/portfolio/project-1-cover.jpg"
  images:
    - src: "/assets/images/portfolio/project-1-before.jpg"
      alt: "后院翻新前"
      caption: "施工前"
    - src: "/assets/images/portfolio/project-1-after.jpg"
      alt: "后院翻新后"
      caption: "施工后"
  services:
    - "景观设计与施工"
    - "天然石材露台"
    - "挡土墙"

- id: "front-yard-paving"
  title: "前院铺装与绿化"
  description: "新的联锁砖车道和带灌溉系统的前花园。"
  cover: "/assets/images/portfolio/project-2-cover.jpg"
  images:
    - src: "/assets/images/portfolio/project-2-before.jpg"
      alt: "前院铺装前"
      caption: "施工前"
    - src: "/assets/images/portfolio/project-2-after.jpg"
      alt: "前院铺装后"
      caption: "施工后"
  services:
    - "铺路石与联锁砖车道"
    - "花坛建造与种植"
    - "灌溉与喷淋系统"

- id: "outdoor-living-deck"
  title: "定制甲板与户外厨房"
  description: "多层复合材料甲板，配有内置烧烤区和凉亭。"
  cover: "/assets/images/portfolio/project-3-cover.jpg"
  images:
    - src: "/assets/images/portfolio/project-3-before.jpg"
      alt: "甲板建造前"
      caption: "施工前"
    - src: "/assets/images/portfolio/project-3-after.jpg"
      alt: "完成的甲板和户外厨房"
      caption: "施工后"
  services:
    - "定制木甲板（实木与复合材料）"
    - "户外厨房与烧烤区"
    - "凉亭与花架"

- id: "garden-retaining-wall"
  title: "阶梯式花园与挡土墙"
  description: "多层挡土墙系统，集成花坛和照明。"
  cover: "/assets/images/portfolio/project-4-cover.jpg"
  images:
    - src: "/assets/images/portfolio/project-4-before.jpg"
      alt: "挡土墙施工前"
      caption: "施工前"
    - src: "/assets/images/portfolio/project-4-after.jpg"
      alt: "阶梯式花园与挡土墙"
      caption: "施工后"
  services:
    - "挡土墙"
    - "花坛建造与种植"
    - "户外照明与景观照明"

- id: "cedar-fence-privacy"
  title: "雪松围栏与隐私屏风"
  description: "整个物业的雪松围栏，配有定制大门和隐私屏风。"
  cover: "/assets/images/portfolio/project-5-cover.jpg"
  images:
    - src: "/assets/images/portfolio/project-5-before.jpg"
      alt: "围栏施工前"
      caption: "施工前"
    - src: "/assets/images/portfolio/project-5-after.jpg"
      alt: "完成的雪松围栏"
      caption: "施工后"
  services:
    - "木围栏"
    - "大门与入口"
    - "隐私屏风"

- id: "complete-exterior"
  title: "外部全面翻新"
  description: "车道更换、人行道安装和景观照明。"
  cover: "/assets/images/portfolio/project-6-cover.jpg"
  images:
    - src: "/assets/images/portfolio/project-6-before.jpg"
      alt: "外部翻新前"
      caption: "施工前"
    - src: "/assets/images/portfolio/project-6-after.jpg"
      alt: "外部翻新后"
      caption: "施工后"
  services:
    - "铺路石与联锁砖车道"
    - "人行道与小径"
    - "户外照明与景观照明"
```

**Step 5: Create `_data/contact.yml`**

```yaml
phone: "(604) 555-0123"
email: "info@peoplesconstruction.com"
wechat_qr: "/assets/images/contact/wechat-qr.jpg"
address: "Vancouver, BC, Canada"
service_area: "Vancouver & Lower Mainland"
hours:
  weekday: "Mon - Fri: 8:00 AM - 6:00 PM"
  weekend: "Sat: 9:00 AM - 4:00 PM"
  closed: "Sun: Closed"
google_maps_embed: "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d83327.34348747158!2d-123.19394!3d49.257784!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x548673f143a94fb3%3A0xbb9196ea9b81ef5b!2sVancouver%2C%20BC!5e0!3m2!1sen!2sca!4v1"
```

**Step 6: Commit**

```bash
git add _data/
git commit -m "feat: add data files for services, projects, and contact info"
```

---

### Task 4: CSS Stylesheet

**Files:**
- Create: `assets/css/main.css`

**Step 1: Create `assets/css/main.css`**

```css
/* ============================================
   BCCA People Construction - Main Stylesheet
   Clean & Modern Design
   ============================================ */

/* --- Reset & Base --- */
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

:root {
  --color-primary: #2d5a3d;
  --color-primary-light: #3a7d44;
  --color-primary-dark: #1e3d2a;
  --color-accent: #4a8c5c;
  --color-text: #2c2c2c;
  --color-text-light: #666666;
  --color-bg: #ffffff;
  --color-bg-alt: #f5f5f5;
  --color-border: #e0e0e0;
  --color-white: #ffffff;
  --font-heading: 'Montserrat', sans-serif;
  --font-body: 'Inter', sans-serif;
  --max-width: 1200px;
  --nav-height: 70px;
}

html {
  font-size: 16px;
  scroll-behavior: smooth;
}

body {
  font-family: var(--font-body);
  color: var(--color-text);
  background: var(--color-bg);
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
}

img {
  max-width: 100%;
  height: auto;
  display: block;
}

a {
  color: var(--color-primary);
  text-decoration: none;
}

a:hover {
  color: var(--color-primary-light);
}

ul {
  list-style: none;
}

.container {
  max-width: var(--max-width);
  margin: 0 auto;
  padding: 0 24px;
}

/* --- Typography --- */
h1, h2, h3, h4 {
  font-family: var(--font-heading);
  font-weight: 700;
  line-height: 1.2;
  color: var(--color-text);
}

h1 { font-size: 2.5rem; margin-bottom: 1rem; }
h2 { font-size: 2rem; margin-bottom: 0.75rem; }
h3 { font-size: 1.5rem; margin-bottom: 0.5rem; }
h4 { font-size: 1.125rem; margin-bottom: 0.5rem; }
p { margin-bottom: 1rem; }

/* --- Header & Navigation --- */
.site-header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: var(--nav-height);
  background: var(--color-white);
  box-shadow: 0 1px 3px rgba(0,0,0,0.1);
  z-index: 1000;
  display: flex;
  align-items: center;
}

.nav-container {
  max-width: var(--max-width);
  margin: 0 auto;
  padding: 0 24px;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.site-brand {
  font-family: var(--font-heading);
  font-size: 1.25rem;
  font-weight: 700;
  color: var(--color-primary);
  white-space: nowrap;
}

.site-brand span {
  display: block;
  font-size: 0.7rem;
  font-weight: 400;
  color: var(--color-text-light);
  letter-spacing: 0.05em;
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 32px;
}

.nav-links a {
  font-family: var(--font-heading);
  font-size: 0.9rem;
  font-weight: 500;
  color: var(--color-text);
  padding: 8px 0;
  border-bottom: 2px solid transparent;
  transition: color 0.2s, border-color 0.2s;
}

.nav-links a:hover,
.nav-links a.active {
  color: var(--color-primary);
  border-bottom-color: var(--color-primary);
}

.lang-switch {
  font-size: 0.85rem;
  padding: 4px 12px;
  border: 1px solid var(--color-border);
  border-radius: 4px;
  color: var(--color-text-light);
  transition: border-color 0.2s;
}

.lang-switch:hover {
  border-color: var(--color-primary);
  color: var(--color-primary);
}

.nav-toggle {
  display: none;
  background: none;
  border: none;
  cursor: pointer;
  padding: 8px;
}

.nav-toggle span {
  display: block;
  width: 24px;
  height: 2px;
  background: var(--color-text);
  margin: 5px 0;
  transition: transform 0.3s, opacity 0.3s;
}

/* Main content offset for fixed header */
main {
  margin-top: var(--nav-height);
}

/* --- Hero Section --- */
.hero {
  position: relative;
  height: 80vh;
  min-height: 500px;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  color: var(--color-white);
  overflow: hidden;
}

.hero-bg {
  position: absolute;
  inset: 0;
  background-size: cover;
  background-position: center;
  z-index: 0;
}

.hero-bg::after {
  content: '';
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, 0.5);
}

.hero-content {
  position: relative;
  z-index: 1;
  max-width: 700px;
  padding: 0 24px;
}

.hero h1 {
  font-size: 3rem;
  color: var(--color-white);
  margin-bottom: 0.5rem;
  text-shadow: 0 2px 4px rgba(0,0,0,0.3);
}

.hero .tagline {
  font-size: 1.25rem;
  margin-bottom: 2rem;
  opacity: 0.9;
}

/* --- Buttons --- */
.btn {
  display: inline-block;
  padding: 14px 32px;
  font-family: var(--font-heading);
  font-size: 0.95rem;
  font-weight: 600;
  border-radius: 4px;
  transition: background 0.2s, transform 0.1s;
  cursor: pointer;
  border: none;
}

.btn-primary {
  background: var(--color-primary);
  color: var(--color-white);
}

.btn-primary:hover {
  background: var(--color-primary-light);
  color: var(--color-white);
  transform: translateY(-1px);
}

.btn-outline {
  background: transparent;
  color: var(--color-white);
  border: 2px solid var(--color-white);
}

.btn-outline:hover {
  background: var(--color-white);
  color: var(--color-primary);
}

/* --- Section --- */
.section {
  padding: 80px 0;
}

.section-alt {
  background: var(--color-bg-alt);
}

.section-title {
  text-align: center;
  margin-bottom: 48px;
}

.section-title h2 {
  position: relative;
  display: inline-block;
}

.section-title h2::after {
  content: '';
  display: block;
  width: 60px;
  height: 3px;
  background: var(--color-primary);
  margin: 12px auto 0;
}

/* --- Cards Grid --- */
.cards-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 32px;
}

.card {
  background: var(--color-white);
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  transition: transform 0.2s, box-shadow 0.2s;
}

.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0,0,0,0.12);
}

.card-image {
  width: 100%;
  aspect-ratio: 4/3;
  object-fit: cover;
}

.card-body {
  padding: 24px;
}

.card-body h3 {
  margin-bottom: 8px;
}

.card-body p {
  color: var(--color-text-light);
  font-size: 0.95rem;
}

/* --- Service Icons Grid (Home Page) --- */
.icon-cards {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}

.icon-card {
  text-align: center;
  padding: 32px 24px;
  border-radius: 8px;
  background: var(--color-white);
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
  transition: transform 0.2s;
}

.icon-card:hover {
  transform: translateY(-2px);
}

.icon-card .icon {
  font-size: 2.5rem;
  margin-bottom: 16px;
}

.icon-card h3 {
  font-size: 1.1rem;
  margin-bottom: 8px;
}

.icon-card p {
  font-size: 0.9rem;
  color: var(--color-text-light);
}

/* --- Trust Bar --- */
.trust-bar {
  background: var(--color-primary);
  color: var(--color-white);
  padding: 40px 0;
  text-align: center;
}

.trust-items {
  display: flex;
  justify-content: center;
  gap: 64px;
  flex-wrap: wrap;
}

.trust-item {
  text-align: center;
}

.trust-item .number {
  font-family: var(--font-heading);
  font-size: 2.5rem;
  font-weight: 700;
  display: block;
}

.trust-item .label {
  font-size: 0.9rem;
  opacity: 0.9;
}

/* --- Services Page --- */
.service-category {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 48px;
  align-items: center;
  padding: 48px 0;
  border-bottom: 1px solid var(--color-border);
}

.service-category:last-child {
  border-bottom: none;
}

.service-category:nth-child(even) {
  direction: rtl;
}

.service-category:nth-child(even) > * {
  direction: ltr;
}

.service-category img {
  border-radius: 8px;
  width: 100%;
  aspect-ratio: 4/3;
  object-fit: cover;
}

.service-category h3 {
  font-size: 1.5rem;
  margin-bottom: 12px;
  color: var(--color-primary);
}

.service-category p {
  margin-bottom: 16px;
}

.service-list {
  list-style: none;
}

.service-list li {
  padding: 6px 0;
  padding-left: 20px;
  position: relative;
  color: var(--color-text-light);
}

.service-list li::before {
  content: '✓';
  position: absolute;
  left: 0;
  color: var(--color-primary);
  font-weight: 700;
}

/* --- Portfolio Detail --- */
.project-detail {
  max-width: 900px;
  margin: 0 auto;
}

.project-gallery {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 24px;
  margin: 32px 0;
}

.project-gallery figure {
  margin: 0;
}

.project-gallery img {
  border-radius: 8px;
  width: 100%;
  aspect-ratio: 4/3;
  object-fit: cover;
}

.project-gallery figcaption {
  text-align: center;
  font-size: 0.85rem;
  color: var(--color-text-light);
  margin-top: 8px;
}

.project-services {
  margin-top: 32px;
}

.project-services h3 {
  margin-bottom: 12px;
}

.tag-list {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.tag {
  background: var(--color-bg-alt);
  color: var(--color-text-light);
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 0.85rem;
}

/* --- About Page --- */
.about-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 48px;
  align-items: center;
}

.about-content img {
  border-radius: 8px;
  width: 100%;
}

.why-choose {
  margin-top: 48px;
}

.why-choose-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 32px;
  margin-top: 32px;
}

.why-item {
  text-align: center;
  padding: 24px;
}

.why-item .icon {
  font-size: 2rem;
  margin-bottom: 12px;
}

/* --- Contact Page --- */
.contact-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 48px;
}

.contact-info-item {
  display: flex;
  gap: 16px;
  margin-bottom: 24px;
  align-items: flex-start;
}

.contact-info-item .icon {
  font-size: 1.5rem;
  color: var(--color-primary);
  min-width: 32px;
  text-align: center;
}

.contact-info-item h4 {
  margin-bottom: 4px;
}

.contact-info-item p {
  color: var(--color-text-light);
  margin-bottom: 0;
  font-size: 0.95rem;
}

.wechat-qr {
  max-width: 200px;
  border-radius: 8px;
}

.map-container {
  border-radius: 8px;
  overflow: hidden;
  height: 100%;
  min-height: 400px;
}

.map-container iframe {
  width: 100%;
  height: 100%;
  border: 0;
  min-height: 400px;
}

/* --- Footer --- */
.site-footer {
  background: var(--color-primary-dark);
  color: var(--color-white);
  padding: 48px 0 24px;
}

.footer-grid {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr;
  gap: 48px;
  margin-bottom: 32px;
}

.footer-brand {
  font-family: var(--font-heading);
  font-size: 1.25rem;
  font-weight: 700;
  margin-bottom: 12px;
}

.site-footer p {
  opacity: 0.8;
  font-size: 0.9rem;
}

.site-footer h4 {
  color: var(--color-white);
  margin-bottom: 16px;
  font-size: 1rem;
}

.footer-links a {
  display: block;
  color: var(--color-white);
  opacity: 0.8;
  padding: 4px 0;
  font-size: 0.9rem;
}

.footer-links a:hover {
  opacity: 1;
  color: var(--color-white);
}

.footer-bottom {
  border-top: 1px solid rgba(255,255,255,0.15);
  padding-top: 24px;
  text-align: center;
  font-size: 0.85rem;
  opacity: 0.7;
}

/* --- CTA Banner --- */
.cta-banner {
  background: var(--color-primary);
  color: var(--color-white);
  text-align: center;
  padding: 64px 24px;
}

.cta-banner h2 {
  color: var(--color-white);
  margin-bottom: 16px;
}

.cta-banner p {
  opacity: 0.9;
  margin-bottom: 24px;
  font-size: 1.1rem;
}

/* --- Page Header --- */
.page-header {
  background: var(--color-primary);
  color: var(--color-white);
  text-align: center;
  padding: 64px 24px;
}

.page-header h1 {
  color: var(--color-white);
}

.page-header p {
  opacity: 0.9;
  max-width: 600px;
  margin: 0 auto;
}

/* --- Responsive --- */
@media (max-width: 768px) {
  .nav-toggle {
    display: block;
  }

  .nav-links {
    display: none;
    position: absolute;
    top: var(--nav-height);
    left: 0;
    right: 0;
    background: var(--color-white);
    flex-direction: column;
    padding: 24px;
    gap: 16px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
  }

  .nav-links.open {
    display: flex;
  }

  h1 { font-size: 2rem; }
  h2 { font-size: 1.5rem; }

  .hero { height: 60vh; min-height: 400px; }
  .hero h1 { font-size: 2rem; }
  .hero .tagline { font-size: 1rem; }

  .cards-grid,
  .icon-cards,
  .why-choose-grid {
    grid-template-columns: 1fr;
  }

  .service-category {
    grid-template-columns: 1fr;
  }

  .service-category:nth-child(even) {
    direction: ltr;
  }

  .about-content {
    grid-template-columns: 1fr;
  }

  .contact-grid {
    grid-template-columns: 1fr;
  }

  .project-gallery {
    grid-template-columns: 1fr;
  }

  .footer-grid {
    grid-template-columns: 1fr;
  }

  .trust-items {
    gap: 32px;
  }

  .section {
    padding: 48px 0;
  }
}

@media (min-width: 769px) and (max-width: 1024px) {
  .cards-grid,
  .icon-cards {
    grid-template-columns: repeat(2, 1fr);
  }

  .why-choose-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
```

**Step 2: Commit**

```bash
git add assets/css/main.css
git commit -m "feat: add main CSS stylesheet with responsive design"
```

---

### Task 5: JavaScript

**Files:**
- Create: `assets/js/main.js`

**Step 1: Create `assets/js/main.js`**

```javascript
(function() {
  'use strict';

  // Mobile nav toggle
  var toggle = document.querySelector('.nav-toggle');
  var navLinks = document.querySelector('.nav-links');

  if (toggle && navLinks) {
    toggle.addEventListener('click', function() {
      navLinks.classList.toggle('open');
      toggle.setAttribute('aria-expanded',
        navLinks.classList.contains('open'));
    });
  }

  // Close mobile nav on link click
  if (navLinks) {
    navLinks.querySelectorAll('a').forEach(function(link) {
      link.addEventListener('click', function() {
        navLinks.classList.remove('open');
        if (toggle) toggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  // Shrink header on scroll
  var header = document.querySelector('.site-header');
  if (header) {
    window.addEventListener('scroll', function() {
      if (window.scrollY > 50) {
        header.classList.add('scrolled');
      } else {
        header.classList.remove('scrolled');
      }
    });
  }
})();
```

**Step 2: Commit**

```bash
git add assets/js/main.js
git commit -m "feat: add JavaScript for mobile nav toggle"
```

---

### Task 6: Layouts & Includes

**Files:**
- Create: `_layouts/default.html`
- Create: `_layouts/page.html`
- Create: `_layouts/project.html`
- Create: `_includes/header.html`
- Create: `_includes/footer.html`

**Step 1: Create `_layouts/default.html`**

```html
<!DOCTYPE html>
<html lang="{{ page.lang | default: 'en' }}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{{ page.title }} | BCCA People Construction</title>
  <meta name="description" content="{{ page.description | default: site.description }}">

  {% if page.lang == 'en' and page.zh_pair %}
  <link rel="alternate" hreflang="zh" href="{{ site.url }}{{ page.zh_pair }}">
  <link rel="alternate" hreflang="en" href="{{ page.url }}">
  {% elsif page.lang == 'zh' and page.en_pair %}
  <link rel="alternate" hreflang="en" href="{{ site.url }}{{ page.en_pair }}">
  <link rel="alternate" hreflang="zh" href="{{ page.url }}">
  {% endif %}

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500&family=Montserrat:wght@600;700&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="/assets/css/main.css">

  {% if page.lang == 'en' %}
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "name": "BCCA People Construction",
    "description": "Quality Landscaping & Construction Since 2009",
    "url": "{{ site.url }}",
    "telephone": "{{ site.data.contact.phone }}",
    "email": "{{ site.data.contact.email }}",
    "address": {
      "@type": "PostalAddress",
      "addressLocality": "Vancouver",
      "addressRegion": "BC",
      "addressCountry": "CA"
    },
    "areaServed": "Vancouver & Lower Mainland",
    "foundingDate": "2009"
  }
  </script>
  {% endif %}
</head>
<body>
  {% include header.html %}
  <main>
    {{ content }}
  </main>
  {% include footer.html %}
  <script src="/assets/js/main.js"></script>
</body>
</html>
```

**Step 2: Create `_layouts/page.html`**

```html
---
layout: default
---
<div class="page-header">
  <div class="container">
    <h1>{{ page.heading | default: page.title }}</h1>
    {% if page.subtitle %}
    <p>{{ page.subtitle }}</p>
    {% endif %}
  </div>
</div>
{{ content }}
```

**Step 3: Create `_layouts/project.html`**

```html
---
layout: default
---
<div class="page-header">
  <div class="container">
    <h1>{{ page.title }}</h1>
  </div>
</div>
<section class="section">
  <div class="container project-detail">
    {{ content }}
  </div>
</section>
```

**Step 4: Create `_includes/header.html`**

```html
<header class="site-header">
  <nav class="nav-container">
    <a href="/{{ page.lang }}/" class="site-brand">
      BCCA People Construction
      <span>Est. 2009</span>
    </a>
    <button class="nav-toggle" aria-label="Toggle navigation" aria-expanded="false">
      <span></span><span></span><span></span>
    </button>
    <div class="nav-links">
      {% if page.lang == 'en' %}
      <a href="/en/" {% if page.nav == 'home' %}class="active"{% endif %}>Home</a>
      <a href="/en/services/" {% if page.nav == 'services' %}class="active"{% endif %}>Services</a>
      <a href="/en/portfolio/" {% if page.nav == 'portfolio' %}class="active"{% endif %}>Portfolio</a>
      <a href="/en/about/" {% if page.nav == 'about' %}class="active"{% endif %}>About</a>
      <a href="/en/contact/" {% if page.nav == 'contact' %}class="active"{% endif %}>Contact</a>
      {% if page.zh_pair %}
      <a href="{{ page.zh_pair }}" class="lang-switch">中文</a>
      {% endif %}
      {% elsif page.lang == 'zh' %}
      <a href="/zh/" {% if page.nav == 'home' %}class="active"{% endif %}>首页</a>
      <a href="/zh/services/" {% if page.nav == 'services' %}class="active"{% endif %}>服务</a>
      <a href="/zh/portfolio/" {% if page.nav == 'portfolio' %}class="active"{% endif %}>项目</a>
      <a href="/zh/about/" {% if page.nav == 'about' %}class="active"{% endif %}>关于</a>
      <a href="/zh/contact/" {% if page.nav == 'contact' %}class="active"{% endif %}>联系</a>
      {% if page.en_pair %}
      <a href="{{ page.en_pair }}" class="lang-switch">English</a>
      {% endif %}
      {% endif %}
    </div>
  </nav>
</header>
```

**Step 5: Create `_includes/footer.html`**

```html
<div class="cta-banner">
  <div class="container">
    {% if page.lang == 'en' %}
    <h2>Ready to Transform Your Outdoor Space?</h2>
    <p>Contact us today for a free consultation</p>
    <a href="/en/contact/" class="btn btn-outline">Get in Touch</a>
    {% else %}
    <h2>准备好改造您的户外空间了吗？</h2>
    <p>立即联系我们，获取免费咨询</p>
    <a href="/zh/contact/" class="btn btn-outline">联系我们</a>
    {% endif %}
  </div>
</div>
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <div class="footer-brand">BCCA People Construction</div>
        {% if page.lang == 'en' %}
        <p>Quality landscaping and construction services in Vancouver and the Lower Mainland since 2009.</p>
        {% else %}
        <p>自2009年以来，为温哥华和大温地区提供优质园林绿化和建筑服务。</p>
        {% endif %}
      </div>
      <div>
        {% if page.lang == 'en' %}
        <h4>Quick Links</h4>
        <div class="footer-links">
          <a href="/en/">Home</a>
          <a href="/en/services/">Services</a>
          <a href="/en/portfolio/">Portfolio</a>
          <a href="/en/about/">About</a>
          <a href="/en/contact/">Contact</a>
        </div>
        {% else %}
        <h4>快速链接</h4>
        <div class="footer-links">
          <a href="/zh/">首页</a>
          <a href="/zh/services/">服务</a>
          <a href="/zh/portfolio/">项目</a>
          <a href="/zh/about/">关于</a>
          <a href="/zh/contact/">联系</a>
        </div>
        {% endif %}
      </div>
      <div>
        {% if page.lang == 'en' %}
        <h4>Contact</h4>
        {% else %}
        <h4>联系方式</h4>
        {% endif %}
        <div class="footer-links">
          <a href="tel:{{ site.data.contact.phone }}">{{ site.data.contact.phone }}</a>
          <a href="mailto:{{ site.data.contact.email }}">{{ site.data.contact.email }}</a>
          <p>{{ site.data.contact.address }}</p>
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      &copy; {{ 'now' | date: '%Y' }} BCCA People Construction. All rights reserved.
    </div>
  </div>
</footer>
```

**Step 6: Commit**

```bash
git add _layouts/ _includes/
git commit -m "feat: add Jekyll layouts and includes (header, footer, nav)"
```

---

### Task 7: Root Redirect & English Home Page

**Files:**
- Create: `index.html` (root redirect)
- Create: `en/index.html`

**Step 1: Create root `index.html`**

```html
---
redirect_to: /en/
---
<!DOCTYPE html>
<html>
<head>
  <meta http-equiv="refresh" content="0; url=/en/">
  <link rel="canonical" href="/en/">
</head>
<body>
  <p>Redirecting to <a href="/en/">English</a>...</p>
</body>
</html>
```

**Step 2: Create `en/index.html`**

```html
---
layout: default
title: "Vancouver Landscaping Contractor"
description: "BCCA People Construction - Quality landscaping, hardscaping, and outdoor construction services in Vancouver & Lower Mainland since 2009."
lang: en
nav: home
zh_pair: /zh/
---

<!-- Hero -->
<section class="hero">
  <div class="hero-bg" style="background-image: url('/assets/images/home/hero.jpg')"></div>
  <div class="hero-content">
    <h1>BCCA People Construction</h1>
    <p class="tagline">Quality Landscaping & Construction Since 2009</p>
    <a href="/en/portfolio/" class="btn btn-primary">View Our Work</a>
  </div>
</section>

<!-- Services Overview -->
<section class="section section-alt">
  <div class="container">
    <div class="section-title"><h2>Our Services</h2></div>
    <div class="icon-cards">
      <a href="/en/services/" class="icon-card">
        <div class="icon">🌿</div>
        <h3>Landscaping</h3>
        <p>Complete landscape design, installation, and garden maintenance</p>
      </a>
      <a href="/en/services/" class="icon-card">
        <div class="icon">🧱</div>
        <h3>Hardscaping</h3>
        <p>Patios, driveways, retaining walls, and stonework</p>
      </a>
      <a href="/en/services/" class="icon-card">
        <div class="icon">🏡</div>
        <h3>Outdoor Living</h3>
        <p>Decks, pergolas, outdoor kitchens, and fire features</p>
      </a>
      <a href="/en/services/" class="icon-card">
        <div class="icon">🔒</div>
        <h3>Fencing</h3>
        <p>Wood, vinyl, and composite fencing with custom gates</p>
      </a>
      <a href="/en/services/" class="icon-card">
        <div class="icon">💡</div>
        <h3>Lighting</h3>
        <p>Outdoor and landscape lighting design and installation</p>
      </a>
      <a href="/en/services/" class="icon-card">
        <div class="icon">🔧</div>
        <h3>Exterior</h3>
        <p>Concrete work, excavation, pressure washing, and more</p>
      </a>
    </div>
  </div>
</section>

<!-- Featured Projects -->
<section class="section">
  <div class="container">
    <div class="section-title"><h2>Featured Projects</h2></div>
    <div class="cards-grid">
      {% for project in site.data.projects_en limit:3 %}
      <a href="/en/portfolio/{{ project.id }}/" class="card">
        <img src="{{ project.cover }}" alt="{{ project.title }}" class="card-image">
        <div class="card-body">
          <h3>{{ project.title }}</h3>
          <p>{{ project.description }}</p>
        </div>
      </a>
      {% endfor %}
    </div>
  </div>
</section>

<!-- Trust Bar -->
<section class="trust-bar">
  <div class="container">
    <div class="trust-items">
      <div class="trust-item">
        <span class="number">17+</span>
        <span class="label">Years Experience</span>
      </div>
      <div class="trust-item">
        <span class="number">500+</span>
        <span class="label">Projects Completed</span>
      </div>
      <div class="trust-item">
        <span class="number">100%</span>
        <span class="label">Client Satisfaction</span>
      </div>
    </div>
  </div>
</section>
```

**Step 3: Commit**

```bash
git add index.html en/index.html
git commit -m "feat: add root redirect and English home page"
```

---

### Task 8: Chinese Home Page

**Files:**
- Create: `zh/index.html`

**Step 1: Create `zh/index.html`**

```html
---
layout: default
title: "温哥华园林承包商"
description: "BCCA People Construction - 自2009年以来，为温哥华和大温地区提供优质的园林绿化、硬质景观和户外建筑服务。"
lang: zh
nav: home
en_pair: /en/
---

<!-- Hero -->
<section class="hero">
  <div class="hero-bg" style="background-image: url('/assets/images/home/hero.jpg')"></div>
  <div class="hero-content">
    <h1>BCCA People Construction</h1>
    <p class="tagline">自2009年以来的优质园林绿化与建筑服务</p>
    <a href="/zh/portfolio/" class="btn btn-primary">查看我们的项目</a>
  </div>
</section>

<!-- Services Overview -->
<section class="section section-alt">
  <div class="container">
    <div class="section-title"><h2>我们的服务</h2></div>
    <div class="icon-cards">
      <a href="/zh/services/" class="icon-card">
        <div class="icon">🌿</div>
        <h3>园林绿化</h3>
        <p>完整的景观设计、施工和花园维护</p>
      </a>
      <a href="/zh/services/" class="icon-card">
        <div class="icon">🧱</div>
        <h3>硬质景观</h3>
        <p>露台、车道、挡土墙和石材工程</p>
      </a>
      <a href="/zh/services/" class="icon-card">
        <div class="icon">🏡</div>
        <h3>户外生活</h3>
        <p>木甲板、凉亭、户外厨房和火炉</p>
      </a>
      <a href="/zh/services/" class="icon-card">
        <div class="icon">🔒</div>
        <h3>围栏工程</h3>
        <p>木质、乙烯基和复合材料围栏及定制大门</p>
      </a>
      <a href="/zh/services/" class="icon-card">
        <div class="icon">💡</div>
        <h3>照明工程</h3>
        <p>户外和景观照明设计与安装</p>
      </a>
      <a href="/zh/services/" class="icon-card">
        <div class="icon">🔧</div>
        <h3>外部工程</h3>
        <p>混凝土工程、挖掘、高压清洗等</p>
      </a>
    </div>
  </div>
</section>

<!-- Featured Projects -->
<section class="section">
  <div class="container">
    <div class="section-title"><h2>精选项目</h2></div>
    <div class="cards-grid">
      {% for project in site.data.projects_zh limit:3 %}
      <a href="/zh/portfolio/{{ project.id }}/" class="card">
        <img src="{{ project.cover }}" alt="{{ project.title }}" class="card-image">
        <div class="card-body">
          <h3>{{ project.title }}</h3>
          <p>{{ project.description }}</p>
        </div>
      </a>
      {% endfor %}
    </div>
  </div>
</section>

<!-- Trust Bar -->
<section class="trust-bar">
  <div class="container">
    <div class="trust-items">
      <div class="trust-item">
        <span class="number">17+</span>
        <span class="label">年经验</span>
      </div>
      <div class="trust-item">
        <span class="number">500+</span>
        <span class="label">完成项目</span>
      </div>
      <div class="trust-item">
        <span class="number">100%</span>
        <span class="label">客户满意度</span>
      </div>
    </div>
  </div>
</section>
```

**Step 2: Commit**

```bash
git add zh/index.html
git commit -m "feat: add Chinese home page"
```

---

### Task 9: Services Pages

**Files:**
- Create: `en/services.html`
- Create: `zh/services.html`

**Step 1: Create `en/services.html`**

```html
---
layout: page
title: "Our Services"
heading: "Our Services"
subtitle: "Comprehensive landscaping and construction services for residential and commercial properties"
description: "Landscaping, hardscaping, deck building, fencing, and outdoor construction services in Vancouver BC."
lang: en
nav: services
zh_pair: /zh/services/
---

<section class="section">
  <div class="container">
    {% for service in site.data.services_en %}
    <div class="service-category">
      <img src="{{ service.image }}" alt="{{ service.category }}">
      <div>
        <h3>{{ service.category }}</h3>
        <p>{{ service.description }}</p>
        <ul class="service-list">
          {% for item in service.items %}
          <li>{{ item }}</li>
          {% endfor %}
        </ul>
      </div>
    </div>
    {% endfor %}
  </div>
</section>
```

**Step 2: Create `zh/services.html`**

```html
---
layout: page
title: "我们的服务"
heading: "我们的服务"
subtitle: "为住宅和商业物业提供全面的园林绿化和建筑服务"
description: "温哥华园林绿化、硬质景观、木甲板建造、围栏和户外建筑服务。"
lang: zh
nav: services
en_pair: /en/services/
---

<section class="section">
  <div class="container">
    {% for service in site.data.services_zh %}
    <div class="service-category">
      <img src="{{ service.image }}" alt="{{ service.category }}">
      <div>
        <h3>{{ service.category }}</h3>
        <p>{{ service.description }}</p>
        <ul class="service-list">
          {% for item in service.items %}
          <li>{{ item }}</li>
          {% endfor %}
        </ul>
      </div>
    </div>
    {% endfor %}
  </div>
</section>
```

**Step 3: Commit**

```bash
git add en/services.html zh/services.html
git commit -m "feat: add bilingual services pages"
```

---

### Task 10: Portfolio Pages & Project Detail Pages

**Files:**
- Create: `en/portfolio.html`
- Create: `zh/portfolio.html`
- Create: `en/portfolio/backyard-transformation.html` (and 5 more)
- Create: `zh/portfolio/backyard-transformation.html` (and 5 more)

**Step 1: Create `en/portfolio.html`**

```html
---
layout: page
title: "Our Portfolio"
heading: "Our Portfolio"
subtitle: "Browse our completed projects and see the quality of our work"
description: "Portfolio of landscaping and construction projects by BCCA People Construction in Vancouver BC."
lang: en
nav: portfolio
zh_pair: /zh/portfolio/
---

<section class="section">
  <div class="container">
    <div class="cards-grid">
      {% for project in site.data.projects_en %}
      <a href="/en/portfolio/{{ project.id }}/" class="card">
        <img src="{{ project.cover }}" alt="{{ project.title }}" class="card-image">
        <div class="card-body">
          <h3>{{ project.title }}</h3>
          <p>{{ project.description }}</p>
        </div>
      </a>
      {% endfor %}
    </div>
  </div>
</section>
```

**Step 2: Create `zh/portfolio.html`**

```html
---
layout: page
title: "我们的项目"
heading: "我们的项目"
subtitle: "浏览我们已完成的项目，了解我们的工程质量"
description: "BCCA People Construction 在温哥华完成的园林绿化和建筑项目展示。"
lang: zh
nav: portfolio
en_pair: /en/portfolio/
---

<section class="section">
  <div class="container">
    <div class="cards-grid">
      {% for project in site.data.projects_zh %}
      <a href="/zh/portfolio/{{ project.id }}/" class="card">
        <img src="{{ project.cover }}" alt="{{ project.title }}" class="card-image">
        <div class="card-body">
          <h3>{{ project.title }}</h3>
          <p>{{ project.description }}</p>
        </div>
      </a>
      {% endfor %}
    </div>
  </div>
</section>
```

**Step 3: Create English project detail pages**

For each project in `_data/projects_en.yml`, create a file at `en/portfolio/<id>.html`. All 6 follow this pattern (substitute the project id and index):

```html
---
layout: project
title: "[project.title from YAML]"
description: "[project.description from YAML]"
lang: en
nav: portfolio
zh_pair: /zh/portfolio/[project.id]/
---

{% assign project = site.data.projects_en | where: "id", "[project.id]" | first %}

<p>{{ project.description }}</p>

<div class="project-gallery">
  {% for img in project.images %}
  <figure>
    <img src="{{ img.src }}" alt="{{ img.alt }}">
    <figcaption>{{ img.caption }}</figcaption>
  </figure>
  {% endfor %}
</div>

<div class="project-services">
  <h3>Services Used</h3>
  <div class="tag-list">
    {% for svc in project.services %}
    <span class="tag">{{ svc }}</span>
    {% endfor %}
  </div>
</div>

<p style="margin-top: 32px;"><a href="/en/portfolio/">&larr; Back to Portfolio</a></p>
```

Create all 6 English project files:
- `en/portfolio/backyard-transformation.html`
- `en/portfolio/front-yard-paving.html`
- `en/portfolio/outdoor-living-deck.html`
- `en/portfolio/garden-retaining-wall.html`
- `en/portfolio/cedar-fence-privacy.html`
- `en/portfolio/complete-exterior.html`

**Step 4: Create Chinese project detail pages**

Same pattern for all 6 Chinese pages at `zh/portfolio/<id>.html`, using `site.data.projects_zh`, Chinese title/description from YAML, swapping `en_pair`/`zh_pair`, and "使用的服务" / "← 返回项目" for labels.

Create all 6 Chinese project files:
- `zh/portfolio/backyard-transformation.html`
- `zh/portfolio/front-yard-paving.html`
- `zh/portfolio/outdoor-living-deck.html`
- `zh/portfolio/garden-retaining-wall.html`
- `zh/portfolio/cedar-fence-privacy.html`
- `zh/portfolio/complete-exterior.html`

**Step 5: Commit**

```bash
git add en/portfolio/ zh/portfolio/ en/portfolio.html zh/portfolio.html
git commit -m "feat: add bilingual portfolio pages with project details"
```

---

### Task 11: About Pages

**Files:**
- Create: `en/about.html`
- Create: `zh/about.html`

**Step 1: Create `en/about.html`**

```html
---
layout: page
title: "About Us"
heading: "About Us"
subtitle: "Learn about BCCA People Construction and our commitment to quality"
description: "About BCCA People Construction - Vancouver's trusted landscaping and construction company since 2009."
lang: en
nav: about
zh_pair: /zh/about/
---

<section class="section">
  <div class="container">
    <div class="about-content">
      <div>
        <h2>Our Story</h2>
        <p>Founded in 2009, BCCA People Construction has been serving the Vancouver and Lower Mainland area with professional landscaping and construction services for over 17 years.</p>
        <p>We started as a small, family-run operation with a simple philosophy: deliver quality craftsmanship, use the best materials, and treat every project — big or small — with the same dedication and attention to detail.</p>
        <p>Over the years, we've grown into a full-service landscaping and construction company, trusted by hundreds of homeowners and businesses across the Lower Mainland.</p>
      </div>
      <img src="/assets/images/about/team.jpg" alt="BCCA People Construction team">
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container why-choose">
    <div class="section-title"><h2>Why Choose Us</h2></div>
    <div class="why-choose-grid">
      <div class="why-item">
        <div class="icon">⭐</div>
        <h3>Quality Craftsmanship</h3>
        <p>We use premium materials and proven techniques to ensure lasting results.</p>
      </div>
      <div class="why-item">
        <div class="icon">🤝</div>
        <h3>Reliable & Professional</h3>
        <p>On-time delivery, clear communication, and respect for your property.</p>
      </div>
      <div class="why-item">
        <div class="icon">💬</div>
        <h3>Bilingual Service</h3>
        <p>We serve clients in both English and Chinese for your convenience.</p>
      </div>
      <div class="why-item">
        <div class="icon">📋</div>
        <h3>Free Consultations</h3>
        <p>We provide detailed free estimates and design consultations.</p>
      </div>
      <div class="why-item">
        <div class="icon">🏆</div>
        <h3>17+ Years Experience</h3>
        <p>Decades of experience across all types of landscaping and construction.</p>
      </div>
      <div class="why-item">
        <div class="icon">📍</div>
        <h3>Locally Owned</h3>
        <p>Proud to serve Vancouver and the entire Lower Mainland community.</p>
      </div>
    </div>
  </div>
</section>
```

**Step 2: Create `zh/about.html`**

```html
---
layout: page
title: "关于我们"
heading: "关于我们"
subtitle: "了解 BCCA People Construction 和我们对质量的承诺"
description: "关于 BCCA People Construction - 自2009年以来温哥华值得信赖的园林绿化和建筑公司。"
lang: zh
nav: about
en_pair: /en/about/
---

<section class="section">
  <div class="container">
    <div class="about-content">
      <div>
        <h2>我们的故事</h2>
        <p>BCCA People Construction 成立于2009年，十七年来一直为温哥华和大温地区提供专业的园林绿化和建筑服务。</p>
        <p>我们从一个小型家庭企业起步，秉持简单的理念：提供优质的工艺、使用最好的材料，以同样的专注和细致对待每一个项目——无论大小。</p>
        <p>多年来，我们已发展成为一家全方位服务的园林绿化和建筑公司，赢得了大温地区数百位业主和企业的信赖。</p>
      </div>
      <img src="/assets/images/about/team.jpg" alt="BCCA People Construction 团队">
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container why-choose">
    <div class="section-title"><h2>为什么选择我们</h2></div>
    <div class="why-choose-grid">
      <div class="why-item">
        <div class="icon">⭐</div>
        <h3>优质工艺</h3>
        <p>我们使用优质材料和成熟技术，确保持久的效果。</p>
      </div>
      <div class="why-item">
        <div class="icon">🤝</div>
        <h3>可靠专业</h3>
        <p>准时交付，沟通清晰，尊重您的物业。</p>
      </div>
      <div class="why-item">
        <div class="icon">💬</div>
        <h3>双语服务</h3>
        <p>我们提供中英双语服务，方便您的沟通。</p>
      </div>
      <div class="why-item">
        <div class="icon">📋</div>
        <h3>免费咨询</h3>
        <p>我们提供详细的免费估价和设计咨询。</p>
      </div>
      <div class="why-item">
        <div class="icon">🏆</div>
        <h3>17年以上经验</h3>
        <p>在各类园林绿化和建筑项目中拥有丰富经验。</p>
      </div>
      <div class="why-item">
        <div class="icon">📍</div>
        <h3>本地经营</h3>
        <p>自豪地服务温哥华和整个大温地区。</p>
      </div>
    </div>
  </div>
</section>
```

**Step 3: Commit**

```bash
git add en/about.html zh/about.html
git commit -m "feat: add bilingual about pages"
```

---

### Task 12: Contact Pages

**Files:**
- Create: `en/contact.html`
- Create: `zh/contact.html`

**Step 1: Create `en/contact.html`**

```html
---
layout: page
title: "Contact Us"
heading: "Contact Us"
subtitle: "Get in touch for a free consultation"
description: "Contact BCCA People Construction for landscaping and construction services in Vancouver BC. Phone, email, and WeChat available."
lang: en
nav: contact
zh_pair: /zh/contact/
---

<section class="section">
  <div class="container">
    <div class="contact-grid">
      <div>
        <h2>Get in Touch</h2>
        <p>We'd love to hear about your project. Contact us for a free consultation and estimate.</p>

        <div class="contact-info-item">
          <div class="icon">📞</div>
          <div>
            <h4>Phone</h4>
            <p><a href="tel:{{ site.data.contact.phone }}">{{ site.data.contact.phone }}</a></p>
          </div>
        </div>

        <div class="contact-info-item">
          <div class="icon">✉️</div>
          <div>
            <h4>Email</h4>
            <p><a href="mailto:{{ site.data.contact.email }}">{{ site.data.contact.email }}</a></p>
          </div>
        </div>

        <div class="contact-info-item">
          <div class="icon">💬</div>
          <div>
            <h4>WeChat</h4>
            <img src="{{ site.data.contact.wechat_qr }}" alt="WeChat QR Code" class="wechat-qr">
          </div>
        </div>

        <div class="contact-info-item">
          <div class="icon">📍</div>
          <div>
            <h4>Service Area</h4>
            <p>{{ site.data.contact.service_area }}</p>
          </div>
        </div>

        <div class="contact-info-item">
          <div class="icon">🕐</div>
          <div>
            <h4>Business Hours</h4>
            <p>{{ site.data.contact.hours.weekday }}</p>
            <p>{{ site.data.contact.hours.weekend }}</p>
            <p>{{ site.data.contact.hours.closed }}</p>
          </div>
        </div>
      </div>

      <div class="map-container">
        <iframe src="{{ site.data.contact.google_maps_embed }}" allowfullscreen loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
      </div>
    </div>
  </div>
</section>
```

**Step 2: Create `zh/contact.html`**

```html
---
layout: page
title: "联系我们"
heading: "联系我们"
subtitle: "联系我们获取免费咨询"
description: "联系 BCCA People Construction，获取温哥华园林绿化和建筑服务。电话、电子邮件和微信均可联系。"
lang: zh
nav: contact
en_pair: /en/contact/
---

<section class="section">
  <div class="container">
    <div class="contact-grid">
      <div>
        <h2>联系我们</h2>
        <p>我们很乐意了解您的项目需求。联系我们获取免费咨询和报价。</p>

        <div class="contact-info-item">
          <div class="icon">📞</div>
          <div>
            <h4>电话</h4>
            <p><a href="tel:{{ site.data.contact.phone }}">{{ site.data.contact.phone }}</a></p>
          </div>
        </div>

        <div class="contact-info-item">
          <div class="icon">✉️</div>
          <div>
            <h4>电子邮件</h4>
            <p><a href="mailto:{{ site.data.contact.email }}">{{ site.data.contact.email }}</a></p>
          </div>
        </div>

        <div class="contact-info-item">
          <div class="icon">💬</div>
          <div>
            <h4>微信</h4>
            <img src="{{ site.data.contact.wechat_qr }}" alt="微信二维码" class="wechat-qr">
          </div>
        </div>

        <div class="contact-info-item">
          <div class="icon">📍</div>
          <div>
            <h4>服务区域</h4>
            <p>{{ site.data.contact.service_area }}</p>
          </div>
        </div>

        <div class="contact-info-item">
          <div class="icon">🕐</div>
          <div>
            <h4>营业时间</h4>
            <p>{{ site.data.contact.hours.weekday }}</p>
            <p>{{ site.data.contact.hours.weekend }}</p>
            <p>{{ site.data.contact.hours.closed }}</p>
          </div>
        </div>
      </div>

      <div class="map-container">
        <iframe src="{{ site.data.contact.google_maps_embed }}" allowfullscreen loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
      </div>
    </div>
  </div>
</section>
```

**Step 3: Commit**

```bash
git add en/contact.html zh/contact.html
git commit -m "feat: add bilingual contact pages"
```

---

### Task 13: Final Build & Verification

**Step 1: Install dependencies and build**

Run: `cd /Users/yunfe/Documents/GitHub/peoplesconstruction.github.io && bundle install && bundle exec jekyll build`
Expected: Build succeeds, `_site/` directory created

**Step 2: Verify all pages generated**

Run: `find _site -name "*.html" | sort`
Expected: All English and Chinese pages present under `_site/en/` and `_site/zh/`

**Step 3: Serve locally and spot-check**

Run: `bundle exec jekyll serve`
Expected: Site serves at `http://localhost:4000`, manually verify:
- Root redirects to `/en/`
- All nav links work
- Language switcher works
- Services load from YAML data
- Portfolio cards link to detail pages
- Images display (placeholders)
- Mobile nav works (resize browser)

**Step 4: Fix any issues found during verification**

**Step 5: Final commit if any fixes were needed**

```bash
git add -A && git commit -m "fix: address issues found during build verification"
```
