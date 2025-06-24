<script setup lang="ts">
import {ref} from "vue";

const selectText = (event) => {
  event.target.select()
  event.target.setSelectionRange(0, 99999) // For mobile devices
}

const projects = ref([
  {
    id: 1,
    title: 'Enterprise Information System for Event Organizer',
    category: 'Full Stack Application',
    status: 'Completed',
    image: 'Screenshot 2025-06-23 at 13.48.55.png', // add image URL if needed
    demoUrl: 'http://82.25.108.76/auth/login',
    githubUrl: 'https://github.com/topahilangharapan/sispa-backend',
    description: 'Enterprise-grade system for event organizers, covering finance, freelancer tracking, and secure deployment with clean code architecture.',
    highlights: [
      'JWT-secured RESTful API using Spring Boot',
      'Frontend built with Vue.js and TypeScript',
      'CI/CD and Docker-based deployment',
      'PostgreSQL optimization and clean code'
    ],
    technologies: ['Spring Boot', 'Vue.js', 'PostgreSQL', 'RESTful API', 'Docker', 'TypeScript'],
    duration: '4 months',
    teamSize: '5 developers',
    role: 'Lead Engineer & Full Stack Developer'
  },
  {
    id: 2,
    title: 'Used Car Sales Prediction',
    category: 'Machine Learning',
    status: 'Completed',
    image: 'output.png', // add image URL if needed
    demoUrl: '',
    githubUrl: '', // not available
    description: 'Machine learning project to predict used car sales using classification, regression, and clustering techniques for business insight.',
    highlights: [
      'Handled imbalanced data with over/undersampling',
      'Built models using Random Forest, Gradient Boosting, Logistic & Linear Regression',
      'Clustering with K-Means and EDA for insight',
      'Applied full preprocessing-to-evaluation ML pipeline'
    ],
    technologies: ['Python', 'Scikit-learn', 'Gradient Boosting', 'Random Forest', 'Logistic Regression', 'Linear Regression', 'Naive Bayes', 'K-Means', 'EDA', 'Pandas', 'NumPy'],
    duration: '1.5 months',
    teamSize: '1 developer',
    role: 'Machine Learning Analyst'
  },
  {
    id: 3,
    title: 'Apap Medika Web - Enterprise Web Application',
    category: 'Full Stack Application',
    status: 'Completed',
    image: '', // add image URL if needed
    demoUrl: '',
    githubUrl: 'https://github.com/topahilangharapan/apap-medika-insurance',
    description: 'Secure and scalable enterprise web app for managing insurance and user profiles using Spring Boot microservices and Vue.js frontend.',
    highlights: [
      'Modular backend with JWT-auth microservices',
      'CI/CD pipeline with Docker containers',
      'Frontend-Backend integration via RESTful API',
      'Built with clean architecture and MVC principles'
    ],
    technologies: ['Spring Boot', 'Vue.js', 'PostgreSQL', 'Typescript', 'RESTful API', 'Docker'],
    duration: '3 months',
    teamSize: '4 developers',
    role: 'Full Stack Developer'
  },
  {
    id: 4,
    title: 'Marmut Merah Jambu - Music & Podcast Streaming Web',
    category: 'Full Stack Application',
    status: 'Completed',
    image: '', // add image URL if needed
    demoUrl: '',
    githubUrl: 'https://github.com/BASDAT-F7/marmut_merah_jambu',
    description: 'Django-based streaming platform for music and podcasts with full CRUD support, custom SQL integration, and playlist features.',
    highlights: [
      'Custom SQL queries, triggers, and stored procedures',
      'Relational DB design and optimization',
      'User management and playlist CRUD',
      'Full integration of backend logic and frontend UI'
    ],
    technologies: ['Django', 'PostgreSQL', 'Manual SQL Queries', 'SQL Triggers', 'Stored Procedures', 'CRUD Operations'],
    duration: '3.5 months',
    teamSize: '5 developers',
    role: 'Full Stack Developer'
  },
  {
    id: 5,
    title: 'PathFinder - Education and Career Guidance App',
    category: 'UI/UX Design',
    status: 'Completed',
    image: '', // add image URL if needed
    demoUrl: '',
    githubUrl: '', // not available
    description: 'Designed and validated user-centered education guidance app through UX research, prototyping, and usability testing.',
    highlights: [
      'Built wireframes and high-fidelity prototypes',
      'Conducted usability testing with real users',
      'Mapped user journeys and information architecture',
      'Applied iterative UX design process'
    ],
    technologies: ['Figma', 'UX Research', 'Wireframing', 'Prototyping', 'Usability Testing'],
    duration: '2.5 months',
    teamSize: '3 designers',
    role: 'UI/UX Designer & Researcher'
  },
  {
    id: 6,
    title: 'LibPanda - Online Library Management System',
    category: 'Web & Mobile App',
    status: 'Completed',
    image: '', // add image URL if needed
    demoUrl: '',
    githubUrl: 'https://github.com/PBP-E15/LibPanda',
    description: 'Cross-platform library system built with Django and Flutter, supporting book management, search, and wallet features.',
    highlights: [
      'Flutter mobile app integrated with Django backend',
      'CRUD and search functionality with REST API',
      'Responsive web & mobile design',
      'Unit tested for reliability'
    ],
    technologies: ['Django', 'Flutter', 'PostgreSQL', 'Responsive CSS Framework', 'REST API', 'CRUD Operations'],
    duration: '3 months',
    teamSize: '4 developers',
    role: 'Full Stack Developer'
  }

])

const getCategoryIcon = (category) => {
  switch (category) {
    case 'Full Stack Application': return '🌐'
    case 'SaaS Application': return '💼'
    case 'Machine Learning': return '🤖'
    case 'Web & Mobile App': return '📱'
    case 'FinTech Application': return '💰'
    case 'Educational Platform': return '📚'
    case 'UI/UX Design': return '🎨'
    default: return '💻'
  }
}
</script>

<template>
  <!-- Projects Section -->
  <div class="max-w-5xl mx-auto">
    <div class="xp-window">
      <!-- XP Title Bar -->
      <div class="xp-title-bar">
        <div class="flex items-center">
          <span class="w-4 h-4 bg-white rounded-sm mr-2 flex items-center justify-center text-xs">🚀</span>
          <span class="font-xp-title">Portfolio Projects - Development Showcase</span>
        </div>
        <div class="xp-window-controls">
          <div class="xp-control-btn">_</div>
          <div class="xp-control-btn">□</div>
          <div class="xp-control-btn xp-close-btn">×</div>
        </div>
      </div>

      <!-- XP Menu Bar -->
      <div class="xp-menubar flex-shrink-0">
        <span class="xp-menu-item inline-block">File</span>
        <span class="xp-menu-item inline-block">Edit</span>
        <span class="xp-menu-item inline-block">View</span>
        <span class="xp-menu-item inline-block">Navigate</span>
        <span class="xp-menu-item inline-block">Help</span>
      </div>

      <!-- XP Window Content -->
      <div class="p-6 bg-xp-window">

        <!-- Projects Grid -->
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
          <div v-for="project in projects" :key="project.id" class="xp-group">

            <!-- Project Header -->
            <div class="xp-group-title">
              <div class="flex items-center justify-between">
                <div class="flex items-center space-x-2">
                  <span class="text-lg">{{ getCategoryIcon(project.category) }}</span>
                  <span class="font-bold">{{ project.title }}</span>
                </div>
              </div>
            </div>

            <!-- Project Content -->
            <div class="xp-panel-raised p-4 space-y-4">

              <!-- Project Image & Quick Info -->
              <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
                <!-- Project Image -->
                <div class="sm:col-span-3" v-if="project.image">

                  <div class="xp-panel-raised p-4">
                  <div class="xp-panel-inset p-1">
                    <img
                        :src="project.image"
                        :alt="project.title"
                        class="w-full h-full object-cover xp-panel"
                        loading="lazy"
                    />
                  </div>
                  </div>
                </div>

                <!-- Quick Info -->
                <div class="sm:col-span-3 space-y-2">
                  <div class="xp-panel p-2">
                    <div class="grid grid-cols-2 gap-2 text-xs">
                      <div>
                        <span class="font-xp font-bold text-gray-600">Category:</span>
                        <div class="font-xp text-black">{{ project.category }}</div>
                      </div>
                      <div>
                        <span class="font-xp font-bold text-gray-600">Duration:</span>
                        <div class="font-xp text-black">{{ project.duration }}</div>
                      </div>
                      <div>
                        <span class="font-xp font-bold text-gray-600">Team Size:</span>
                        <div class="font-xp text-black">{{ project.teamSize }}</div>
                      </div>
                      <div>
                        <span class="font-xp font-bold text-gray-600">My Role:</span>
                        <div class="font-xp text-black font-bold">{{ project.role }}</div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <!-- Project Description -->
              <div class="xp-panel p-3">
                <div class="flex items-center space-x-2 mb-2">
                  <span class="w-2 h-2 bg-blue-500 rounded-full"></span>
                  <span class="font-xp text-xs font-bold text-gray-700">Project Overview:</span>
                </div>
                <p class="font-xp text-sm text-black leading-relaxed">
                  {{ project.description }}
                </p>
              </div>

              <!-- Key Highlights -->
              <div class="xp-group">
                <div class="xp-group-title">✨ Key Highlights</div>
                <div class="xp-panel p-3">
                  <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
                    <div
                        v-for="highlight in project.highlights"
                        :key="highlight"
                        class="xp-button p-2 text-left"
                    >
                      <div class="flex items-start space-x-2">
                        <span class="text-green-600 flex-shrink-0 mt-0.5">✓</span>
                        <span class="font-xp text-xs leading-relaxed">{{ highlight }}</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <!-- Technologies Used -->
              <div class="xp-group">
                <div class="xp-group-title">🛠️ Tech Stack</div>
                <div class="xp-panel p-3">
                  <div class="flex flex-wrap gap-1">
                    <span
                        v-for="tech in project.technologies"
                        :key="tech"
                        class="xp-button px-2 py-1 text-xs font-xp"
                    >
                      {{ tech }}
                    </span>
                  </div>
                </div>
              </div>

              <!-- Project Links (Enhanced) -->
              <div class="space-y-2">
                <!-- Demo URL -->
                <div class="xp-panel p-2" v-if="project.demoUrl">
                  <label class="font-xp text-xs font-bold text-gray-700 block mb-1">Live Demo URL:</label>
                  <div class="flex items-center space-x-2">
                    <textarea
                        readonly
                        class="flex-1 px-2 py-1 text-xs font-xp border-2 border-xp-inset bg-white resize-none"
                        rows="1"
                        @click="selectText"
                    >{{ project.demoUrl }}</textarea>
                    <a :href="project.demoUrl" target="_blank" class="xp-button px-2 py-1 font-xp text-xs">
                      <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/>
                      </svg>
                    </a>
                  </div>
                </div>

                <!-- GitHub URL -->
                <div class="xp-panel p-2" v-if="project.githubUrl">
                  <label class="font-xp text-xs font-bold text-gray-700 block mb-1">Source Code Repository:</label>
                  <div class="flex items-center space-x-2">
                    <textarea
                        readonly
                        class="flex-1 px-2 py-1 text-xs font-xp border-2 border-xp-inset bg-white resize-none"
                        rows="1"
                        @click="selectText"
                    >{{ project.githubUrl }}</textarea>
                    <a :href="project.githubUrl" target="_blank" class="xp-button px-2 py-1 font-xp text-xs">
                      <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/>
                      </svg>
                    </a>
                  </div>
                </div>
              </div>

            </div>
          </div>
        </div>
      </div>

      <!-- Enhanced XP Status Bar -->
      <div class="xp-status flex justify-between items-center">
        <div class="flex items-center space-x-2">
          <span class="font-xp text-sm">Projets Loaded Successfully</span>
        </div>
        <div class="flex items-center space-x-4">
          <span class="font-xp text-xs">{{ projects.length }} Project{{ projects.length !== 1 ? 's' : '' }}</span>
          <span class="font-xp text-xs">{{ new Set(projects.flatMap(p => p.technologies)).size }} Technologies</span>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
</style>