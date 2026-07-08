<script setup lang="ts">
import { ref } from 'vue';

const isMinimized = ref(false);

const researchChips = ['FPGA Design', 'VHDL-93', 'Computer Architecture', 'EDA', 'RTL Design'];
const relevantCourses = ['Computer Architecture', 'AI & Data Science', 'Enterprise Architecture', 'Databases'];

function downloadCV() {
  window.open('/CV_Musthofa Joko Anggoro.pdf', '_blank');
}
</script>

<template>
  <div class="xp-window w-full h-full flex flex-col">

    <!-- Title Bar -->
    <div class="xp-title-bar flex items-center justify-between flex-shrink-0">
      <div class="flex items-center gap-1">
        <span class="text-sm">🎓</span>
        <span class="font-xp-title text-xs">Academic Profile</span>
      </div>
      <button
        class="xp-control-btn w-4 h-4 text-xs flex items-center justify-center"
        title="Minimize"
        @click="isMinimized = !isMinimized"
      >_</button>
    </div>

    <!-- Scrollable body -->
    <div v-show="!isMinimized" class="flex-1 overflow-y-auto bg-xp-window p-2 space-y-2 xp-scroll">

      <!-- 1. Identity -->
      <div class="xp-panel-raised p-3">
        <p class="font-xp font-bold text-black" style="font-size: 13px;">Musthofa Joko Anggoro</p>
        <p class="font-xp font-bold" style="font-size: 11px; color: var(--xp-dark-blue);">
          Computer Architecture Researcher · PhD Aspirant
        </p>
        <p class="font-xp text-gray-600" style="font-size: 10px; margin-top: 2px;">
          Universitas Indonesia · Fasilkom · Information Systems
        </p>
      </div>

      <!-- 2. Quick Actions -->
      <div class="flex flex-wrap gap-1">
        <button
          class="xp-button flex items-center gap-1"
          style="font-size: 11px;"
          @click="downloadCV"
        >
          📄 Download CV
        </button>
        <a
          href="mailto:musthofaja.topa@gmail.com"
          class="xp-button flex items-center gap-1"
          style="font-size: 11px; text-decoration: none; color: inherit;"
        >
          📧 Email
        </a>
        <a
          href="https://www.linkedin.com/in/musthofa-joko-anggoro/"
          target="_blank"
          rel="noopener noreferrer"
          class="xp-button flex items-center gap-1"
          style="font-size: 11px; text-decoration: none; color: inherit;"
        >
          🔗 LinkedIn
        </a>
        <a
          href="https://github.com/topahilangharapan"
          target="_blank"
          rel="noopener noreferrer"
          class="xp-button flex items-center gap-1"
          style="font-size: 11px; text-decoration: none; color: inherit;"
        >
          💻 GitHub
        </a>
      </div>

      <!-- 3. Current Research -->
      <div class="xp-group">
        <div class="xp-group-title">Current Research</div>
        <div class="p-2 space-y-2">
          <div class="xp-panel p-2">
            <p class="font-xp font-bold text-black leading-snug" style="font-size: 11px;">
              Bridging the Gap Between the Mano Register-Transfer Model and FPGA Realization
              Through a Synthesisable VHDL-93 Architecture
            </p>
            <p class="font-xp mt-1" style="font-size: 10px; color: var(--xp-dark-blue); font-weight: bold;">
              ⚡ 58.648 MHz on Xilinx Spartan-3AN FPGA
            </p>
          </div>
          <p class="font-xp text-gray-600" style="font-size: 10px;">
            Supervised by <span class="font-bold text-black">Prof. Dr. Ir. Petrus Mursanto, M.Sc.</span>
          </p>
          <div class="flex flex-wrap gap-1">
            <span v-for="chip in researchChips" :key="chip" class="research-chip">{{ chip }}</span>
          </div>
        </div>
      </div>

      <!-- 4. Education -->
      <div class="xp-group">
        <div class="xp-group-title">Education</div>
        <div class="p-2 space-y-2">
          <div class="flex items-start gap-2">
            <span style="font-size: 16px; flex-shrink: 0;">🎓</span>
            <div>
              <p class="font-xp font-bold text-black" style="font-size: 11px;">University of Indonesia, Fasilkom</p>
              <p class="font-xp text-gray-700" style="font-size: 10px;">
                Bachelor of Computer Science · Information Systems
              </p>
              <p class="font-xp text-gray-600" style="font-size: 10px;">
                Expected Graduation: June 2026
              </p>
            </div>
          </div>
          <!-- GPA Bar -->
          <div>
            <div class="flex justify-between mb-1">
              <span class="font-xp font-bold text-black" style="font-size: 11px;">GPA</span>
              <span class="font-xp font-bold" style="font-size: 11px; color: var(--xp-dark-blue);">3.85 / 4.00</span>
            </div>
            <div class="xp-progress" style="height: 12px;">
              <div class="xp-progress-bar" style="width: 96.25%;"></div>
            </div>
          </div>
          <!-- Thesis badge -->
          <div class="xp-panel-raised p-1 flex items-center gap-1">
            <span style="font-size: 12px;">🔬</span>
            <span class="font-xp text-gray-700" style="font-size: 10px;">
              Thesis: FPGA Architecture Implementation ·
              <span class="font-bold" style="color: #2e7d32;">✓ Completed 2026</span>
            </span>
          </div>
          <!-- Relevant Courses -->
          <div>
            <p class="font-xp text-gray-600 mb-1" style="font-size: 10px;">Key Courses:</p>
            <div class="flex flex-wrap gap-1">
              <span
                v-for="course in relevantCourses"
                :key="course"
                class="xp-button cursor-default"
                style="font-size: 10px; padding: 1px 5px;"
              >{{ course }}</span>
            </div>
          </div>
        </div>
      </div>

      <!-- 5. Experience -->
      <div class="xp-group">
        <div class="xp-group-title">Experience</div>
        <div class="p-2 space-y-2">

          <!-- Entry 1 -->
          <div class="xp-panel p-2">
            <div class="flex items-start justify-between gap-1">
              <p class="font-xp font-bold text-black" style="font-size: 11px;">Full Stack Developer</p>
              <span class="font-xp text-gray-500 flex-shrink-0" style="font-size: 9px;">Jan–Jun 2025</span>
            </div>
            <p class="font-xp" style="font-size: 10px; color: var(--xp-dark-blue);">PT Magna Solusi Indonesia · Internship</p>
            <p class="font-xp text-gray-700 mt-1" style="font-size: 10px;">
              Built full-stack modules using Spring Boot, Angular & PostgreSQL; designed RESTful APIs for scalable web architecture.
            </p>
          </div>

          <!-- Entry 2 -->
          <div class="xp-panel p-2">
            <div class="flex items-start justify-between gap-1">
              <p class="font-xp font-bold text-black" style="font-size: 11px;">VP of UI/UX</p>
              <span class="font-xp text-gray-500 flex-shrink-0" style="font-size: 9px;">2023</span>
            </div>
            <p class="font-xp" style="font-size: 10px; color: var(--xp-dark-blue);">COMPFEST · Organisation</p>
            <p class="font-xp text-gray-700 mt-1" style="font-size: 10px;">
              Led design across 5 sprints for compfest.id, managed 11 designers, implemented dark/light mode.
            </p>
          </div>

        </div>
      </div>

      <!-- 6. Selected Projects -->
      <div class="xp-group">
        <div class="xp-group-title">Selected Projects</div>
        <div class="p-2 space-y-2">

          <!-- Thesis / Featured -->
          <div class="xp-panel-raised p-2">
            <div class="flex items-center gap-1 mb-1">
              <span>🔬</span>
              <p class="font-xp font-bold text-black" style="font-size: 11px;">FPGA Computer Architecture (Thesis)</p>
            </div>
            <p class="font-xp text-gray-700" style="font-size: 10px;">
              Synthesisable VHDL-93 implementation of the Mano register-transfer model — 58.648 MHz on Spartan-3AN FPGA.
            </p>
            <div class="flex flex-wrap gap-1 mt-1">
              <span class="research-chip">VHDL-93</span>
              <span class="research-chip">Xilinx ISE</span>
              <span class="research-chip">FPGA</span>
            </div>
          </div>

          <!-- Project 2 -->
          <div class="xp-panel p-2">
            <div class="flex items-center gap-1 mb-1">
              <span>💼</span>
              <p class="font-xp font-bold text-black" style="font-size: 11px;">Enterprise IS for Event Organizer</p>
            </div>
            <p class="font-xp text-gray-700" style="font-size: 10px;">
              Full-stack enterprise system (finance, freelancer tracking, secure deployment).
            </p>
            <p class="font-xp text-gray-500" style="font-size: 10px;">Spring Boot · Vue.js · PostgreSQL · Docker</p>
          </div>

          <!-- Project 3 -->
          <div class="xp-panel p-2">
            <div class="flex items-center gap-1 mb-1">
              <span>🤖</span>
              <p class="font-xp font-bold text-black" style="font-size: 11px;">Used Car Sales Prediction (ML)</p>
            </div>
            <p class="font-xp text-gray-700" style="font-size: 10px;">
              Machine learning model for used car price prediction with data preprocessing pipeline.
            </p>
            <p class="font-xp text-gray-500" style="font-size: 10px;">Python · Scikit-Learn · Supervised Learning</p>
          </div>

        </div>
      </div>

      <!-- 7. Contact -->
      <div class="xp-group">
        <div class="xp-group-title">Contact</div>
        <div class="p-2 space-y-1">
          <a href="mailto:musthofaja.topa@gmail.com" class="flex items-center gap-2 hover:underline" style="text-decoration: none;">
            <span>📧</span>
            <span class="font-xp text-black" style="font-size: 11px;">musthofaja.topa@gmail.com</span>
          </a>
          <a
            href="https://www.linkedin.com/in/musthofa-joko-anggoro/"
            target="_blank"
            rel="noopener noreferrer"
            class="flex items-center gap-2 hover:underline"
            style="text-decoration: none;"
          >
            <span>🔗</span>
            <span class="font-xp text-black" style="font-size: 11px;">linkedin.com/in/musthofa-joko-anggoro</span>
          </a>
          <a
            href="https://github.com/topahilangharapan"
            target="_blank"
            rel="noopener noreferrer"
            class="flex items-center gap-2 hover:underline"
            style="text-decoration: none;"
          >
            <span>💻</span>
            <span class="font-xp text-black" style="font-size: 11px;">github.com/topahilangharapan</span>
          </a>
          <div class="flex items-center gap-2 pt-1">
            <span class="w-2 h-2 rounded-full bg-green-500 flex-shrink-0"></span>
            <span class="font-xp text-gray-600" style="font-size: 10px;">Available · Usually responds within 24 hours</span>
          </div>
        </div>
      </div>

    </div>

    <!-- Restore bar when minimized -->
    <div
      v-show="isMinimized"
      class="bg-xp-window px-3 py-1 text-center cursor-pointer font-xp flex-shrink-0"
      style="font-size: 11px; color: var(--xp-dark-blue);"
      @click="isMinimized = false"
    >
      ▲ Show Academic Profile
    </div>

    <!-- Status Bar -->
    <div class="xp-status flex justify-between flex-shrink-0">
      <span class="font-xp" style="font-size: 10px;">PhD Aspirant · UI Fasilkom 2026</span>
      <span class="font-xp" style="font-size: 10px;">GPA 3.85 / 4.00</span>
    </div>

  </div>
</template>
