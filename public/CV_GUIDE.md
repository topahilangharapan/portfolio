# CV Creation Guide for AI/LLM Agents

This guide provides comprehensive instructions for AI/LLM agents (GitHub Copilot, Claude, GPT, etc.) to create professional LaTeX CVs in this repository.

## Table of Contents

1. [Quick Start](#quick-start)
2. [Installation Requirements](#installation-requirements)
3. [Template Overview](#template-overview)
4. [Directory Structure](#directory-structure)
5. [Compilation Workflow](#compilation-workflow)
6. [Customization Guidelines](#customization-guidelines)
7. [Common Patterns](#common-patterns)
8. [Troubleshooting](#troubleshooting)

---

## Quick Start

**For AI agents creating a new CV:**

1. Copy `public/CV_TEMPLATE.tex` to your target directory (e.g., `public/internship-applications/{company}-{year}/`)
2. Rename to: `CV_Musthofa_Joko_Anggoro_{Company}.tex`
3. Customize content sections based on role requirements
4. Compile using: `pdflatex -interaction=nonstopmode {filename}.tex`
5. Run twice for proper cross-references
6. Clean up auxiliary files: `rm *.aux *.log *.out`

---

## Installation Requirements

### For Ubuntu/Debian-based Systems

```bash
# Update package list
sudo apt-get update

# Install LaTeX distribution
sudo apt-get install -y texlive-latex-base texlive-latex-extra texlive-fonts-recommended texlive-fonts-extra

# Verify installation
pdflatex --version
```

### For macOS

```bash
# Using Homebrew
brew install --cask mactex

# Or install BasicTeX (smaller)
brew install --cask basictex
sudo tlmgr update --self
sudo tlmgr install collection-fontsrecommended
```

### For GitHub Actions / CI/CD

```yaml
- name: Install LaTeX
  run: |
    sudo apt-get update
    sudo apt-get install -y texlive-latex-base texlive-latex-extra texlive-fonts-recommended texlive-fonts-extra
```

### Required LaTeX Packages

The template uses the following packages (included in `texlive-latex-extra`):

- `geometry` - Page margins and layout
- `enumitem` - List customization
- `hyperref` - Clickable links
- `titlesec` - Section formatting
- `xcolor` - Color definitions
- `fontawesome5` - Icons (email, LinkedIn, GitHub, etc.)

---

## Template Overview

The `CV_TEMPLATE.tex` follows this structure:

```latex
\documentclass[10pt,a4paper]{article}

% Preamble
% - Package imports
% - Color definitions
% - Hyperref setup
% - Section formatting
% - Custom commands

\begin{document}

% Header (Name + Contact Info)
% Education Section
% Work Experience Section
% Projects Section
% Technical Skills Section
% Leadership & Activities Section

\end{document}
```

---

## Directory Structure

```
public/
├── CV_TEMPLATE.tex                    # Base template (START HERE)
├── CV_GUIDE.md                        # This guide
├── CV_Musthofa Joko Anggoro.pdf      # General portfolio CV
├── phd-applications/
│   └── {university}-{program}-{year}/
│       ├── CV_Research_Musthofa_Joko_Anggoro.tex
│       └── CV_Research_Musthofa_Joko_Anggoro.pdf
└── internship-applications/
    └── {company}-{year}/
        ├── CV_Musthofa_Joko_Anggoro_{Company}.tex
        └── CV_Musthofa_Joko_Anggoro_{Company}.pdf
```

### Naming Conventions

- **PhD/Research CVs**: `CV_Research_Musthofa_Joko_Anggoro.tex`
- **Company CVs**: `CV_Musthofa_Joko_Anggoro_{CompanyName}.tex`
- **General CV**: `CV_Musthofa Joko Anggoro.tex`

---

## Compilation Workflow

### Basic Compilation

```bash
# Navigate to CV directory
cd public/internship-applications/company-2026/

# Compile (run twice for proper cross-references)
pdflatex -interaction=nonstopmode CV_Musthofa_Joko_Anggoro_Company.tex
pdflatex -interaction=nonstopmode CV_Musthofa_Joko_Anggoro_Company.tex

# Clean up auxiliary files
rm -f *.aux *.log *.out

# Verify output
ls -lh *.pdf
```

### Silent Compilation (for CI/CD)

```bash
# Suppress all output except errors
pdflatex -interaction=nonstopmode CV_file.tex >/dev/null 2>&1

# Check compilation status
if [ $? -eq 0 ]; then
    echo "✓ PDF compiled successfully"
else
    echo "✗ Compilation failed"
    exit 1
fi
```

### Verify Page Count

```bash
# Check if CV is 1 page (recommended for most positions)
pdflatex -interaction=nonstopmode CV_file.tex 2>&1 | grep -E "Output written.*pages"

# Expected output: "Output written on CV_file.pdf (1 page, XXXXX bytes)"
```

---

## Customization Guidelines

### 1. Header Customization

The standard header format (use this consistently):

```latex
% Header
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

**DO NOT** include phone numbers in public CVs (privacy).

### 2. Section Ordering

**For Industry/Internship Positions:**
1. Education
2. Work Experience
3. Projects (if relevant to role)
4. Technical Skills
5. Leadership & Activities

**For PhD/Research Positions:**
1. Research Interests (statement)
2. Education
3. Experience (Research + Industry)
4. Skills (Systems-focused)
5. Research & Technical Projects
6. Publications (if any)
7. Leadership & Activities

### 3. Experience Entry Format

Use the custom `\experienceheader` command:

```latex
\experienceheader{Position/Company}{Location}{Role/Description}{Date Range}
\begin{itemize}[leftmargin=*, itemsep=1pt, topsep=1pt]
    \item Achievement-oriented bullet with metrics and impact
    \item Technical implementation details with specific technologies
    \item Outcome-focused description with quantifiable results
\end{itemize}
```

### 4. Bullet Point Style

✓ **Good bullets** (Action + Technology + Impact):
- "Engineered secure Credential Management System with AES-GCM encryption and MongoDB, reducing security incidents by 90%"
- "Optimized PostgreSQL database performance through indexing strategies, reducing average response time by 35%"

✗ **Bad bullets** (Vague, no metrics):
- "Worked on backend systems"
- "Helped with database optimization"

### 5. Skills Section Formatting

Group skills by category with clear separators:

```latex
\textbf{Languages \& Frameworks:} Java, Python, TypeScript $|$ Spring Boot, Vue.js, Angular \\
\textbf{Databases:} PostgreSQL, MongoDB, Oracle Database, BigQuery \\
\textbf{Cloud \& DevOps:} Docker, Kubernetes, CI/CD pipelines, AWS, Terraform \\
\textbf{Specialized:} [Role-specific skills here]
```

---

## Common Patterns

### Pattern 1: Tailoring for Specific Roles

**Manufacturing/Industrial Automation (e.g., Baker Hughes):**
- Emphasize: Oracle Database, enterprise systems, automation, microservices
- Projects: Enterprise Information Systems, automation tools
- Skills: Oracle Integration Cloud, RESTful APIs, CI/CD

**Research/PhD Programs:**
- Emphasize: Computer architecture, systems, research projects
- Include: Research interests statement, thesis work, publications
- Skills: FPGA, VHDL, distributed systems, OS internals

### Pattern 2: Length Optimization

**Target: 1 page for most positions, 2 pages for senior/research**

To reduce length:
1. Remove or condense less relevant experience
2. Limit bullets to 2-3 per position
3. Remove entire sections (e.g., Projects if work experience is strong)
4. Use compact formatting: `\vspace{-Xpt}` between sections

### Pattern 3: Color Customization

Default colors defined in preamble:

```latex
\definecolor{darkblue}{RGB}{0,51,102}      % Section headers
\definecolor{mediumgray}{RGB}{80,80,80}    % Secondary text
```

To change, modify RGB values. Keep professional colors (blues, grays, blacks).

---

## Troubleshooting

### Issue: "File not found" errors

```bash
# Check if all required packages are installed
sudo apt-get install -y texlive-latex-extra texlive-fonts-extra

# Verify fontawesome5 is available
kpsewhich fontawesome5.sty
```

### Issue: PDF exceeds 1 page

**Solutions:**
1. Reduce bullet points per experience (max 3)
2. Remove less relevant sections
3. Adjust spacing: `\vspace{-10pt}` after header
4. Use `\setlength{\itemsep}{0pt}` for tighter lists
5. Consider `[margin=0.4in]` in geometry (minimum recommended)

### Issue: Broken links in PDF

```latex
% Ensure hyperref setup is correct
\hypersetup{
    colorlinks=true,
    linkcolor=darkblue,
    urlcolor=darkblue,
    pdftitle={CV - Musthofa Joko Anggoro},
    pdfauthor={Musthofa Joko Anggoro}
}
```

### Issue: Icons not displaying

```bash
# Install fontawesome5 package
sudo apt-get install -y texlive-fonts-extra

# Or use alternative syntax
\faIcon{envelope} instead of \faEnvelope
```

### Issue: Compilation hangs

```bash
# Use non-interactive mode
pdflatex -interaction=nonstopmode file.tex

# Or batch mode (suppresses most output)
pdflatex -interaction=batchmode file.tex
```

---

## Best Practices for AI Agents

1. **Always read profile data first**: Check `docs/profile/*.md` or `src/data/portfolio/*.json` for accurate biographical information

2. **Use the template**: Start with `CV_TEMPLATE.tex`, don't create from scratch

3. **Compile twice**: LaTeX needs two passes for cross-references and proper formatting

4. **Verify page count**: Most positions expect 1-page CVs

5. **Clean up files**: Remove `.aux`, `.log`, `.out` files before committing

6. **Test locally if possible**: Compile and visually inspect PDF before pushing

7. **Consistent header**: Always use the standard header format (no phone numbers)

8. **Quantify achievements**: Include metrics (percentages, time saved, scale) in bullets

9. **Tailor content**: Adjust sections and emphasis based on job requirements

10. **Commit both .tex and .pdf**: Always version control both source and output

---

## Example Workflow for Creating a New CV

```bash
# 1. Create directory structure
mkdir -p public/internship-applications/example-company-2026
cd public/internship-applications/example-company-2026

# 2. Copy template
cp ../../CV_TEMPLATE.tex CV_Musthofa_Joko_Anggoro_Example.tex

# 3. Edit content (customize for role)
# [Agent edits file here]

# 4. Compile PDF
pdflatex -interaction=nonstopmode CV_Musthofa_Joko_Anggoro_Example.tex
pdflatex -interaction=nonstopmode CV_Musthofa_Joko_Anggoro_Example.tex

# 5. Verify output
ls -lh *.pdf
pdfinfo CV_Musthofa_Joko_Anggoro_Example.pdf | grep Pages

# 6. Clean auxiliary files
rm -f *.aux *.log *.out

# 7. Commit changes
git add CV_Musthofa_Joko_Anggoro_Example.tex
git add CV_Musthofa_Joko_Anggoro_Example.pdf
git commit -m "Add CV for Example Company internship application"
```

---

## Quick Reference Commands

```bash
# Install LaTeX (Ubuntu)
sudo apt-get install -y texlive-latex-base texlive-latex-extra texlive-fonts-recommended texlive-fonts-extra

# Compile CV
pdflatex -interaction=nonstopmode CV_file.tex

# Check PDF pages
pdflatex CV_file.tex 2>&1 | grep "Output written"

# Clean auxiliary files
rm -f *.aux *.log *.out

# Find all CVs
find public/ -name "*.tex" -type f

# Batch compile all CVs
find public/ -name "*.tex" -type f -exec pdflatex -interaction=nonstopmode {} \;
```

---

## Additional Resources

- **LaTeX Documentation**: https://www.latex-project.org/help/documentation/
- **Overleaf CV Templates**: https://www.overleaf.com/gallery/tagged/cv
- **Font Awesome Icons**: https://fontawesome.com/icons
- **Repository Profile Data**: `docs/profile/` directory for biographical facts

---

**Last Updated**: April 2026  
**Maintained By**: AI/LLM Agents  
**Questions?**: Refer to `.github/copilot-instructions.md` for additional context
