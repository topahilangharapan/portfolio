<script setup lang="ts">
import {ref} from "vue";

const selectText = (event) => {
  event.target.select()
  event.target.setSelectionRange(0, 99999) // For mobile devices
}

const experiences = ref([
  {
    id: 1,
    position: 'Full Stack Developer Intern',
    company: 'PT Magna Solusi Indonesia',
    location: 'Hybrid',
    duration: 'January 2025 - June 2025',
    companyUrl: 'https://www.magnasolusi.com', // add if available
    description: 'Contributed to full-stack development and API integration in a hybrid internship role, focusing on performance, scalability, and usability across modern frameworks.',
    achievements: [
      'Integrated full-stack modules using Spring Boot and Angular',
      'Improved database performance with optimized queries and backups',
      'Developed RESTful APIs for dynamic data flow',
      'Tested and debugged applications to uphold security and usability standards'
    ],
    technologies: ['Spring Boot', 'Angular', 'PostgreSQL', 'Apache HTTP Server', 'Bootstrap', 'Docker', 'Kubernetes']
  },
  {
    id: 2,
    position: 'Vice Person in Charge of UI/UX',
    company: 'COMPFEST',
    location: 'Hybrid',
    duration: 'January 2023 - December 2023',
    companyUrl: 'https://compfest.id', // add if available
    description: 'Led UI/UX initiatives for a national tech event, managing design operations, team coordination, and cross-functional collaboration to deliver consistent and accessible user interfaces.',
    achievements: [
      'Oversaw 5 design sprints and dark/light mode implementation on compfest.id',
      'Led 11 designers in building the landing page and refining the design system',
      'Coordinated with developers to ensure stakeholder-aligned design execution'
    ],
    technologies: ['Figma', 'ClickUp']
  }
])
</script>

<template>
  <!-- Experience Section -->
  <div class="max-w-5xl mx-auto">
    <div class="xp-window">
      <!-- XP Title Bar -->
      <div class="xp-title-bar">
        <div class="flex items-center">
          <span class="w-4 h-4 bg-white rounded-sm mr-2 flex items-center justify-center text-xs">💼</span>
          <span class="font-xp-title">Professional Experience - Career History</span>
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
        <span class="xp-menu-item">Timeline</span>
        <span class="xp-menu-item">Export</span>
        <span class="xp-menu-item">Help</span>
      </div>

      <!-- XP Window Content -->
      <div class="p-4 bg-xp-window">

        <!-- Experience Timeline -->
        <div class="space-y-4">
          <div v-for="(experience, index) in experiences" :key="experience.id" class="xp-group">
            <!-- Experience Header -->
            <div class="xp-group-title">
              <div class="flex items-center justify-between">
                <div class="flex items-center space-x-2">
                  <span class="w-8 h-8 xp-button flex items-center justify-center text-sm font-bold">{{ index + 1 }}</span>
                  <span>{{ experience.position }} @ {{ experience.company }}</span>
                </div>
              </div>
            </div>

            <!-- Experience Content -->
            <div class="xp-panel-raised p-4 space-y-4">
              <!-- Position Header with Company Info -->
              <div class="flex justify-between items-start">
                <div class="flex-1">
                  <div class="flex justify-between items-start mb-2">
                    <!-- Kiri: Ikon dan Info -->
                    <div class="flex items-center space-x-3">
                      <div class="w-10 h-10 xp-button flex items-center justify-center text-lg">🏢</div>
                      <div>
                        <h3 class="font-xp text-lg font-bold text-black">{{ experience.position }}</h3>
                        <h4 class="font-xp text-base font-bold text-blue-700">{{ experience.company }}</h4>
                        <p class="font-xp text-xs text-gray-600">{{ experience.location }}</p>
                      </div>
                    </div>

                    <!-- Kanan: Durasi -->
                    <div class="font-xp text-lg font-bold text-black">
                      {{ experience.duration || 'Present' }}
                    </div>
                  </div>


                  <!-- Company Website -->
                  <div v-if="experience.companyUrl" class="mb-3">
                    <div class="xp-panel p-2">
                      <label class="font-xp text-xs font-bold text-gray-700 block mb-1">Company Website:</label>
                      <div class="flex items-center space-x-2">
                      <textarea
                          readonly
                          class="flex-1 px-2 py-1 text-xs font-xp border-2 border-xp-inset bg-white resize-none"
                          rows="1"
                          @click="selectText"
                      >{{ experience.companyUrl }}</textarea>
                        <button class="xp-button px-2 py-1 font-xp text-xs">
                          <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/>
                          </svg>
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <!-- Role Description -->
              <div class="xp-panel p-3">
                <div class="flex items-center space-x-2 mb-2">
                  <span class="w-2 h-2 bg-blue-500 rounded-full"></span>
                  <span class="font-xp text-xs font-bold text-gray-700">Role Overview:</span>
                </div>
                <p class="font-xp text-sm text-black leading-relaxed">
                  {{ experience.description }}
                </p>
              </div>

              <!-- Main Content Grid -->
              <div class="grid grid-cols-1 lg:grid-cols-2 gap-4">
                <!-- Key Achievements -->
                <div class="space-y-3">
                  <div class="xp-group">
                    <div class="xp-group-title">Key Achievements</div>
                    <div class="xp-panel p-3">
                      <div class="space-y-2">
                        <div
                            v-for="achievement in experience.achievements"
                            :key="achievement"
                            class="xp-button p-2 text-left"
                        >
                          <div class="flex items-start space-x-2">
                            <span class="text-green-600 flex-shrink-0 mt-0.5">✓</span>
                            <span class="font-xp text-xs leading-relaxed">{{ achievement }}</span>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- Technologies Used -->
                <div class="space-y-3">
                  <div class="xp-group">
                    <div class="xp-group-title">Technologies & Tools</div>
                    <div class="xp-panel p-3">
                      <!-- Primary Technologies (first 4) -->
                      <div class="mb-3">
                        <span class="font-xp text-xs text-gray-600 block mb-2">Primary Technologies:</span>
                        <div class="flex flex-wrap gap-1">
                        <span
                            v-for="tech in experience.technologies.slice(0, 4)"
                            :key="tech"
                            class="xp-button-primary px-2 py-1 text-xs font-xp font-bold"
                        >
                          {{ tech }}
                        </span>
                        </div>
                      </div>

                      <!-- Secondary Technologies (remaining) -->
                      <div v-if="experience.technologies.length > 4">
                        <span class="font-xp text-xs text-gray-600 block mb-2">Supporting Technologies:</span>
                        <div class="flex flex-wrap gap-1">
                        <span
                            v-for="tech in experience.technologies.slice(4)"
                            :key="tech"
                            class="xp-button px-2 py-1 text-xs font-xp"
                        >
                          {{ tech }}
                        </span>
                        </div>
                      </div>
                    </div>
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
          <span class="font-xp text-sm">Career Timeline Ready</span>
        </div>
        <div class="flex items-center space-x-4">
          <span class="font-xp text-xs">{{ experiences.length }} Position{{ experiences.length !== 1 ? 's' : '' }}</span>
          <span class="font-xp text-xs">{{ new Set(experiences.flatMap(exp => exp.technologies)).size }} Unique Tech{{ new Set(experiences.flatMap(exp => exp.technologies)).size !== 1 ? 's' : '' }}</span>
          <span class="font-xp text-xs">Professional History</span>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
</style>