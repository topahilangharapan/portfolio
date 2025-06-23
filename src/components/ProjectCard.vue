<script setup lang="ts">
import {ref} from "vue";

const selectText = (event) => {
  event.target.select()
  event.target.setSelectionRange(0, 99999) // For mobile devices
}

const projects = ref([
  {
    id: 1,
    title: 'E-Commerce Platform',
    category: 'Full Stack Application',
    status: 'Production',
    image: 'https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?w=400&h=250&fit=crop',
    demoUrl: 'https://demo-ecommerce.com',
    githubUrl: 'https://github.com/yourusername/ecommerce-platform',
    description: 'A complete e-commerce solution with payment integration, inventory management, and admin dashboard. Built for scalability and performance.',
    highlights: [
      'Handles 10,000+ concurrent users',
      'Integrated Stripe & PayPal payments',
      'Real-time inventory tracking',
      'SEO optimized with SSR'
    ],
    technologies: ['React', 'Node.js', 'MongoDB', 'Stripe API', 'AWS S3', 'Redis'],
    duration: '4 months',
    teamSize: '3 developers',
    role: 'Lead Developer'
  },
  {
    id: 2,
    title: 'Task Management Dashboard',
    category: 'SaaS Application',
    status: 'Production',
    image: 'https://images.unsplash.com/photo-1611224923853-80b023f02d71?w=400&h=250&fit=crop',
    demoUrl: 'https://taskflow-demo.com',
    githubUrl: 'https://github.com/yourusername/task-dashboard',
    description: 'Collaborative project management tool with real-time updates, team collaboration features, and advanced reporting capabilities.',
    highlights: [
      'Real-time collaboration with Socket.io',
      'Advanced analytics dashboard',
      'Mobile-responsive design',
      'Role-based access control'
    ],
    technologies: ['Vue.js', 'Express.js', 'PostgreSQL', 'Socket.io', 'Chart.js', 'Docker'],
    duration: '3 months',
    teamSize: '2 developers',
    role: 'Full Stack Developer'
  },
  {
    id: 3,
    title: 'AI-Powered Content Generator',
    category: 'Machine Learning',
    status: 'Beta',
    image: 'https://images.unsplash.com/photo-1677442136019-21780ecad995?w=400&h=250&fit=crop',
    demoUrl: 'https://ai-content-beta.com',
    githubUrl: 'https://github.com/yourusername/ai-content-generator',
    description: 'AI-driven platform that generates marketing content, blog posts, and social media content using natural language processing.',
    highlights: [
      'OpenAI GPT integration',
      'Custom fine-tuned models',
      'Content optimization algorithms',
      'Multi-language support'
    ],
    technologies: ['Python', 'FastAPI', 'OpenAI API', 'TensorFlow', 'React', 'PostgreSQL'],
    duration: '6 months',
    teamSize: '4 developers',
    role: 'ML Engineer & Backend Lead'
  },
  {
    id: 4,
    title: 'Real Estate Marketplace',
    category: 'Web Application',
    status: 'Production',
    image: 'https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=400&h=250&fit=crop',
    demoUrl: 'https://realestate-marketplace.com',
    githubUrl: 'https://github.com/yourusername/realestate-platform',
    description: 'Comprehensive real estate platform with property listings, virtual tours, mortgage calculator, and agent management system.',
    highlights: [
      'Interactive map integration',
      'Virtual tour functionality',
      'Advanced search filters',
      'CRM for real estate agents'
    ],
    technologies: ['Next.js', 'TypeScript', 'Prisma', 'Google Maps API', 'Vercel', 'Supabase'],
    duration: '5 months',
    teamSize: '5 developers',
    role: 'Frontend Lead'
  },
  {
    id: 5,
    title: 'Cryptocurrency Portfolio Tracker',
    category: 'FinTech Application',
    status: 'Production',
    image: 'https://images.unsplash.com/photo-1621761191319-c6fb62004040?w=400&h=250&fit=crop',
    demoUrl: 'https://crypto-portfolio-tracker.com',
    githubUrl: 'https://github.com/yourusername/crypto-tracker',
    description: 'Real-time cryptocurrency portfolio tracking with advanced analytics, price alerts, and tax reporting features.',
    highlights: [
      'Real-time price tracking',
      'Portfolio performance analytics',
      'Tax reporting generation',
      'Custom price alerts'
    ],
    technologies: ['React', 'Node.js', 'WebSocket', 'CoinGecko API', 'MongoDB', 'JWT'],
    duration: '3 months',
    teamSize: '2 developers',
    role: 'Full Stack Developer'
  },
  {
    id: 6,
    title: 'Learning Management System',
    category: 'Educational Platform',
    status: 'Production',
    image: 'https://images.unsplash.com/photo-1509062522246-3755977927d7?w=400&h=250&fit=crop',
    demoUrl: 'https://lms-platform.com',
    githubUrl: 'https://github.com/yourusername/lms-platform',
    description: 'Comprehensive learning management system with video streaming, progress tracking, assessments, and certification management.',
    highlights: [
      'Video streaming with adaptive quality',
      'Interactive quiz builder',
      'Progress tracking & analytics',
      'Certificate generation system'
    ],
    technologies: ['Vue.js', 'Laravel', 'MySQL', 'AWS CloudFront', 'FFmpeg', 'Pusher'],
    duration: '7 months',
    teamSize: '6 developers',
    role: 'Technical Lead'
  }
])

const getCategoryIcon = (category) => {
  switch (category) {
    case 'Full Stack Application': return '🌐'
    case 'SaaS Application': return '💼'
    case 'Machine Learning': return '🤖'
    case 'Web Application': return '📱'
    case 'FinTech Application': return '💰'
    case 'Educational Platform': return '📚'
    default: return '💻'
  }
}
</script>

<template>
  <!-- Projects Section -->
  <div class="max-w-7xl mx-auto">
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
      <div class="xp-menubar">
        <span class="xp-menu-item">File</span>
        <span class="xp-menu-item">View</span>
        <span class="xp-menu-item">Projects</span>
        <span class="xp-menu-item">Filter</span>
        <span class="xp-menu-item">Help</span>
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
                <div class="sm:col-span-1">
                  <div class="xp-panel-inset p-1">
                    <img
                        :src="project.image"
                        :alt="project.title"
                        class="w-full h-32 object-cover rounded"
                        loading="lazy"
                    />
                  </div>
                </div>

                <!-- Quick Info -->
                <div class="sm:col-span-2 space-y-2">
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
                <div class="xp-panel p-2">
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
                <div class="xp-panel p-2">
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
          <div class="w-2 h-2 rounded-full bg-green-500"></div>
          <span class="font-xp text-sm">Portfolio Loaded Successfully</span>
        </div>
        <div class="flex items-center space-x-4">
          <span class="font-xp text-xs">{{ projects.length }} Project{{ projects.length !== 1 ? 's' : '' }}</span>
          <span class="font-xp text-xs">{{ projects.filter(p => p.status === 'Production').length }} Live</span>
          <span class="font-xp text-xs">{{ new Set(projects.flatMap(p => p.technologies)).size }} Technologies</span>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
</style>