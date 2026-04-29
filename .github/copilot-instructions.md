# GitHub Copilot Instructions

> Repo-specific guidance for GitHub Copilot, Copilot Chat, and the Copilot coding agent.
> Other AI tools (Cursor, Aider, Codex CLI, Continue, Claude Code, etc.) should also read
> [`AGENTS.md`](../AGENTS.md), which mirrors this file in the cross-tool format.

This repository serves **two purposes**:

1. The **source code** of Musthofa Joko Anggoro's personal portfolio website
   (a Vue 3 + TypeScript + Vite single-page app, Windows‑XP themed).
2. A **career / skill / portfolio data center**: canonical, structured information
   about the owner that AI assistants can reference when answering questions, drafting
   resumes/cover letters, suggesting projects, etc.

When in doubt, treat **`src/data/portfolio/*.json` as the canonical source of truth**.
`docs/profile/*.md` is generated from those JSON files for AI/LLM readability.

---

## 1. Project at a glance

| Aspect            | Value                                                                 |
|-------------------|-----------------------------------------------------------------------|
| Owner             | Musthofa Joko Anggoro (`@topahilangharapan`)                          |
| Type              | Personal portfolio SPA                                                |
| Framework         | [Vue 3](https://vuejs.org/) (Composition API, `<script setup lang="ts">`) |
| Build tool        | [Vite 6](https://vitejs.dev/)                                         |
| Language          | TypeScript (strict via `vue-tsc`)                                     |
| Styling           | [Tailwind CSS 4](https://tailwindcss.com/) + scoped component CSS, plus a custom Windows‑XP design system (`.xp-window`, `.xp-title-bar`, `.xp-button`, `.xp-panel`, `.xp-menubar`, `.xp-status`, `font-xp`, `font-xp-title`, etc.) defined in `src/style.css` |
| State             | [Pinia 3](https://pinia.vuejs.org/) (+ `pinia-plugin-persistedstate`) |
| Routing           | [Vue Router 4](https://router.vuejs.org/)                             |
| HTTP              | [axios](https://axios-http.com/)                                      |
| UI helpers        | `@heroicons/vue`, `flowbite`, `flowbite-vue`, `simple-datatables`     |
| Auth helpers      | `jwt-decode`                                                          |
| Linter / formatter| ESLint 9 (flat config: `eslint.config.js`) + Prettier 3 (`.prettierrc`) |
| Node              | Use the version pinned by your local toolchain; project targets modern Node compatible with Vite 6 |
| Package manager   | npm (see `package-lock.json`)                                         |

> The `name` field in `package.json` is currently `sispa-frontend` and the
> top of `README.md` mentions "B01 - Radiant - FE / SiSPA". That is leftover
> boilerplate from a previous project of the owner — this repo is the
> **portfolio**. Do not delete it as a side effect, but feel free to update
> it if the user asks you to clean up the README.

---

## 2. Repository layout

```
.
├── .github/
│   └── copilot-instructions.md   ← you are here
├── AGENTS.md                     ← same guidance for non-Copilot agents
├── README.md
├── docs/
│   └── profile/                  ← AI-readable markdown generated from JSON
│       ├── README.md
│       ├── about.md
│       ├── skills.md
│       ├── education.md
│       ├── experience.md
│       ├── projects.md
│       ├── contact.md
│       └── voice.md              ← writing voice & tone guardrails for cover letters
├── scripts/
│   └── sync-profile-docs.mjs     ← generates docs/profile from src/data/portfolio JSON
├── public/                       ← static assets served as-is (e.g. CV PDF)
├── src/
│   ├── App.vue
│   ├── main.ts                   ← app bootstrap, Pinia + Router setup
│   ├── style.css                 ← global styles + XP design tokens
│   ├── shims-vue.d.ts
│   ├── vite-env.d.ts
│   ├── router/                   ← Vue Router config
│   ├── views/                    ← top-level pages (currently HomeView.vue)
│   ├── components/               ← UI sections
│   │   ├── HeroSection.vue
│   │   ├── AboutSection.vue
│   │   ├── EducationSection.vue
│   │   ├── ExperienceExplorer.vue / ExperienceItem.vue
│   │   ├── ProjectExplorer.vue   / ProjectCard.vue
│   │   ├── ContactSection.vue
│   │   └── WelcomeNotification.vue
│   ├── interfaces/               ← shared TypeScript types (Experience, Project, …)
│   ├── services/                 ← axios-based API clients (if/when added)
│   ├── files/                    ← bundled image assets
│   └── data/
│       └── portfolio/            ← canonical profile JSON used by Vue + markdown generator
├── index.html
├── eslint.config.js
├── .prettierrc
├── tsconfig*.json
├── vite.config.ts
└── package.json
```

---

## 3. Common commands

Always run these from the repository root.

```bash
npm install        # install dependencies
npm run sync:profile # regenerate docs/profile markdown from canonical JSON
npm run dev        # start Vite dev server at http://localhost:5173
npm run build      # type-check (vue-tsc -b) AND production build
npm run preview    # preview the production build locally
```

There is currently **no test runner configured** and **no `lint` npm script**.
If you want to lint manually, run:

```bash
npx eslint .
npx prettier --check .
```

Do not introduce a new test framework, lint script, or CI workflow unless the
user explicitly asks. The build (`npm run build`) is the de-facto correctness
gate — it both type-checks and bundles. **Run it after non-trivial changes.**

---

## 4. Conventions

### Vue / TypeScript
- Always use `<script setup lang="ts">`. No Options API, no plain JS.
- Use `defineProps`, `defineEmits`, `withDefaults`, `defineModel` (Vue 3.4+).
- Typed props: `defineProps<Props>()` with a local `interface Props { … }`.
- Typed emits: `defineEmits<{ (e: 'update:isOpen', value: boolean): void }>()`.
- Prefer `ref` / `computed` / `watch` from `'vue'`. Use `nextTick` when DOM
  measurements are needed.
- Shared types live in `src/interfaces/*.interface.ts` (e.g. `Experience`,
  `Project`). Reuse them; don't redefine.
- Component filenames are `PascalCase.vue`.

### Styling
- Use Tailwind utility classes for layout, spacing, color, and responsiveness.
- Use the existing **XP design tokens / classes** (`xp-window`, `xp-title-bar`,
  `xp-menubar`, `xp-panel`, `xp-panel-raised`, `xp-button`, `xp-group`,
  `xp-group-title`, `xp-status`, `xp-progress`, `xp-progress-bar`,
  `xp-control-btn`, `xp-close-btn`, `xp-input`, `xp-scroll`, `xp-taskbar`,
  `xp-start-button`, `font-xp`, `font-xp-title`, `bg-xp-window`,
  `bg-xp-silver`, …) for anything that should look like the rest of the site.
  Do **not** invent a parallel design system.
- Component-specific styles go in scoped `<style scoped>` blocks. Keep them small.
- The site is responsive — keep `md:` / `lg:` variants intact and test that
  windows still fit on narrow viewports.

### Data
- Profile data lives in `src/data/portfolio/*.json` and is used directly by Vue.
- `docs/profile/*.md` is generated output for AI/LLM consumption.
- After changing JSON, run `npm run sync:profile` and commit the regenerated markdown.

### Formatting
- 2-space indent, semicolons, single quotes (see `.prettierrc`).
- Run `npx prettier --write <file>` on any file you touch substantially if you
  are unsure about formatting.

---

## 5. What to do / what NOT to do

### Do
- Make **small, surgical** changes that fully address the user's request.
- Read `docs/profile/` first when the user asks anything about themselves
  (skills, projects, experience, contact, etc.). Quote it accurately.
- Keep the Windows‑XP aesthetic consistent — every "section" is a fake XP window
  with title bar, menu bar, content area, and status bar.
- Run `npm run build` after non-trivial code changes.
- When adding or updating profile data, edit `src/data/portfolio/*.json`,
  run `npm run sync:profile`, and commit both JSON + regenerated markdown.

### Don't
- Don't rewrite the styling system or replace Tailwind / the XP CSS.
- Don't add new heavy dependencies (state libs, UI kits, test frameworks)
  without being asked.
- Don't change the package name, build scripts, or TS config "to clean up"
  unless the user asks.
- Don't invent biographical facts. If something isn't in canonical JSON or
  generated markdown, ask the user instead of guessing.
- Don't commit secrets, the user's CV PDF source data beyond what's already
  in `public/`, or any file under `node_modules/` or `dist/`.

---

## 6. Where to find ground truth about the owner

For any question about Musthofa's career, skills, education, projects, or
contact info, prefer these sources in this order:

1. `src/data/portfolio/*.json` — canonical source
2. `docs/profile/README.md` — generated index
3. `docs/profile/about.md`
4. `docs/profile/skills.md`
5. `docs/profile/education.md`
6. `docs/profile/experience.md`
7. `docs/profile/projects.md`
8. `docs/profile/contact.md`
9. `docs/profile/voice.md` — writing voice & tone guardrails (cover letters only)

If markdown and JSON disagree, **JSON wins**; re-run `npm run sync:profile`.

---

## 7. LaTeX CV creation workflow

When asked to create or update a LaTeX CV in this repository:

### Quick Reference
- **Comprehensive Guide**: Read `public/CV_GUIDE.md` for complete documentation
- **Template**: Start with `public/CV_TEMPLATE.tex` (do not create from scratch)
- **Standard Header**: Always use the format from NTU research CV (email, LinkedIn, GitHub, portfolio - NO phone number)

### Installation
```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install -y texlive-latex-base texlive-latex-extra texlive-fonts-recommended texlive-fonts-extra
```

### Compilation Process
```bash
# Navigate to CV directory
cd public/{category}/{company-year}/

# Compile twice (required for cross-references)
pdflatex -interaction=nonstopmode CV_Musthofa_Joko_Anggoro_{Company}.tex
pdflatex -interaction=nonstopmode CV_Musthofa_Joko_Anggoro_{Company}.tex

# Verify page count (should be 1 page for most positions)
# Look for: "Output written on *.pdf (1 page, XXXXX bytes)"

# Clean up auxiliary files
rm -f *.aux *.log *.out
```

### Standard Header Format (use this exactly)
```latex
\begin{center}
    {\LARGE \textbf{MUSTHOFA JOKO ANGGORO}} \\[2pt]
    \contactline{
        \faEnvelope\ \href{mailto:musthofaja.topa@gmail.com}{musthofaja.topa@gmail.com} \ $|$ \ 
        \faLinkedin\ \href{https://www.linkedin.com/in/musthofa-joko-anggoro/}{linkedin.com/in/musthofa-joko-anggoro} \ $|$ \
        \faGithub\ \href{https://github.com/topahilangharapan}{github.com/topahilangharapan} \ $|$ \
        \faGlobe\ \href{https://portfolio-topahilangharapan-personal.vercel.app/}{portfolio-topahilangharapan-personal.vercel.app}
    }
\end{center}
```

### Section Order by Role Type

**Industry/Internship:**
1. Education
2. Work Experience  
3. Projects (if relevant)
4. Technical Skills
5. Leadership & Activities

**Research/PhD:**
1. Research Interests (statement)
2. Education
3. Experience
4. Skills
5. Research & Technical Projects
6. Publications (if any)

### Bullet Point Style (Action + Tech + Impact)
✓ **Good**: "Engineered secure Credential Management System with AES-GCM encryption and MongoDB, reducing security incidents by 90%"  
✗ **Bad**: "Worked on backend systems"

### Customization Guidelines
- **Manufacturing/Enterprise**: Emphasize Oracle Database, enterprise systems, automation, microservices
- **Research/PhD**: Emphasize computer architecture, systems programming, FPGA, distributed systems
- **Software/Startups**: Balance full-stack, cloud, DevOps, modern frameworks

### Data Source Priority
1. `src/data/portfolio/*.json` — canonical biographical data
2. `docs/profile/*.md` — AI-readable summaries
3. Existing CVs in `public/phd-applications/` or `public/internship-applications/`

### Page Length Targets
- **1 page**: Most internships and entry-level positions
- **2 pages**: Senior positions, research positions, or when explicitly requested

### Post-Compilation Checklist
- [ ] PDF compiles without errors
- [ ] Page count matches target (usually 1 page)
- [ ] All links are clickable (email, LinkedIn, GitHub, portfolio)
- [ ] No biographical facts invented (all from profile data)
- [ ] Auxiliary files cleaned up (*.aux, *.log, *.out)
- [ ] Both .tex and .pdf committed to git

---

## 8. Cover Letter creation workflow

When asked to create a cover letter in this repository:

### Quick Reference
- **Comprehensive Guide**: Read `public/COVER_LETTER_GUIDE.md` for the full blueprint
- **Voice & Tone**: Read `docs/profile/voice.md` **before** drafting — tone consistency is critical
- **Target length**: 300–400 words, exactly 4 paragraphs, no bullet points in the letter body

### Workflow
```
1. Read job description → identify top 1–2 requirements + keywords to mirror
2. Read docs/profile/experience.md, projects.md, skills.md, education.md, about.md
3. Read docs/profile/voice.md
4. Draft the letter content using the 4-paragraph blueprint (P1 Hook → P2 Proof → P3 Fit → P4 CTA)
5. Run Self-Review Checklist (Section 7 of COVER_LETTER_GUIDE.md)
6. Write content directly into LaTeX source .tex (template in Section 9 of COVER_LETTER_GUIDE.md)
7. Compile to PDF (run pdflatex twice, then remove aux files — see Section 9)
8. Commit .tex and .pdf together alongside matching CV files
```

### Paragraph Blueprint (summary)
- **P1 Hook (2–3 sentences):** Open with a result/story/curiosity — never "I am writing to apply for…". Mirror 1–2 JD keywords. Name the company.
- **P2 Proof (3–4 sentences):** One STAR-lite story (Situation → Action + tech → Metric). Must include a hard number. Pull from `experience.md` first.
- **P3 Fit (2–3 sentences):** Reference something specific about the company. Tie to genuine interest from `about.md` — no "I am passionate about…".
- **P4 CTA (2 sentences):** Forward momentum, not gratitude. Never end with "Thank you for your time".

### Hard-Forbidden Phrases
`"I am writing to apply for…"` · `"passionate about"` · `"I am a quick learner"` ·
`"I am a team player"` · `"responsible for"` · `"leverage my skills"` · `"synergize"` ·
`"Thank you for your time and consideration"` · `"To Whom It May Concern"`

### Post-Draft Checklist
- [ ] Opening sentence does NOT start with "I am writing to apply for…"
- [ ] At least one metric cited (%, count, time, scale)
- [ ] At least one JD keyword mirrored
- [ ] Company named by name (not "your company")
- [ ] No invented facts (traceable to `docs/profile/` or `src/data/portfolio/`)
- [ ] Word count ≤ 400
- [ ] `.tex` created using the LaTeX template (Section 9 of COVER_LETTER_GUIDE.md)
- [ ] PDF compiled (`pdflatex` ×2), 1 page confirmed, auxiliary files removed
- [ ] Both `.tex` and `.pdf` committed together alongside matching CV files

---

## 9. CV authoring style (legacy - for non-LaTeX CVs)

When the user asks to generate or refresh a non-LaTeX CV:

- Keep it to **one page** with a compact, ATS-friendly layout.
- Header format: `Full Name | Email | LinkedIn | GitHub | Portfolio` (NO phone number for privacy)
- Section order should stay:
  1. **Work Experience**
  2. **Education**
  3. **Skills**
- Work experience entry format:
  - `Company`
  - `Role`
  - `Date range`
  - **2–3 bullets** focused on outcomes and implementation details.
- Bullet style:
  - Start with a strong action verb (Engineered, Enhanced, Implemented, Built, Developed, Led).
  - Mention concrete technical stack/tools.
  - End with impact (performance, reliability, security, delivery speed, usability).
  - Keep each bullet concise (roughly one line in final layout; around 18–32 words).
- Education section style:
  - Institution + program + year range in compact format.
  - Include GPA when available.
  - For programs/organizations, keep descriptions very short (1–2 lines) and impact-oriented.
- Skills section style:
  - Group by category, currently:
    - Languages & Frameworks
    - Databases
    - Cloud & DevOps
    - Testing & Tools
  - Use concise comma-separated lists; avoid long explanations.
- Do not invent achievements, metrics, dates, or technologies not present in
  `src/data/portfolio/*.json` (or explicitly provided by the user).
