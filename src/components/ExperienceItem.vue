<script setup lang="ts">
import {ref, watch} from 'vue'

interface Props {
  role: string
  company: string
  dateCreated: string
  dateModified: string
  achievements: string[]
  isOpen: boolean
  icon: string
}

const props = defineProps<Props>();

const emit = defineEmits<{
  (e: 'update:isOpen', value: boolean): void;
}>();

function toggleOpen() {
  emit('update:isOpen', !props.isOpen);
}

const isLoading = ref(true)
const showAchievements = ref(false)

const formatDate = (dateString: string) => {
  return new Date(dateString).toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
  });
};

watch(
    () => props.isOpen,
    (newVal) => {
      if (newVal) {
        setTimeout(() => {
          isLoading.value = false
          setTimeout(() => {
            showAchievements.value = true
          }, 300)
        }, 800)
      } else {
        isLoading.value = true
        showAchievements.value = false
      }
    },
    { immediate: true }
);
</script>

<template>
  <div class="xp-window max-w-3xl">
    <!-- XP Title Bar with proper styling -->
    <div class="xp-title-bar">
      <div class="flex items-center">
        <span class="w-4 h-4 bg-white rounded-sm mr-2 flex items-center justify-center text-xs">{{ icon }}</span>
        <span class="font-xp-title">{{ role }} - Work Experience Properties</span>
      </div>
      <div class="xp-window-controls">
        <div class="xp-control-btn">_</div>
        <div class="xp-control-btn">□</div>
        <div class="xp-control-btn xp-close-btn" @click="toggleOpen">×</div>
      </div>
    </div>

    <!-- Menu Bar -->
    <div class="xp-menubar mb-4">
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
        <p class="font-xp text-black">Loading work experience data...</p>
      </div>

      <!-- Main Content -->
      <div v-else class="space-y-4">
        <!-- Company Information Group -->
        <div class="xp-group">
          <div class="xp-group-title">Employment Details</div>
          <div class="space-y-3">
            <!-- Company Header -->
            <div class="flex items-center space-x-3 mb-4">
              <div class="w-12 h-12 xp-button flex items-center justify-center text-2xl">
                🏢
              </div>
              <div>
                <h3 class="font-xp text-lg font-bold text-black">{{ company }}</h3>
                <p class="font-xp text-sm text-blue-600 font-bold">{{ role }}</p>
              </div>
            </div>

            <!-- Information Panels -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
              <div class="xp-panel p-3">
                <span class="font-xp text-xs text-gray-600 block mb-1">Position:</span>
                <p class="font-xp text-black font-bold">{{ role }}</p>
              </div>
              <div class="xp-panel p-3">
                <span class="font-xp text-xs text-gray-600 block mb-1">Duration:</span>
                <p class="font-xp text-black font-bold">{{ formatDate(dateCreated) + ' - ' + formatDate(dateModified)}}</p>
              </div>
            </div>

            <!-- Status Indicators -->
<!--            <div class="xp-panel-raised p-3">-->
<!--              <div class="flex items-center justify-between">-->
<!--                <div class="flex items-center space-x-2">-->
<!--                  <div class="w-3 h-3 bg-green-500 rounded-full animate-pulse"></div>-->
<!--                  <span class="font-xp text-sm font-bold text-black">Status: Active Experience</span>-->
<!--                </div>-->
<!--                <div class="flex items-center space-x-1">-->
<!--                  <span class="xp-button px-2 py-1 font-xp text-xs">Professional</span>-->
<!--                  <span class="xp-button px-2 py-1 font-xp text-xs bg-green-100">✓ Verified</span>-->
<!--                </div>-->
<!--              </div>-->
<!--            </div>-->
          </div>
        </div>

        <!-- Achievements Group -->
        <div class="xp-group">
          <div class="xp-group-title">Key Achievements & Responsibilities</div>
          <div class="space-y-3">
            <p class="font-xp text-sm text-black mb-3">
              Major accomplishments and contributions during this role:
            </p>

            <!-- Achievements List with XP styling -->
            <div class="xp-panel xp-scroll max-h-48 overflow-y-auto p-2">
              <div class="space-y-2">
                <div
                    v-for="(achievement, index) in achievements"
                    :key="index"
                    :class="[
                      'xp-button p-3 text-left cursor-pointer transition-all duration-200',
                      showAchievements
                    ]"
                    :style="{ animationDelay: `${index * 100}ms` }"
                >
                  <div class="flex items-start space-x-3">
                    <div class="flex-shrink-0 mt-1">
                      <div class="w-3 h-3 xp-button flex items-center justify-center text-xs">
                        ✓
                      </div>
                    </div>
                    <span class="font-xp text-sm text-black leading-relaxed">{{ achievement }}</span>
                  </div>
                </div>
              </div>
            </div>

            <!-- Achievement Statistics -->
            <div class="grid grid-cols-3 gap-2 mt-4">
              <div class="xp-panel p-2 text-center">
                <div class="font-xp text-lg font-bold text-blue-600">{{ achievements.length }}</div>
                <div class="font-xp text-xs text-gray-600">Achievements</div>
              </div>
              <div class="xp-panel p-2 text-center">
                <div class="font-xp text-lg font-bold text-green-600">100%</div>
                <div class="font-xp text-xs text-gray-600">Completion</div>
              </div>
              <div class="xp-panel p-2 text-center">
                <div class="font-xp text-lg font-bold text-purple-600">A+</div>
                <div class="font-xp text-xs text-gray-600">Performance</div>
              </div>
            </div>
          </div>
        </div>

        <!-- Skills & Technologies (Optional Enhancement) -->
        <div class="xp-group">
          <div class="xp-group-title">Technologies & Skills</div>
          <div class="space-y-2">
            <p class="font-xp text-sm text-black mb-2">
              Technologies and methodologies utilized:
            </p>
            <div class="flex flex-wrap gap-1">
              <span class="xp-button px-2 py-1 font-xp text-xs">Project Management</span>
              <span class="xp-button px-2 py-1 font-xp text-xs">Team Leadership</span>
              <span class="xp-button px-2 py-1 font-xp text-xs">Problem Solving</span>
              <span class="xp-button px-2 py-1 font-xp text-xs">Strategic Planning</span>
            </div>
          </div>
        </div>

        <!-- Action Buttons (XP Dialog Style) -->
<!--        <div class="pt-4 border-t-2 border-gray-400 flex justify-end space-x-2">-->
<!--          <button class="xp-button px-4 py-2 font-xp">-->
<!--            📧 Contact Reference-->
<!--          </button>-->
<!--          <button class="xp-button px-4 py-2 font-xp">-->
<!--            📄 View Details-->
<!--          </button>-->
<!--          <button class="xp-button-primary px-6 py-2 font-xp">-->
<!--            OK-->
<!--          </button>-->
<!--        </div>-->
      </div>

      <!-- XP Status Bar -->
      <div class="xp-status mt-4 flex justify-between items-center">
        <span class="font-xp">{{ company }} experience record loaded</span>
        <div class="flex items-center space-x-4">
          <span class="font-xp text-xs">💼 {{ role }}</span>
          <span class="font-xp text-xs">📈 {{ achievements.length }} achievements</span>
          <span class="font-xp text-xs">🕐 {{ formatDate(dateCreated) + ' - ' + formatDate(dateModified) }}</span>
          <span class="font-xp text-xs">{{ isLoading ? 'Loading' : 'Ready'  }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
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

/* XP-style pulse animation for status indicator */
@keyframes pulse {
  0%, 100% {
    opacity: 1;
  }
  50% {
    opacity: 0.5;
  }
}

.animate-pulse {
  animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
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
  background: linear-gradient(180deg, var(--xp-silver-light) 0%, var(--xp-silver) 50%, var(--xp-silver-dark) 100%);
  border: 1px outset var(--xp-silver-dark);
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .xp-window {
    margin: 1rem;
  }

  .grid-cols-3 {
    grid-template-columns: repeat(1, minmax(0, 1fr));
  }

  .md\:grid-cols-2 {
    grid-template-columns: repeat(1, minmax(0, 1fr));
  }
}
</style>