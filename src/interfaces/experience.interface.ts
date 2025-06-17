export interface Experience {
  id: string;
  role: string;
  company: string;
  achievements: string[];
  technologies?: string[];
  type: 'Full-time' | 'Part-time' | 'Contract' | 'Freelance' | 'Internship' | 'Organization';
  location: string;
  icon: string;
  dateModified: string;
  dateCreated: string;
  duration: string;
}