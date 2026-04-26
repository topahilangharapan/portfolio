# 📂 Profile — Career / Skill / Portfolio Data Center

This folder contains **AI-readable markdown generated from the canonical JSON source** in:

- `/src/data/portfolio/*.json`

> **Owner:** Musthofa Joko Anggoro
> **Handle:** [`@topahilangharapan`](https://github.com/topahilangharapan)
> **Role:** Full-Stack Developer · Software Engineer · CS Student at Universitas Indonesia
> **Last generated:** 2026-04-26

## Index

| File | Contents |
|------|----------|
| [`about.md`](about.md) | Personal summary, strengths, grouped technical skills |
| [`skills.md`](skills.md) | Full technical and soft skill inventory |
| [`education.md`](education.md) | University, GPA, coursework, achievements, summer program |
| [`experience.md`](experience.md) | Internships and organizational experience |
| [`projects.md`](projects.md) | Featured projects with role, stack, links, and outcomes |
| [`contact.md`](contact.md) | Email, social links, and availability |

## Source of truth

- **Canonical data source:** JSON under `/src/data/portfolio/`
- **Derived artifacts:** markdown files in this folder

## Update flow

1. Edit JSON in `/src/data/portfolio/`.
2. Run:
   `npm run sync:profile`
3. Commit both JSON and regenerated markdown files.

This keeps:
- Vue app data consumption (**JSON**)
- AI/LLM-friendly documentation (**markdown**)

in sync from one source.
