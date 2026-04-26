# 🪟 Musthofa Joko Anggoro — Portfolio

Personal portfolio site of [**Musthofa Joko Anggoro**](https://github.com/topahilangharapan)
— a full-stack developer and final-year Computer Science student at Universitas
Indonesia. The site is a Vue 3 + TypeScript + Vite single-page app with a
custom Windows‑XP‑themed UI.

This repository is also the owner's **career / skill / portfolio data center**:
structured markdown files in [`docs/profile/`](docs/profile/) act as the
canonical source of truth for AI assistants, recruiters, and humans who want
the facts without having to render the site.

---

## 🧠 For AI assistants (Copilot, Cursor, Codex, Claude, …)

If you are an AI / LLM / coding agent working in this repo, **read these
first** — in this order:

1. [`.github/copilot-instructions.md`](.github/copilot-instructions.md) — full
   repo-specific instructions (stack, conventions, do/don't, build commands).
2. [`AGENTS.md`](AGENTS.md) — condensed cross-tool version of the same.
3. [`docs/profile/README.md`](docs/profile/README.md) — index of the career /
   skill / portfolio data center, plus links to:
   - [`about.md`](docs/profile/about.md)
   - [`skills.md`](docs/profile/skills.md)
   - [`education.md`](docs/profile/education.md)
   - [`experience.md`](docs/profile/experience.md)
   - [`projects.md`](docs/profile/projects.md)
   - [`contact.md`](docs/profile/contact.md)

Treat the markdown in `docs/profile/` as the **source of truth** about the
owner. If a `.vue` component disagrees, the markdown wins.

---

## 🧱 Tech stack

- [Vue 3](https://vuejs.org/) (Composition API, `<script setup lang="ts">`)
- [TypeScript](https://www.typescriptlang.org/) (strict, type-checked via `vue-tsc`)
- [Vite 6](https://vitejs.dev/)
- [Tailwind CSS 4](https://tailwindcss.com/) + custom Windows‑XP design system in `src/style.css`
- [Pinia 3](https://pinia.vuejs.org/) (+ `pinia-plugin-persistedstate`)
- [Vue Router 4](https://router.vuejs.org/)
- [axios](https://axios-http.com/), `@heroicons/vue`, `flowbite`, `flowbite-vue`, `simple-datatables`, `jwt-decode`
- ESLint 9 (flat config) + Prettier 3

## 🚀 Getting started

```bash
# 1. Install dependencies
npm install

# 2. Start the dev server (http://localhost:5173)
npm run dev

# 3. Type-check + production build
npm run build

# 4. Preview the production build
npm run preview
```

Optional manual checks (no npm scripts are configured for these):

```bash
npx eslint .
npx prettier --check .
```

## 🗂 Repository layout

```
.github/copilot-instructions.md   AI guidance for GitHub Copilot
AGENTS.md                         AI guidance for other coding agents
docs/profile/                     Career / skill / portfolio data center (markdown)
src/
  App.vue, main.ts, style.css
  router/, views/, components/, interfaces/, services/, files/
public/                           Static assets (CV PDF, etc.)
index.html, vite.config.ts, tsconfig*.json, eslint.config.js, .prettierrc
```

See [`.github/copilot-instructions.md`](.github/copilot-instructions.md) for a
deeper tour, conventions, and the dos and don'ts.

## 📬 Contact

- **Email:** [musthofaja.topa@gmail.com](mailto:musthofaja.topa@gmail.com)
- **LinkedIn:** [musthofa-joko-anggoro](https://www.linkedin.com/in/musthofa-joko-anggoro/)
- **GitHub:** [@topahilangharapan](https://github.com/topahilangharapan)

More in [`docs/profile/contact.md`](docs/profile/contact.md).
