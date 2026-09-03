---
name: update-content
description: Update a factual claim on the portfolio site — dates, GPA, work history, thesis numbers, project details, contact info, or any other fact about Musthofa. Use whenever the user asks to change, add, correct, or refresh a fact on any page of the site.
---

Facts on this site are sourced from `guide/content.md`; the HTML pages must never
drift from it or from each other. The site is a homepage plus category list pages
(`research.html`, `experience.html`, `projects.html`) each with a subdirectory of
detail pages (`research/thesis.html`, `experience/traveloka.html`, etc.) — see
`guide/design-guide.md` §16. A single fact (e.g. a role's dates) commonly appears on
the homepage highlight, the category list page, and the detail page all at once.
Follow these steps in order:

1. **Read `guide/content.md`** and find the table row for the fact being changed.
   If it doesn't have a row yet, add one — don't let a fact exist only in HTML.
2. **Update the value in `guide/content.md` first.** This file is the source of
   truth; the HTML is a mirror of it.
3. **Grep every HTML page** (`grep -rl "<old value>" --include=*.html .` from the
   repo root) for the old value. The same fact often repeats across three levels —
   a homepage highlight, a category list page's descriptor, and a detail page's
   facts table/prose — update every occurrence to match the new value in
   `content.md` exactly.
4. **Do not touch layout, markup structure, or CSS** while doing this — a content
   update and a design change are different kinds of edit. If the new fact
   doesn't fit the existing markup (e.g. a table now needs a 7th row, which
   `guide/design-guide.md` §8 caps at six), stop and flag the conflict instead of
   silently breaking the rule.
5. **Check whether this update involves an image** (the user supplied a photo/file,
   or the fact is a natural fit for one — e.g. a new thesis figure, a project
   screenshot, a profile photo). Default to no. If yes:
   - it must fit one of the four categories in `guide/design-guide.md` §3;
   - place the file under `assets/img/`, wrap it in `<figure class="evidence">`
     with a `<figcaption>`, and give it `alt`/`width`/`height`, per §3's markup and
     budget rules exactly;
   - update the tracking table in `guide/content.md`'s **Images** section.
   Do not add an image just because a fact update happens to touch that section —
   it still has to be evidence, not illustration.
6. **Run the checklist script**: `python3 scripts/check.py` from the repo root.
   It must exit 0 before the change is done — it validates both the general rules
   and, if you added one, the image against §3.
7. **Update the `last updated` `<time>` element** at the bottom of any page you
   changed, to the current date.
8. Report which files changed and confirm the script passed.
