# Musthofa Joko Anggoro — academic portfolio

Hand-written static HTML/CSS. Zero JS, zero build step, zero dependencies, zero
frameworks — by design, not by omission. It must still work, unchanged, in ten years.
Do not "modernize" it by introducing tooling.

## Read before editing

- Changing anything visual, structural, or behavioral → read
  [guide/design-guide.md](guide/design-guide.md) first. Design direction is locked;
  §14 is the acceptance checklist, and a change that fails it is wrong, not a style
  choice.
- Adding an image → default answer is no. It must fit one of the four categories in
  design-guide.md §3 (thesis/technical figure, project screenshot, the one profile
  photo, or a future personal-interests image) and follow that section's markup,
  styling, and file-budget rules exactly — evidentiary only, never decorative.
- Changing anything factual (dates, GPA, work history, thesis numbers, contact info,
  project descriptions) → read [guide/content.md](guide/content.md) first. It is the
  source of truth. Update it, then mirror the change into every page that repeats that
  fact. Never hand-derive a fact from prose already on a page — pull it from
  content.md, and if it's missing there, add it. The `update-content` skill
  (`.claude/skills/update-content/`) encodes this exact workflow.

Skip both for purely mechanical edits (fixing a typo, a broken link) that touch no
fact and no design rule.

## Files

- `index.html` — homepage; `for-committees.html` — academic dossier
- `research.html`, `experience.html`, `projects.html` — category list pages, each
  paired with a same-named subdirectory of detail pages (`research/thesis.html`,
  `experience/traveloka.html`, `projects/sispa.html`, etc.) — see
  design-guide.md §16 for the list/detail page pattern and directory convention
- `style.css` — the one stylesheet
- `assets/pdf/` — cv and thesis, linked from the homepage and dossier
- `assets/img/` — evidentiary images only (design-guide.md §3); doesn't exist yet
- `guide/design-guide.md` — locked visual/behavioral spec
- `guide/content.md` — canonical facts

## Hard constraints (full detail in design-guide.md)

No framework, no JS on the front page, no icons or web fonts, no border-radius or
shadows, no decorative images (evidentiary images only, see §3). Every text-only page
under 30KB, image-bearing page under 500KB. Semantic HTML, WCAG AA. Links always
underlined, visited-link purple preserved, color never used decoratively.

## Verification

Run `python3 scripts/check.py` from the repo root after any edit — it mechanically
checks the parts of design-guide.md §14 that don't require judgment (forbidden
CSS/HTML, external requests, decorative unicode, file size/weight budget, heading
structure, and — if any `<img>` is present — the §3 image rules: `<figure
class="evidence">` wrapper, `<figcaption>`, `alt`/`width`/`height`, `assets/img/`
location, per-image and per-page size caps). Exit 0 required; it prints `file:line`
for every failure. It does **not** cover bold budget, descriptor voice, or viewport
fit — read §14 directly for those. The same script runs in CI on every push and PR
(`.github/workflows/check.yml`).

No build step otherwise. Open the file directly or serve statically
(`.claude/launch.json` runs `python3 -m http.server`) to eyeball a visual change.
