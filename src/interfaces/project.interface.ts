export interface Project {
  id: string
  title: string
  description: string
  technologies: string[]
  githubLink: string | GitHubRepo[]; // Support both old format and new array format
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

export interface GitHubRepo {
  name: string;
  url: string;
  description?: string;
  type?: 'main' | 'frontend' | 'backend' | 'api' | 'docs' | 'microservice' | 'other';
}
