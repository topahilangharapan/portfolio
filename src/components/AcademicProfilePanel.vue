<script setup lang="ts">
import { ref } from 'vue';

const isMinimized = ref(false);

const researchChips = ['FPGA Design', 'VHDL-93', 'Computer Architecture', 'EDA', 'RTL Design', 'Digital Hardware'];

const allCourses = [
  'Introduction to Computer Architecture',
  'AI & Data Science',
  'Enterprise Application Architecture',
  'Information Systems Development',
  'Data Structures & Algorithms',
  'Databases',
  'Operating Systems',
  'Data Communication Networks',
];

const achievements = [
  'Vice Person in Charge of UI/UX — COMPFEST (National CS Event)',
  'Mentor of Programming Foundations 0 — UI Fasilkom',
];

const skills = {
  hardware: ['VHDL-93', 'Xilinx ISE 14.x', 'Spartan-3AN FPGA', 'XST Synthesizer', 'GHDL / ISim', 'RTL Design'],
  programming: ['Python', 'Java', 'TypeScript', 'Golang'],
  frameworks: ['Vue.js', 'Spring Boot', 'Angular', 'Django', 'PostgreSQL', 'Docker'],
  aiml: ['Scikit-Learn', 'Data Preprocessing', 'Supervised Learning', 'Unsupervised Learning'],
};

const projects = [
  {
    icon: '🔬',
    title: 'FPGA Computer Architecture — Undergraduate Thesis',
    description: 'Synthesisable VHDL-93 implementation of the Mano register-transfer model, achieving 58.648 MHz on Xilinx Spartan-3AN FPGA. Full RTL-to-hardware pipeline from gap analysis to bitstream.',
    stack: ['VHDL-93', 'Xilinx ISE', 'Spartan-3AN FPGA'],
    featured: true,
  },
  {
    icon: '🎤',
    title: 'Enterprise IS for Event Organizer (SISPA)',
    description: 'All-in-one enterprise system for event organiser operations — finance, freelancer tracking, secure deployment.',
    stack: ['Spring Boot', 'Vue.js', 'PostgreSQL', 'Docker'],
    featured: false,
  },
  {
    icon: '🚘',
    title: 'Used Car Sales Prediction',
    description: 'ML model for used car price prediction using imbalanced classification, regression, and clustering.',
    stack: ['Python', 'Scikit-Learn', 'Gradient Boosting', 'K-Means'],
    featured: false,
  },
  {
    icon: '🏥',
    title: 'Apap Medika Web',
    description: 'Secure enterprise web app with Spring Boot microservices for a medical clinic (insurance, profiles, CI/CD).',
    stack: ['Spring Boot', 'Vue.js', 'PostgreSQL', 'Docker'],
    featured: false,
  },
  {
    icon: '🐹',
    title: 'Marmut Merah Jambu — Music & Podcast Streaming',
    description: 'Full-stack streaming platform with playlist management, user subscriptions, and direct SQL integration.',
    stack: ['Django', 'PostgreSQL', 'SQL Triggers', 'Stored Procedures'],
    featured: false,
  },
  {
    icon: '🧭',
    title: 'PathFinder — Career Guidance App (UI/UX)',
    description: 'User-centric guidance app design: UX research, journey mapping, wireframing, prototyping, usability testing.',
    stack: ['Figma', 'UX Research', 'Prototyping'],
    featured: false,
  },
];

function downloadCV() {
  window.open('/CV_Musthofa Joko Anggoro.pdf', '_blank');
}
</script>

<template>
  <div class="xp-window w-full h-full flex flex-col">

    <!-- Title Bar -->
    <div class="xp-title-bar flex items-center justify-between flex-shrink-0">
      <div class="flex items-center gap-2">
        <span>🎓</span>
        <span class="font-xp-title" style="font-size: 12px;">Academic Profile — Musthofa Joko Anggoro</span>
      </div>
      <button
        class="xp-control-btn w-4 h-4 text-xs flex items-center justify-center"
        title="Minimize"
        @click="isMinimized = !isMinimized"
      >_</button>
    </div>

    <!-- Scrollable body -->
    <div v-show="!isMinimized" class="flex-1 overflow-y-auto bg-xp-window p-3 space-y-3 xp-scroll">

      <!-- 1. Identity -->
      <div class="xp-panel-raised p-3 flex items-center gap-3">
        <div
          class="flex-shrink-0 flex items-center justify-center font-bold text-white"
          style="width:48px;height:48px;background:linear-gradient(135deg,var(--xp-blue),var(--xp-dark-blue));border:2px outset var(--xp-silver-dark);font-size:14px;font-family:'Tahoma',sans-serif;"
        >
          MJA
        </div>
        <div>
          <p class="font-xp font-bold text-black" style="font-size: 14px;">Musthofa Joko Anggoro</p>
          <p class="font-xp font-bold" style="font-size: 12px; color: var(--xp-dark-blue);">
            Computer Architecture Researcher · PhD Aspirant
          </p>
          <p class="font-xp text-gray-600" style="font-size: 11px; margin-top: 1px;">
            Universitas Indonesia · Fasilkom · Information Systems
          </p>
          <div class="flex items-center gap-1 mt-1">
            <span class="w-2 h-2 rounded-full bg-green-500 flex-shrink-0"></span>
            <span class="font-xp text-gray-600" style="font-size: 10px;">Open to PhD positions</span>
          </div>
        </div>
      </div>

      <!-- 2. Quick Actions -->
      <div class="flex flex-wrap gap-1">
        <button class="xp-button flex items-center gap-1" style="font-size: 12px;" @click="downloadCV">
          📄 Download CV
        </button>
        <a
          href="mailto:musthofaja.topa@gmail.com"
          class="xp-button flex items-center gap-1"
          style="font-size: 12px; text-decoration: none; color: inherit;"
        >📧 Email</a>
        <a
          href="https://www.linkedin.com/in/musthofa-joko-anggoro/"
          target="_blank" rel="noopener noreferrer"
          class="xp-button flex items-center gap-1"
          style="font-size: 12px; text-decoration: none; color: inherit;"
        >🔗 LinkedIn</a>
        <a
          href="https://github.com/topahilangharapan"
          target="_blank" rel="noopener noreferrer"
          class="xp-button flex items-center gap-1"
          style="font-size: 12px; text-decoration: none; color: inherit;"
        >💻 GitHub</a>
      </div>

      <!-- 3. Current Research -->
      <div class="xp-group">
        <div class="xp-group-title">Current Research</div>
        <div class="p-2 space-y-2">
          <div class="xp-panel p-3">
            <p class="font-xp font-bold text-black leading-snug" style="font-size: 12px;">
              Bridging the Gap Between the Mano Register-Transfer Model and FPGA Realization
              Through a Synthesisable VHDL-93 Architecture
            </p>
            <p class="font-xp font-bold mt-1" style="font-size: 11px; color: var(--xp-dark-blue);">
              ⚡ 58.648 MHz on Xilinx Spartan-3AN FPGA · 1,675 LUTs (14%) · 638 flip-flops (5%)
            </p>
          </div>
          <p class="font-xp text-gray-700" style="font-size: 11px; line-height: 1.5;">
            This work conducts a systematic gap analysis to identify undefined engineering constraints
            in the Mano model — register organisation, instruction encoding, control mechanism, memory
            partitioning, and I/O interface — and maps each to concrete VHDL-93 design decisions. The
            result is a complete, verified 8-bit datapath implementing the full microoperation sequence
            with board-level testing on a Xilinx Spartan-3AN starter board.
          </p>
          <p class="font-xp text-gray-600" style="font-size: 11px;">
            Supervised by <span class="font-bold text-black">Prof. Dr. Ir. Petrus Mursanto, M.Sc.</span>
            · Universitas Indonesia Fasilkom · 2026
          </p>
          <div class="flex flex-wrap gap-1">
            <span v-for="chip in researchChips" :key="chip" class="research-chip">{{ chip }}</span>
          </div>
        </div>
      </div>

      <!-- 4. Education -->
      <div class="xp-group">
        <div class="xp-group-title">Education</div>
        <div class="p-2 space-y-3">

          <div class="flex items-start gap-3">
            <span style="font-size: 20px; flex-shrink: 0;">🎓</span>
            <div>
              <p class="font-xp font-bold text-black" style="font-size: 12px;">University of Indonesia (Universitas Indonesia)</p>
              <p class="font-xp text-gray-700" style="font-size: 11px;">Faculty of Computer Science (Fasilkom)</p>
              <p class="font-xp text-gray-700" style="font-size: 11px;">Bachelor of Computer Science · Major: Information Systems</p>
              <p class="font-xp text-gray-600" style="font-size: 11px;">Expected Graduation: June 2026 · 7th Semester</p>
            </div>
          </div>

          <!-- GPA -->
          <div>
            <div class="flex justify-between mb-1">
              <span class="font-xp font-bold text-black" style="font-size: 12px;">GPA</span>
              <span class="font-xp font-bold" style="font-size: 12px; color: var(--xp-dark-blue);">3.85 / 4.00</span>
            </div>
            <div class="xp-progress" style="height: 14px;">
              <div class="xp-progress-bar" style="width: 96.25%;"></div>
            </div>
          </div>

          <!-- Thesis badge -->
          <div class="xp-panel-raised p-2 flex items-center gap-2">
            <span style="font-size: 14px;">🔬</span>
            <div>
              <p class="font-xp font-bold text-black" style="font-size: 11px;">
                Thesis: FPGA Architecture Implementation
                <span class="font-bold ml-2" style="color: #2e7d32;">✓ Completed 2026</span>
              </p>
              <p class="font-xp text-gray-600" style="font-size: 10px;">
                Supervisor: Prof. Dr. Ir. Petrus Mursanto, M.Sc.
              </p>
            </div>
          </div>

          <!-- All Relevant Courses -->
          <div>
            <p class="font-xp font-bold text-gray-700 mb-1" style="font-size: 11px;">Relevant Coursework:</p>
            <div class="flex flex-wrap gap-1">
              <span
                v-for="course in allCourses"
                :key="course"
                class="xp-button cursor-default"
                style="font-size: 10px; padding: 2px 6px;"
              >{{ course }}</span>
            </div>
          </div>

          <!-- Academic Achievements -->
          <div>
            <p class="font-xp font-bold text-gray-700 mb-1" style="font-size: 11px;">Academic Achievements:</p>
            <div class="space-y-1">
              <div v-for="a in achievements" :key="a" class="flex items-start gap-2">
                <span class="font-bold flex-shrink-0" style="font-size: 11px; color: var(--xp-dark-blue);">★</span>
                <span class="font-xp text-black" style="font-size: 11px;">{{ a }}</span>
              </div>
            </div>
          </div>

        </div>
      </div>

      <!-- 5. Technical Skills -->
      <div class="xp-group">
        <div class="xp-group-title">Technical Skills</div>
        <div class="p-2 space-y-2">

          <div>
            <p class="font-xp font-bold text-gray-700 mb-1" style="font-size: 11px;">🔩 Hardware / EDA</p>
            <div class="flex flex-wrap gap-1">
              <span v-for="s in skills.hardware" :key="s" class="research-chip">{{ s }}</span>
            </div>
          </div>

          <div>
            <p class="font-xp font-bold text-gray-700 mb-1" style="font-size: 11px;">💻 Programming Languages</p>
            <div class="flex flex-wrap gap-1">
              <span
                v-for="s in skills.programming" :key="s"
                class="xp-button cursor-default"
                style="font-size: 10px; padding: 2px 6px;"
              >{{ s }}</span>
            </div>
          </div>

          <div>
            <p class="font-xp font-bold text-gray-700 mb-1" style="font-size: 11px;">🌐 Frameworks & Tools</p>
            <div class="flex flex-wrap gap-1">
              <span
                v-for="s in skills.frameworks" :key="s"
                class="xp-button cursor-default"
                style="font-size: 10px; padding: 2px 6px;"
              >{{ s }}</span>
            </div>
          </div>

          <div>
            <p class="font-xp font-bold text-gray-700 mb-1" style="font-size: 11px;">🤖 AI / Machine Learning</p>
            <div class="flex flex-wrap gap-1">
              <span
                v-for="s in skills.aiml" :key="s"
                class="xp-button cursor-default"
                style="font-size: 10px; padding: 2px 6px;"
              >{{ s }}</span>
            </div>
          </div>

        </div>
      </div>

      <!-- 6. Experience -->
      <div class="xp-group">
        <div class="xp-group-title">Experience</div>
        <div class="p-2 space-y-2">

          <div class="xp-panel p-3">
            <div class="flex items-start justify-between gap-2">
              <div>
                <p class="font-xp font-bold text-black" style="font-size: 12px;">Full Stack Developer</p>
                <p class="font-xp" style="font-size: 11px; color: var(--xp-dark-blue);">PT Magna Solusi Indonesia · Internship · Hybrid</p>
              </div>
              <span class="font-xp text-gray-500 flex-shrink-0" style="font-size: 10px;">Jan 2025 – Jun 2025</span>
            </div>
            <p class="font-xp text-gray-700 mt-2" style="font-size: 11px; line-height: 1.5;">
              Developed and integrated full-stack modules using Spring Boot, Angular, and PostgreSQL.
              Optimised database performance and built RESTful APIs for scalable web architecture.
            </p>
            <div class="flex flex-wrap gap-1 mt-1">
              <span class="xp-button cursor-default" style="font-size: 10px; padding: 1px 5px;">Spring Boot</span>
              <span class="xp-button cursor-default" style="font-size: 10px; padding: 1px 5px;">Angular</span>
              <span class="xp-button cursor-default" style="font-size: 10px; padding: 1px 5px;">PostgreSQL</span>
              <span class="xp-button cursor-default" style="font-size: 10px; padding: 1px 5px;">RESTful API</span>
            </div>
          </div>

          <div class="xp-panel p-3">
            <div class="flex items-start justify-between gap-2">
              <div>
                <p class="font-xp font-bold text-black" style="font-size: 12px;">Vice Person in Charge — UI/UX</p>
                <p class="font-xp" style="font-size: 11px; color: var(--xp-dark-blue);">COMPFEST · National CS Event · Organisation</p>
              </div>
              <span class="font-xp text-gray-500 flex-shrink-0" style="font-size: 10px;">Jan 2023 – Dec 2023</span>
            </div>
            <p class="font-xp text-gray-700 mt-2" style="font-size: 11px; line-height: 1.5;">
              Led design process across 5 sprints for compfest.id, implemented dark/light mode,
              managed a team of 11 designers, and coordinated with software and automation engineers.
            </p>
            <div class="flex flex-wrap gap-1 mt-1">
              <span class="xp-button cursor-default" style="font-size: 10px; padding: 1px 5px;">Figma</span>
              <span class="xp-button cursor-default" style="font-size: 10px; padding: 1px 5px;">UI/UX Design</span>
              <span class="xp-button cursor-default" style="font-size: 10px; padding: 1px 5px;">Team Leadership</span>
            </div>
          </div>

        </div>
      </div>

      <!-- 7. All Projects -->
      <div class="xp-group">
        <div class="xp-group-title">Projects</div>
        <div class="p-2 space-y-2">
          <div
            v-for="p in projects"
            :key="p.title"
            :class="p.featured ? 'xp-panel-raised p-3' : 'xp-panel p-2'"
          >
            <div class="flex items-center gap-1 mb-1">
              <span style="font-size: 14px;">{{ p.icon }}</span>
              <p class="font-xp font-bold text-black" :style="p.featured ? 'font-size: 12px;' : 'font-size: 11px;'">
                {{ p.title }}
              </p>
            </div>
            <p class="font-xp text-gray-700" style="font-size: 11px; line-height: 1.4;">{{ p.description }}</p>
            <div class="flex flex-wrap gap-1 mt-1">
              <span
                v-for="t in p.stack"
                :key="t"
                :class="p.featured ? 'research-chip' : 'xp-button cursor-default'"
                :style="p.featured ? '' : 'font-size: 10px; padding: 1px 5px;'"
              >{{ t }}</span>
            </div>
          </div>
        </div>
      </div>

      <!-- 8. Contact -->
      <div class="xp-group">
        <div class="xp-group-title">Contact</div>
        <div class="p-2 space-y-2">
          <a href="mailto:musthofaja.topa@gmail.com" class="flex items-center gap-2" style="text-decoration: none;">
            <span>📧</span>
            <span class="font-xp text-black" style="font-size: 12px;">musthofaja.topa@gmail.com</span>
          </a>
          <a
            href="https://www.linkedin.com/in/musthofa-joko-anggoro/"
            target="_blank" rel="noopener noreferrer"
            class="flex items-center gap-2" style="text-decoration: none;"
          >
            <span>🔗</span>
            <span class="font-xp text-black" style="font-size: 12px;">linkedin.com/in/musthofa-joko-anggoro</span>
          </a>
          <a
            href="https://github.com/topahilangharapan"
            target="_blank" rel="noopener noreferrer"
            class="flex items-center gap-2" style="text-decoration: none;"
          >
            <span>💻</span>
            <span class="font-xp text-black" style="font-size: 12px;">github.com/topahilangharapan</span>
          </a>
          <div class="flex items-center gap-2 pt-1 border-t border-gray-300">
            <span class="w-2 h-2 rounded-full bg-green-500 flex-shrink-0"></span>
            <span class="font-xp text-gray-600" style="font-size: 11px;">Available · Usually responds within 24 hours</span>
          </div>
        </div>
      </div>

    </div>

    <!-- Restore bar -->
    <div
      v-show="isMinimized"
      class="bg-xp-window px-3 py-1 text-center cursor-pointer font-xp flex-shrink-0"
      style="font-size: 11px; color: var(--xp-dark-blue);"
      @click="isMinimized = false"
    >▲ Show Academic Profile</div>

    <!-- Status Bar -->
    <div class="xp-status flex justify-between flex-shrink-0">
      <span class="font-xp" style="font-size: 10px;">PhD Aspirant · Computer Architecture · UI Fasilkom 2026</span>
      <span class="font-xp" style="font-size: 10px;">GPA 3.85 / 4.00</span>
    </div>

  </div>
</template>
