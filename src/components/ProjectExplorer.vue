<script setup lang="ts">
import { ref, computed } from 'vue';
import ProjectCard from './ProjectCard.vue';
import type { Project } from '../interfaces/project.interface.ts';

interface Props {
  projects?: Project[];
  isOpen: boolean;
}

const emit = defineEmits<{
  (e: 'update:isOpen', value: boolean): void;
}>();

function toggleOpen() {
  emit('update:isOpen', !props.isOpen);
}

const props = withDefaults(defineProps<Props>(), {
  projects: () => [
    {
      id: '1',
      title: 'Enterprise Information System for Event Organizer',
      description:
        'An all-in-one enterprise system built to streamline event organizer operations. From finance to freelancer tracking with secure deployment and clean code standards.',
      technologies: ['Spring Boot', 'Vue.js', 'PostgreSQL', 'RESTful API', 'Docker', 'TypeScript'],
      githubLink: 'none',
      liveDemoLink: 'none',
      role: 'Lead Engineer & Full Stack Developer',
      icon: '🎤',
      dateModified: '2025-05-28',
      size: '408.4 MB',
      type: 'Web App',
      category: 'Company',
      dateCreated: '2025-02-03',
      status: 'completed',
      skillsAndCompetencies: [
        'Full-Stack Development',
        'RESTful API Design',
        'PostgreSQL Optimization',
        'CI/CD & Docker',
        'Secure Authentication (JWT)',
        'Code Quality & Leadership',
      ],
    },
    {
      id: '2',
      title: 'Used Car Sales Prediction',
      description:
        'Built a predictive model for used car sales using classification, regression, and clustering to uncover insights and improve business decision-making.',
      technologies: [
        'Python',
        'Scikit-learn',
        'Gradient Boosting',
        'Random Forest',
        'Logistic Regression',
        'Linear Regression',
        'Naive Bayes',
        'K-Means',
        'EDA',
        'Data Preprocessing',
        'Oversampling',
        'Pandas',
        'NumPy',
      ],
      githubLink: 'none',
      liveDemoLink: 'none',
      role: 'Machine Learning Analyst',
      icon: '🚘',
      dateModified: '2025-05-12',
      size: '9.5 MB',
      type: 'AI/ML',
      category: 'Course Project',
      dateCreated: '2025-04-07',
      status: 'completed',
      skillsAndCompetencies: [
        'Machine Learning Modeling',
        'EDA & Business Insight',
        'Data Preprocessing',
        'Imbalanced Data Handling',
        'Model Evaluation',
        'Regression & Classification',
        'Clustering & Segmentation',
        'Python & Scikit-learn Workflow',
      ],
    },
    {
      id: '3',
      title: 'Apap Medika Web - Enterprise Web Application',
      description:
        'Built a secure and scalable enterprise web app using Spring Boot and Vue.js, focusing on RESTful API development, policy management, and CI/CD deployment with Docker.\n',
      technologies: ['Spring Boot', 'Vue.js', 'PostgreSQL', 'Typescript', 'RESTful API', 'Docker'],
      githubLink: 'none',
      liveDemoLink: 'none',
      role: 'Full Stack Developer',
      icon: '🏥',
      dateModified: '2024-11-25',
      size: '2.46 GB',
      type: 'Web App',
      category: 'Course Project',
      dateCreated: '2024-09-04',
      status: 'completed',
      skillsAndCompetencies: [
        'Full Stack Development',
        'RESTful API Design',
        'Secure Authentication (JWT)',
        'CI/CD & Docker',
        'MVC Architecture',
        'Frontend-Backend Integration',
      ],
    },
    {
      id: '4',
      title: 'Marmut Merah Jambu - Music & Podcast Streaming Web',
      description:
        'Developed a full-stack music and podcast streaming web app, focusing on playlist management, user registration, and song playback with strong database integration.',
      technologies: [
        'Django',
        'PostgreSQL',
        'Manual SQL Queries',
        'SQL Triggers',
        'Stored Procedures',
        'Relational Database',
        'DDL & DML',
        'CRUD Operations',
      ],
      githubLink: 'none',
      liveDemoLink: 'none',
      role: 'Full Stack Developer',
      icon: '🐹',
      dateModified: '2024-06-24',
      size: '104 MB',
      type: 'Web App',
      category: 'Course Project',
      dateCreated: '2024-03-17',
      status: 'completed',
      skillsAndCompetencies: [
        'Full-stack web development',
        'Manual SQL query & optimization',
        'Trigger & stored procedure handling',
        'Relational DB design',
        'CRUD operations',
      ],
    },
    {
      id: '5',
      title: 'PathFinder - Education and Career Guidance App (App Design)',
      description:
        'Designed a user-centric guidance app for students, from research and journey mapping to wireframing, prototyping, and usability testing to ensure intuitive user experience.',
      technologies: [
        'Figma',
        'UX Research',
        'User Journey Mapping',
        'Information Architecture',
        'Wireframing',
        'Prototyping',
        'Usability Testing',
      ],
      githubLink: 'none',
      liveDemoLink: 'none',
      role: 'UI/UX Designer & Researcher',
      icon: '🧭',
      dateModified: '2024-06-13',
      size: '32.1 MB',
      type: 'UI/UX Design',
      category: 'Course Project',
      dateCreated: '2024-03-01',
      status: 'completed',
      skillsAndCompetencies: [
        'UX research & validation',
        'Journey mapping',
        'Wireframe & prototype',
        'Usability testing',
        'User-first thinking',
      ],
    },
    {
      id: '6',
      title: 'LibPanda - Online Library Management System',
      description:
        'Developed a responsive library management system with Django and Flutter, handling CRUD, search, wallet management, and seamless integration across web and mobile platforms.',
      technologies: [
        'Django',
        'Flutter',
        'Mobile Integration',
        'PostgreSQL',
        'Responsive CSS Framework',
        'REST API',
        'CRUD Operations',
        'Unit Testing',
      ],
      githubLink: 'none',
      liveDemoLink: 'none',
      role: 'Full Stack Developer',
      icon: '📚',
      dateModified: '2023-12-20',
      size: '172 MB',
      type: 'Web & Mobile App',
      category: 'Course Project',
      dateCreated: '2023-10-01',
      status: 'completed',
      skillsAndCompetencies: [
        'Web & Mobile integration',
        'CRUD & REST API',
        'UI Responsiveness',
        'Cross-platform Deployment',
      ],
    },
  ],
});

// Component state
const selectedProject = ref<Project | null>(null);
const openProjects = ref<Project[]>([]);
const activeProjectId = ref<string | null>(null);
const viewMode = ref<'list' | 'icons'>('list');
const sortBy = ref<'name' | 'date' | 'size' | 'type'>('date');
const sortOrder = ref<'asc' | 'desc'>('desc');
const searchQuery = ref('');

// Computed properties
const filteredProjects = computed(() => {
  let filtered = props.projects.filter(
    (project) =>
      project.title.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
      project.description.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
      project.technologies.some((tech) =>
        tech.toLowerCase().includes(searchQuery.value.toLowerCase())
      )
  );

  // Sort projects
  filtered.sort((a, b) => {
    let aValue: any, bValue: any;

    switch (sortBy.value) {
      case 'name':
        aValue = a.title.toLowerCase();
        bValue = b.title.toLowerCase();
        break;
      case 'date':
        aValue = new Date(a.dateModified);
        bValue = new Date(b.dateModified);
        break;
      case 'size':
        aValue = parseFloat(a.size);
        bValue = parseFloat(b.size);
        break;
      case 'type':
        aValue = a.type;
        bValue = b.type;
        break;
      default:
        return 0;
    }

    if (aValue < bValue) return sortOrder.value === 'asc' ? -1 : 1;
    if (aValue > bValue) return sortOrder.value === 'asc' ? 1 : -1;
    return 0;
  });

  return filtered;
});

// Methods
const selectProject = (project: Project) => {
  selectedProject.value = project;
};

const openProject = (project: Project) => {
  // Check if project is already open
  const existingProject = openProjects.value.find((p) => p.id === project.id);
  if (!existingProject) {
    openProjects.value.push(project);
  }
  activeProjectId.value = project.id;
};

const closeProject = (projectId: string) => {
  const index = openProjects.value.findIndex((p) => p.id === projectId);
  if (index > -1) {
    openProjects.value.splice(index, 1);

    // If closing active project, switch to another or close all
    if (activeProjectId.value === projectId) {
      if (openProjects.value.length > 0) {
        activeProjectId.value = openProjects.value[openProjects.value.length - 1].id;
      } else {
        activeProjectId.value = null;
      }
    }
  }
};

const switchToProject = (projectId: string) => {
  activeProjectId.value = projectId;
};

const toggleViewMode = () => {
  viewMode.value = viewMode.value === 'list' ? 'icons' : 'list';
};

const changeSortBy = (newSortBy: typeof sortBy.value) => {
  if (sortBy.value === newSortBy) {
    sortOrder.value = sortOrder.value === 'asc' ? 'desc' : 'asc';
  } else {
    sortBy.value = newSortBy;
    sortOrder.value = sortBy.value === 'date' ? 'desc' : 'asc';
  }
};

const getProjectIcon = (project: Project) => {
  return project.icon || '📁';
};

const formatDate = (dateString: string) => {
  return new Date(dateString).toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
  });
};

const getCurrentTime = () => {
  return new Date().toLocaleTimeString('en-US', {
    hour: '2-digit',
    minute: '2-digit',
    hour12: false,
  });
};

const currentTime = ref(getCurrentTime());
setInterval(() => {
  currentTime.value = getCurrentTime();
}, 1000);
</script>

<template>
  <div class="h-full flex flex-col relative">
    <!-- Main Explorer Window -->
    <div class="xp-window m-2 flex-1 flex flex-col" :class="{ 'z-10': !activeProjectId }">
      <!-- Title Bar -->
      <div class="xp-title-bar">
        <div class="flex items-center">
          <span class="mr-2">💼</span>
          <span class="font-xp-title">My Projects - Portfolio Explorer</span>
        </div>
        <div class="xp-window-controls">
          <div class="xp-control-btn">_</div>
          <div class="xp-control-btn">□</div>
          <div class="xp-control-btn xp-close-btn" @click="toggleOpen">×</div>
        </div>
      </div>

      <!-- XP Menu Bar -->
      <div class="xp-menubar">
        <span class="xp-menu-item inline-block">File</span>
        <span class="xp-menu-item inline-block">Edit</span>
        <span class="xp-menu-item inline-block">View</span>
        <span class="xp-menu-item inline-block">Navigate</span>
        <span class="xp-menu-item inline-block">Help</span>
      </div>

      <!-- Toolbar -->
      <div class="xp-panel p-2 flex items-center justify-between border-b border-gray-400">
        <div class="flex items-center space-x-2">
          <button class="xp-button px-2 py-1 font-xp text-xs">Back</button>
          <button class="xp-button px-2 py-1 font-xp text-xs">Forward</button>
          <button class="xp-button px-2 py-1 font-xp text-xs">Up</button>
          <div class="border-l border-gray-500 h-4 mx-2"></div>
          <button @click="toggleViewMode" class="xp-button px-2 py-1 font-xp text-xs">
            {{ viewMode === 'list' ? 'Icons' : 'List' }}
          </button>
        </div>
        <div class="flex items-center space-x-2">
          <span class="font-xp text-xs">Search:</span>
          <input
            v-model="searchQuery"
            class="xp-input w-32 h-6 text-xs"
            placeholder="Find projects..."
          />
        </div>
      </div>

      <!-- Address Bar -->
      <div class="xp-panel-raised p-1 flex items-center space-x-2">
        <span class="font-xp text-xs">Address:</span>
        <div class="xp-input flex-1 h-6 flex items-center px-2">
          <span class="font-xp text-xs">📁 My Computer > Portfolio > Projects</span>
        </div>
      </div>

      <!-- Main Content Area -->
      <div class="flex-1 flex">
        <!-- Left Sidebar -->
        <div class="w-48 border-r-2 border-gray-400 bg-xp-silver">
          <div class="xp-panel-raised m-2 p-2">
            <div class="font-xp text-xs font-bold mb-2">Project Categories</div>
            <div class="space-y-1">
              <div class="font-xp text-xs p-1 hover:bg-blue-100 cursor-pointer">🌐 Web Apps</div>
              <div class="font-xp text-xs p-1 hover:bg-blue-100 cursor-pointer">📱 Mobile Apps</div>
<!--              <div class="font-xp text-xs p-1 hover:bg-blue-100 cursor-pointer">-->
<!--                💻 Desktop Apps-->
<!--              </div>-->
<!--              <div class="font-xp text-xs p-1 hover:bg-blue-100 cursor-pointer">📚 Libraries</div>-->
<!--              <div class="font-xp text-xs p-1 hover:bg-blue-100 cursor-pointer">🔌 APIs</div>-->
              <div class="font-xp text-xs p-1 hover:bg-blue-100 cursor-pointer">
                ✨ AI/ML
              </div>
            </div>
          </div>

          <div class="xp-panel-raised m-2 p-2">
            <div class="font-xp text-xs font-bold mb-2">Quick Actions</div>
            <div class="space-y-1">
              <button class="w-full xp-button p-1 font-xp text-xs">New Project</button>
              <button class="w-full xp-button p-1 font-xp text-xs">Import</button>
              <button class="w-full xp-button p-1 font-xp text-xs">Export</button>
            </div>
          </div>
        </div>

        <!-- Project List/Grid -->
        <div class="flex-1 p-2 bg-white xp-scroll overflow-auto">
          <!-- List View Header -->
          <div
            v-if="viewMode === 'list'"
            class="flex font-xp text-xs font-bold border-b border-gray-300 pb-1 mb-2"
          >
            <div class="flex-1 cursor-pointer hover:bg-gray-100 p-1" @click="changeSortBy('name')">
              Name {{ sortBy === 'name' ? (sortOrder === 'asc' ? '↑' : '↓') : '' }}
            </div>
            <div class="w-24 cursor-pointer hover:bg-gray-100 p-1" @click="changeSortBy('size')">
              Size {{ sortBy === 'size' ? (sortOrder === 'asc' ? '↑' : '↓') : '' }}
            </div>
            <div class="w-24 cursor-pointer hover:bg-gray-100 p-1" @click="changeSortBy('type')">
              Type {{ sortBy === 'type' ? (sortOrder === 'asc' ? '↑' : '↓') : '' }}
            </div>
            <div class="w-32 cursor-pointer hover:bg-gray-100 p-1" @click="changeSortBy('date')">
              Date Completed {{ sortBy === 'date' ? (sortOrder === 'asc' ? '↑' : '↓') : '' }}
            </div>
          </div>

          <!-- List View -->
          <div v-if="viewMode === 'list'" class="space-y-1">
            <div
              v-for="project in filteredProjects"
              :key="project.id"
              class="flex items-center p-1 hover:bg-blue-100 cursor-pointer font-xp text-xs"
              :class="{ 'bg-blue-200': openProjects.includes(project) }"
              @click="selectProject(project)"
              @dblclick="openProject(project)"
            >
              <div class="flex items-center flex-1">
                <span class="mr-2">{{ getProjectIcon(project) }}</span>
                <span>{{ project.title }}</span>
              </div>
              <div class="w-24">{{ project.size }}</div>
              <div class="w-24">{{ project.type }}</div>
              <div class="w-32">{{ formatDate(project.dateModified) }}</div>
            </div>
          </div>

          <!-- Icons View -->
          <div v-else class="grid grid-cols-4 gap-4">
            <div
              v-for="project in filteredProjects"
              :key="project.id"
              class="flex flex-col items-center p-2 hover:bg-blue-100 cursor-pointer"
              :class="{ 'bg-blue-200': openProjects.includes(project) }"
              @click="selectProject(project)"
              @dblclick="openProject(project)"
            >
              <div class="text-2xl mb-1">{{ getProjectIcon(project) }}</div>
              <div class="font-xp text-xs text-center">{{ project.title }}</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Status Bar -->
      <div class="xp-status flex justify-between items-center">
        <div class="flex items-center space-x-4">
          <span class="font-xp">{{ filteredProjects.length }} project(s)</span>
          <span v-if="selectedProject" class="font-xp">{{ selectedProject.title }} selected</span>
        </div>
        <div class="flex items-center space-x-4">
          <span class="font-xp text-xs">{{ openProjects.length }} open</span>
          <span class="font-xp text-xs">Ready</span>
        </div>
      </div>
    </div>

    <!-- Project Card Windows -->
    <div
      v-for="(project, index) in openProjects"
      :key="project.id"
      class="absolute"
      :class="{ 'z-20': openProjects.includes(project), 'z-10': activeProjectId !== project.id }"
      :style="{
        top: `${-10 + index * 30}px`,
        left: `${200 + index * 30}px`,
        width: '1200px',
        height: '75vh',
      }"
    >
      <div>
        <ProjectCard
          :title="project.title"
          :description="project.description"
          :technologies="project.technologies"
          :github-link="project.githubLink"
          :live-demo-link="project.liveDemoLink"
          :role="project.role"
          :category="project.category"
          :icon="project.icon"
          :dateCreated="project.dateCreated"
          :dateModified="project.dateModified"
          :size="project.size"
          :type="project.type"
          :status="project.status"
          :skillsAndCompetencies="project.skillsAndCompetencies"
          :isOpen="openProjects.includes(project)"
          @update:isOpen="
            (val) => {
              if (val) {
                activeProjectId = project.id;
              } else {
                closeProject(project.id);
              }
            }
          "
        />
      </div>
    </div>

    <!-- XP Taskbar -->
    <div class="xp-taskbar">
      <button class="xp-start-button">Start</button>

      <!-- Quick Launch -->
      <div class="flex items-center space-x-1 mr-4">
        <div
          class="w-6 h-6 bg-blue-500 rounded-sm flex items-center justify-center text-white text-xs cursor-pointer"
        >
          IE
        </div>
        <div
          class="w-6 h-6 bg-yellow-500 rounded-sm flex items-center justify-center text-white text-xs cursor-pointer"
        >
          📁
        </div>
      </div>

      <!-- Open Project Tabs -->
      <div class="flex items-center space-x-1 flex-1">
        <div
          v-for="project in openProjects"
          :key="project.id"
          class="xp-button px-3 py-1 font-xp text-xs max-w-32 truncate cursor-pointer"
          :class="{ 'border-inset': activeProjectId === project.id }"
          @click="switchToProject(project.id)"
        >
          {{ project.title }}
        </div>
      </div>

      <!-- System Tray -->
      <div class="flex items-center space-x-2">
        <div class="w-4 h-4 bg-green-500 rounded-sm"></div>
        <div class="w-4 h-4 bg-blue-500 rounded-sm"></div>
        <div class="font-xp text-white text-xs">{{ currentTime }}</div>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* Custom dragging styles */
.cursor-move {
  cursor: move;
}

/* Ensure proper z-indexing for overlapping windows */
.z-10 {
  z-index: 10;
}

.z-20 {
  z-index: 20;
}

/* Smooth transitions for window switching */
.xp-title-bar {
  transition: opacity 0.2s ease;
}
</style>
