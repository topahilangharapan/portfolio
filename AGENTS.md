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
   structured profile data lives in [`docs/profile/`](docs/profile/) and is
   the source of truth for any question about him.

Always read `docs/profile/` before answering questions about the owner's
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
- When you change hard-coded portfolio data inside a component, update the
  matching file in `docs/profile/` in the **same change**, and vice versa.

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

1. [`docs/profile/README.md`](docs/profile/README.md)
2. [`docs/profile/about.md`](docs/profile/about.md)
3. [`docs/profile/skills.md`](docs/profile/skills.md)
4. [`docs/profile/education.md`](docs/profile/education.md)
5. [`docs/profile/experience.md`](docs/profile/experience.md)
6. [`docs/profile/projects.md`](docs/profile/projects.md)
7. [`docs/profile/contact.md`](docs/profile/contact.md)

If markdown and a `.vue` component disagree, the markdown wins.
