#!/usr/bin/env python3
"""Generate placeholder images for BCCA Peoples Construction LTD website."""

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
