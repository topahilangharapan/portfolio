export interface Experience {
  id: string;
  role: string;
  company: string;
  achievements: string[];
  technologies?: string[];
  type: 'Full-time' | 'Part-time' | 'Contract' | 'Freelance' | 'Internship';
  location: string;
  icon: string;
  dateModified: string;
  dateCreated: string;
  duration: string;
  size: string; // For display purposes (e.g., "2.3 years")
}