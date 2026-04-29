# Cover Letter Creation Guide for AI/LLM Agents

This guide gives any AI/LLM agent (GitHub Copilot, Claude, GPT, etc.) everything needed
to write a **tailored, HR-catching cover letter** for Musthofa Joko Anggoro from first
principles — no guessing, no filler, no generic templates.

Mirror of `CV_GUIDE.md` for cover letters. Read both when creating application materials.

## Table of Contents

1. [Quick Start](#1-quick-start)
2. [Anatomy of the Letter](#2-anatomy-of-the-letter-paragraph-by-paragraph-blueprint)
3. [Job-to-Profile Mapping Matrix](#3-job-to-profile-mapping-matrix)
4. [Voice & Tone Rules](#4-voice--tone-rules)
5. [Role-Type Customizations](#5-role-type-customizations)
6. [What HR Actually Reads](#6-what-hr-actually-reads-priority-order)
7. [Self-Review Checklist](#7-self-review-checklist)
8. [File & Directory Conventions](#8-file--directory-conventions)
9. [LaTeX Cover Letter Template & Compilation](#9-latex-cover-letter-template--compilation)
10. [Example Letter Skeletons](#10-example-letter-skeletons)

---

## 1. Quick Start

**Workflow for agents creating a new cover letter:**

```
Step 1 → Read the job description in full. Identify:
           - The top 1–2 technical requirements
           - The company's core mission / product area
           - Any keywords that appear more than once (mirror these)

Step 2 → Read profile data (in this order):
           docs/profile/experience.md      ← proof points and metrics
           docs/profile/projects.md        ← supplementary proof
           docs/profile/skills.md          ← technology specifics
           docs/profile/education.md       ← GPA, university, programs
           docs/profile/about.md           ← personality and framing

Step 3 → Read docs/profile/voice.md
           ← tone guardrails, forbidden phrases, opener patterns

Step 4 → Draft using the 4-paragraph blueprint in Section 2

Step 5 → Run the Self-Review Checklist in Section 7

Step 6 → Save Markdown draft alongside the matching CV:
           public/internship-applications/{company}-{year}/
             CoverLetter_Musthofa_Joko_Anggoro_{Company}.md

Step 7 → Create LaTeX source file (see Section 9):
           public/internship-applications/{company}-{year}/
             CoverLetter_Musthofa_Joko_Anggoro_{Company}.tex

Step 8 → Compile LaTeX to PDF (see Section 9):
           cd public/internship-applications/{company}-{year}/
           pdflatex -interaction=nonstopmode CoverLetter_Musthofa_Joko_Anggoro_{Company}.tex
           pdflatex -interaction=nonstopmode CoverLetter_Musthofa_Joko_Anggoro_{Company}.tex
           rm -f *.aux *.log *.out

Step 9 → Commit .md, .tex, and .pdf together
```

**Never skip Step 3.** Voice consistency is what makes the letter sound human.

---

## 2. Anatomy of the Letter (Paragraph-by-Paragraph Blueprint)

Target length: **300–400 words total**. Four paragraphs. No more, no less.

---

### P1 — Hook + Role Signal (2–3 sentences)

**Purpose:** Grab attention in the first sentence. Signal role awareness.

**Rules:**
- Open with a result, a story, or a curiosity hook — **never** with "I am writing to apply for…"
- Mirror 1–2 exact words or phrases from the job posting in this paragraph
- Name the company by name (not "your company")
- Include one proof point — a single sharp fact that earns the reader's trust immediately

**Structure:**
```
[Hook sentence: result / story / curiosity]
[Bridge: connect that hook to what {Company} is building]
[Signal: why this role specifically, in one tight sentence]
```

**Good example:**
> "Cutting manual booking intervention by 85% wasn't the original goal — building a
> resilient automation pipeline was. That experience is exactly what drew me to
> {Company}'s open role on the reliability engineering team: the problems are the same
> kind, just at a different scale."

**Bad example:**
> "I am writing to express my strong interest in the Software Engineer Intern position
> at {Company}. I believe I would be a great fit for your team."

---

### P2 — Strongest Proof (3–4 sentences)

**Purpose:** One story that directly maps to the top criterion in the job posting.
HR remembers one strong story far longer than five weak ones.

**Rules:**
- Use STAR-lite: Situation (1 sentence) → Action + technology (1–2 sentences) → Metric/outcome (1 sentence)
- Pull from `experience.md` first; use `projects.md` only if experience doesn't fit
- The technology named must appear in the job posting OR be an obvious analog
- Include at least one hard number (%, count, time, scale)

**Structure:**
```
[Situation: what problem existed, why it mattered]
[Action: what I specifically built/designed/led, with tech stack]
[Metric: the concrete outcome]
```

**Good example (maps to "automation / reliability" JD signal):**
> "At Traveloka, one of the largest flight inventory providers had no automated
> reschedule path — operators manually processed thousands of booking modifications
> daily. I built an end-to-end pipeline with configurable scrapers, failover backup
> mechanisms, and 99.9% processing accuracy, reducing manual intervention by 85%.
> The team now handles exceptions instead of repetition."

---

### P3 — Culture & Domain Fit (2–3 sentences)

**Purpose:** Prove you actually understand what the company does and why you
belong there — not just that you want a job.

**Rules:**
- Reference something specific about the company: a product area, a technical challenge,
  a recent initiative, or a value from their engineering blog / job posting
- Tie it back to a genuine interest from `about.md` (AI/ML, distributed systems,
  cloud, craftsmanship) — but show it, don't state it
- **Never write:** "I am passionate about…" — show the curiosity through a specific fact
  or question instead

**Structure:**
```
[What I know/understand about what {Company} is doing]
[Why that specific problem space connects to my genuine interests]
[Optional: a question or observation that signals depth of thinking]
```

**Good example:**
> "{Company}'s move toward real-time personalization at the infrastructure layer is
> exactly the kind of problem that keeps me up — I spent the last eight months building
> structured logging pipelines into BigQuery to make that kind of insight possible at
> Traveloka. The gap between raw event streams and actionable dashboards is where I
> find the most interesting engineering decisions."

---

### P4 — Closing + CTA (2 sentences)

**Purpose:** End with forward momentum, not gratitude.

**Rules:**
- Do NOT end with "Thank you for your time and consideration"
- Express anticipation or curiosity about a specific aspect of the role/team
- Keep it tight — 2 sentences maximum

**Structure:**
```
[Forward-looking statement: what I'd like to discuss / explore]
[Implicit or explicit CTA: I'm available / I'm looking forward to it]
```

**Good example:**
> "I'd welcome the chance to talk through how the automation pipeline approach maps to
> {Company}'s scale — and whether the team's thinking on failover strategies aligns
> with what I ran into at Traveloka. Happy to make time whenever works for you."

**Bad example:**
> "Thank you for considering my application. I hope to hear from you soon and look
> forward to the opportunity to discuss my qualifications further."

---

## 3. Job-to-Profile Mapping Matrix

When you see a signal in the job posting, pull from these specific profile assets.
**Always prefer `experience.md` over `projects.md`.** Projects supplement; experience proves.

| Job Posting Signal | Best Profile Asset to Use | Key Stat / Detail |
|--------------------|--------------------------|-------------------|
| automation / efficiency / scale | Traveloka — reschedule pipeline | 85% reduction in manual intervention, 99.9% accuracy, thousands of daily modifications |
| reliability / high availability | Traveloka — Account Authentication service | configurable scrapers, failover backup, high availability design |
| AI tooling / developer productivity | Traveloka — GitHub Copilot CLI usage | "significantly enhanced development velocity, code quality, and automated testing" |
| security / secrets management | Traveloka — Credential Management System | AES-GCM encryption, automated rotation snapshots, granular audit logging, MongoDB |
| CI/CD / DevOps / testing | Traveloka — Karate pipelines | automated API testing integration, auto-rollback logic, production defect prevention |
| data pipelines / analytics | Traveloka — BigQuery logging | real-time data sync, structured logging for BigQuery analytics dashboards |
| backend / language agnostic | Traveloka (Java) + Magna (Spring Boot/Angular) + projects (Django/Vue/TypeScript) | 4 production languages: Java, Python, TypeScript, Go |
| full-stack / frontend + backend | PT Magna Solusi Indonesia | Spring Boot + Angular + PostgreSQL, RESTful APIs, Docker/Kubernetes |
| database / query optimization | PT Magna Solusi Indonesia + Marmut project | efficient query design, manual SQL, triggers, stored procedures |
| ML / data science | Used Car Sales Prediction project | Gradient Boosting, Random Forest, imbalanced classification, scikit-learn |
| leadership / team management | COMPFEST Vice PIC UI/UX | 11-person design team, 5 sprints, cross-functional stakeholder alignment |
| design systems / UI/UX | COMPFEST + PathFinder project | design system leadership, dark/light mode, component libraries, usability testing |
| enterprise systems | Enterprise Information System project | Lead Engineer, Spring Boot + Vue.js + PostgreSQL, Docker, JWT auth |
| academic excellence | University of Indonesia, Fasilkom | GPA 3.84/4.00, Information Systems, expected graduation June–August 2026 |
| international / research exposure | NTU Summer Program 2025 | LPDP Scholarship Awardee, NTU Singapore + ITS Surabaya, sustainability + tech |
| mentoring / teaching | Programming Foundations 0 | Mentor role, University of Indonesia |

---

## 4. Voice & Tone Rules

> **Full voice guide:** `docs/profile/voice.md` — read it before drafting.

### Summary of non-negotiables

- **Voice:** First-person, active, direct. No passive constructions.
- **Tone dial:** Confident (8/10), slightly informal (3/10) — warm but professional.
- **Every claim needs a noun:** a technology, a company, a number, or a name.
- **Max 400 words.** If it's longer, cut the weakest sentence in each paragraph.

### Hard-forbidden phrases

Never let any of these appear in the final draft:

- "I am writing to apply for…" / "I am pleased to submit my application…"
- "passionate about"
- "I am a quick learner" / "I am a hard worker" / "I am a team player"
- "responsible for" (use action verbs: engineered, built, led, designed)
- "leverage my skills"
- "synergize" / "synergy"
- "dynamic environment"
- "I believe I would be a great fit"
- "Thank you for your time and consideration"
- "To Whom It May Concern"

### Preferred opener patterns (in order)

1. **Result-first:** Lead with the outcome, then reveal the context
2. **Curiosity-first:** Lead with the intellectual problem that drew him in
3. **Story-first:** Open with a specific decision or moment
4. **Company-mirroring:** Reflect a phrase from the job posting directly back

---

## 5. Role-Type Customizations

Pick **one mode** based on the job type. Adjust emphasis in P1, P2, and P3 accordingly.

---

### Mode A: AI / Startup / Tech-Forward

**JD signals:** "move fast", "ship", "LLM", "AI tooling", "growth", "0→1"

| Section | Emphasis |
|---------|----------|
| P1 Hook | Lead with a shipped product moment or a curiosity observation about AI/automation |
| P2 Proof | Traveloka automation pipeline OR GitHub Copilot CLI productivity story |
| P3 Fit | Genuine AI/ML enthusiasm from `about.md`; reference speed-to-impact or agentic tooling |
| P4 CTA | Reference the specific AI/product problem you'd want to work on |

**Tone:** Slightly more energetic and informal. Show that you experiment for fun, not just work.

---

### Mode B: Enterprise / Industrial / Regulated

**JD signals:** "reliability", "compliance", "audit", "security", "microservices", "enterprise"

| Section | Emphasis |
|---------|----------|
| P1 Hook | Lead with scale, reliability, or a security outcome |
| P2 Proof | AES-GCM Credential Management System OR reschedule pipeline at 99.9% accuracy |
| P3 Fit | Understanding of what it takes to operate at enterprise scale; reference audit logging, failover |
| P4 CTA | Reference the team's specific reliability or security challenge |

**Tone:** More precise and measured. Let the metrics carry the confidence.

---

### Mode C: Research / PhD / Academic

**JD signals:** "research", "PhD", "systems", "architecture", "publications", "thesis"

| Section | Emphasis |
|---------|----------|
| P1 Hook | Lead with an intellectual framing — a question or observation, not a product metric |
| P2 Proof | NTU Summer Program + academic ML project + coursework depth |
| P3 Fit | Reference computer architecture, distributed systems curiosity; GPA 3.84, Fasilkom UI |
| P4 CTA | Express a specific research question you'd want to explore with the group |

**Tone:** More thoughtful, slightly slower pacing. Show methodology curiosity, not just output.

---

## 6. What HR Actually Reads (Priority Order)

Understanding this shapes how much effort to spend on each section.

| Priority | What HR checks | Agent implication |
|----------|---------------|-------------------|
| 🥇 1st | **First sentence** — does it grab attention? | Spend the most revision effort on P1 sentence 1 |
| 🥈 2nd | **Single best proof point** — specific and credible? | P2 must have a metric; vague bullets get skipped |
| 🥉 3rd | **Company/role fit signal** — did they read our JD? | P3 must reference something specific to this company |
| 4th | **Tone match** — would I want to work with this person? | Check against `voice.md` before finalizing |
| 5th | Length — is it respectful of my time? | Cut to ≤400 words before submitting |

**Implication:** P1 and P2 are worth 70% of the letter's impact. If time-constrained,
polish those two paragraphs above all else.

---

## 7. Self-Review Checklist

Run this **before** saving the final file. Every box must be checked.

**Content**
- [ ] Opening sentence does NOT start with "I am writing to apply for…" or any variant
- [ ] At least one specific metric or outcome is cited (%, count, time, scale)
- [ ] At least one word or phrase is mirrored directly from the job posting
- [ ] The company is named by name at least once (not "your company" or "your organization")
- [ ] P3 references something specific about the company — not a generic mission statement

**Accuracy**
- [ ] Every claimed fact, technology, and metric is traceable to `docs/profile/` or `src/data/portfolio/`
- [ ] No technologies or roles are invented or exaggerated
- [ ] Dates and durations match `experience.md` and `education.md`

**Voice**
- [ ] None of the forbidden phrases appear (Section 4)
- [ ] Closing does NOT end with "Thank you for your time and consideration"
- [ ] First-person, active voice throughout (grep for "was responsible for", "was involved in")

**Format**
- [ ] Word count is ≤ 400 words (count programmatically if unsure)
- [ ] Four paragraphs (P1 through P4) — no bullet points in the letter body
- [ ] Saved as `CoverLetter_Musthofa_Joko_Anggoro_{Company}.md` in the correct directory
- [ ] Placed alongside the matching CV file for that application

**LaTeX & PDF**
- [ ] LaTeX source created as `CoverLetter_Musthofa_Joko_Anggoro_{Company}.tex` (see Section 9)
- [ ] PDF compiled with `pdflatex` (run twice): output shows `(1 page, XXXXX bytes)`
- [ ] Auxiliary files removed (`*.aux`, `*.log`, `*.out`)
- [ ] All three files (`.md`, `.tex`, `.pdf`) committed together

---

## 8. File & Directory Conventions

### Directory structure

```
public/
├── COVER_LETTER_GUIDE.md           ← this file
├── CV_GUIDE.md                     ← CV creation guide
├── CV_TEMPLATE.tex                 ← CV LaTeX template
├── internship-applications/
│   └── {company}-{year}/
│       ├── CV_Musthofa_Joko_Anggoro_{Company}.tex
│       ├── CV_Musthofa_Joko_Anggoro_{Company}.pdf
│       ├── CoverLetter_Musthofa_Joko_Anggoro_{Company}.md   ← Markdown draft
│       ├── CoverLetter_Musthofa_Joko_Anggoro_{Company}.tex  ← LaTeX source
│       └── CoverLetter_Musthofa_Joko_Anggoro_{Company}.pdf  ← compiled PDF
└── phd-applications/
    └── {university}-{program}-{year}/
        ├── CV_Research_Musthofa_Joko_Anggoro.tex
        ├── CV_Research_Musthofa_Joko_Anggoro.pdf
        ├── CoverLetter_Musthofa_Joko_Anggoro_{University}.md
        ├── CoverLetter_Musthofa_Joko_Anggoro_{University}.tex
        └── CoverLetter_Musthofa_Joko_Anggoro_{University}.pdf
```

### Naming convention

| Application type | Cover letter filenames (all three) |
|------------------|------------------------------------|
| Internship | `CoverLetter_Musthofa_Joko_Anggoro_{CompanyName}.{md\|tex\|pdf}` |
| PhD / Research | `CoverLetter_Musthofa_Joko_Anggoro_{UniversityName}.{md\|tex\|pdf}` |
| General | `CoverLetter_Musthofa_Joko_Anggoro.{md\|tex\|pdf}` |

### What to commit

Always commit all three cover letter files alongside their matching CV files.

```bash
git add public/internship-applications/{company}-{year}/CoverLetter_Musthofa_Joko_Anggoro_{Company}.md
git add public/internship-applications/{company}-{year}/CoverLetter_Musthofa_Joko_Anggoro_{Company}.tex
git add public/internship-applications/{company}-{year}/CoverLetter_Musthofa_Joko_Anggoro_{Company}.pdf
git add public/internship-applications/{company}-{year}/CV_Musthofa_Joko_Anggoro_{Company}.tex
git add public/internship-applications/{company}-{year}/CV_Musthofa_Joko_Anggoro_{Company}.pdf
git commit -m "Add application materials for {Company} {Year}"
```

---

## 9. LaTeX Cover Letter Template & Compilation

Every cover letter **must** be created as both a Markdown draft (`.md`) and a compiled
LaTeX PDF (`.tex` + `.pdf`). The LaTeX version is the document you actually submit.

---

### Installation

```bash
# Ubuntu/Debian (CI/sandboxed environments — e.g. GitHub Copilot agent)
sudo apt-get update
sudo apt-get install -y texlive-latex-base texlive-latex-extra \
     texlive-fonts-recommended texlive-fonts-extra

# macOS
brew install --cask mactex          # full distribution
# or: brew install --cask basictex  # lighter alternative
```

---

### LaTeX template structure

A cover letter `.tex` file should follow this skeleton exactly.
Use the packages already proven to work: `geometry`, `hyperref`, `xcolor`,
`fontawesome5`, `parskip`.

```latex
\documentclass[11pt,a4paper]{article}
\usepackage[top=0.75in, bottom=0.75in, left=0.85in, right=0.85in]{geometry}
\usepackage{hyperref}
\usepackage{xcolor}
\usepackage{fontawesome5}
\usepackage{parskip}

\definecolor{darkblue}{RGB}{0,51,102}
\hypersetup{colorlinks=true, urlcolor=darkblue,
    pdftitle={Cover Letter - Musthofa Joko Anggoro - {Company}},
    pdfauthor={Musthofa Joko Anggoro}}

\pagestyle{empty}
\setlength{\parindent}{0pt}
\setlength{\parskip}{10pt}

\begin{document}

% ── HEADER ──────────────────────────────────────────────────
\begin{center}
    {\LARGE \textbf{MUSTHOFA JOKO ANGGORO}} \\[4pt]
    \small
    \faEnvelope\ \href{mailto:musthofaja.topa@gmail.com}{musthofaja.topa@gmail.com}
    \ $|$ \
    \faLinkedin\ \href{https://www.linkedin.com/in/musthofa-joko-anggoro/}{linkedin.com/in/musthofa-joko-anggoro}
    \ $|$ \
    \faGithub\ \href{https://github.com/topahilangharapan}{github.com/topahilangharapan}
    \ $|$ \
    \faGlobe\ \href{https://portfolio-topahilangharapan-personal.vercel.app/}{portfolio-topahilangharapan-personal.vercel.app}
\end{center}

\vspace{4pt}\hrule\vspace{14pt}

% ── DATE & SALUTATION ────────────────────────────────────────
{Month Day, Year}

\vspace{6pt}
Hiring Team \\
{Company Name} \\
{City, Country}

\vspace{6pt}
Dear {Company Name} Hiring Team,

% ── P1 HOOK ──────────────────────────────────────────────────
{P1 paragraph — result/curiosity hook, company named, role signal}

% ── P2 PROOF ─────────────────────────────────────────────────
{P2 paragraph — STAR-lite story with hard number}

% ── P3 FIT ───────────────────────────────────────────────────
{P3 paragraph — specific company reference + genuine interest}

% ── P4 CTA ───────────────────────────────────────────────────
{P4 paragraph — forward momentum, no "Thank you for your time"}

\vspace{10pt}
Sincerely,

\vspace{18pt}
\textbf{Musthofa Joko Anggoro}

% ── FOOTER ───────────────────────────────────────────────────
\vspace{10pt}\hrule\vspace{6pt}
\footnotesize
\textit{University of Indonesia, Fasilkom\ $\cdot$\ Information Systems\ $\cdot$\
GPA 3.84/4.00\ $\cdot$\ Expected graduation June--August 2026}

\end{document}
```

**Key rules for the `.tex` file:**
- Match the header exactly (same icons and links as the CV template)
- Use `---` in LaTeX as `---` (em-dash: `---`) inside text blocks
- Escape special LaTeX characters: `%` → `\%`, `&` → `\&`, `_` → `\_`, `#` → `\#`
- Keep the footer with academic credentials — it fills the page naturally and adds credibility

---

### Compilation commands

```bash
# Navigate to the application directory
cd public/internship-applications/{company}-{year}/
# (or phd-applications/{university}-{program}-{year}/)

# Compile — must run TWICE to resolve cross-references and hyperlinks
pdflatex -interaction=nonstopmode CoverLetter_Musthofa_Joko_Anggoro_{Company}.tex
pdflatex -interaction=nonstopmode CoverLetter_Musthofa_Joko_Anggoro_{Company}.tex

# Verify: expected output on second run
# "Output written on CoverLetter_Musthofa_Joko_Anggoro_{Company}.pdf (1 page, XXXXX bytes)"

# Clean up auxiliary files (do not commit these)
rm -f CoverLetter_Musthofa_Joko_Anggoro_{Company}.aux \
      CoverLetter_Musthofa_Joko_Anggoro_{Company}.log \
      CoverLetter_Musthofa_Joko_Anggoro_{Company}.out
```

---

### Post-compilation checklist

- [ ] PDF compiles without errors (exit code 0)
- [ ] Output confirms exactly **1 page**
- [ ] All hyperlinks are clickable (email, LinkedIn, GitHub, portfolio)
- [ ] Auxiliary files removed (`*.aux`, `*.log`, `*.out`)
- [ ] `.md`, `.tex`, and `.pdf` all committed in the same commit

---

## 10. Example Letter Skeletons

These are fill-in-the-blank starting points. Replace all `{placeholders}` with real content
from the mapping matrix (Section 3) and the job posting.

---

### Skeleton A: AI / Startup Role

```markdown
{Result or curiosity hook tied to AI/automation}. {Company}'s work on {specific product/problem}
is exactly the context where that kind of thinking compounds — {one-sentence role signal}.

At Traveloka, {situation in one sentence}. I {action: built/designed/engineered} {specific system}
using {technology from JD or analog}, {brief mechanism}, resulting in {metric}. {One-sentence
human/business impact}.

What draws me to {Company} specifically is {something concrete about their tech/mission/product} —
{tie to genuine interest from about.md without saying "passionate about"}. {Optional: a question
or observation that shows depth}.

I'd welcome the chance to {specific topic to discuss related to role}. {Forward-momentum closing,
no thanks}.
```

---

### Skeleton B: Enterprise / Regulated Role

```markdown
{Scale or reliability hook with a metric}. {Company}'s focus on {compliance/security/enterprise
area} is the kind of environment where that matters most — {one-sentence role signal}.

{Situation: the problem that existed at Traveloka or Magna}. I {action: engineered/built/led}
{specific system — e.g., AES-GCM Credential Management System}, {brief mechanism — encryption,
audit logging, failover}, {metric or observable outcome}. {One-sentence business impact}.

{Company}'s {specific product domain or compliance challenge} maps closely to {what I built/saw} —
{observation that shows you understand their problem space}. {Tie to craftsmanship or reliability
interest from about.md without filler phrases}.

I'd welcome the chance to discuss {specific reliability or security challenge relevant to role}.
{Forward-momentum closing}.
```

---

### Skeleton C: Research / PhD Application

```markdown
{Intellectual observation or question that frames the research area}. {University/Lab}'s work on
{specific research direction} is where I think the most interesting open questions currently sit —
{one-sentence signal of why this specific program}.

{Relevant experience or project that demonstrates research-adjacent thinking}. I {action: built/
designed/analyzed} {specific work}, {mechanism}, {outcome or insight gained}. {Why that experience
sharpened a specific research question}.

{University/Lab}'s approach to {methodology or research question} connects directly to my
coursework in {relevant course from education.md} and the questions I've been sitting with since
{specific experience}. {GPA 3.84 / Fasilkom UI / NTU Summer Program as credibility anchor
if appropriate}.

I'd welcome the chance to discuss {specific research question or paper from the lab}. {Forward-
momentum closing}.
```

---

## Best Practices for AI Agents

1. **Always read `voice.md` before drafting** — tone consistency is what makes the letter human
2. **One story beats five** — resist the urge to mention every project; P2 gets one story only
3. **Mirror the JD language** — use the mapping matrix to match signals to assets precisely
4. **Count words before finalizing** — run `wc -w` on the file; cut if over 400
5. **Never invent facts** — if a claim isn't in `docs/profile/` or `src/data/portfolio/`, cut it
6. **Re-read P1 sentence 1 last** — it's the highest-leverage sentence; refine it after drafting the rest
7. **Always produce all three artefacts** — `.md` draft, `.tex` source, and compiled `.pdf`; commit them together
8. **Run pdflatex twice** — the second pass resolves hyperlinks and outlines correctly
9. **Clean aux files** — never commit `*.aux`, `*.log`, or `*.out`

---

**Last Updated:** April 2026
**Maintained By:** AI/LLM Agents
**Related Files:** `public/CV_GUIDE.md` · `docs/profile/voice.md` · `docs/profile/experience.md`
