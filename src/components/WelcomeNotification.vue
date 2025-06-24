<template>
  <div
      v-if="isVisible"
      class="fixed bottom-16 right-6 w-80 z-50 pointer-events-auto"
      :class="{ 'animate-slide-in': showAnimation, 'animate-slide-out': hideAnimation }"
  >
    <!-- Windows XP Notification Window -->
    <div class="xp-window shadow-2xl">
      <!-- Title Bar -->
      <div class="xp-title-bar flex-shrink-0">
        <div class="flex items-center">
          <span class="w-4 h-4 bg-white rounded-sm mr-2 flex items-center justify-center text-xs"
          >💡</span
          >
          <span class="font-xp-title">Portfolio Guide</span>
        </div>
        <div class="xp-window-controls">
          <div class="xp-control-btn">_</div>
          <div class="xp-control-btn">□</div>
          <div class="xp-control-btn xp-close-btn" @click="closeNotification">×</div>
        </div>
      </div>

      <!-- Content Area -->
      <div class="bg-xp-window p-4">
        <!-- Header -->
        <div class="flex items-center mb-3">
          <div class="w-8 h-8 rounded-full flex items-center justify-center mr-3">
            <span class="text-white text-lg">ℹ️</span>
          </div>
          <div>
            <h3 class="font-xp font-bold text-sm text-gray-800">Welcome to my Portfolio!</h3>
            <p class="font-xp text-xs text-gray-600">Learn how to navigate</p>
          </div>
        </div>

        <!-- Instructions -->
        <div class="space-y-2 text-xs font-xp">
          <div class="flex items-start">
            <span class="text-blue-600 mr-2 font-bold">•</span>
            <span class="text-gray-700">
              <strong>Double-click</strong> desktop icons to open applications
            </span>
          </div>
          <div class="flex items-start">
            <span class="text-blue-600 mr-2 font-bold">•</span>
            <span class="text-gray-700">
              Click <strong>"Start"</strong> button for quick access menu
            </span>
          </div>
          <div class="flex items-start">
            <span class="text-blue-600 mr-2 font-bold">•</span>
            <span class="text-gray-700">
              Use <strong>taskbar</strong> to switch between open windows
            </span>
          </div>
          <div class="flex items-start">
            <span class="text-blue-600 mr-2 font-bold">•</span>
            <span class="text-gray-700">
              Check out the <strong>Hero section</strong> on the top right
            </span>
          </div>
        </div>

        <!-- Progress Bar -->
        <div class="mt-4">
          <div class="flex items-center justify-between mb-1">
            <span class="font-xp text-xs text-gray-600">Auto-close in:</span>
            <span class="font-xp text-xs text-gray-800 font-bold">{{ timeLeft }}s</span>
          </div>
          <div class="xp-progress">
            <div
                class="xp-progress-bar transition-all duration-[1000ms] ease-linear"
                :style="{ width: progressWidth + '%' }"
            ></div>
          </div>
        </div>

        <!-- Action Buttons -->
        <div class="flex justify-end space-x-2 mt-4">
          <button
              class="xp-button px-3 py-1 text-xs"
              @click="closeNotification"
          >
            Got it!
          </button>
          <button
              class="xp-button px-3 py-1 text-xs"
              @click="extendTime"
              v-if="timeLeft <= 3"
          >
            +10s
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue';

// Props
interface Props {
  duration?: number; // Duration in seconds (default: 10)
}

const props = withDefaults(defineProps<Props>(), {
  duration: 10
});

// Reactive state
const isVisible = ref(false);
const showAnimation = ref(false);
const hideAnimation = ref(false);
const timeLeft = ref(props.duration);
const progressWidth = ref(100);

let interval: NodeJS.Timeout | null = null;

// Methods
const startTimer = () => {
  interval = setInterval(() => {
    timeLeft.value--;
    progressWidth.value = (timeLeft.value / props.duration) * 100;

    if (timeLeft.value <= 0) {
      closeNotification();
    }
  }, 1000);
};

const closeNotification = () => {
  hideAnimation.value = true;
  showAnimation.value = false;

  setTimeout(() => {
    isVisible.value = false;
    if (interval) {
      clearInterval(interval);
      interval = null;
    }
  }, 300);
};

const extendTime = () => {
  timeLeft.value += 10;
  progressWidth.value = (timeLeft.value / (props.duration + 10)) * 100;
};

const showNotification = () => {
  isVisible.value = true;
  showAnimation.value = true;
  hideAnimation.value = false;

  // Start the countdown timer
  // setTimeout(() => {
  //   startTimer();
  // }, 500); // Small delay to let animation finish
  startTimer()
};

// Lifecycle
onMounted(() => {
  // Show notification after a brief delay
  setTimeout(() => {
    showNotification();
  }, 500);
});

onUnmounted(() => {
  if (interval) {
    clearInterval(interval);
  }
});

// Expose methods for parent component
defineExpose({
  showNotification,
  closeNotification
});
</script>

<style scoped>
/* Animation Classes */
.animate-slide-in {
  animation: slideIn 0.4s ease-out forwards;
}

.animate-slide-out {
  animation: slideOut 0.3s ease-in forwards;
}

@keyframes slideIn {
  from {
    transform: translateX(100%) translateY(20px);
    opacity: 0;
  }
  to {
    transform: translateX(0) translateY(0);
    opacity: 1;
  }
}

@keyframes slideOut {
  from {
    transform: translateX(0) translateY(0);
    opacity: 1;
  }
  to {
    transform: translateX(100%) translateY(-20px);
    opacity: 0;
  }
}

/* Custom shadow for notification */
.shadow-2xl {
  box-shadow: 4px 4px 8px rgba(0, 0, 0, 0.3);
}
</style>