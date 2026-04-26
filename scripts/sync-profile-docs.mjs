import { promises as fs } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const repoRoot = path.resolve(__dirname, '..');
const dataDir = path.join(repoRoot, 'src', 'data', 'portfolio');
const docsDir = path.join(repoRoot, 'docs', 'profile');

const readJson = async (name) => {
  const raw = await fs.readFile(path.join(dataDir, `${name}.json`), 'utf8');
  return JSON.parse(raw);
};

const bullets = (items) => items.map((item) => `- ${item}`).join('\n');
const dateNow = () => new Date().toISOString().slice(0, 10);

const mdHeader = (title) => `${title}\n\n> ⚠️ This file is auto-generated from JSON in \`/src/data/portfolio/\`.\n> Edit JSON, then run \`npm run sync:profile\`.\n\n`;

const joinRepoLines = (githubLink) => {
  if (!githubLink || githubLink === 'none') return '- Repo / demo: Not public';
  if (Array.isArray(githubLink)) return githubLink.map((repo) => `- ${repo.name}: ${repo.url}`).join('\n');
  return `- Repo: ${githubLink}`;
};

const titleCase = (value) => value.charAt(0).toUpperCase() + value.slice(1);

const generateAbout = (about) => `${mdHeader('# 👤 About')}## Personal summary\n\n${about.professionalSummary.join('\n\n')}\n\n## Core strengths\n\n${bullets(about.coreStrengths)}\n\n## Technical skill groups\n\n${about.technicalSkills
  .map((group) => `### ${group.title}\n\n${bullets(group.items)}`)
  .join('\n\n')}\n\n## Additional information\n\n${about.additionalInfo
  .map((item) => `- **${item.title.replace(/^.+?\s/, '')}:** ${item.value}`)
  .join('\n')}\n`;

const generateSkills = (skills) => `${mdHeader('# 🛠 Skills')}> **Summary:** ${skills.summary}\n\n## Programming languages\n\n${bullets(skills.programmingLanguages)}\n\n## Frameworks\n\n- **Frontend:** ${skills.frameworks.frontend.join(', ')}\n- **Backend:** ${skills.frameworks.backend.join(', ')}\n\n## Databases & tools\n\n${bullets(skills.databasesAndTools)}\n\n## Operating systems\n\n${bullets(skills.operatingSystems)}\n\n## AI / ML\n\n${bullets(skills.aiMl)}\n\n## UI / UX & design\n\n${bullets(skills.uiUxAndDesign)}\n\n## Other engineering practices\n\n${bullets(skills.otherEngineeringPractices)}\n\n## Soft skills\n\n${bullets(skills.softSkills)}\n`;

const generateEducation = (education) => `${mdHeader('# 🎓 Education')}> **Summary:** ${education.degree} (${education.major}) at ${education.university}, ${education.faculty}, GPA ${education.gpa.toFixed(2)} / ${education.maxGpa.toFixed(2)}.\n\n## University\n\n| Field | Value |\n|------|-------|\n| University | ${education.university} |\n| Faculty | ${education.faculty} |\n| Degree | ${education.degree} |\n| Major | ${education.major} |\n| Current status | ${education.currentSemester} |\n| Expected graduation | ${education.expectedGraduation} |\n| GPA | **${education.gpa.toFixed(2)} / ${education.maxGpa.toFixed(2)}** |\n| Academic year | ${education.statusBarAcademicYear} |\n\n## Relevant coursework\n\n${bullets(education.relevantCourses)}\n\n### Categorized\n\n${education.courseCategories
  .map((category) => `- **${category.title.replace(/^.+?\s/, '').replace(/\s+/g, ' ').trim()}:** ${category.items.join(', ')}`)
  .join('\n')}\n\n## Achievements\n\n${bullets(education.achievements)}\n\n## Summer program\n\n| Field | Value |\n|------|-------|\n| Program | ${education.summerProgram.title} |\n| Status | **${education.summerProgram.status}** |\n| Institutions | ${education.summerProgram.institutions} |\n| Focus | ${education.summerProgram.focus} |\n| Description | ${education.summerProgram.description} |\n`;

const generateExperience = (experiences) => `${mdHeader('# 💼 Experience')}> **Summary:** Experience records generated from structured JSON for portfolio and AI/LLM consumption.\n\n---\n\n${experiences
  .map(
    (exp, index) => `## ${index + 1}. ${exp.role} · ${exp.company}\n\n| Field | Value |\n|------|-------|\n| Type | ${exp.type} |\n| Location | ${exp.location} |\n| Duration | ${exp.dateCreated} – ${exp.dateModified} (${exp.duration}) |\n| Icon | ${exp.icon} |\n\n### Achievements\n${bullets(exp.achievements)}\n\n### Technologies\n${exp.technologies.join(' · ')}`
  )
  .join('\n\n---\n\n')}\n`;

const generateProjects = (projects) => `${mdHeader('# 🚀 Projects')}> **Summary:** Project records generated from structured JSON for portfolio and AI/LLM consumption.\n\n---\n\n${projects
  .map(
    (project, index) => `## ${index + 1}. ${project.icon} ${project.title}\n\n- **Role:** ${project.role}\n- **Type / Category:** ${project.type} · ${project.category}\n- **Duration:** ${project.dateCreated} – ${project.dateModified}\n- **Status:** ${titleCase(project.status)}\n- **Live demo:** ${project.liveDemoLink === 'none' ? 'Not public' : project.liveDemoLink}\n\n**Description.** ${project.description.trim()}\n\n**Repos**\n${joinRepoLines(project.githubLink)}\n\n**Technologies.** ${project.technologies.join(' · ')}\n\n**Skills demonstrated.** ${project.skillsAndCompetencies.join(' · ')}`
  )
  .join('\n\n---\n\n')}\n`;

const generateContact = (contact, hero) => {
  const linkedin = contact.socialLinks.find((link) => link.name.toLowerCase().includes('linkedin'));
  const github = contact.socialLinks.find((link) => link.name.toLowerCase().includes('github'));
  const available = hero.contactStatus.find((item) => item.label.toLowerCase().includes('available'));
  const collaboration = hero.contactStatus.find((item) => item.label.toLowerCase().includes('collaboration'));
  const internship = hero.contactStatus.find((item) => item.label.toLowerCase().includes('internship'));

  return `${mdHeader('# 📧 Contact')}> **Summary:** ${contact.intro}\n\n## Primary contact\n\n| Channel | Where |\n|------|-------|\n| Email | [${contact.email}](mailto:${contact.email}) |\n| LinkedIn | [${linkedin?.url ?? '-'}](${linkedin?.url ?? '#'}) |\n| GitHub | [${github?.url ?? '-'}](${github?.url ?? '#'}) |\n\n## Availability\n\n- **Available for opportunities:** ${available?.value ? 'Yes' : 'No'}\n- **Open to collaboration:** ${collaboration?.value ? 'Yes' : 'No'}\n- **Open to internships:** ${internship?.value ? 'Yes' : 'No'}\n\n## Response time\n\n${contact.responseTime}.\n`;
};

const generateReadme = () => `# 📂 Profile — Career / Skill / Portfolio Data Center\n\nThis folder contains **AI-readable markdown generated from the canonical JSON source** in:\n\n- \`/src/data/portfolio/*.json\`\n\n> **Owner:** Musthofa Joko Anggoro\n> **Handle:** [\`@topahilangharapan\`](https://github.com/topahilangharapan)\n> **Role:** Full-Stack Developer · Software Engineer · CS Student at Universitas Indonesia\n> **Last generated:** ${dateNow()}\n\n## Index\n\n| File | Contents |\n|------|----------|\n| [\`about.md\`](about.md) | Personal summary, strengths, grouped technical skills |\n| [\`skills.md\`](skills.md) | Full technical and soft skill inventory |\n| [\`education.md\`](education.md) | University, GPA, coursework, achievements, summer program |\n| [\`experience.md\`](experience.md) | Internships and organizational experience |\n| [\`projects.md\`](projects.md) | Featured projects with role, stack, links, and outcomes |\n| [\`contact.md\`](contact.md) | Email, social links, and availability |\n\n## Source of truth\n\n- **Canonical data source:** JSON under \`/src/data/portfolio/\`\n- **Derived artifacts:** markdown files in this folder\n\n## Update flow\n\n1. Edit JSON in \`/src/data/portfolio/\`.\n2. Run:\n   \`npm run sync:profile\`\n3. Commit both JSON and regenerated markdown files.\n\nThis keeps:\n- Vue app data consumption (**JSON**)\n- AI/LLM-friendly documentation (**markdown**)\n\nin sync from one source.\n`;

async function main() {
  const [about, contact, education, experience, projects, hero, skills] = await Promise.all([
    readJson('about'),
    readJson('contact'),
    readJson('education'),
    readJson('experience'),
    readJson('projects'),
    readJson('hero'),
    readJson('skills')
  ]);

  await Promise.all([
    fs.writeFile(path.join(docsDir, 'about.md'), generateAbout(about), 'utf8'),
    fs.writeFile(path.join(docsDir, 'skills.md'), generateSkills(skills), 'utf8'),
    fs.writeFile(path.join(docsDir, 'education.md'), generateEducation(education), 'utf8'),
    fs.writeFile(path.join(docsDir, 'experience.md'), generateExperience(experience), 'utf8'),
    fs.writeFile(path.join(docsDir, 'projects.md'), generateProjects(projects), 'utf8'),
    fs.writeFile(path.join(docsDir, 'contact.md'), generateContact(contact, hero), 'utf8'),
    fs.writeFile(path.join(docsDir, 'README.md'), generateReadme(), 'utf8')
  ]);

  console.log('Profile markdown docs synced from JSON.');
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
