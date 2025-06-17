<script setup lang="ts">

interface Props {
  skills: string[];
  isOpen: boolean;
}

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
                  <p class="font-xp text-black leading-relaxed">
                    I'm someone who truly enjoys learning, especially when it opens up new
                    perspectives about the world and how things work. That's what led me to fall in
                    love with computers. For me, programming is more than just writing code, it's an
                    art form, a blend of creativity and logic to solve real-world problems.
                  </p>
                  <p class="font-xp text-black leading-relaxed mt-4">
                    Every line of code I write is a reflection of my thought process and effort, so I
                    always strive to give my best. I see myself as a professional who takes pride in
                    his work, but I also like to keep things relaxed and fun. It's how I stay grounded
                    and keep learning with joy.
                  </p>
                </div>
              </div>

              <!-- Core Strengths -->
              <div class="xp-group">
                <div class="xp-group-title">Core Strengths</div>
                <div class="xp-panel p-3">
                  <div class="space-y-2">
                    <div class="flex items-start">
                      <div
                          class="w-3 h-3 xp-button flex items-center justify-center text-xs mr-3 mt-0.5"
                      >
                        *
                      </div>
                      <span class="font-xp text-black">Full-Stack Web Development</span>
                    </div>
                    <div class="flex items-start">
                      <div
                          class="w-3 h-3 xp-button flex items-center justify-center text-xs mr-3 mt-0.5"
                      >
                        *
                      </div>
                      <span class="font-xp text-black">RESTful API Design & Integration</span>
                    </div>
                    <div class="flex items-start">
                      <div
                          class="w-3 h-3 xp-button flex items-center justify-center text-xs mr-3 mt-0.5"
                      >
                        *
                      </div>
                      <span class="font-xp text-black">Database Design & Optimization</span>
                    </div>
                    <div class="flex items-start">
                      <div
                          class="w-3 h-3 xp-button flex items-center justify-center text-xs mr-3 mt-0.5"
                      >
                        *
                      </div>
                      <span class="font-xp text-black">Responsive UI & UX Implementation</span>
                    </div>
                    <div class="flex items-start">
                      <div
                          class="w-3 h-3 xp-button flex items-center justify-center text-xs mr-3 mt-0.5"
                      >
                        *
                      </div>
                      <span class="font-xp text-black">CI/CD & DevOps Practices</span>
                    </div>
                    <div class="flex items-start">
                      <div
                          class="w-3 h-3 xp-button flex items-center justify-center text-xs mr-3 mt-0.5"
                      >
                        *
                      </div>
                      <span class="font-xp text-black">Leadership in Engineering Projects</span>
                    </div>
                    <div class="flex items-start">
                      <div
                          class="w-3 h-3 xp-button flex items-center justify-center text-xs mr-3 mt-0.5"
                      >
                        *
                      </div>
                      <span class="font-xp text-black">Solid Computer Science Foundation</span>
                    </div>
                    <div class="flex items-start">
                      <div
                          class="w-3 h-3 xp-button flex items-center justify-center text-xs mr-3 mt-0.5"
                      >
                        *
                      </div>
                      <span class="font-xp text-black">Determination and Hopes & Dreams</span>
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
                    <div>
                      <h4 class="font-xp font-bold text-black text-sm mb-2 flex items-center">
                        <span class="w-3 h-3 bg-blue-500 rounded-sm mr-2"></span>
                        Programming Languages
                      </h4>
                      <div class="flex flex-wrap gap-2">
                        <span class="xp-button px-3 py-1 font-xp text-xs">Java</span>
                        <span class="xp-button px-3 py-1 font-xp text-xs">Python</span>
                        <span class="xp-button px-3 py-1 font-xp text-xs">TypeScript</span>
                        <span class="xp-button px-3 py-1 font-xp text-xs">C</span>
                        <span class="xp-button px-3 py-1 font-xp text-xs">C++</span>
                        <span class="xp-button px-3 py-1 font-xp text-xs">Assembly</span>
                        <span class="xp-button px-3 py-1 font-xp text-xs">Golang</span>
                      </div>
                    </div>

                    <!-- Frontend Technologies -->
                    <div>
                      <h4 class="font-xp font-bold text-black text-sm mb-2 flex items-center">
                        <span class="w-3 h-3 bg-green-500 rounded-sm mr-2"></span>
                        Frameworks
                      </h4>
                      <div class="flex flex-wrap gap-2">
                        <span class="xp-button px-3 py-1 font-xp text-xs">Vue.js</span>
                        <span class="xp-button px-3 py-1 font-xp text-xs">Angular</span>
                        <span class="xp-button px-3 py-1 font-xp text-xs">React.js</span>
                        <span class="xp-button px-3 py-1 font-xp text-xs">Spring Boot</span>
                        <span class="xp-button px-3 py-1 font-xp text-xs">Django</span>
                      </div>
                    </div>

                    <!-- Database & Tools -->
                    <div>
                      <h4 class="font-xp font-bold text-black text-sm mb-2 flex items-center">
                        <span class="w-3 h-3 bg-purple-500 rounded-sm mr-2"></span>
                        Database & Tools
                      </h4>
                      <div class="flex flex-wrap gap-2">
                        <span class="xp-button px-3 py-1 font-xp text-xs">PostgreSQL</span>
                        <span class="xp-button px-3 py-1 font-xp text-xs">MongoDB</span>
                        <span class="xp-button px-3 py-1 font-xp text-xs">Git/GitHub</span>
                        <span class="xp-button px-3 py-1 font-xp text-xs">Docker</span>
                        <span class="xp-button px-3 py-1 font-xp text-xs">Kubernetes</span>
                      </div>
                    </div>

                    <!-- Operating System -->
                    <div>
                      <h4 class="font-xp font-bold text-black text-sm mb-2 flex items-center">
                        <span class="w-3 h-3 bg-yellow-500 rounded-sm mr-2"></span>
                        Operating Systems
                      </h4>
                      <div class="flex flex-wrap gap-2">
                        <span class="xp-button px-3 py-1 font-xp text-xs">Windows</span>
                        <span class="xp-button px-3 py-1 font-xp text-xs">Linux</span>
                        <span class="xp-button px-3 py-1 font-xp text-xs">Unix</span>
                      </div>
                    </div>

                    <!-- ML -->
                    <div>
                      <h4 class="font-xp font-bold text-black text-sm mb-2 flex items-center">
                        <span class="w-3 h-3 bg-red-500 rounded-sm mr-2"></span>
                        AI/ML
                      </h4>
                      <div class="flex flex-wrap gap-2">
                        <span class="xp-button px-3 py-1 font-xp text-xs">Model Development (Sci-Kit Learn)</span>
                        <span class="xp-button px-3 py-1 font-xp text-xs">Data Preprocessing</span>
                        <span class="xp-button px-3 py-1 font-xp text-xs">Supervised & Unsupervised Learning</span>
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
              <div class="xp-panel p-4 text-center">
                <div class="font-xp text-lg font-bold text-blue-600 mb-2">📚 Currently Learning</div>
                <div class="font-xp text-sm text-black">Machine Learning, AWS, Microservices</div>
              </div>
              <div class="xp-panel p-4 text-center">
                <div class="font-xp text-lg font-bold text-green-600 mb-2">💡 Interests</div>
                <div class="font-xp text-sm text-black">AI/ML, Cloud Computing, Distributed Systems</div>
              </div>
              <div class="xp-panel p-4 text-center">
                <div class="font-xp text-lg font-bold text-purple-600 mb-2">🎯 Career Goal</div>
                <div class="font-xp text-sm text-black">Software Engineer that inspire a lot of people</div>
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
          <span class="font-xp text-xs">💼 CS Student</span>
          <span class="font-xp text-xs">🎓 UI 2022-2026</span>
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

/* Enhanced progress bar animation */
.xp-progress-bar {
  transition: width 2s cubic-bezier(0.4, 0, 0.2, 1);
}

/* Scrollable content area enhancements */
.xp-scroll {
  scrollbar-width: thin;
}
</style>