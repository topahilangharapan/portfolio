<script setup lang="ts">
import { ref } from 'vue';

const isMinimized = ref(false);

const researchTags = [
  'FPGA Design',
  'VHDL-93',
  'Computer Architecture',
  'EDA',
  'RTL Design',
  'Xilinx ISE',
];

function downloadCV() {
  window.open('/CV_Musthofa Joko Anggoro.pdf', '_blank');
}
</script>

<template>
  <div class="xp-window w-full">
    <!-- Title Bar -->
    <div class="xp-title-bar flex items-center justify-between">
      <div class="flex items-center gap-1">
        <span class="text-sm">🔬</span>
        <span class="font-xp-title text-xs">Research Profile — PhD Aspirant</span>
      </div>
      <div class="flex items-center gap-1">
        <button
          class="xp-control-btn w-4 h-4 text-xs flex items-center justify-center"
          title="Minimize"
          @click="isMinimized = !isMinimized"
        >_</button>
      </div>
    </div>

    <!-- Card Body -->
    <div v-show="!isMinimized" class="bg-xp-window p-2 space-y-2">

      <!-- Identity -->
      <div class="xp-panel-raised p-2">
        <p class="font-xp font-bold text-black" style="font-size: 12px;">Musthofa Joko Anggoro</p>
        <p class="font-xp font-bold" style="font-size: 11px; color: var(--xp-dark-blue);">
          Computer Architecture Researcher · PhD Aspirant
        </p>
        <p class="font-xp text-gray-600" style="font-size: 10px; margin-top: 2px;">
          Universitas Indonesia · Fasilkom
        </p>
      </div>

      <!-- Research Focus Chips -->
      <div class="xp-group">
        <div class="xp-group-title">Research Focus</div>
        <div class="flex flex-wrap gap-1 pt-1">
          <span
            v-for="tag in researchTags"
            :key="tag"
            class="research-chip"
          >{{ tag }}</span>
        </div>
      </div>

      <!-- Current Research (Thesis) -->
      <div class="xp-group">
        <div class="xp-group-title">Current Research</div>
        <div class="xp-panel p-2 mt-1">
          <p class="font-xp font-bold text-black leading-tight" style="font-size: 11px;">
            Bridging the Gap Between the Mano Register-Transfer Model and FPGA Realization
            Through a Synthesisable VHDL-93 Architecture
          </p>
          <p class="font-xp text-gray-700 mt-1" style="font-size: 10px;">
            Full hierarchical VHDL-93 implementation achieving <strong>58.648 MHz</strong> on Xilinx Spartan-3AN FPGA.
          </p>
        </div>
        <p class="font-xp text-gray-600 mt-1" style="font-size: 10px;">
          Supervised by:
          <span class="font-bold text-black">Prof. Dr. Ir. Petrus Mursanto, M.Sc.</span>
        </p>
      </div>

      <!-- Education -->
      <div class="xp-panel p-2 flex items-center gap-2">
        <span style="font-size: 16px;">🎓</span>
        <div>
          <p class="font-xp font-bold text-black" style="font-size: 11px;">Universitas Indonesia, Fasilkom</p>
          <p class="font-xp text-gray-600" style="font-size: 10px;">
            Information Systems · GPA <strong class="text-black">3.85 / 4.0</strong> · June 2026
          </p>
        </div>
      </div>

      <!-- Action Buttons -->
      <div class="flex gap-1 pt-1 flex-wrap">
        <button class="xp-button flex items-center gap-1" style="font-size: 11px;" @click="downloadCV">
          📄 Download CV
        </button>
        <a
          href="mailto:musthofaja12@gmail.com"
          class="xp-button flex items-center gap-1"
          style="font-size: 11px; text-decoration: none; color: inherit;"
        >
          📧 Contact
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
      </div>
    </div>

    <!-- Restore bar when minimized -->
    <div
      v-show="isMinimized"
      class="bg-xp-window px-3 py-1 text-center cursor-pointer font-xp"
      style="font-size: 11px; color: var(--xp-dark-blue);"
      @click="isMinimized = false"
    >
      ▲ Show Research Profile
    </div>

    <!-- Status Bar -->
    <div class="xp-status flex justify-between">
      <span class="font-xp" style="font-size: 10px;">PhD Aspirant · Computer Architecture</span>
      <span class="font-xp" style="font-size: 10px;">UI Fasilkom 2026</span>
    </div>
  </div>
</template>
