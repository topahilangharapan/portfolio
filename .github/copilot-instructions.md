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

When in doubt, **prefer the data in `docs/profile/` as the source of truth** over what
you might infer from individual `.vue` files. Component data (e.g. project lists in
`src/components/ProjectExplorer.vue`) and the markdown profile **must stay in sync**.

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
│   └── profile/                  ← career / skill / portfolio data center (markdown)
│       ├── README.md
│       ├── about.md
│       ├── skills.md
│       ├── education.md
│       ├── experience.md
│       ├── projects.md
│       └── contact.md
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
│   └── files/                    ← bundled image assets
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
- Hard‑coded data (experiences, projects, education, etc.) currently lives
  inside the relevant component as a `withDefaults(defineProps<Props>(), { … })`
  default. When you change that data, **also update the matching markdown
  file in `docs/profile/`** (and vice versa). They must agree.

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
- When adding a new project / experience / skill: update **both** the relevant
  Vue component **and** the corresponding markdown file in `docs/profile/`.

### Don't
- Don't rewrite the styling system or replace Tailwind / the XP CSS.
- Don't add new heavy dependencies (state libs, UI kits, test frameworks)
  without being asked.
- Don't change the package name, build scripts, or TS config "to clean up"
  unless the user asks.
- Don't invent biographical facts. If something isn't in `docs/profile/` or
  in a component, ask the user instead of guessing.
- Don't commit secrets, the user's CV PDF source data beyond what's already
  in `public/`, or any file under `node_modules/` or `dist/`.

---

## 6. Where to find ground truth about the owner

For any question about Musthofa's career, skills, education, projects, or
contact info, read these files (in this order of authority):

1. `docs/profile/README.md` — index + last-updated marker
2. `docs/profile/about.md`
3. `docs/profile/skills.md`
4. `docs/profile/education.md`
5. `docs/profile/experience.md`
6. `docs/profile/projects.md`
7. `docs/profile/contact.md`

If a fact disagrees between markdown and a `.vue` component, **the markdown
wins** and the component should be updated to match (after confirming with
the user).
