# Public Assets & CV Directory

This directory contains static assets and LaTeX CVs for Musthofa Joko Anggoro's portfolio.

## 📄 For AI/LLM Agents Creating CVs

**Start here**: [`CV_GUIDE.md`](CV_GUIDE.md) - Comprehensive documentation for creating LaTeX CVs

**Template**: [`CV_TEMPLATE.tex`](CV_TEMPLATE.tex) - Reusable LaTeX CV template

## Directory Structure

```
public/
├── CV_GUIDE.md                        # AI/LLM documentation for CV creation
├── CV_TEMPLATE.tex                    # LaTeX CV template (START HERE for new CVs)
├── CV_TEMPLATE.pdf                    # Compiled template preview
├── CV_Musthofa Joko Anggoro.pdf      # General portfolio CV
├── phd-applications/                  # PhD/research position CVs
│   └── {university}-{program}-{year}/
│       ├── CV_Research_Musthofa_Joko_Anggoro.tex
│       └── CV_Research_Musthofa_Joko_Anggoro.pdf
├── internship-applications/           # Industry/internship CVs
│   └── {company}-{year}/
│       ├── CV_Musthofa_Joko_Anggoro_{Company}.tex
│       └── CV_Musthofa_Joko_Anggoro_{Company}.pdf
└── [other static assets]
```

## Quick Start for New CVs

```bash
# 1. Copy template
cp CV_TEMPLATE.tex internship-applications/company-2026/CV_Musthofa_Joko_Anggoro_Company.tex

# 2. Edit content for role

# 3. Compile (run twice)
cd internship-applications/company-2026/
pdflatex -interaction=nonstopmode CV_Musthofa_Joko_Anggoro_Company.tex
pdflatex -interaction=nonstopmode CV_Musthofa_Joko_Anggoro_Company.tex

# 4. Clean up
rm -f *.aux *.log *.out

# 5. Commit both .tex and .pdf
git add CV_Musthofa_Joko_Anggoro_Company.tex CV_Musthofa_Joko_Anggoro_Company.pdf
```

## Standard Header Format

All CVs use this header (for consistency and privacy):

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

**Note**: NO phone numbers in public CVs for privacy reasons.

## Data Sources

For accurate biographical information:

1. **Primary**: `../src/data/portfolio/*.json` (canonical source)
2. **Secondary**: `../docs/profile/*.md` (AI-readable summaries)

Never invent achievements, dates, or technologies not in these sources.

## Additional Resources

- **Copilot Instructions**: `../.github/copilot-instructions.md` - Section 7 covers LaTeX CVs
- **General Agent Guide**: `../AGENTS.md` - Cross-tool AI instructions
- **Profile Data**: `../docs/profile/` - Career information for CVs
