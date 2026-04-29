# AGENTS.md

> Cross-tool instructions for AI coding agents working in this repository
> (Codex CLI, Cursor, Aider, Claude Code, Continue, etc.).
>
> GitHub Copilot uses [`.github/copilot-instructions.md`](.github/copilot-instructions.md),
> which is the **canonical, more detailed** version. Everything below is a
> condensed mirror of that document; if they ever disagree, prefer the Copilot
> instructions file.

## TL;DR for agents

This repo is **two things at once**:

1. The Vue 3 + TypeScript + Vite source code of Musthofa Joko Anggoro's
   personal portfolio website (Windows‑XP themed).
2. A **career / skill / portfolio data center** for the owner. The canonical,
   structured profile data lives in `src/data/portfolio/*.json`. Markdown in
   [`docs/profile/`](docs/profile/) is generated from that JSON for AI readability.

Read `docs/profile/` before answering questions about the owner's
skills, experience, projects, education, or contact info.

## Stack

- Vue 3 (`<script setup lang="ts">`, Composition API)
- TypeScript (strict, type-checked via `vue-tsc` during build)
- Vite 6
- Tailwind CSS 4 + a custom Windows‑XP design system in `src/style.css`
- Pinia 3 (+ `pinia-plugin-persistedstate`), Vue Router 4, axios
- ESLint 9 (flat config) + Prettier 3
- Package manager: npm

## Commands

```bash
npm install        # install deps
npm run sync:profile # regenerate docs/profile markdown from canonical JSON
npm run dev        # dev server on http://localhost:5173
npm run build      # type-check + production build  ← correctness gate
npm run preview    # preview the prod build
npx eslint .       # optional manual lint
npx prettier --check .   # optional manual format check
```

There is **no test runner** and **no `lint` script**. Don't add one unless
the user asks.

## Layout

```
.github/copilot-instructions.md  ← detailed instructions (read this too)
AGENTS.md                        ← this file
docs/profile/                    ← career data center (markdown, ground truth)
src/data/portfolio/             ← canonical profile JSON (ground truth)
src/
  App.vue, main.ts, style.css
  router/, views/, components/, interfaces/, services/, files/
public/                          ← static assets (CV PDF, etc.)
index.html, vite.config.ts, tsconfig*.json, eslint.config.js, .prettierrc
```

## Conventions (short list)

- Vue SFCs in `PascalCase.vue` with `<script setup lang="ts">`.
- Type props with a local `interface Props` and `defineProps<Props>()`.
- Reuse types from `src/interfaces/*.interface.ts` (`Experience`, `Project`, …).
- Use existing **XP design classes** (`xp-window`, `xp-title-bar`, `xp-menubar`,
  `xp-panel`, `xp-button`, `xp-status`, `font-xp`, `font-xp-title`, …) plus
  Tailwind utilities. Don't invent a parallel design system.
- 2-space indent, semicolons, single quotes (see `.prettierrc`).
- When you change profile data, update `src/data/portfolio/*.json`, then run
  `npm run sync:profile` and commit regenerated markdown.

## Do / Don't

**Do**
- Make small, surgical changes.
- Read `docs/profile/` for any biographical question.
- Run `npm run build` after non-trivial edits.
- Keep the XP aesthetic consistent across components.

**Don't**
- Don't add new dependencies, test frameworks, or CI workflows unsolicited.
- Don't rename the package, change build scripts, or rewrite the styling system
  for cleanup.
- Don't invent facts about the owner — if something isn't documented, ask.
- Don't commit secrets or large generated artifacts.

## Source of truth for "who is the owner"

Read these in order:

1. `src/data/portfolio/*.json` (canonical)
2. [`docs/profile/README.md`](docs/profile/README.md)
3. [`docs/profile/about.md`](docs/profile/about.md)
4. [`docs/profile/skills.md`](docs/profile/skills.md)
5. [`docs/profile/education.md`](docs/profile/education.md)
6. [`docs/profile/experience.md`](docs/profile/experience.md)
7. [`docs/profile/projects.md`](docs/profile/projects.md)
8. [`docs/profile/contact.md`](docs/profile/contact.md)
9. [`docs/profile/voice.md`](docs/profile/voice.md) — writing voice & tone (cover letters only)

If markdown and JSON disagree, JSON wins; re-run `npm run sync:profile`.

## LaTeX CV creation (quick reference)

For creating or updating LaTeX CVs:

1. **Read full guide**: `public/CV_GUIDE.md` (comprehensive documentation)
2. **Use template**: Start with `public/CV_TEMPLATE.tex` (never from scratch)
3. **Install LaTeX**: `sudo apt-get install -y texlive-latex-base texlive-latex-extra texlive-fonts-recommended texlive-fonts-extra`
4. **Standard header**: Email | LinkedIn | GitHub | Portfolio (NO phone number)
5. **Compile**: Run `pdflatex -interaction=nonstopmode file.tex` twice
6. **Target**: 1 page for most positions, 2 pages for research/senior only
7. **Data source**: `src/data/portfolio/*.json` and `docs/profile/*.md`
8. **Clean up**: `rm -f *.aux *.log *.out` before committing

Section order varies by role:
- **Industry**: Education → Work Experience → Projects → Skills → Leadership
- **Research**: Research Interests → Education → Experience → Skills → Projects

Bullet format: `Action verb + Technology + Impact with metrics`

## Cover Letter creation (quick reference)

For creating a cover letter:

1. **Read full guide**: `public/COVER_LETTER_GUIDE.md` (paragraph blueprint, mapping matrix, LaTeX template, checklist)
2. **Read voice file**: `docs/profile/voice.md` **before drafting** — non-negotiable
3. **Target**: 300–400 words, 4 paragraphs (P1 Hook → P2 Proof → P3 Fit → P4 CTA), no bullets in body
4. **P1**: Open with result/story/curiosity. Never "I am writing to apply for…". Mirror JD keywords.
5. **P2**: One STAR-lite story with a hard number. Pull from `experience.md` first.
6. **P3**: Specific company reference + genuine interest from `about.md`. No "I am passionate about…".
7. **P4**: Forward momentum closing. Never "Thank you for your time and consideration."
8. **Write directly into LaTeX source** using the template in Section 9 of `COVER_LETTER_GUIDE.md` — no `.md` draft:
   `public/{category}/{company}-{year}/CoverLetter_Musthofa_Joko_Anggoro_{Company}.tex`
9. **Compile to PDF** (run twice, then clean aux files):
    ```bash
    pdflatex -interaction=nonstopmode CoverLetter_Musthofa_Joko_Anggoro_{Company}.tex
    pdflatex -interaction=nonstopmode CoverLetter_Musthofa_Joko_Anggoro_{Company}.tex
    rm -f *.aux *.log *.out
    ```
10. **Commit both** (`.tex` and `.pdf`) alongside the matching CV files

**Forbidden phrases**: "responsible for" · "passionate about" · "I am a quick learner" ·
"leverage my skills" · "synergize" · "Thank you for your time and consideration"

## CV writing style for non-LaTeX CVs

When generating an updated non-LaTeX CV, follow the existing template in
`public/CV_Musthofa Joko Anggoro.pdf`:

- Keep it one page and compact.
- Header: `Name | Email | LinkedIn | GitHub | Portfolio` (NO phone number for privacy).
- Section order: **Work Experience → Education → Skills**.
- Experience entries: company, role, date range, then 2–3 impact-oriented bullets.
- Bullet style: action verb + tech stack + outcome; keep each bullet short
  (roughly one line, around 18–32 words).
- Education: concise institution/program/date format; include GPA when known;
  program/organization descriptions stay brief (1–2 lines).
- Skills: grouped categories with concise comma-separated lists
  (Languages & Frameworks, Databases, Cloud & DevOps, Testing & Tools).
- Never invent facts; source details from `src/data/portfolio/*.json` or direct
  user input.
