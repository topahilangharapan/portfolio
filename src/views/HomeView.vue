<script setup lang="ts">
import {ref, reactive, onMounted, watch} from 'vue';
import HeroSection from '../components/HeroSection.vue';
import AboutSection from '../components/AboutSection.vue';
import EducationSection from '../components/EducationSection.vue';
import ContactSection from '../components/ContactSection.vue';
import ProjectExplorer from '../components/ProjectExplorer.vue';
import ExperienceExplorer from '../components/ExperienceExplorer.vue';

// Desktop State Management
const currentTime = ref(new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }));
const isStartMenuOpen = ref(false);
const openWindows = ref<string[]>([]);
const activeWindow = ref<string | null>(null);
const minimizedWindows = ref<string[]>([]);

const isOpenContact = ref(false);
const isOpenProjects = ref(false);

const skillsList = ref(['JavaScript/TypeScript', 'Vue.js']);

const contactInfo = reactive({
  email: 'rahmat.pratama@ui.ac.id',
  linkedin: 'https://linkedin.com/in/rahmat-pratama-ui',
  github: 'https://github.com/rahmatpratama-ui',
  phone: '+62 812-3456-7890',
});

// Desktop Applications (removed 'hero' from the list)
const desktopApps = ref([
  { id: 'about', name: 'About Me', icon: '👤', x: 20, y: 20 },
  { id: 'projects', name: 'My Projects', icon: '💼', x: 20, y: 100 },
  { id: 'experience', name: 'Experience', icon: '🏢', x: 20, y: 180 },
  { id: 'education', name: 'Education', icon: '🎓', x: 20, y: 260 },
  { id: 'contact', name: 'Contact', icon: '📧', x: 20, y: 340 },
]);

// Window Management Functions
const openWindow = (appId: string) => {
  if (!openWindows.value.includes(appId)) {
    openWindows.value.push(appId);
  }
  activeWindow.value = appId;
  if (minimizedWindows.value.includes(appId)) {
    minimizedWindows.value = minimizedWindows.value.filter((id) => id !== appId);
  }
  isStartMenuOpen.value = false;
};

// const closeWindow = (appId: string) => {
//   openWindows.value = openWindows.value.filter((id) => id !== appId);
//   minimizedWindows.value = minimizedWindows.value.filter((id) => id !== appId);
//   if (activeWindow.value === appId) {
//     activeWindow.value = openWindows.value[openWindows.value.length - 1] || null;
//   }
// };
//
// const minimizeWindow = (appId: string) => {
//   if (!minimizedWindows.value.includes(appId)) {
//     minimizedWindows.value.push(appId);
//   }
//   if (activeWindow.value === appId) {
//     const remainingWindows = openWindows.value.filter((id) => !minimizedWindows.value.includes(id));
//     activeWindow.value = remainingWindows[remainingWindows.length - 1] || null;
//   }
// };

const focusWindow = (appId: string) => {
  activeWindow.value = appId;
  if (minimizedWindows.value.includes(appId)) {
    minimizedWindows.value = minimizedWindows.value.filter((id) => id !== appId);
  }
};

const toggleStartMenu = () => {
  isStartMenuOpen.value = !isStartMenuOpen.value;
};

// Update time every minute
onMounted(() => {
  setInterval(() => {
    currentTime.value = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
  }, 60000);
});

// Get window title
const getWindowTitle = (appId: string) => {
  const app = desktopApps.value.find((a) => a.id === appId);
  return app ? app.name : 'Application';
};

// Get window icon
const getWindowIcon = (appId: string) => {
  const app = desktopApps.value.find((a) => a.id === appId);
  return app ? app.icon : '📄';
};

watch(isOpenContact, (newVal) => {
  if (newVal) {
    openWindow('contact')
  } else {
    const idx = openWindows.value.indexOf('contact');
    if (idx !== -1) openWindows.value.splice(idx, 1);
  }
})

watch(isOpenProjects, (newVal) => {
  if (newVal) {
    openWindow('projects')
  } else {
    const idx = openWindows.value.indexOf('projects');
    if (idx !== -1) openWindows.value.splice(idx, 1);
  }
})
</script>

<template>
  <div class="min-h-screen bg-xp-desktop relative overflow-hidden select-none">
    <!-- Static Hero Section - Top Right -->
    <div class="absolute right-2 z-20 pointer-events-auto">
      <div class="">
        <HeroSection
          v-model:isOpenContact="isOpenContact"
          v-model:isOpenProjects="isOpenProjects"
        />
      </div>
    </div>

    <!-- Desktop Icons -->
    <div class="absolute inset-0 z-10">
      <div
        v-for="app in desktopApps"
        :key="app.id"
        :style="{ left: app.x + 'px', top: app.y + 'px' }"
        class="absolute w-16 h-20 flex flex-col items-center justify-center cursor-pointer group"
        @dblclick="openWindow(app.id)"
      >
        <div
          class="w-12 h-12 bg-white border-2 border-gray-400 flex items-center justify-center text-2xl mb-1 group-hover:bg-blue-100 group-active:border-inset"
        >
          {{ app.icon }}
        </div>
        <span class="font-xp text-xs text-white text-center text-shadow leading-tight">
          {{ app.name }}
        </span>
      </div>
    </div>

    <!-- Windows Container -->
    <div class="absolute inset-0 z-20 pointer-events-none">
      <!-- About Window -->
      <div
        v-if="openWindows.includes('about')"
        :class="[
          'absolute w-4/5 max-w-4xl h-4/5 max-h-3xl',
          'pointer-events-auto',
          minimizedWindows.includes('about') ? 'hidden' : '',
          activeWindow === 'about' ? 'z-30' : 'z-20',
        ]"
        style="left: 10%; top: 10%"
        @click="focusWindow('about')"
      >
        <div class="">
          <AboutSection
            :skills="skillsList"
            :isOpen="openWindows.includes('about')"
            @update:isOpen="
              (val) => {
                if (val) {
                  if (!openWindows.includes('about')) openWindows.push('about');
                } else {
                  const idx = openWindows.indexOf('about');
                  if (idx !== -1) openWindows.splice(idx, 1);
                }
              }
            "
          />
        </div>
      </div>

      <!-- Projects Window -->
      <div
        v-if="openWindows.includes('projects')"
        :class="[
          'absolute w-4/5 max-w-5xl h-4/5 max-h-4xl',
          'pointer-events-auto',
          minimizedWindows.includes('projects') ? 'hidden' : '',
          activeWindow === 'projects' ? 'z-30' : 'z-20',
        ]"
        style="left: 12%; top: 8%"
        @click="focusWindow('projects')"
      >
        <div>
          <ProjectExplorer
            :isOpen="openWindows.includes('projects')"
            @update:isOpen="
              (val) => {
                if (val) {
                  if (!openWindows.includes('projects')) openWindows.push('projects');
                } else {
                  const idx = openWindows.indexOf('projects');
                  if (idx !== -1) openWindows.splice(idx, 1);
                  isOpenProjects = false;
                }
              }
            "
          />
        </div>
      </div>

      <!-- Experience Window -->
      <div
        v-if="openWindows.includes('experience')"
        :class="[
          'absolute w-4/5 max-w-4xl h-4/5 max-h-3xl',
          'pointer-events-auto',
          minimizedWindows.includes('experience') ? 'hidden' : '',
          activeWindow === 'experience' ? 'z-30' : 'z-20',
        ]"
        style="left: 14%; top: 12%"
        @click="focusWindow('experience')"
      >
        <div class="xp-scroll">
          <ExperienceExplorer
            :isOpen="openWindows.includes('experience')"
            @update:isOpen="
              (val) => {
                if (val) {
                  if (!openWindows.includes('experience')) openWindows.push('experience');
                } else {
                  const idx = openWindows.indexOf('experience');
                  if (idx !== -1) openWindows.splice(idx, 1);
                }
              }
            "
          />
        </div>
      </div>

      <!-- Education Window -->
      <div
        v-if="openWindows.includes('education')"
        :class="[
          'absolute w-4/5 max-w-5xl h-4/5 max-h-4xl',
          'pointer-events-auto',
          minimizedWindows.includes('education') ? 'hidden' : '',
          activeWindow === 'education' ? 'z-30' : 'z-20',
        ]"
        style="left: 8%; top: 6%"
        @click="focusWindow('education')"
      >
        <div class="">
          <EducationSection
            :isOpen="openWindows.includes('education')"
            @update:isOpen="
              (val) => {
                if (val) {
                  if (!openWindows.includes('education')) openWindows.push('education');
                } else {
                  const idx = openWindows.indexOf('education');
                  if (idx !== -1) openWindows.splice(idx, 1);
                }
              }
            "
          />
        </div>
      </div>

      <!-- Contact Window -->
      <div
        v-if="openWindows.includes('contact')"
        :class="[
          'absolute w-4/5 max-w-3xl h-3/5 max-h-2xl',
          'pointer-events-auto',
          minimizedWindows.includes('contact') ? 'hidden' : '',
          activeWindow === 'contact' ? 'z-30' : 'z-20',
        ]"
        style="left: 16%; top: 15%"
        @click="focusWindow('contact')"
      >
        <div class="">
          <ContactSection
            :contact-info="contactInfo"
            :isOpen="openWindows.includes('contact')"
            @update:isOpen="
              (val) => {
                if (val) {
                  if (!openWindows.includes('contact')) openWindows.push('contact');
                } else {
                  const idx = openWindows.indexOf('contact');
                  if (idx !== -1) openWindows.splice(idx, 1);
                  isOpenContact = false;
                }
              }
            "
          />
        </div>
      </div>
    </div>

    <!-- Start Menu -->
    <div v-if="isStartMenuOpen" class="absolute bottom-8 left-1 w-80 xp-window z-40">
      <div class="xp-title-bar">
        <span class="font-xp-title">Portfolio Applications</span>
      </div>
      <div class="bg-xp-window p-2">
        <div class="space-y-1">
          <div
            v-for="app in desktopApps"
            :key="app.id"
            class="xp-menu-item flex items-center p-2 cursor-pointer"
            @click="openWindow(app.id)"
          >
            <span class="text-lg mr-3">{{ app.icon }}</span>
            <span class="font-xp">{{ app.name }}</span>
          </div>
        </div>
        <div class="border-t border-gray-400 mt-2 pt-2">
          <div class="xp-menu-item flex items-center p-2 cursor-pointer">
            <span class="text-lg mr-3">🔧</span>
            <span class="font-xp">Settings</span>
          </div>
          <div class="xp-menu-item flex items-center p-2 cursor-pointer">
            <span class="text-lg mr-3">📁</span>
            <span class="font-xp">My Documents</span>
          </div>
        </div>
      </div>
    </div>

    <!-- XP Taskbar -->
    <div class="xp-taskbar">
      <!-- Start Button -->
      <div class="xp-start-button" @click="toggleStartMenu">Start</div>

      <!-- Taskbar Separator -->
      <div class="w-px h-6 bg-gray-600 mx-2"></div>

      <!-- Open Applications -->
      <div class="flex space-x-1 flex-1">
        <div
          v-for="appId in openWindows"
          :key="appId"
          :class="[
            'xp-button px-3 py-1 text-xs flex items-center cursor-pointer',
            activeWindow === appId && !minimizedWindows.includes(appId)
              ? 'border-inset bg-blue-200'
              : '',
            minimizedWindows.includes(appId) ? 'opacity-75' : '',
          ]"
          @click="focusWindow(appId)"
        >
          <span class="mr-1">{{ getWindowIcon(appId) }}</span>
          <span class="font-xp truncate max-w-24">{{ getWindowTitle(appId) }}</span>
        </div>
      </div>

      <!-- System Tray -->
      <div class="flex items-center space-x-4 ml-4">
        <div class="xp-panel px-2 py-1">
          <span class="font-xp text-xs">🔊</span>
        </div>
        <div class="xp-panel px-2 py-1">
          <span class="font-xp text-xs">🌐</span>
        </div>
        <div class="xp-panel px-3 py-1">
          <span class="font-xp text-xs">{{ currentTime }}</span>
        </div>
      </div>
    </div>

    <!-- Click outside to close start menu -->
    <div v-if="isStartMenuOpen" class="fixed inset-0 z-30" @click="isStartMenuOpen = false"></div>
  </div>
</template>

<style scoped>
/* Custom XP Desktop Styles */
.text-shadow {
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.8);
}

/* XP Window z-index management */
.z-30 {
  z-index: 30;
}

.z-40 {
  z-index: 40;
}

.z-50 {
  z-index: 50;
}

/* Custom scrollbar for windows */
.xp-scroll {
  scrollbar-width: thin;
  scrollbar-color: var(--xp-silver-dark) var(--xp-silver);
}

/* Desktop icon hover effects */
.group:hover .group-hover\:bg-blue-100 {
  background-color: rgba(59, 130, 246, 0.1);
}

.group:active .group-active\:border-inset {
  border-style: inset;
}

.xp-window {
  transition:
    transform 0.2s ease,
    opacity 0.2s ease;
}

.xp-window:not(.hidden) {
  animation: windowOpen 0.3s ease-out;
}

@keyframes windowOpen {
  from {
    transform: scale(0.8);
    opacity: 0;
  }
  to {
    transform: scale(1);
    opacity: 1;
  }
}

/* Start menu animation */
.absolute.bottom-8 {
  animation: startMenuOpen 0.2s ease-out;
}

@keyframes startMenuOpen {
  from {
    transform: translateY(100%);
    opacity: 0;
  }
  to {
    transform: translateY(0);
    opacity: 1;
  }
}

/* Static Hero Section Styles */
.absolute.top-4.right-4 {
  position: fixed; /* Make it truly static */
}
</style>
