<script setup lang="ts">
import { ref, watch, computed } from 'vue';

interface Props {
  title: string;
  description: string;
  technologies: string[];
  githubLink: string;
  liveDemoLink: string;
  role: string;
  category: string;
  icon: string;
  dateCreated: string;
  dateModified: string;
  size: string;
  type: string;
  status: 'completed' | 'in-progress' | 'archived';
  skillsAndCompetencies: string[];
  isOpen: boolean;
}

const isLoading = ref(true);
const showDetails = ref(false);

const props = defineProps<Props>();

const emit = defineEmits<{
  (e: 'update:isOpen', value: boolean): void;
}>();

function toggleOpen() {
  emit('update:isOpen', !props.isOpen);
}

const openLink = (url: string) => {
  window.open(url, '_blank', 'noopener,noreferrer');
};

// Computed properties for better data presentation
const statusColor = computed(() => {
  switch (props.status) {
    case 'completed':
      return 'bg-green-500';
    case 'in-progress':
      return 'bg-yellow-500';
    case 'archived':
      return 'bg-gray-500';
    default:
      return 'bg-blue-500';
  }
});

const statusText = computed(() => {
  switch (props.status) {
    case 'completed':
      return 'Project Completed';
    case 'in-progress':
      return 'In Development';
    case 'archived':
      return 'Archived Project';
    default:
      return 'Unknown Status';
  }
});

// const projectAge = computed(() => {
//   const created = new Date(props.dateCreated);
//   const modified = new Date(props.dateModified);
//   const now = new Date();
//
//   const daysSinceCreated = Math.floor((now.getTime() - created.getTime()) / (1000 * 60 * 60 * 24));
//   const daysSinceModified = Math.floor(
//     (now.getTime() - modified.getTime()) / (1000 * 60 * 60 * 24)
//   );
//
//   return {
//     created:
//       daysSinceCreated > 30
//         ? `${Math.floor(daysSinceCreated / 30)} month(s) ago`
//         : `${daysSinceCreated} day(s) ago`,
//     modified:
//       daysSinceModified > 30
//         ? `${Math.floor(daysSinceModified / 30)} month(s) ago`
//         : `${daysSinceModified} day(s) ago`,
//   };
// });

// const complexityScore = computed(() => {
//   // Simple algorithm to assess project complexity based on tech stack and size
//   const techCount = props.technologies.length;
//   const sizeMultiplier = props.size === 'large' ? 3 : props.size === 'medium' ? 2 : 1;
//   const typeMultiplier = props.type === 'full-stack' ? 2.5 : props.type === 'frontend' ? 1.5 : 2;
//
//   const score = Math.min(Math.floor((techCount * sizeMultiplier * typeMultiplier) / 2), 5);
//   return score;
// });

const primaryTechnologies = computed(() => {
  // Show first 3 technologies as primary, rest as secondary
  return props.technologies.slice(0, 3);
});

const secondaryTechnologies = computed(() => {
  return props.technologies.slice(3);
});

watch(
  () => props.isOpen,
  (newVal) => {
    if (newVal) {
      setTimeout(() => {
        isLoading.value = false;
        setTimeout(() => {
          showDetails.value = true;
        }, 300);
      }, 800);
    } else {
      isLoading.value = true;
      showDetails.value = false;
    }
  },
  { immediate: true }
);
</script>

<template>
  <div class="xp-window max-w-2xl">
    <!-- XP Title Bar -->
    <div class="xp-title-bar flex-shrink-0">
      <div class="flex items-center">
        <span class="w-4 h-4 bg-white rounded-sm mr-2 flex items-center justify-center text-xs">{{
          icon
        }}</span>
        <span class="font-xp-title truncate">{{ title }} - Project Properties</span>
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

    <!-- XP Window Content -->
    <div class="p-4 bg-xp-window">
      <!-- Loading State (XP Style) -->
      <div v-if="isLoading" class="text-center py-8">
        <div class="xp-progress w-64 mx-auto mb-4">
          <div class="xp-progress-bar animate-xp-loading w-full"></div>
        </div>
        <p class="font-xp text-black">Loading project data...</p>
      </div>

      <div v-else class="space-y-4">
        <!-- Project Header -->
        <div class="flex items-center space-x-3 mb-4">
          <div class="w-12 h-12 xp-button flex items-center justify-center text-2xl">
            {{ icon }}
          </div>
          <div class="flex-1">
            <h3 class="font-xp text-lg font-bold text-black">{{ title }}</h3>
            <div class="flex items-center space-x-2">
              <span class="font-xp text-sm text-blue-600 font-bold">{{ role }}</span>
              <span class="text-gray-400">•</span>
              <span class="font-xp text-sm text-gray-600">{{ category }}</span>
            </div>
          </div>
          <div class="flex items-center space-x-2">
            <div :class="['w-3 h-3 rounded-full', statusColor]"></div>
            <span class="font-xp text-xs">{{ status.toUpperCase() }}</span>
          </div>
        </div>

        <!-- Project Overview Stats -->
        <div class="grid grid-cols-2 md:grid-cols-3 gap-2 mb-4">
          <div class="xp-panel p-2 text-center">
            <div class="font-xp text-lg font-bold text-blue-600">{{ type.toUpperCase() }}</div>
            <div class="font-xp text-xs text-gray-600">Type</div>
          </div>
          <div class="xp-panel p-2 text-center">
            <div class="font-xp text-lg font-bold text-green-600">{{ size.toUpperCase() }}</div>
            <div class="font-xp text-xs text-gray-600">Scale</div>
          </div>
<!--          <div class="xp-panel p-2 text-center">-->
<!--            <div class="font-xp text-lg font-bold text-purple-600">-->
<!--              {{ '★'.repeat(complexityScore) }}{{ '☆'.repeat(5 - complexityScore) }}-->
<!--            </div>-->
<!--            <div class="font-xp text-xs text-gray-600">Complexity</div>-->
<!--          </div>-->
          <div class="xp-panel p-2 text-center">
            <div class="font-xp text-lg font-bold text-orange-600">{{ technologies.length }}</div>
            <div class="font-xp text-xs text-gray-600">Technologies</div>
          </div>
        </div>

        <!-- Project Content Section -->
        <div class="flex-1 space-y-2 sm:space-y-4 overflow-y-auto">
          <!-- Project Description -->
          <div class="xp-group">
            <div class="xp-group-title">Project Overview & My Contribution</div>
            <div class="xp-panel-raised p-2 sm:p-3">
              <p class="font-xp text-black leading-relaxed text-sm sm:text-base mb-3">
                {{ description }}
              </p>
              <div class="xp-panel p-2">
                <div class="flex items-center space-x-2">
                  <span class="w-2 h-2 bg-blue-500 rounded-full"></span>
                  <span class="font-xp text-sm font-bold text-black">My Role: {{ role }}</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Technical Implementation -->
          <div class="xp-group">
            <div class="xp-group-title">Technical Implementation</div>
            <div class="space-y-3">
              <!-- Primary Technologies -->
              <div class="xp-panel p-2 sm:p-3">
                <span class="font-xp text-xs text-gray-600 block mb-2">Core Technologies:</span>
                <div class="flex flex-wrap gap-1 sm:gap-2">
                  <span
                    v-for="tech in primaryTechnologies"
                    :key="tech"
                    class="xp-button-primary px-2 sm:px-3 py-1 font-xp text-xs font-bold"
                  >
                    {{ tech }}
                  </span>
                </div>
              </div>

              <!-- Secondary Technologies (if any) -->
              <div v-if="secondaryTechnologies.length > 0" class="xp-panel p-2 sm:p-3">
                <span class="font-xp text-xs text-gray-600 block mb-2"
                  >Supporting Technologies:</span
                >
                <div class="flex flex-wrap gap-1 sm:gap-2">
                  <span
                    v-for="tech in secondaryTechnologies"
                    :key="tech"
                    class="xp-button px-2 sm:px-3 py-1 font-xp text-xs"
                  >
                    {{ tech }}
                  </span>
                </div>
              </div>

              <!-- Project Architecture Info -->
              <!--              <div class="grid grid-cols-1 md:grid-cols-2 gap-3">-->
              <!--                <div class="xp-panel p-2 sm:p-3">-->
              <!--                  <span class="font-xp text-xs text-gray-600 block mb-1">Architecture:</span>-->
              <!--                  <p class="font-xp text-black font-bold text-sm">{{ type }} Application</p>-->
              <!--                </div>-->
              <!--                <div class="xp-panel p-2 sm:p-3">-->
              <!--                  <span class="font-xp text-xs text-gray-600 block mb-1">Project Scale:</span>-->
              <!--                  <p class="font-xp text-black font-bold text-sm">{{ size }} Project</p>-->
              <!--                </div>-->
              <!--              </div>-->
            </div>
          </div>

          <!-- Project Timeline & Maintenance -->
          <!--          <div class="xp-group">-->
          <!--            <div class="xp-group-title">Development Timeline</div>-->
          <!--            <div class="grid grid-cols-1 md:grid-cols-2 gap-3">-->
          <!--              <div class="xp-panel p-2 sm:p-3">-->
          <!--                <span class="font-xp text-xs text-gray-600 block mb-1">Started:</span>-->
          <!--                <p class="font-xp text-black font-bold text-sm">{{ projectAge.created }}</p>-->
          <!--                <p class="font-xp text-xs text-gray-500">{{ new Date(dateCreated).toLocaleDateString() }}</p>-->
          <!--              </div>-->
          <!--              <div class="xp-panel p-2 sm:p-3">-->
          <!--                <span class="font-xp text-xs text-gray-600 block mb-1">Last Updated:</span>-->
          <!--                <p class="font-xp text-black font-bold text-sm">{{ projectAge.modified }}</p>-->
          <!--                <p class="font-xp text-xs text-gray-500">{{ new Date(dateModified).toLocaleDateString() }}</p>-->
          <!--              </div>-->
          <!--            </div>-->
          <!--          </div>-->

          <!-- Skills Demonstrated -->
          <div class="xp-group" :class="showDetails && 'animate-fade-in'">
            <div class="xp-group-title">Skills & Competencies Demonstrated</div>
            <div class="xp-panel xp-scroll max-h-32 overflow-y-auto p-2">
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
                <div
                  v-for="skillAndCompetency in skillsAndCompetencies"
                  :key="skillAndCompetency"
                  class="xp-button p-2 text-left"
                >
                  <div class="flex items-center space-x-2">
                    <span class="text-green-600">✓</span>
                    <span class="font-xp text-xs">{{ skillAndCompetency }}</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Action Buttons Section -->
        <div class="flex space-x-2 sm:space-x-3 flex-shrink-0">
          <!-- Source Code Button -->
          <button
            @click="openLink(githubLink)"
            class="w-full xp-button p-2 sm:p-3 font-xp flex items-center justify-center space-x-2 text-sm sm:text-base hover:bg-gray-100"
          >
            <svg class="w-3 h-3 sm:w-4 sm:h-4" fill="currentColor" viewBox="0 0 20 20">
              <path
                fill-rule="evenodd"
                d="M10 0C4.477 0 0 4.484 0 10.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0110 4.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.203 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.942.359.31.678.921.678 1.856 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0020 10.017C20 4.484 15.522 0 10 0z"
                clip-rule="evenodd"
              />
            </svg>
            <span>Review Source Code</span>
          </button>

          <!-- Live Demo Button -->
          <button
            @click="openLink(liveDemoLink)"
            class="w-full xp-button-primary p-2 sm:p-3 font-xp flex items-center justify-center space-x-2 text-sm sm:text-base"
          >
            <svg
              class="w-3 h-3 sm:w-4 sm:h-4"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"
              />
            </svg>
            <span>Experience Live Demo</span>
          </button>
        </div>
      </div>
      <!-- Enhanced XP Status Bar -->
      <div class="xp-status mt-4 flex justify-between items-center">
        <div class="flex items-center space-x-2">
          <div :class="['w-2 h-2 rounded-full', statusColor]"></div>
          <span class="font-xp text-xs sm:text-sm">{{ statusText }}</span>
        </div>
        <div class="flex items-center space-x-2 sm:space-x-4">
          <span class="font-xp text-xs">{{ type.toUpperCase() }}</span>
          <span class="font-xp text-xs"
            >{{ technologies.length }} Tech{{ technologies.length !== 1 ? 's' : '' }}</span
          >
<!--          <span class="font-xp text-xs">{{ complexityScore }}/5 ★</span>-->
          <span class="font-xp text-xs">{{ isLoading ? 'Loading' : 'Ready' }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* Responsive height transitions */
.xp-window {
  transition:
    height 0.3s ease-in-out,
    min-height 0.3s ease-in-out,
    max-height 0.3s ease-in-out;
}

/* Ensure proper spacing for the content sections */
.xp-group:first-child {
  margin-top: 0;
}

/* Mobile responsive adjustments */
@media (max-width: 640px) {
  .xp-window {
    min-width: 280px;
  }

  .xp-progress {
    width: 200px !important;
  }

  .grid-cols-2 {
    grid-template-columns: repeat(1, minmax(0, 1fr));
  }

  .md\:grid-cols-4 {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

/* Ensure content doesn't overflow on smaller screens */
@media (max-height: 600px) {
  .xp-window:not(.h-32) {
    max-height: 90vh;
  }
}

/* XP Loading Animation */
@keyframes xp-loading {
  0% {
    background-position: 0% 0%;
  }
  100% {
    background-position: 100% 0%;
  }
}

.animate-xp-loading {
  background-image: repeating-linear-gradient(
    45deg,
    #4a9eff 0px,
    #4a9eff 10px,
    #0054e3 10px,
    #0054e3 20px
  );
  background-size: 40px 100%;
  animation: xp-loading 2s linear infinite;
}

/* Fade-in animation for achievements */
@keyframes fade-in {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-fade-in {
  animation: fade-in 0.5s ease-out forwards;
  opacity: 0;
}

/* Custom scrollbar for achievements list */
.xp-scroll::-webkit-scrollbar {
  width: 17px;
}

.xp-scroll::-webkit-scrollbar-track {
  background: var(--xp-silver-dark);
  border: 1px inset var(--xp-silver-dark);
}

.xp-scroll::-webkit-scrollbar-thumb {
  background: linear-gradient(
    180deg,
    var(--xp-silver-light) 0%,
    var(--xp-silver) 50%,
    var(--xp-silver-dark) 100%
  );
  border: 1px outset var(--xp-silver-dark);
}

/* Status indicator pulse animation */
@keyframes pulse {
  0%,
  100% {
    opacity: 1;
  }
  50% {
    opacity: 0.5;
  }
}

.animate-pulse {
  animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}
</style>
