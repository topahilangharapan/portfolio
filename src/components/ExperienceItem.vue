<script setup lang="ts">
import { ref, watch, nextTick } from 'vue'

interface Props {
  role: string
  company: string
  dateCreated: string
  dateModified: string
  achievements: string[]
  technologies: string[]
  type: string
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
const scrollContainer = ref<HTMLElement | null>(null);
const isScrolledToBottom = ref(false);
const showScrollIndicator = ref(false);

const formatDate = (dateString: string) => {
  return new Date(dateString).toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
  });
};

// Enhanced scroll handling
const handleScroll = () => {
  if (!scrollContainer.value) return;

  const { scrollTop, scrollHeight, clientHeight } = scrollContainer.value;

  // Check if scrolled to bottom (within 5px tolerance)
  isScrolledToBottom.value = scrollTop + clientHeight >= scrollHeight - 5;

  // Show scroll indicator if there's more content below
  showScrollIndicator.value = !isScrolledToBottom.value && scrollHeight > clientHeight;
};

// Auto-scroll to top when opening
const scrollToTop = () => {
  if (scrollContainer.value) {
    scrollContainer.value.scrollTop = 0;
  }
};

watch(
    () => props.isOpen,
    async (newVal) => {
      if (newVal) {
        setTimeout(() => {
          isLoading.value = false
          setTimeout(async () => {
            await nextTick();
            scrollToTop();
            // Check scroll after content loads
            setTimeout(() => {
              handleScroll();
            }, 100);
          }, 300)
        }, 800)
      } else {
        isLoading.value = true
        isScrolledToBottom.value = false;
        showScrollIndicator.value = false;
      }
    },
    { immediate: true }
);
</script>

<template>
  <div class="xp-window max-w-2xl max-h-[70vh] flex flex-col relative">
    <!-- XP Title Bar with proper styling -->
    <div class="xp-title-bar flex-shrink-0">
      <div class="flex items-center">
        <span class="w-4 h-4 bg-white rounded-sm mr-2 flex items-center justify-center text-xs">{{ icon }}</span>
        <span class="font-xp-title truncate">{{ role }} - Work Experience Properties</span>
      </div>
      <div class="xp-window-controls">
        <div class="xp-control-btn">_</div>
        <div class="xp-control-btn">□</div>
        <div class="xp-control-btn xp-close-btn" @click="toggleOpen">×</div>
      </div>
    </div>

    <!-- Menu Bar -->
    <div class="xp-menubar flex-shrink-0">
      <span class="xp-menu-item inline-block">File</span>
      <span class="xp-menu-item inline-block">Edit</span>
      <span class="xp-menu-item inline-block">View</span>
      <span class="xp-menu-item inline-block">Navigate</span>
      <span class="xp-menu-item inline-block">Help</span>
    </div>

    <!-- XP Window Content -->
    <div class="flex-1 flex flex-col p-4 bg-xp-window overflow-hidden">
      <!-- Loading State (XP Style) -->
      <div v-if="isLoading" class="flex-1 flex items-center justify-center">
        <div class="text-center">
          <div class="xp-progress w-64 mx-auto mb-4">
            <div class="xp-progress-bar animate-xp-loading w-full"></div>
          </div>
          <p class="font-xp text-black">Loading work experience data...</p>
        </div>
      </div>

      <!-- Main Content -->
      <div v-else class="flex-1 flex flex-col space-y-4 overflow-hidden">
        <!-- Company Header - Fixed at top -->
        <div class="flex items-center space-x-3 flex-shrink-0">
          <div class="w-12 h-12 xp-button flex items-center justify-center text-2xl">
            🏢
          </div>
          <div class="flex-1">
            <h3 class="font-xp text-lg font-bold text-black">{{ company }}</h3>
            <p class="font-xp text-sm text-blue-600 font-bold">{{ role }}</p>
          </div>
          <div class="flex items-center space-x-2">
<!--            <div class="w-3 h-3 bg-green-500 rounded-full animate-pulse"></div>-->
            <span class="font-xp"> {{ type }}</span>
          </div>
        </div>

        <!-- Duration and Position Info - Fixed -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-3 flex-shrink-0">
          <div class="xp-panel p-3">
            <span class="font-xp text-xs text-gray-600 block mb-1">Position:</span>
            <p class="font-xp text-black font-bold">{{ role }}</p>
          </div>
          <div class="xp-panel p-3">
            <span class="font-xp text-xs text-gray-600 block mb-1">Duration:</span>
            <p class="font-xp text-black font-bold">{{ formatDate(dateCreated) + ' - ' + formatDate(dateModified)}}</p>
          </div>
        </div>

        <!-- Enhanced Scrollable Content Section -->
        <div class="flex-1 relative overflow-hidden">
          <!-- Main scrollable content -->
          <div
              class="h-full space-y-4 overflow-y-auto pr-2 xp-scroll scroll-smooth"
          >
            <!-- Achievements Group -->
            <div class="xp-group">
              <div class="xp-group-title">Key Achievements & Responsibilities</div>
              <div class="space-y-3">

                <!-- Achievements List with enhanced styling -->
                <div class="space-y-2">
                  <div
                      v-for="(achievement, index) in achievements"
                      :key="index"
                      :class="[
                        'xp-button p-3 text-left'
                      ]"
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
            </div>

            <!-- Skills & Technologies -->
            <div class="xp-group">
              <div class="xp-group-title">Technologies & Skills</div>
              <div class="space-y-2">
                <div class="flex flex-wrap gap-1 sm:gap-2">
                  <span
                      v-for="tech in technologies"
                      :key="tech"
                      class="xp-button px-2 sm:px-3 py-1 font-xp text-xs"
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

    <!-- Enhanced XP Status Bar -->
    <div class="xp-status flex-shrink-0 flex justify-between items-center">
      <span class="font-xp text-xs sm:text-sm">{{ company }} experience record loaded</span>
      <div class="flex items-center space-x-2 sm:space-x-4">
        <span class="font-xp text-xs">💼 {{ role }}</span>
        <span class="font-xp text-xs">📈 {{ achievements.length }} achievements</span>
        <span class="font-xp text-xs">{{ isLoading ? 'Loading' : 'Ready'  }}</span>
        <!-- Scroll indicator in status bar -->
        <span v-if="showScrollIndicator" class="font-xp text-xs text-blue-600">↓ More</span>
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

  .space-x-4 {
    gap: 0.5rem;
  }

  .space-x-2 {
    gap: 0.25rem;
  }
}

/* Scroll smooth behavior */
.scroll-smooth {
  scroll-behavior: smooth;
}
</style>