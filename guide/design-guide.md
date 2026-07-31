# Design Guide — Academic Portfolio ("The Index", variant C)

**For:** whoever builds this site next.
**Status:** design direction is locked. Do not reinterpret it.
**Reference point:** craigslist.org — its discipline, not its logo.

This document specifies *how the site must look and behave*. It does not specify what
sections exist or what content goes in them; take that from the client. If a rule here
conflicts with something you'd normally do, this document wins.

---

## 1. The single rule

**The page is a directory. Everything on it is either a link, a label for links, or a
fact that saves the reader a click.**

Before adding any element, ask: does this help someone find something, or verify
something? If neither, it does not go on the page. This is the test that resolves
almost every question below.

The site's job is to let four different visitors — a search committee member, a
prospective student, a journalist, a collaborator — each complete a different errand in
under thirty seconds. It is not to impress anyone, and it is not to express a
personality. The restraint *is* the personality.

---

## 2. What "classic and simple" means here

It means the plain-document web: black text, white background, blue underlined links,
system fonts, hairline rules, high information density, no images.

It does **not** mean "minimal." Minimalism removes content and adds whitespace. This
design keeps all the content and removes decoration. A correct page will look *fuller*
than a typical modern portfolio, not emptier.

### Explicitly forbidden

These are not stylistic preferences. Any of them present means the build is wrong.

- Border radius anywhere. Every corner is 90°.
- Box shadows, drop shadows, glows, blurs.
- Gradients of any kind, including subtle ones.
- Cards. No bordered, padded, elevated content containers.
- Hero sections, banner areas, full-width colored bands.
- Photography, illustration, stock imagery, avatars, logos, decorative SVG.
- Icons — including a single small one. Use words.
- Web fonts. Not Inter, not a Google Font, not a self-hosted face.
- Emoji, emoticons, and any pictographic or dingbat character.
- Decorative unicode symbols standing in for words or icons — arrows (↗ → ← ▲),
  stars, checkmarks, bullets-as-glyphs, or any other symbol used as a visual marker.
  If something needs marking, say it in words. An external link is identified by its
  URL and context, not a trailing arrow.
- Animation, transitions, parallax, scroll-triggered reveals, fade-ins, counters.
- Dark mode toggles, theme switchers, cookie banners, analytics popups, newsletter
  modals, chat widgets, back-to-top buttons.
- Skeleton loaders or spinners. The page is static; there is nothing to load.
- Any framework — React, Vue, Tailwind, Bootstrap, or a CSS reset library.

---

## 3. Color

The palette is five values. There is no sixth.

| Token | Hex | Use |
|---|---|---|
| `--ink` | `#000000` | All body text, headings, hard rules |
| `--faint` | `#767676` | Descriptors, metadata, timestamps, table keys |
| `--link` | `#0000cc` | Unvisited links |
| `--visited` | `#551a8b` | Visited links — **must be preserved** |
| `--rule` | `#d4d4d4` | Structural rules |
| `--hair` | `#ebebeb` | Rules inside dense lists and tables |
| `--bg` | `#ffffff` | Page background |

Rules on color:

- The background is white. Not off-white, not cream, not `#fafafa`.
- Color carries exactly one meaning: **blue means clickable, purple means already
  visited, gray means secondary, black means primary.** Never use color decoratively,
  for categories, for emphasis, or for mood.
- Keep the visited-link color. It is a genuine navigational aid on a directory and
  most modern sites throw it away for no reason.
- One highlight is permitted where a selection or match must be shown: `#ffffaa`,
  flat, no border. Use it nowhere else.

---

## 4. Typography

### Faces

```css
--sans: Helvetica, Arial, "Liberation Sans", sans-serif;
--mono: "Courier New", Courier, monospace;
```

Sans for everything. Mono only for numeric columns that must align (years, counts,
dates in ISO form) and for inline code. No serif face on this variant — serif belongs
to a different concept and mixing them muddies the direction.

Do not load fonts. The correct rendering is whatever the visitor's OS provides; the
mild inconsistency across machines is part of the plain-document character.

### Scale

Five sizes, no more.

| Role | Size | Weight |
|---|---|---|
| Name / page title | 22px | bold |
| Column heading | 13px | bold, underlined |
| Body, links | 13px | normal |
| Descriptor, metadata | 12px | normal, `--faint` |
| Footer, timestamps | 11px | normal, `--faint` |

- Line height: 1.5 for prose, 1.6 for stacked link lists, 1.35 for a link that wraps
  onto a descriptor line beneath it.
- Sentence case or lowercase for headings. Never Title Case, never ALL CAPS, never
  letter-spaced small caps.
- Bold is a scarce resource: the name, column headings, and the *for search committees*
  link. That is the entire budget. Do not bold for emphasis inside prose.
- No italic except for publication titles and journal names.
- Never center anything. Everything is left-aligned except numbers in table columns,
  which align right.

---

## 5. Layout

### Page frame

- Max width **980px**, centered, `padding: 14px 16px`.
- Do not go full-bleed. Do not narrow it to 720px "for readability" — this is a
  directory, and the columns need the width.

### The grid

Four columns, left to right:

```
+------------------+----------+----------+----------+
| SUMMARY          | research | teaching | elsewhere|
| (facts, selected |          |          |          |
|  work, committee |          |          |          |
|  link)           |          |          |          |
+------------------+----------+----------+----------+
```

- Summary column: ~31% width, separated from the rest by a 1px `--hair` rule on its
  right edge. That rule is the only thing marking it as different — no background
  tint, no border box, no padding well.
- The three category columns share the remaining width equally, gap 13–26px.
- Use flexbox. Do not use CSS Grid's fancy features; nothing here needs them.

### Vertical structure

Top of page, in order: name → 1px solid black rule → the four columns → 1px `--rule` →
footer line with last-updated date. Nothing above the name. No navigation bar — the
directory *is* the navigation.

### Spacing

Use a 4px base unit: 4 / 8 / 12 / 16 / 24. Nothing larger than 24px of vertical space
anywhere on the page. If a section feels crowded, that is correct; resist the urge to
open it up. Whitespace here is a bug, not a feature.

---

## 6. Links

- Always underlined. Always. Underlines are removed on the modern web to make
  interfaces look cleaner, and every time it makes them harder to use. Not here.
- Hover: no color change, no underline change. Optional: white text on `--link`
  background (the classic selected-row inversion). Nothing else.
- Focus: `outline: 2px solid #000; outline-offset: 1px`. Visible, not suppressed.
- No buttons. There is no action on this site that isn't navigation, so there is
  nothing a button would be honest about. Links only.
- No hover cards, tooltips, previews, or expanding panels.
- No trailing arrow, glyph, or symbol on external links — not `↗`, not `→`, nothing.
  Word choice and the URL do the work. `target="_blank"` is fine; the visual mark is
  not.
- File links state format and size inline: `cv (pdf, 4pp)`. Always warn before a
  download.

---

## 7. The summary column

This column exists to solve one problem: a pure directory tells a hiring committee
nothing. It must answer four questions before the reader clicks anything — rank and
institution, field, best work, availability.

Three parts, in this order:

**1. Facts table.** A key/value table, keys in `--faint` on the left, values in
`--ink`. Keys are one lowercase word. Values are noun phrases, never sentences. This
is a table because a table is *verifiable* — it reads as a record, not a pitch. Cap it
at six rows; if there's a seventh, something else has to go.

**2. Selected work.** Two to four items. Title as a link, venue and year on a second
line in `--faint`. No abstract, no thumbnail, no "read more."

**3. The committee link.** One bold link routing the highest-stakes visitor to a page
assembled for them, plus one gray line saying what's on it.

Do not let this column grow into a bio. If it exceeds the height of the category
columns beside it, cut it.

---

## 8. Descriptors — the voice rule

Links in the category columns may carry a short gray descriptor. This is what makes
the directory self-summarizing, and it is also the easiest thing in this design to get
wrong.

**Descriptors contain counts, venues, dates, formats, and scale. Nothing else.**

Good:
- `publications (24)` — `9 journal, 15 conference`
- `datasets (6)` — `4 languages, CC-BY`
- `ling 512 — corpus methods` — `taught 6x`

Forbidden:
- `groundbreaking work on…`
- `widely used by researchers`
- `passionate about low-resource NLP`
- `award-winning`

The moment a descriptor becomes an adjective, the page stops reading as a record and
starts reading as marketing — and the plain visual language stops protecting the
content and starts looking like an affectation instead. Verifiable or absent.

Keep descriptors under 40 characters. Set them on a second line beneath the link when
they'd otherwise cause an awkward wrap.

---

## 9. Tables

Tables are a primary element here, not a fallback.

- `border-collapse: collapse`. Header row: bottom border 1px `--ink`. Body rows:
  bottom border 1px `--hair`. No vertical rules. No zebra striping. No outer border.
- Cell padding `2px 6px`. Tight.
- Numbers right-aligned in `--mono`; text left-aligned in `--sans`.
- Header cells that sort are `--link` and underlined, because they behave like links.
- Never wrap a table in a card, and never replace it with cards on mobile. A table
  that scrolls horizontally is better than a table converted into stacked blocks.

---

## 10. Responsive behavior

Two breakpoints. That's enough.

- **≥ 900px** — the four-column grid as specified.
- **620–899px** — summary column keeps full width at the top with a bottom `--hair`
  rule; the three category columns sit below it, still three across.
- **< 620px** — everything stacks in one column. Order: name, summary, research,
  teaching, elsewhere, footer. The summary comes first on mobile, which is the correct
  reading order anyway.

Rules:

- Never hide content at small sizes. No hamburger menu, no accordions, no "show more."
  A long scroll on a phone is fine; a hidden link is not.
- Body text stays 13px on mobile. Do not scale type up — density is the point.
- Tap targets: links in stacked lists need at least 32px of vertical rhythm. This is
  the one place you may add space.

---

## 11. Accessibility floor

Non-negotiable, and cheap given the constraints.

- Semantic HTML: one `<h1>` (the name), `<h2>` per column heading, `<ul>` for link
  lists, real `<table>` markup with `<th>` and `scope`.
- All text meets WCAG AA. `--faint` `#767676` on white is 4.54:1 — do not lighten it
  further.
- Never signal anything by color alone.
- Visible focus outlines on every interactive element.
- Zooming to 200% must not break the layout or require horizontal scrolling.
- A skip link is unnecessary — there's no repeated nav to skip — but the page must be
  fully operable by keyboard in a sensible tab order.
- `prefers-reduced-motion` is trivially satisfied because there is no motion.

---

## 12. Performance and build

- Hand-written HTML and CSS. One stylesheet, or a `<style>` block if it's under ~8 KB.
- **Zero JavaScript on the front page.** If a later page needs sorting, that's ~20
  lines of vanilla JS on that page only. Nothing else justifies a script.
- Every page under 30 KB total, no external requests, first paint effectively instant
  on a slow connection.
- No build step, no bundler, no dependencies. This site must still work, unchanged, in
  ten years — which is a design goal, not an engineering one.
- Print stylesheet: hide nothing, set links to black, print the URL after external
  links in parentheses.

---

## 13. Acceptance checklist

Reject the build if any of these is false:

- [ ] Page loads with zero JavaScript and zero network requests beyond the HTML.
- [ ] No border radius, shadow, gradient, icon, image, or web font anywhere.
- [ ] No emoji, emoticon, or decorative unicode symbol (arrows, stars, checkmarks)
      anywhere, including as a trailing mark on external links.
- [ ] Every link is underlined; visited links render purple.
- [ ] The four committee facts are visible without scrolling on a 1280×800 screen.
- [ ] Every descriptor is a count, venue, date, format, or scale — no adjectives.
- [ ] Bold appears on the name, the column headings, and the committee link only.
- [ ] Nothing is centered; nothing is animated; nothing is hidden behind a control.
- [ ] The page still makes sense with CSS disabled entirely.
- [ ] Total weight under 30 KB.

---

## 14. When in doubt

Ask what craigslist would do, then check the answer against Section 1. If it's still
unclear, choose the option with less on the screen and more in the link.
