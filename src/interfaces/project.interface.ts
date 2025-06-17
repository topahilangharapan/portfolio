export interface Project {
  id: string
  title: string
  description: string
  technologies: string[]
  githubLink: string
  liveDemoLink: string
  role: string
  category: string
  icon: string
  dateCreated: string
  dateModified: string
  size: string
  type: string
  skillsAndCompetencies: string[]
  status: 'completed' | 'in-progress' | 'archived'
}
