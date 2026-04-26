# 📂 Profile — Career / Skill / Portfolio Data Center

This folder is the **canonical, structured source of truth** about the repository
owner. AI assistants, recruiters, automation, and humans should read it first
when they need to know anything about him.

> **Owner:** Musthofa Joko Anggoro
> **Handle:** [`@topahilangharapan`](https://github.com/topahilangharapan)
> **Role:** Full‑Stack Developer · Software Engineer · CS Student at Universitas Indonesia
> **Last reviewed:** 2026-04-26

## Index

| File | Contents |
|------|----------|
| [`about.md`](about.md)         | Personal summary, core strengths, interests, career goal |
| [`skills.md`](skills.md)       | Programming languages, frameworks, databases, tools, OS, AI/ML |
| [`education.md`](education.md) | University, GPA, coursework, achievements, summer program |
| [`experience.md`](experience.md) | Internships and organizational experience (Traveloka, PT MSI, COMPFEST) |
| [`projects.md`](projects.md)   | Featured portfolio projects with tech stack, role, links |
| [`contact.md`](contact.md)     | Email, LinkedIn, GitHub, availability |

## How to use this folder

### If you are an AI / LLM / coding agent
- Read this `README.md` first to understand what's available, then load
  whichever specific file answers the user's question.
- Treat these files as **ground truth**. If a `.vue` component has different
  data, the markdown wins until the user says otherwise.
- When the user asks you to draft a resume bullet, cover letter, LinkedIn blurb,
  README, or pitch, **quote facts from these files** rather than inventing them.

### If you are a human reading the repo
- These files are a clean, copy‑pasteable summary of the same information that
  is rendered (with Windows‑XP styling) on the live portfolio site.

### If you are the owner updating your profile
1. Edit the relevant markdown file here.
2. Update the matching hard‑coded data inside `src/components/*.vue`
   (e.g. `ProjectExplorer.vue`, `ExperienceExplorer.vue`,
   `EducationSection.vue`, `AboutSection.vue`, `ContactSection.vue`) so the
   site matches.
3. Bump the **Last reviewed** date at the top of this file.

## Conventions

- Dates use ISO‑8601 (`YYYY-MM-DD`) where exactness matters; human-friendly
  phrasing (e.g. "Aug 2025 – Feb 2026") elsewhere.
- Skill / technology names are written exactly as they would appear on a
  resume (e.g. "Spring Boot", "Vue.js", "PostgreSQL", "Scikit-learn").
- Each section file starts with a short summary so an LLM reading just the top
  of the file still gets useful context.
