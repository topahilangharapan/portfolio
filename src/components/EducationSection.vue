<script setup lang="ts">
// Education data
import {ref, watch} from "vue";

const education = {
  university: 'University of Indonesia (UI)',
  faculty: 'Faculty of Computer Science (Fasilkom)',
  degree: 'Bachelor of Computer Science',
  major: 'Information Systems',
  expectedGraduation: 'June 2026',
  currentSemester: '7th Semester',
  gpa: 3.84,
  maxGpa: 4,
  relevantCourses: [
    'Data Structures and Algorithms',
    'Enterprise Application Architecture and Programming',
    'Information Systems Development Project',
    'Introduction to AI & Data Science',
    'Databases',
    'Data Communication Networks',
    'Operating System for Information System',
    'Introduction to Computer Architecture',
  ],
  achievements: [
    'Vice Person in Charge of UI/UX COMPFEST',
    'Mentor of Programming Foundations 0',
  ]
}

const progressWidth = ref('0%')

interface Props {
  isOpen: boolean;
}

const props = defineProps<Props>();
const emit = defineEmits<{
  (e: 'update:isOpen', value: boolean): void;
}>();

watch(
    () => props.isOpen,
    (newVal) => {
      if (newVal) {
        setTimeout(() => {
          progressWidth.value = `${(education.gpa / education.maxGpa) * 100}%`
        }, 500)
      } else {
        progressWidth.value = '0%';
      }
    },
    { immediate: true }
);

function toggleOpen() {
  emit('update:isOpen', !props.isOpen);
}
</script>

<template>
  <div class="container mx-auto px-4 py-8 h-screen flex items-center justify-center">
    <!-- XP Window Container - 3/4 screen height -->
    <div class="xp-window max-w-5xl mx-auto h-2/4 flex flex-col">
      <!-- XP Title Bar -->
      <div class="xp-title-bar flex-shrink-0">
        <div class="flex items-center">
          <span class="w-4 h-4 bg-white rounded-sm mr-2 flex items-center justify-center text-xs">🎓</span>
          <span class="font-xp-title">Education Information - Student Properties</span>
        </div>
        <div class="xp-window-controls">
          <div class="xp-control-btn">_</div>
          <div class="xp-control-btn">□</div>
          <div class="xp-control-btn xp-close-btn" @click="toggleOpen">×</div>
        </div>
      </div>

      <!-- Menu Bar - Fixed at top -->
      <div class="xp-menubar mb-0 flex-shrink-0">
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
            <!-- Main Education Info -->
            <div class="space-y-4">
              <!-- Academic Information Group -->
              <div class="xp-group">
                <div class="xp-group-title">Academic Information</div>
                <div class="space-y-4">
                  <div>
                    <h3 class="font-xp text-lg font-bold text-black mb-1">{{ education.university }}</h3>
                    <p class="font-xp text-blue-600 font-bold">{{ education.faculty }}</p>
                  </div>

                  <!-- Information Grid -->
                  <div class="grid grid-cols-2 gap-3">
                    <div class="xp-panel p-2">
                      <span class="font-xp text-xs text-gray-600 block">Degree:</span>
                      <p class="font-xp text-black font-bold text-sm">{{ education.degree }}</p>
                    </div>
                    <div class="xp-panel p-2">
                      <span class="font-xp text-xs text-gray-600 block">Major:</span>
                      <p class="font-xp text-black font-bold text-sm">{{ education.major }}</p>
                    </div>
                    <div class="xp-panel p-2">
                      <span class="font-xp text-xs text-gray-600 block">Expected Graduation:</span>
                      <p class="font-xp text-black font-bold text-sm">{{ education.expectedGraduation }}</p>
                    </div>
                    <div class="xp-panel p-2">
                      <span class="font-xp text-xs text-gray-600 block">Current Status:</span>
                      <p class="font-xp text-black font-bold text-sm">{{ education.currentSemester }}</p>
                    </div>
                  </div>

                  <!-- GPA Progress -->
                  <div class="xp-panel p-3">
                    <div class="flex items-center justify-between mb-2">
                      <span class="font-xp font-bold text-black">Current GPA:</span>
                      <span class="font-xp text-lg font-bold text-blue-600">
                        {{ `${education.gpa.toFixed(2)} / ${education.maxGpa.toFixed(2)}` }}
                      </span>
                    </div>
                    <div class="xp-progress">
                      <div
                          class="xp-progress-bar transition-all duration-[2000ms] ease-out"
                          :style="{ width: progressWidth }"
                      ></div>
                    </div>
                    <div class="flex justify-between mt-1">
                      <span class="font-xp text-xs text-gray-600">0.00</span>
                      <span class="font-xp text-xs text-gray-600">4.00</span>
                    </div>
                  </div>
                </div>
              </div>

              <!-- Achievements Group -->
              <div class="xp-group">
                <div class="xp-group-title">Academic Achievements</div>
                <div class="space-y-2">
                  <div
                      v-for="(achievement, index) in education.achievements"
                      :key="index"
                      class="flex items-start space-x-3 p-2 hover:bg-blue-50 cursor-pointer"
                  >
                    <div class="w-4 h-4 xp-button flex items-center justify-center text-xs mt-0.5">
                      ★
                    </div>
                    <span class="font-xp text-black text-sm">{{ achievement }}</span>
                  </div>
                </div>
              </div>
            </div>

            <!-- Relevant Courses -->
            <div>
              <div class="xp-group h-full">
                <div class="xp-group-title">Relevant Coursework</div>
                <div class="space-y-4">
                  <p class="font-xp text-sm text-black">
                    Key courses that have shaped my technical foundation and programming skills:
                  </p>

                  <!-- Course List -->
                  <div class="xp-panel xp-scroll max-h-60 overflow-y-auto p-2">
                    <div class="space-y-1">
                      <div
                          v-for="(course, index) in education.relevantCourses"
                          :key="index"
                          class="xp-button p-2 text-left hover:bg-blue-100 cursor-pointer transition-colors duration-100"
                      >
                        <div class="flex items-center space-x-2">
                          <div class="w-2 h-2 bg-green-500 rounded-full"></div>
                          <span class="font-xp text-sm">{{ course }}</span>
                        </div>
                      </div>
                    </div>
                  </div>

                  <!-- Course Categories -->
                  <div class="space-y-3">
                    <div>
                      <h4 class="font-xp font-bold text-black text-sm mb-2">📚 Core Programming</h4>
                      <div class="flex flex-wrap gap-1">
                        <span class="xp-button px-2 py-1 font-xp text-xs">Data Structures</span>
                        <span class="xp-button px-2 py-1 font-xp text-xs">Algorithms</span>
                        <span class="xp-button px-2 py-1 font-xp text-xs">OOP</span>
                      </div>
                    </div>

                    <div>
                      <h4 class="font-xp font-bold text-black text-sm mb-2">🌐 Web & Mobile</h4>
                      <div class="flex flex-wrap gap-1">
                        <span class="xp-button px-2 py-1 font-xp text-xs">Web Programming</span>
                        <span class="xp-button px-2 py-1 font-xp text-xs">Mobile Development</span>
                      </div>
                    </div>

                    <div>
                      <h4 class="font-xp font-bold text-black text-sm mb-2">⚙️ Systems</h4>
                      <div class="flex flex-wrap gap-1">
                        <span class="xp-button px-2 py-1 font-xp text-xs">Database Systems</span>
                        <span class="xp-button px-2 py-1 font-xp text-xs">Operating Systems</span>
                        <span class="xp-button px-2 py-1 font-xp text-xs">Networks</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Statistics Panel -->
          <div class="mt-6 pt-4 border-t-2 border-gray-400">
            <div class="grid md:grid-cols-3 gap-4">
              <div class="xp-panel p-4 text-center">
                <div class="font-xp text-2xl font-bold text-blue-600 mb-1">6</div>
                <div class="font-xp text-xs text-gray-600">Semesters Completed</div>
              </div>
              <div class="xp-panel p-4 text-center">
                <div class="font-xp text-2xl font-bold text-green-600 mb-1">117+</div>
                <div class="font-xp text-xs text-gray-600">Credit Hours</div>
              </div>
              <div class="xp-panel p-4 text-center">
                <div class="font-xp text-2xl font-bold text-purple-600 mb-1">2026</div>
                <div class="font-xp text-xs text-gray-600">Expected Graduation</div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- XP Status Bar - Fixed at bottom -->
      <div class="xp-status flex justify-between items-center flex-shrink-0">
        <span class="font-xp">Student record loaded successfully</span>
        <div class="flex items-center space-x-4">
          <span class="font-xp text-xs">🎓 Academic Year: 2022-2026</span>
          <span class="font-xp text-xs">📊 GPA: {{ education.gpa.toFixed(2) }}</span>
          <span class="font-xp text-xs">Ready</span>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.container {
  max-width: 1200px;
}

/* Custom XP Loading Animation for Progress Bar */
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
  animation: xp-loading 3s linear infinite;
}

/* Override progress bar for XP style */
.xp-progress-bar {
  background: linear-gradient(180deg, var(--xp-light-blue) 0%, var(--xp-blue) 100%);
  position: relative;
}

.xp-progress-bar::after {
  content: '';
  position: absolute;
  top: 1px;
  left: 0;
  right: 0;
  height: 1px;
  background: rgba(255, 255, 255, 0.5);
}
</style>