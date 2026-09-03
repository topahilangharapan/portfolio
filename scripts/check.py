#!/usr/bin/env python3
"""Mechanically-checkable subset of guide/design-guide.md §14.

Not a substitute for the full checklist — items that require visual or
editorial judgment (bold budget, descriptor voice, viewport fit) still need a
human or an agent to eyeball them against the design guide. This only catches
the violations that are unambiguous from source text: forbidden CSS/HTML,
external requests, stray decoration, oversized pages, broken heading structure,
and — for the narrow images exception in §3 — malformed or oversized images.

Exit 0 and silent output means every mechanical check passed. Exit 1 prints
each failure as `file:line: message`.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# Every HTML page in the repo, root and category subdirectories alike
# (index.html, for-committees.html, research.html, research/thesis.html, ...).
HTML_FILES = sorted(
    p.relative_to(ROOT).as_posix()
    for p in ROOT.rglob("*.html")
    if ".git" not in p.parts
)
CSS_FILES = ["style.css"]
MAX_TEXT_ONLY_BYTES = 30 * 1024

# §3 image budget
MAX_IMAGE_BYTES = 150 * 1024
MAX_IMAGES_PER_PAGE = 3
MAX_PAGE_WEIGHT_WITH_IMAGES = 500 * 1024
IMAGE_DIR_PREFIX = "assets/img/"

FORBIDDEN_CSS_PROPS = [
    "border-radius",
    "box-shadow",
    "text-shadow",
    "filter",
    "backdrop-filter",
    "animation",
    "transition",
    "@keyframes",
]
GRADIENT_RE = re.compile(r"(linear|radial|conic)-gradient\s*\(")
CENTER_RE = re.compile(r"text-align\s*:\s*center")
UNDERLINE_OFF_RE = re.compile(r"text-decoration\s*:\s*none")
VISITED_RULE_RE = re.compile(r"a:visited")

# §3 permits <img>, wrapped and validated separately below. Everything else
# decorative/embedded stays fully forbidden.
FORBIDDEN_HTML_TAGS = [
    "picture",
    "svg",
    "video",
    "audio",
    "iframe",
    "embed",
    "object",
]
SCRIPT_TAG_RE = re.compile(r"<script\b", re.IGNORECASE)
EXTERNAL_HREF_RE = re.compile(
    r'(?:href|src)\s*=\s*["\']https?://', re.IGNORECASE
)
FONT_IMPORT_RE = re.compile(r"fonts\.(googleapis|gstatic)\.com|@font-face")

IMG_TAG_RE = re.compile(r"<img\b[^>]*>", re.IGNORECASE)
FIGURE_RE = re.compile(r"<figure\b([^>]*)>(.*?)</figure>", re.DOTALL | re.IGNORECASE)
FIGCAPTION_RE = re.compile(r"<figcaption\b", re.IGNORECASE)

# Ranges covering emoji, arrows, dingbats, and other decorative symbols the
# design guide forbids. Deliberately excludes general punctuation (em dash,
# middle dot, curly quotes) which the site's prose uses legitimately.
DECORATIVE_RANGES = [
    (0x2190, 0x21FF),  # arrows
    (0x2600, 0x27BF),  # misc symbols & dingbats (stars, checkmarks, etc.)
    (0x2B00, 0x2BFF),  # misc symbols and arrows
    (0x1F300, 0x1FAFF),  # emoji blocks
]

errors = []


def fail(path, lineno, message):
    errors.append(f"{path}:{lineno}: {message}")


def line_of(text, offset):
    return text.count("\n", 0, offset) + 1


def parse_attrs(attr_text):
    attrs = {}
    for m in re.finditer(r'(\w[\w-]*)\s*=\s*"([^"]*)"', attr_text):
        attrs[m.group(1).lower()] = m.group(2)
    for m in re.finditer(r"(\w[\w-]*)\s*=\s*'([^']*)'", attr_text):
        attrs.setdefault(m.group(1).lower(), m.group(2))
    return attrs


def check_css_rules(path, text):
    lines = text.splitlines()
    for i, line in enumerate(lines, start=1):
        stripped = line.strip()
        if stripped.startswith("/*") or stripped.startswith("//"):
            continue
        for prop in FORBIDDEN_CSS_PROPS:
            if re.search(rf"\b{re.escape(prop)}\s*:", line) or (
                prop == "@keyframes" and prop in line
            ):
                fail(path.relative_to(ROOT).as_posix(), i, f"forbidden CSS property/rule: {prop}")
        if GRADIENT_RE.search(line):
            fail(path.relative_to(ROOT).as_posix(), i, "gradient used — forbidden")
        if CENTER_RE.search(line):
            fail(path.relative_to(ROOT).as_posix(), i, "text-align: center — nothing is centered")
        if UNDERLINE_OFF_RE.search(line):
            fail(path.relative_to(ROOT).as_posix(), i, "text-decoration: none — links must stay underlined")
        if FONT_IMPORT_RE.search(line):
            fail(path.relative_to(ROOT).as_posix(), i, "web font reference — forbidden, system fonts only")

    if not VISITED_RULE_RE.search(text):
        fail(path.relative_to(ROOT).as_posix(), 1, "no a:visited rule found — visited-link color must be preserved")


def check_images(path, text):
    """§3: every <img> must sit inside <figure class="evidence"> with a
    <figcaption>, carry alt/width/height, live under assets/img/, and stay
    within the per-image size cap. Returns total referenced image bytes."""
    all_imgs = list(IMG_TAG_RE.finditer(text))
    wrapped_spans = set()
    total_bytes = 0

    for fm in FIGURE_RE.finditer(text):
        fig_attrs = parse_attrs(fm.group(1))
        fig_body = fm.group(2)
        fig_line = line_of(text, fm.start())
        classes = fig_attrs.get("class", "").split()
        is_evidence = "evidence" in classes
        body_imgs = list(IMG_TAG_RE.finditer(fig_body))

        if not body_imgs:
            continue
        if not is_evidence:
            fail(path.relative_to(ROOT).as_posix(), fig_line, '<figure> containing an <img> must have class="evidence"')
        if not FIGCAPTION_RE.search(fig_body):
            fail(path.relative_to(ROOT).as_posix(), fig_line, "<figure class=\"evidence\"> is missing a <figcaption>")
        if len(body_imgs) > 1:
            fail(path.relative_to(ROOT).as_posix(), fig_line, "more than one <img> in a single <figure> — one image per figure")

        for im in body_imgs:
            abs_start = fm.start(2) + im.start()
            abs_end = fm.start(2) + im.end()
            wrapped_spans.add((abs_start, abs_end))
            img_line = line_of(text, abs_start)
            attrs = parse_attrs(im.group(0))

            if not attrs.get("alt", "").strip():
                fail(path.relative_to(ROOT).as_posix(), img_line, "<img> missing a non-empty alt attribute")
            if "width" not in attrs:
                fail(path.relative_to(ROOT).as_posix(), img_line, "<img> missing a width attribute")
            if "height" not in attrs:
                fail(path.relative_to(ROOT).as_posix(), img_line, "<img> missing a height attribute")

            src = attrs.get("src", "")
            if not src:
                fail(path.relative_to(ROOT).as_posix(), img_line, "<img> missing a src attribute")
                continue
            if src.startswith("http://") or src.startswith("https://"):
                fail(path.relative_to(ROOT).as_posix(), img_line, "external/hotlinked image — image must ship in this repo")
                continue

            # Resolve relative to this page's own directory — a page in a
            # category subdirectory (experience/traveloka.html) references
            # ../assets/img/..., not a root-relative assets/img/... path.
            img_path = (path.parent / src).resolve()
            img_dir = (ROOT / IMAGE_DIR_PREFIX).resolve()
            try:
                img_path.relative_to(img_dir)
            except ValueError:
                fail(path.relative_to(ROOT).as_posix(), img_line, f"image src must live under {IMAGE_DIR_PREFIX}, got {src!r}")
                continue
            if not img_path.is_file():
                fail(path.relative_to(ROOT).as_posix(), img_line, f"image file not found: {src}")
                continue

            size = img_path.stat().st_size
            total_bytes += size
            if size > MAX_IMAGE_BYTES:
                fail(path.relative_to(ROOT).as_posix(), img_line, f"{src} is {size} bytes, over the {MAX_IMAGE_BYTES}-byte per-image cap")

    for im in all_imgs:
        if (im.start(), im.end()) not in wrapped_spans:
            fail(path.relative_to(ROOT).as_posix(), line_of(text, im.start()), '<img> must be wrapped in <figure class="evidence"> with a <figcaption>')

    if len(all_imgs) > MAX_IMAGES_PER_PAGE:
        fail(path.relative_to(ROOT).as_posix(), 1, f"{len(all_imgs)} images on the page, over the {MAX_IMAGES_PER_PAGE}-image cap")

    return len(all_imgs), total_bytes


def check_html_structure(path, text):
    lines = text.splitlines()
    for i, line in enumerate(lines, start=1):
        for tag in FORBIDDEN_HTML_TAGS:
            if re.search(rf"<{tag}\b", line, re.IGNORECASE):
                fail(path.relative_to(ROOT).as_posix(), i, f"forbidden tag: <{tag}> — no icons/embeds/decorative media")
        if SCRIPT_TAG_RE.search(line):
            fail(path.relative_to(ROOT).as_posix(), i, "forbidden <script> tag — zero JavaScript")
        if EXTERNAL_HREF_RE.search(line):
            tag_match = re.search(r"<(\w+)", line)
            tag = tag_match.group(1).lower() if tag_match else ""
            if tag in ("link", "script", "source", "iframe"):
                fail(path.relative_to(ROOT).as_posix(), i, "external resource request — must be zero-dependency")
        if CENTER_RE.search(line):
            fail(path.relative_to(ROOT).as_posix(), i, "text-align: center — nothing is centered")
        if UNDERLINE_OFF_RE.search(line):
            fail(path.relative_to(ROOT).as_posix(), i, "text-decoration: none — links must stay underlined")
        for lo, hi in DECORATIVE_RANGES:
            for ch in line:
                if lo <= ord(ch) <= hi:
                    fail(path.relative_to(ROOT).as_posix(), i, f"decorative unicode character {ch!r} (U+{ord(ch):04X})")
                    break

    h1_count = len(re.findall(r"<h1\b", text, re.IGNORECASE))
    if h1_count != 1:
        fail(path.relative_to(ROOT).as_posix(), 1, f"expected exactly one <h1>, found {h1_count}")


def main():
    for name in CSS_FILES:
        path = ROOT / name
        text = path.read_text()
        size = path.stat().st_size
        if size > MAX_TEXT_ONLY_BYTES:
            fail(path.relative_to(ROOT).as_posix(), 1, f"file is {size} bytes, over the {MAX_TEXT_ONLY_BYTES}-byte budget")
        check_css_rules(path, text)

    css_bytes = sum((ROOT / name).stat().st_size for name in CSS_FILES)

    for name in HTML_FILES:
        path = ROOT / name
        text = path.read_text()
        check_html_structure(path, text)
        for style_block in re.findall(r"<style\b[^>]*>(.*?)</style>", text, re.DOTALL | re.IGNORECASE):
            check_css_rules(path, style_block)

        image_count, image_bytes = check_images(path, text)
        html_bytes = path.stat().st_size

        if image_count == 0:
            if html_bytes > MAX_TEXT_ONLY_BYTES:
                fail(path.relative_to(ROOT).as_posix(), 1, f"file is {html_bytes} bytes, over the {MAX_TEXT_ONLY_BYTES}-byte text-only budget")
        else:
            page_weight = html_bytes + css_bytes + image_bytes
            if page_weight > MAX_PAGE_WEIGHT_WITH_IMAGES:
                fail(path.relative_to(ROOT).as_posix(), 1, f"page weight (html+css+images) is {page_weight} bytes, over the {MAX_PAGE_WEIGHT_WITH_IMAGES}-byte §3 budget")

    if errors:
        for e in errors:
            print(e)
        print(f"\n{len(errors)} check(s) failed. See guide/design-guide.md for the full rule.")
        return 1

    print("All mechanical checks passed. Reminder: bold budget, descriptor voice, "
          "and viewport fit still need a manual read against guide/design-guide.md §14.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
