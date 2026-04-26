<script setup lang="ts">
import aboutData from '../data/portfolio/about.json';

interface Props {
  skills: string[];
  isOpen: boolean;
}

interface SkillCategory {
  title: string;
  dotClass: string;
  items: string[];
}

interface AdditionalInfoCard {
  title: string;
  value: string;
  titleClass: string;
}

interface AboutData {
  professionalSummary: string[];
  coreStrengths: string[];
  technicalSkills: SkillCategory[];
  additionalInfo: AdditionalInfoCard[];
  statusBar: {
    right: string[];
  };
}

const about = aboutData as AboutData;

const props = defineProps<Props>();
const emit = defineEmits<{
  (e: 'update:isOpen', value: boolean): void;
}>();

function toggleOpen() {
  emit('update:isOpen', !props.isOpen);
}
</script>

<template>
  <div class="container mx-auto px-4 py-8 h-screen items-center justify-center">
    <!-- XP Window Container - Fixed at 3/4 screen height -->
    <div class="xp-window max-w-5xl mx-auto h-[70vh] flex flex-col">
      <!-- XP Title Bar -->
      <div class="xp-title-bar flex-shrink-0">
        <div class="flex items-center">
          <span class="w-4 h-4 bg-white rounded-sm mr-2 flex items-center justify-center text-xs"
          >👤</span
          >
          <span class="font-xp-title">About Me - Personal Profile Properties</span>
        </div>
        <div class="xp-window-controls">
          <div class="xp-control-btn">_</div>
          <div class="xp-control-btn">□</div>
          <div class="xp-control-btn xp-close-btn" @click="toggleOpen">×</div>
        </div>
      </div>

      <!-- Menu Bar - Fixed at top -->
      <div class="xp-menubar flex-shrink-0">
        <span class="xp-menu-item inline-block">File</span>
        <span class="xp-menu-item inline-block">Edit</span>
        <span class="xp-menu-item inline-block">View</span>
        <span class="xp-menu-item inline-block">Navigate</span>
        <span class="xp-menu-item inline-block">Help</span>
      </div>

      <!-- Scrollable Content Area -->
      <div class="flex-1 overflow-hidden bg-xp-window">
        <div class="xp-scroll h-full overflow-y-auto p-4">
          <div class="grid lg:grid-cols-2 gap-6">
            <!-- About Text Section -->
            <div class="space-y-4">
              <!-- Professional Summary -->
              <div class="xp-group">
                <div class="xp-group-title">Professional Summary</div>
                <div class="xp-panel-raised p-4">
                  <p
                    v-for="(paragraph, index) in about.professionalSummary"
                    :key="index"
                    class="font-xp text-black leading-relaxed"
                    :class="{ 'mt-4': index > 0 }"
                  >
                    {{ paragraph }}
                  </p>
                </div>
              </div>

              <!-- Core Strengths -->
              <div class="xp-group">
                <div class="xp-group-title">Core Strengths</div>
                <div class="xp-panel p-3">
                  <div class="space-y-2">
                    <div v-for="strength in about.coreStrengths" :key="strength" class="flex items-start">
                      <div
                        class="w-3 h-3 xp-button flex items-center justify-center text-xs mr-3 mt-0.5"
                      >
                        *
                      </div>
                      <span class="font-xp text-black">{{ strength }}</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Technical Skills Section -->
            <div>
              <div class="xp-group">
                <div class="xp-group-title">Technical Skills Inventory</div>
                <div class="xp-panel p-3">
                  <div class="space-y-4">
                    <!-- Programming Languages -->
                    <div v-for="category in about.technicalSkills" :key="category.title">
                      <h4 class="font-xp font-bold text-black text-sm mb-2 flex items-center">
                        <span class="w-3 h-3 rounded-sm mr-2" :class="category.dotClass"></span>
                        {{ category.title }}
                      </h4>
                      <div class="flex flex-wrap gap-2">
                        <span
                          v-for="item in category.items"
                          :key="item"
                          class="xp-button px-3 py-1 font-xp text-xs"
                        >
                          {{ item }}
                        </span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Additional Information Panel -->
          <div class="mt-6 pt-4 border-t-2 border-gray-400">
            <div class="grid md:grid-cols-3 gap-4">
              <div v-for="card in about.additionalInfo" :key="card.title" class="xp-panel p-4 text-center">
                <div class="font-xp text-lg font-bold mb-2" :class="card.titleClass">{{ card.title }}</div>
                <div class="font-xp text-sm text-black">{{ card.value }}</div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- XP Status Bar - Fixed at bottom -->
      <div class="xp-status flex-shrink-0 flex justify-between items-center">
        <div class="flex items-center space-x-2">
          <span class="w-2 h-2 bg-green-500 rounded-full"></span>
          <span class="font-xp">Profile loaded successfully</span>
        </div>
        <div class="flex items-center space-x-4">
          <span v-for="item in about.statusBar.right" :key="item" class="font-xp text-xs">{{ item }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.container {
  max-width: 1200px;
}

/* Enhanced progress bar animation */
.xp-progress-bar {
  transition: width 2s cubic-bezier(0.4, 0, 0.2, 1);
}

</style>
