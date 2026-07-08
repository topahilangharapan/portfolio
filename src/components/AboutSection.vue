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
              <!-- Research Summary -->
              <div class="xp-group">
                <div class="xp-group-title">Research Summary</div>
                <div class="xp-panel-raised p-4">
                  <p class="font-xp text-black leading-relaxed">
                    I am a Computer Architecture researcher fascinated by the gap between theoretical
                    models and physical hardware. My undergraduate thesis demonstrates a complete
                    RTL-to-FPGA pipeline — translating the Mano register-transfer model into a
                    synthesisable VHDL-93 architecture running at 58.648 MHz on a Xilinx Spartan-3AN FPGA.
                  </p>
                  <p class="font-xp text-black leading-relaxed mt-4">
                    Beyond hardware, I have a strong foundation in software engineering and AI/ML,
                    which gives me the ability to bridge low-level hardware design with higher-level
                    systems. I am pursuing a PhD to deepen my research in digital hardware architecture,
                    FPGA-based systems, and EDA methodologies. I believe in rigorous, reproducible
                    research and enjoy making complex engineering problems approachable and elegant.
                  </p>
                </div>
              </div>

              <!-- Research Interests -->
              <div class="xp-group">
                <div class="xp-group-title">Research Interests</div>
                <div class="xp-panel p-3">
                  <div class="flex flex-wrap gap-2">
                    <span class="research-chip">FPGA Design</span>
                    <span class="research-chip">Computer Architecture</span>
                    <span class="research-chip">Digital Hardware Design</span>
                    <span class="research-chip">EDA & Synthesis</span>
                    <span class="research-chip">VHDL / RTL Design</span>
                    <span class="research-chip">Register-Transfer Level</span>
                    <span class="research-chip">AI / Machine Learning</span>
                  </div>
                </div>
              </div>

              <!-- Core Strengths -->
              <div class="xp-group">
                <div class="xp-group-title">Core Strengths</div>
                <div class="xp-panel p-3">
                  <div class="space-y-2">
                    <div class="flex items-start">
                      <div class="w-3 h-3 xp-button flex items-center justify-center text-xs mr-3 mt-0.5">*</div>
                      <span class="font-xp text-black">VHDL-93 Hierarchical Hardware Design</span>
                    </div>
                    <div class="flex items-start">
                      <div class="w-3 h-3 xp-button flex items-center justify-center text-xs mr-3 mt-0.5">*</div>
                      <span class="font-xp text-black">FPGA Synthesis, Timing Analysis & Implementation</span>
                    </div>
                    <div class="flex items-start">
                      <div class="w-3 h-3 xp-button flex items-center justify-center text-xs mr-3 mt-0.5">*</div>
                      <span class="font-xp text-black">Systematic Gap Analysis & Research Methodology</span>
                    </div>
                    <div class="flex items-start">
                      <div class="w-3 h-3 xp-button flex items-center justify-center text-xs mr-3 mt-0.5">*</div>
                      <span class="font-xp text-black">Full-Stack Software Engineering (Vue.js, Spring Boot, Python)</span>
                    </div>
                    <div class="flex items-start">
                      <div class="w-3 h-3 xp-button flex items-center justify-center text-xs mr-3 mt-0.5">*</div>
                      <span class="font-xp text-black">Machine Learning & Data Science (Scikit-Learn)</span>
                    </div>
                    <div class="flex items-start">
                      <div class="w-3 h-3 xp-button flex items-center justify-center text-xs mr-3 mt-0.5">*</div>
                      <span class="font-xp text-black">Solid Computer Science Foundation</span>
                    </div>
                    <div class="flex items-start">
                      <div class="w-3 h-3 xp-button flex items-center justify-center text-xs mr-3 mt-0.5">*</div>
                      <span class="font-xp text-black">Leadership & Technical Mentoring</span>
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
                        <span class="xp-button px-3 py-1 font-xp text-xs">VHDL-93</span>
                        <span class="xp-button px-3 py-1 font-xp text-xs">Python</span>
                        <span class="xp-button px-3 py-1 font-xp text-xs">Java</span>
                        <span class="xp-button px-3 py-1 font-xp text-xs">TypeScript</span>
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
                        <span class="xp-button px-3 py-1 font-xp text-xs">Xilinx ISE</span>
                        <span class="xp-button px-3 py-1 font-xp text-xs">Vue.js</span>
                        <span class="xp-button px-3 py-1 font-xp text-xs">Spring Boot</span>
                        <span class="xp-button px-3 py-1 font-xp text-xs">React.js</span>
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
                <div class="font-xp text-lg font-bold text-blue-600 mb-2">📚 Currently Exploring</div>
                <div class="font-xp text-sm text-black">Advanced EDA Tools, RISC-V Architecture, Hardware Security</div>
              </div>
              <div class="xp-panel p-4 text-center">
                <div class="font-xp text-lg font-bold text-green-600 mb-2">💡 Research Interests</div>
                <div class="font-xp text-sm text-black">FPGA Design, Computer Architecture, Digital Hardware, AI Systems</div>
              </div>
              <div class="xp-panel p-4 text-center">
                <div class="font-xp text-lg font-bold text-purple-600 mb-2">🎯 Career Goal</div>
                <div class="font-xp text-sm text-black">PhD Researcher in Computer Architecture & FPGA Systems</div>
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
          <span class="font-xp text-xs">🔬 PhD Aspirant</span>
          <span class="font-xp text-xs">🎓 UI Fasilkom 2026</span>
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

</style>