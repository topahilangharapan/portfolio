# portfolio

Musthofa Joko Anggoro's directory site, targeting both research and industry
opportunities. Hand-written HTML and CSS, no build step, no framework, no
dependencies. Design is specified in [guide/design-guide.md](guide/design-guide.md)
and facts are specified in [guide/content.md](guide/content.md) — any future change to
this site must follow those documents. See [CLAUDE.md](CLAUDE.md) for AI-agent
working conventions.

## Files

- `index.html` — the homepage
- `for-committees.html` — dossier assembled for PhD admissions / search committees
- `research.html`, `experience.html`, `projects.html` — category list pages, each
  with a same-named subdirectory of detail pages (`research/thesis.html`,
  `experience/traveloka.html`, `projects/sispa.html`, etc.) — see
  design-guide.md §16
- `style.css` — the one stylesheet
- `assets/pdf/` — cv and thesis PDFs, linked from the homepage and dossier
- `assets/img/` — evidentiary images only, per design-guide.md §3 (empty for now)
- `guide/design-guide.md` — locked visual/behavioral spec
- `guide/content.md` — canonical facts, the source of truth for every claim on the site
- `scripts/check.py` — mechanical checklist runner, see below

## Run

Open `index.html` directly in a browser, or serve the directory with any static file
server, e.g. `python3 -m http.server`.

## Check

```bash
python3 scripts/check.py
```

Verifies the mechanically-checkable subset of `guide/design-guide.md` §14 — forbidden
CSS/HTML, external requests, decorative unicode, file size/weight budget, heading
structure, and (if any image is present) the §3 image rules. Runs in CI on every push
and pull request (`.github/workflows/check.yml`). It doesn't cover judgment calls like
bold budget or descriptor voice; those still need a manual read against the design
guide.
