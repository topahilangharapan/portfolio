<template>
  <div class="min-h-screen bg-xp-desktop-fallback relative overflow-x-hidden">

    <!-- Main Content -->
    <div class="relative z-10 p-6 pb-14 space-y-6">
      <HeroSection is-open-contact="" is-open-projects=""></HeroSection>

      <ExperienceItem></ExperienceItem>

      <ProjectCard></ProjectCard>

      <EducationSection is-open="" is-open-projects=""></EducationSection>

      <ContactSection is-open=""></ContactSection>

    </div>

    <!-- XP Taskbar -->
    <!-- XP Taskbar -->
    <div class="xp-taskbar">
      <!-- Start Button -->
      <div
          class="xp-start-button cursor-pointer"
          :class="{ 'border-inset': isStartMenuOpen }"
          @click="toggleStartMenu"
      >
        Start
      </div>

      <!-- Taskbar Separator -->
      <div class="w-px h-6 bg-gray-300 mx-1 opacity-50"></div>

      <!-- Open Applications -->
      <div class="flex space-x-1 flex-1 overflow-hidden">
        <div
            v-for="appId in openWindows"
            :key="appId"
            :class="[
        'xp-taskbar-button cursor-pointer flex items-center px-3 py-3 min-w-0 max-w-40',
        activeWindow === appId && !minimizedWindows.includes(appId)
          ? 'xp-taskbar-button-active'
          : 'xp-taskbar-button-inactive',
        minimizedWindows.includes(appId) ? 'xp-taskbar-button-minimized' : ''
      ]"
            @click="focusWindow(appId)"
            :title="getWindowTitle(appId)"
        >
          <span class="mr-2 text-sm flex-shrink-0">{{ getWindowIcon(appId) }}</span>
          <span class="font-xp text-xs truncate">{{ getWindowTitle(appId) }}</span>
        </div>
      </div>

      <!-- System Tray Area -->
      <div class="flex items-center ml-2">
        <!-- Tray Separator -->
        <div class="w-px h-6 bg-gray-300 mx-1 opacity-50"></div>

        <!-- System Tray Icons -->
        <div class="flex items-center space-x-1 px-2">
          <div class="xp-tray-icon cursor-pointer" title="Volume">
            🔊
          </div>
          <div class="xp-tray-icon cursor-pointer" title="Network">
            🌐
          </div>
          <div class="xp-tray-icon cursor-pointer" title="Antivirus">
            🛡️
          </div>
        </div>

        <!-- Clock -->
        <div class="xp-clock px-3 py-3 cursor-pointer" :title="new Date().toLocaleDateString()">
          <div class="font-xp text-xs text-white text-center leading-tight">
            <div>{{ currentTime }}</div>
            <div class="text-10">{{ new Date().toLocaleDateString('en-US', { month: 'short', day: 'numeric' }) }}</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import ExperienceItem from "../components/ExperienceItem.vue";
import ProjectCard from "../components/ProjectCard.vue";
import HeroSection from "../components/HeroSection.vue";
import EducationSection from "../components/EducationSection.vue";
import ContactSection from "../components/ContactSection.vue";

const currentTime = ref('')
const currentDate = ref('')

// Personal Information
const personalInfo = ref({
  name: 'Musthofa Joko Anggoro',
  title: 'Senior Full Stack Developer',
  bio: 'Passionate full stack developer with 6+ years of experience building modern web applications. Specialized in creating scalable solutions using cutting-edge technologies including React, Node.js, and cloud platforms. Strong focus on user experience and clean, maintainable code.',
  email: 'alex.johnson@email.com',
  linkedin: 'https://linkedin.com/in/alexjohnson-dev',
  resume: '/resume-alex-johnson.pdf',
  github: 'https://github.com/alexjohnson'
})

// Education
const education = ref({
  degree: 'Master of Computer Science',
  university: 'Stanford University',
  universityUrl: 'https://stanford.edu',
  duration: '2016 - 2018',
  gpa: 'GPA: 3.9/4.0',
  description: 'Specialized in Distributed Systems and Machine Learning. Completed thesis on "Scalable Microservices Architecture for Real-time Applications." Dean\'s List for 4 consecutive semesters.'
})

// Certification
const certification = ref({
  name: 'AWS Certified Solutions Architect - Professional',
  issuer: 'Amazon Web Services',
  date: 'January 2024',
  icon: '☁️',
  description: 'Advanced certification demonstrating expertise in designing distributed applications and systems on AWS platform. Validates skills in complex multi-tier architectures.',
  verificationUrl: 'https://aws.amazon.com/verification/ALEX-JOHNSON-2024-SAP'
})

// Contact Information
const contactInfo = ref([
  { label: 'Email', icon: '📧', value: 'alex.johnson@email.com' },
  { label: 'Phone', icon: '📱', value: '+1 (555) 123-4567' },
  { label: 'Location', icon: '🌍', value: 'San Francisco, CA' }
])

// Professional Links
const professionalLinks = ref([
  { label: 'LinkedIn', icon: '💼', url: 'https://linkedin.com/in/alexjohnson-dev' },
  { label: 'GitHub', icon: '🐙', url: 'https://github.com/alexjohnson' },
  { label: 'Blog', icon: '✍️', url: 'https://alexjohnson.dev/blog' },
  { label: 'Resume', icon: '📄', url: '/resume-alex-johnson.pdf' }
])

const updateClock = () => {
  const now = new Date()
  currentTime.value = now.toLocaleTimeString('en-US', {
    hour12: true,
    hour: '2-digit',
    minute: '2-digit'
  })
  currentDate.value = now.toLocaleDateString('en-US', {
    month: '2-digit',
    day: '2-digit'
  })
}

const selectText = (event) => {
  event.target.select()
  event.target.setSelectionRange(0, 99999) // For mobile devices
}

let clockInterval

onMounted(() => {
  updateClock()
  clockInterval = setInterval(updateClock, 1000)
})

onUnmounted(() => {
  if (clockInterval) {
    clearInterval(clockInterval)
  }
})
</script>

<style scoped>
/* Text area styling to match XP theme */
textarea {
  font-family: 'MS Sans Serif', sans-serif;
  cursor: text;
}

textarea:focus {
  outline: 1px dotted #000;
  outline-offset: -1px;
}

textarea:hover {
  background-color: #f8f8f8;
}

/* Smooth transitions for interactive elements */
.transition-opacity {
  transition: opacity 0.2s ease;
}

/* Remove hover effects from taskbar quick launch since they're now non-interactive */
.xp-quick-launch-item {
  padding: 2px;
  margin: 1px;
  border: 1px solid transparent;
  cursor: default;
}

/* Print-friendly styles */
@media print {
  .xp-taskbar {
    display: none;
  }

  .fixed {
    position: static !important;
  }

  .bg-xp-desktop {
    display: none;
  }

  textarea {
    border: 1px solid #000 !important;
    background: white !important;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }

  .xp-window {
    break-inside: avoid;
    page-break-inside: avoid;
  }
}

/* Ensure text areas are easily selectable */
textarea {
  user-select: all;
  -webkit-user-select: all;
  -moz-user-select: all;
  -ms-user-select: all;
}
</style>