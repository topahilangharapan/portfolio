<script setup lang="ts">
defineProps<{
  isOpen: boolean;
}>();

const emit = defineEmits<{
  'update:isOpen': [value: boolean];
}>();

const techStack = ['VHDL-93', 'Xilinx ISE 14.x', 'Spartan-3AN FPGA', 'XST Synthesizer', 'ISim / GHDL', 'Register-Transfer Level'];
const researchTopics = ['Computer Architecture', 'FPGA Design', 'Electronic Design Automation', 'RTL Design', 'Digital Hardware', 'Synthesisable Architecture'];

const highlights = [
  '58.648 MHz max clock frequency (17.051 ns min period)',
  '1,675 LUTs (14%) · 638 flip-flops (5%) on XC3S700AN',
  'Full VHDL-93 hierarchical 3-tier component structure',
  '256×32-bit microoperation memory + 256×8-bit data memory',
  'Verified via unit testbenches (ISim/GHDL) and board-level testing',
  'Live LCD display of complete microoperation sequences',
];

function close() {
  emit('update:isOpen', false);
}
</script>

<template>
  <div v-if="isOpen" class="xp-window w-full h-full flex flex-col">
    <!-- Title Bar -->
    <div class="xp-title-bar flex items-center justify-between flex-shrink-0">
      <div class="flex items-center gap-2">
        <span>🔬</span>
        <span class="font-xp-title text-sm">Research &amp; Thesis — Computer Architecture</span>
      </div>
      <div class="flex items-center gap-1">
        <button class="xp-control-btn" title="Close" @click="close">✕</button>
      </div>
    </div>

    <!-- Menu Bar -->
    <div class="xp-menubar flex-shrink-0">
      <span class="xp-menu-item font-xp px-2 py-0.5" style="font-size: 11px;">File</span>
      <span class="xp-menu-item font-xp px-2 py-0.5" style="font-size: 11px;">View</span>
      <span class="xp-menu-item font-xp px-2 py-0.5" style="font-size: 11px;">Navigate</span>
      <span class="xp-menu-item font-xp px-2 py-0.5" style="font-size: 11px;">Help</span>
    </div>

    <!-- Body: two-column grid -->
    <div class="bg-xp-window flex-1 overflow-y-auto p-3">
      <div class="grid grid-cols-2 gap-3">

        <!-- LEFT COLUMN -->
        <div class="space-y-3">

          <!-- Thesis Overview -->
          <div class="xp-group">
            <div class="xp-group-title">Thesis Overview</div>
            <div class="p-2 space-y-2">
              <p class="font-xp font-bold text-black leading-snug" style="font-size: 11px;">
                Bridging the Gap Between the Mano Register-Transfer Model and FPGA Realization
                Through a Synthesisable VHDL-93 Architecture
              </p>
              <p class="font-xp text-gray-700" style="font-size: 11px;">
                This research addresses the engineering gap between the theoretical Mano register-transfer
                computer architecture model—widely used in undergraduate CS education—and its practical
                synthesizable implementation on FPGAs.
              </p>
              <p class="font-xp text-gray-700" style="font-size: 11px;">
                The work conducts a systematic gap analysis to identify undefined engineering constraints
                (register organization, instruction encoding, control mechanism, memory partitioning, I/O
                interface) and maps each to concrete design decisions, resulting in a complete,
                hierarchically-structured 8-bit datapath implemented in VHDL-93.
              </p>
              <div class="flex items-center gap-2 pt-1">
                <span class="font-xp text-gray-600" style="font-size: 10px;">Supervisor:</span>
                <span class="font-xp font-bold text-black" style="font-size: 11px;">
                  Prof. Dr. Ir. Petrus Mursanto, M.Sc.
                </span>
              </div>
              <div class="flex items-center gap-2">
                <span
                  class="xp-button font-xp cursor-default"
                  style="font-size: 10px; background: linear-gradient(180deg,#d4edda,#b8dfc8); border-color: #4CAF50;"
                >✓ Completed · June 2026</span>
              </div>
            </div>
          </div>

          <!-- Key Technical Achievement -->
          <div class="xp-group">
            <div class="xp-group-title">Key Technical Achievements</div>
            <div class="p-2 space-y-2">
              <div class="xp-panel-raised p-2 text-center">
                <p class="font-xp font-bold" style="font-size: 14px; color: var(--xp-dark-blue);">58.648 MHz</p>
                <p class="font-xp text-gray-600" style="font-size: 10px;">Max clock frequency on Xilinx Spartan-3AN FPGA</p>
              </div>
              <div class="xp-group" style="margin: 0;">
                <div class="xp-group-title" style="font-size: 10px;">Clock Performance</div>
                <div class="px-2 pt-1 pb-2">
                  <div class="xp-progress" style="height: 14px;">
                    <div class="xp-progress-bar" style="width: 58.648%; min-width: 4px;"></div>
                  </div>
                  <p class="font-xp text-gray-500 mt-1" style="font-size: 10px;">58.648 MHz / 100 MHz reference</p>
                </div>
              </div>
              <ul class="space-y-1">
                <li
                  v-for="h in highlights"
                  :key="h"
                  class="font-xp text-gray-700 flex items-start gap-1"
                  style="font-size: 10px;"
                >
                  <span class="text-green-600 flex-shrink-0">▸</span>
                  <span>{{ h }}</span>
                </li>
              </ul>
            </div>
          </div>

        </div>

        <!-- RIGHT COLUMN -->
        <div class="space-y-3">

          <!-- Technology Stack -->
          <div class="xp-group">
            <div class="xp-group-title">Technology Stack</div>
            <div class="flex flex-wrap gap-1 p-2">
              <span
                v-for="tech in techStack"
                :key="tech"
                class="research-chip"
              >{{ tech }}</span>
            </div>
          </div>

          <!-- Research Topics -->
          <div class="xp-group">
            <div class="xp-group-title">Research Topics</div>
            <div class="flex flex-wrap gap-1 p-2">
              <span
                v-for="topic in researchTopics"
                :key="topic"
                class="xp-button cursor-default"
                style="font-size: 10px; padding: 1px 6px;"
              >{{ topic }}</span>
            </div>
          </div>

          <!-- Research Context -->
          <div class="xp-group">
            <div class="xp-group-title">Research Context</div>
            <div class="p-2 space-y-1">
              <p class="font-xp text-gray-700" style="font-size: 11px;">
                The <strong>Mano basic computer</strong> is the canonical model used in undergraduate
                computer architecture education worldwide, but its textbook form leaves critical
                engineering constraints undefined, making direct FPGA implementation non-trivial.
              </p>
              <p class="font-xp text-gray-700" style="font-size: 11px;">
                This work provides a reproducible reference framework that bridges the gap, serving as
                a pedagogical platform for teaching register-transfer concepts through hands-on
                hardware implementation.
              </p>
            </div>
          </div>

          <!-- Research Output -->
          <div class="xp-group">
            <div class="xp-group-title">Research Output</div>
            <div class="p-2 space-y-2">
              <div class="xp-panel p-2 flex items-center gap-2">
                <span>📄</span>
                <div>
                  <p class="font-xp font-bold text-black" style="font-size: 11px;">Undergraduate Thesis</p>
                  <p class="font-xp text-gray-600" style="font-size: 10px;">Fasilkom Universitas Indonesia · 2026</p>
                </div>
              </div>
              <div class="xp-panel p-2 flex items-center gap-2">
                <span>💻</span>
                <div>
                  <p class="font-xp font-bold text-black" style="font-size: 11px;">VHDL Implementation</p>
                  <p class="font-xp text-gray-600" style="font-size: 10px;">Contact for access to source repository</p>
                </div>
              </div>
              <a
                href="mailto:musthofaja12@gmail.com"
                class="xp-button flex items-center gap-1 w-fit"
                style="font-size: 11px; text-decoration: none; color: inherit;"
              >
                📧 Request thesis document
              </a>
            </div>
          </div>

        </div>
      </div>
    </div>

    <!-- Status Bar -->
    <div class="xp-status flex justify-between flex-shrink-0">
      <span class="font-xp" style="font-size: 10px;">Thesis Status: Completed · June 2026</span>
      <span class="font-xp" style="font-size: 10px;">Supervisor: Prof. Petrus Mursanto</span>
    </div>
  </div>
</template>
