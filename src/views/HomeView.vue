<script setup lang="ts">
import {ref, onMounted} from 'vue';
import InternetExplorer from '../components/InternetExplorer.vue';
import ResearchExplorer from '../components/ResearchExplorer.vue';
import AboutSection from '../components/AboutSection.vue';
import EducationSection from '../components/EducationSection.vue';
import ContactSection from '../components/ContactSection.vue';
import ProjectExplorer from '../components/ProjectExplorer.vue';
import ExperienceExplorer from '../components/ExperienceExplorer.vue';
import WelcomeNotification from '../components/WelcomeNotification.vue';

// Desktop State Management
const currentTime = ref(new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }));
const isStartMenuOpen = ref(false);
const openWindows = ref<string[]>([]);
const activeWindow = ref<string | null>(null);
const minimizedWindows = ref<string[]>([]);

const skillsList = ref(['VHDL', 'FPGA Design', 'Computer Architecture', 'Python', 'Vue.js', 'Java']);

// Desktop Applications
const desktopApps = ref([
  { id: 'browser',    name: 'My Portfolio', icon: '🌐', x: 20, y: 20 },
  { id: 'about',      name: 'About Me',     icon: '👤', x: 20, y: 100 },
  { id: 'projects',   name: 'My Projects',  icon: '💼', x: 20, y: 180 },
  { id: 'research',   name: 'Research',     icon: '🔬', x: 20, y: 260 },
  { id: 'experience', name: 'Experience',   icon: '🧠', x: 20, y: 340 },
  { id: 'education',  name: 'Education',    icon: '🎓', x: 20, y: 420 },
  { id: 'contact',    name: 'Contact',      icon: '📧', x: 20, y: 500 },
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

const focusWindow = (appId: string) => {
  activeWindow.value = appId;
  if (minimizedWindows.value.includes(appId)) {
    minimizedWindows.value = minimizedWindows.value.filter((id) => id !== appId);
  }
};

const toggleStartMenu = () => {
  isStartMenuOpen.value = !isStartMenuOpen.value;
};

// Update time every minute; auto-open the IE browser on load
onMounted(() => {
  setInterval(() => {
    currentTime.value = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
  }, 60000);
  openWindow('browser');
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

</script>

<template>
  <div class="min-h-screen bg-xp-desktop relative overflow-hidden select-none">

    <!-- Desktop Icons -->
    <div class="absolute inset-0 z-10">
      <div
          v-for="app in desktopApps"
          :key="app.id"
          :style="{ left: app.x + 'px', top: app.y + 'px' }"
          class="absolute w-16 h-20 flex flex-col items-center justify-center cursor-pointer group"
          @click="openWindow(app.id)"
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

      <!-- Internet Explorer Browser Window (auto-opens on load) -->
      <div
          v-if="openWindows.includes('browser')"
          :class="[
          'absolute pointer-events-auto',
          minimizedWindows.includes('browser') ? 'hidden' : '',
          activeWindow === 'browser' ? 'z-30' : 'z-20',
        ]"
          style="left: 90px; top: 4px; right: 8px; height: calc(100vh - 52px);"
          @click="focusWindow('browser')"
      >
        <InternetExplorer
            :isOpen="openWindows.includes('browser')"
            @update:isOpen="
            (val) => {
              if (val) {
                if (!openWindows.includes('browser')) openWindows.push('browser');
              } else {
                const idx = openWindows.indexOf('browser');
                if (idx !== -1) openWindows.splice(idx, 1);
              }
            }
          "
        />
      </div>

      <!-- About Window -->
      <div
          v-if="openWindows.includes('about')"
          :class="[
          'absolute w-4/5 max-w-4xl h-4/5 max-h-3xl',
          'pointer-events-auto',
          minimizedWindows.includes('about') ? 'hidden' : '',
          activeWindow === 'about' ? 'z-30' : 'z-20',
        ]"
          style="left: 10%; top: 1.5%"
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
          style="left: 12%; top: 1.7%"
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
                }
              }
            "
          />
        </div>
      </div>

      <!-- Research / Thesis Window -->
      <div
          v-if="openWindows.includes('research')"
          :class="[
          'absolute w-4/5 max-w-5xl h-4/5',
          'pointer-events-auto',
          minimizedWindows.includes('research') ? 'hidden' : '',
          activeWindow === 'research' ? 'z-30' : 'z-20',
        ]"
          style="left: 10%; top: 2%"
          @click="focusWindow('research')"
      >
        <ResearchExplorer
            :isOpen="openWindows.includes('research')"
            @update:isOpen="
            (val) => {
              if (val) {
                if (!openWindows.includes('research')) openWindows.push('research');
              } else {
                const idx = openWindows.indexOf('research');
                if (idx !== -1) openWindows.splice(idx, 1);
              }
            }
          "
        />
      </div>

      <!-- Experience Window -->
      <div
          v-if="openWindows.includes('experience')"
          :class="[
          'absolute w-4/5 max-w-6xl h-4/5 max-h-3xl',
          'pointer-events-auto',
          minimizedWindows.includes('experience') ? 'hidden' : '',
          activeWindow === 'experience' ? 'z-30' : 'z-20',
        ]"
          style="left: 14%; top: 5.5%"
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
          style="left: 8%; top: 2.1%"
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
          style="left: 16%; top: 3.3%"
          @click="focusWindow('contact')"
      >
        <div class="">
          <ContactSection
              :isOpen="openWindows.includes('contact')"
              @update:isOpen="
              (val) => {
                if (val) {
                  if (!openWindows.includes('contact')) openWindows.push('contact');
                } else {
                  const idx = openWindows.indexOf('contact');
                  if (idx !== -1) openWindows.splice(idx, 1);
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

    <!-- Welcome Notification Component -->
    <WelcomeNotification :duration="10" />

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