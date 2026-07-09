<script setup lang="ts">
import { ref } from 'vue';

defineProps<{ isOpen: boolean }>();
const emit = defineEmits<{ 'update:isOpen': [value: boolean] }>();

const activeTab = ref('home');
const tabs = [
  { id: 'home',      label: 'Home' },
  { id: 'research',  label: 'Research' },
  { id: 'education', label: 'Education' },
  { id: 'projects',  label: 'Projects' },
  { id: 'contact',   label: 'Contact' },
];

const projects = [
  { icon: '🔬', title: 'FPGA Computer Architecture (Undergraduate Thesis)', stack: 'VHDL-93 · Xilinx ISE · Spartan-3AN FPGA', desc: 'Synthesisable VHDL-93 implementation of the Mano register-transfer model. Achieved 58.648 MHz clock frequency — 1,675 LUTs, 638 flip-flops on Xilinx Spartan-3AN.' },
  { icon: '🎤', title: 'Enterprise IS for Event Organizer (SISPA)', stack: 'Spring Boot · Vue.js · PostgreSQL · Docker', desc: 'All-in-one enterprise system for event operations: finance, freelancer tracking, JWT auth, Docker deployment.' },
  { icon: '🚘', title: 'Used Car Sales Prediction', stack: 'Python · Scikit-Learn · Gradient Boosting · K-Means', desc: 'ML model for used car price prediction using imbalanced classification, regression, and clustering.' },
  { icon: '🏥', title: 'Apap Medika Web', stack: 'Spring Boot · Vue.js · PostgreSQL · Microservices', desc: 'Secure enterprise medical clinic web app with Spring Boot microservices (insurance, profiles, CI/CD).' },
  { icon: '🐹', title: 'Marmut Merah Jambu — Music & Podcast Streaming', stack: 'Django · PostgreSQL · SQL Triggers · Stored Procedures', desc: 'Full-stack streaming platform with playlist management, user subscriptions, direct SQL integration.' },
  { icon: '🧭', title: 'PathFinder — Career Guidance App (UI/UX)', stack: 'Figma · UX Research · Prototyping', desc: 'UX research, journey mapping, wireframing, and usability testing for a student career guidance app.' },
];

function downloadCV() {
  window.open('/CV_Musthofa Joko Anggoro.pdf', '_blank');
}
</script>

<template>
  <div v-if="isOpen" class="xp-window w-full h-full flex flex-col">

    <!-- XP Title Bar -->
    <div class="xp-title-bar flex items-center justify-between flex-shrink-0">
      <div class="flex items-center gap-1 min-w-0">
        <span class="flex-shrink-0">🌐</span>
        <span class="font-xp-title truncate" style="font-size:11px;">
          Musthofa Joko Anggoro — Personal Homepage — Microsoft Internet Explorer
        </span>
      </div>
      <div class="flex items-center gap-1 flex-shrink-0 ml-2">
        <button class="xp-control-btn w-4 h-4 text-xs flex items-center justify-center" title="Minimize">_</button>
        <button class="xp-control-btn w-4 h-4 text-xs flex items-center justify-center" title="Maximize">□</button>
        <button class="xp-control-btn w-4 h-4 text-xs flex items-center justify-center" title="Close"
          @click="emit('update:isOpen', false)">✕</button>
      </div>
    </div>

    <!-- IE Menu Bar -->
    <div class="ie-menubar flex-shrink-0">
      <span class="ie-menu-item">File</span>
      <span class="ie-menu-item">Edit</span>
      <span class="ie-menu-item">View</span>
      <span class="ie-menu-item">Favorites</span>
      <span class="ie-menu-item">Tools</span>
      <span class="ie-menu-item">Help</span>
    </div>

    <!-- IE Toolbar -->
    <div class="ie-toolbar flex-shrink-0 flex items-center gap-1 px-1 py-1">
      <button class="ie-btn" title="Back">◀ Back</button>
      <button class="ie-btn" title="Forward">▶</button>
      <button class="ie-btn" title="Stop">✕</button>
      <button class="ie-btn" title="Refresh">↻</button>
      <button class="ie-btn" title="Home">🏠</button>
      <div class="w-px h-5 bg-gray-400 mx-1"></div>
      <span class="ie-label">Address</span>
      <div class="ie-addressbar flex-1">http://www.musthofa.ac.id/</div>
      <button class="ie-go-btn">Go</button>
    </div>

    <!-- IE Links Bar -->
    <div class="ie-linksbar flex-shrink-0 flex items-center gap-3 px-2 py-0.5">
      <span class="ie-link-label">Links</span>
      <span class="ie-link">MSN.com</span>
      <span class="ie-link">Windows</span>
      <span class="ie-link">Free Hotmail</span>
    </div>

    <!-- Webpage Content -->
    <div class="flex-1 overflow-y-auto webpage-bg">

      <!-- Site Header (Frutiger Aero glossy banner) -->
      <div class="site-header">
        <div class="site-header-gloss"></div>
        <div class="site-header-content">
          <div class="site-avatar">MJA</div>
          <div>
            <h1 class="site-title">Musthofa Joko Anggoro</h1>
            <p class="site-subtitle">Computer Architecture Researcher &amp; PhD Aspirant</p>
            <p class="site-subtitle2">Universitas Indonesia · Fasilkom · Class of 2026</p>
          </div>
        </div>
      </div>

      <!-- Site Navigation -->
      <nav class="site-nav">
        <button
          v-for="tab in tabs"
          :key="tab.id"
          :class="['site-nav-btn', activeTab === tab.id ? 'site-nav-btn--active' : '']"
          @click="activeTab = tab.id"
        >{{ tab.label }}</button>
      </nav>

      <!-- Page Content -->
      <div class="site-body">

        <!-- Sidebar (always visible) -->
        <aside class="site-sidebar">
          <div class="sidebar-section">
            <div class="sidebar-avatar">MJA</div>
            <p class="sidebar-name">Musthofa Joko Anggoro</p>
            <p class="sidebar-role">PhD Aspirant</p>
            <div class="sidebar-status">
              <span class="status-dot"></span> Online
            </div>
          </div>

          <div class="sidebar-section">
            <div class="sidebar-heading">Quick Info</div>
            <table class="sidebar-table">
              <tr><td class="sidebar-key">GPA:</td><td class="sidebar-val">3.85 / 4.00</td></tr>
              <tr><td class="sidebar-key">Grad:</td><td class="sidebar-val">June 2026</td></tr>
              <tr><td class="sidebar-key">Focus:</td><td class="sidebar-val">FPGA &amp; CA</td></tr>
            </table>
          </div>

          <div class="sidebar-section">
            <div class="sidebar-heading">Contact</div>
            <div class="sidebar-links">
              <a href="mailto:musthofaja.topa@gmail.com" class="sidebar-link">📧 Email</a>
              <a href="https://www.linkedin.com/in/musthofa-joko-anggoro/" target="_blank" rel="noopener noreferrer" class="sidebar-link">🔗 LinkedIn</a>
              <a href="https://github.com/topahilangharapan" target="_blank" rel="noopener noreferrer" class="sidebar-link">💻 GitHub</a>
            </div>
          </div>

          <div class="sidebar-section">
            <div class="sidebar-heading">Downloads</div>
            <button class="sidebar-dl-btn" @click="downloadCV">
              📄 Download CV
            </button>
          </div>

          <div class="sidebar-counter">
            <img src="" alt="" style="display:none"/>
            <div class="counter-label">You are visitor</div>
            <div class="counter-number">001,337</div>
          </div>
        </aside>

        <!-- Main Content (tab-switched) -->
        <main class="site-main">

          <!-- HOME TAB -->
          <div v-if="activeTab === 'home'">
            <div class="page-card">
              <div class="page-card-header">Welcome to My Homepage!</div>
              <div class="page-card-body">
                <p class="page-text">
                  Hi! I'm <strong>Musthofa Joko Anggoro</strong>, a Computer Science final-year student
                  at Universitas Indonesia (Fasilkom) with a deep passion for computer architecture
                  and digital hardware design. I am actively seeking PhD opportunities in
                  Computer Architecture, FPGA Design, and related fields.
                </p>
                <p class="page-text">
                  My undergraduate thesis bridges the gap between theoretical register-transfer
                  models and practical FPGA realisation — implementing a complete, synthesisable
                  VHDL-93 architecture on a Xilinx Spartan-3AN FPGA achieving <strong>58.648 MHz</strong>.
                </p>
              </div>
            </div>

            <div class="page-card">
              <div class="page-card-header">Research Highlights</div>
              <div class="page-card-body">
                <div class="highlight-box">
                  <div class="highlight-icon">🔬</div>
                  <div>
                    <p class="highlight-title">FPGA Implementation of the Mano Register-Transfer Model</p>
                    <p class="page-text">Synthesisable VHDL-93 · 58.648 MHz · 1,675 LUTs · Xilinx Spartan-3AN</p>
                    <p class="page-text">Supervised by <strong>Prof. Dr. Ir. Petrus Mursanto, M.Sc.</strong></p>
                  </div>
                </div>
                <div class="tag-row">
                  <span v-for="t in ['FPGA Design','VHDL-93','Computer Architecture','EDA','RTL Design']" :key="t" class="frutiger-tag">{{ t }}</span>
                </div>
              </div>
            </div>

            <div class="page-card">
              <div class="page-card-header">News &amp; Updates</div>
              <div class="page-card-body space-y-2">
                <div class="news-item">
                  <span class="news-date">Jun 2026</span>
                  <span class="news-text">✓ Undergraduate thesis completed and defended</span>
                </div>
                <div class="news-item">
                  <span class="news-date">Jan 2025</span>
                  <span class="news-text">Started internship as Full Stack Developer at PT Magna Solusi Indonesia</span>
                </div>
                <div class="news-item">
                  <span class="news-date">2023</span>
                  <span class="news-text">Served as VP of UI/UX at COMPFEST — UI's national CS event</span>
                </div>
              </div>
            </div>
          </div>

          <!-- RESEARCH TAB -->
          <div v-if="activeTab === 'research'">
            <div class="page-card">
              <div class="page-card-header">Undergraduate Thesis</div>
              <div class="page-card-body">
                <p class="page-title-large">
                  Bridging the Gap Between the Mano Register-Transfer Model and FPGA Realization
                  Through a Synthesisable VHDL-93 Architecture
                </p>
                <table class="info-table">
                  <tr><td class="info-key">Supervisor</td><td>Prof. Dr. Ir. Petrus Mursanto, M.Sc.</td></tr>
                  <tr><td class="info-key">Institution</td><td>Universitas Indonesia, Fasilkom</td></tr>
                  <tr><td class="info-key">Status</td><td><span class="badge-green">✓ Completed — June 2026</span></td></tr>
                  <tr><td class="info-key">Platform</td><td>Xilinx Spartan-3AN (XC3S700AN)</td></tr>
                  <tr><td class="info-key">Max Frequency</td><td><strong>58.648 MHz</strong> (17.051 ns min period)</td></tr>
                  <tr><td class="info-key">Resource Usage</td><td>1,675 LUTs (14%) · 638 flip-flops (5%)</td></tr>
                </table>
              </div>
            </div>

            <div class="page-card">
              <div class="page-card-header">Research Summary</div>
              <div class="page-card-body">
                <p class="page-text">
                  The Mano basic computer is the canonical model used in undergraduate computer
                  architecture education worldwide. However, the textbook form leaves critical
                  engineering constraints undefined, making direct FPGA implementation non-trivial.
                </p>
                <p class="page-text">
                  This work conducts a systematic gap analysis to identify those undefined
                  constraints — register organisation, instruction encoding, control mechanism,
                  memory partitioning, I/O interface — and maps each to concrete VHDL-93
                  design decisions. The result is a complete, hierarchically-structured 8-bit
                  datapath verified through functional simulation (ISim / GHDL) and board-level
                  testing with a live LCD display.
                </p>
                <p class="page-text">
                  The implementation preserves the single-cycle microoperation contract of the
                  original textbook model while meeting real-time constraints, providing a
                  reproducible reference framework for teaching register-transfer concepts.
                </p>
              </div>
            </div>

            <div class="page-card">
              <div class="page-card-header">Technology Stack</div>
              <div class="page-card-body">
                <div class="tag-row">
                  <span v-for="t in ['VHDL-93','Xilinx ISE 14.x','Spartan-3AN FPGA','XST Synthesizer','ISim / GHDL','RTL Design','Register-Transfer Level','EDA']" :key="t" class="frutiger-tag">{{ t }}</span>
                </div>
              </div>
            </div>
          </div>

          <!-- EDUCATION TAB -->
          <div v-if="activeTab === 'education'">
            <div class="page-card">
              <div class="page-card-header">Academic Background</div>
              <div class="page-card-body">
                <div class="highlight-box">
                  <div class="highlight-icon">🎓</div>
                  <div>
                    <p class="highlight-title">University of Indonesia (Universitas Indonesia)</p>
                    <p class="page-text">Faculty of Computer Science (Fasilkom) · Information Systems</p>
                    <p class="page-text">Bachelor of Computer Science · Expected Graduation: June 2026</p>
                    <p class="page-text"><strong>GPA: 3.85 / 4.00</strong></p>
                  </div>
                </div>
                <div class="gpa-bar-wrap">
                  <div class="gpa-bar-track">
                    <div class="gpa-bar-fill" style="width:96.25%"></div>
                  </div>
                  <span class="gpa-bar-label">3.85 / 4.00</span>
                </div>
              </div>
            </div>

            <div class="page-card">
              <div class="page-card-header">Relevant Coursework</div>
              <div class="page-card-body">
                <div class="tag-row">
                  <span v-for="c in ['Introduction to Computer Architecture','AI &amp; Data Science','Enterprise Application Architecture','Information Systems Development','Data Structures &amp; Algorithms','Databases','Operating Systems','Data Communication Networks']" :key="c" class="frutiger-tag" v-html="c"></span>
                </div>
              </div>
            </div>

            <div class="page-card">
              <div class="page-card-header">Academic Achievements</div>
              <div class="page-card-body space-y-2">
                <div class="achievement-item">
                  <span class="achievement-star">★</span>
                  <span>Vice Person in Charge of UI/UX — COMPFEST (UI's National CS Event)</span>
                </div>
                <div class="achievement-item">
                  <span class="achievement-star">★</span>
                  <span>Mentor of Programming Foundations 0 — UI Fasilkom</span>
                </div>
              </div>
            </div>
          </div>

          <!-- PROJECTS TAB -->
          <div v-if="activeTab === 'projects'">
            <div class="page-card">
              <div class="page-card-header">Projects &amp; Work</div>
              <div class="page-card-body space-y-3">
                <div
                  v-for="p in projects"
                  :key="p.title"
                  :class="['project-item', p.icon === '🔬' ? 'project-item--featured' : '']"
                >
                  <div class="project-header">
                    <span class="project-icon">{{ p.icon }}</span>
                    <span class="project-title">{{ p.title }}</span>
                  </div>
                  <p class="project-desc">{{ p.desc }}</p>
                  <p class="project-stack">{{ p.stack }}</p>
                </div>
              </div>
            </div>
          </div>

          <!-- CONTACT TAB -->
          <div v-if="activeTab === 'contact'">
            <div class="page-card">
              <div class="page-card-header">Get In Touch</div>
              <div class="page-card-body">
                <p class="page-text">
                  I am currently seeking PhD positions in Computer Architecture, FPGA Design,
                  and Digital Hardware Systems. Feel free to reach out if you'd like to discuss
                  research opportunities or collaborations.
                </p>
                <table class="info-table">
                  <tr>
                    <td class="info-key">Email</td>
                    <td><a href="mailto:musthofaja.topa@gmail.com" class="page-link">musthofaja.topa@gmail.com</a></td>
                  </tr>
                  <tr>
                    <td class="info-key">LinkedIn</td>
                    <td><a href="https://www.linkedin.com/in/musthofa-joko-anggoro/" target="_blank" rel="noopener noreferrer" class="page-link">linkedin.com/in/musthofa-joko-anggoro</a></td>
                  </tr>
                  <tr>
                    <td class="info-key">GitHub</td>
                    <td><a href="https://github.com/topahilangharapan" target="_blank" rel="noopener noreferrer" class="page-link">github.com/topahilangharapan</a></td>
                  </tr>
                  <tr>
                    <td class="info-key">Response</td>
                    <td>Usually within 24 hours</td>
                  </tr>
                </table>
                <div class="contact-btn-row">
                  <a href="mailto:musthofaja.topa@gmail.com" class="frutiger-btn">📧 Send Email</a>
                  <button class="frutiger-btn" @click="downloadCV">📄 Download CV</button>
                </div>
              </div>
            </div>
          </div>

        </main>
      </div><!-- end site-body -->

      <!-- Site Footer -->
      <footer class="site-footer">
        <p>© 2007 Musthofa Joko Anggoro · All Rights Reserved</p>
        <p>Best viewed in Internet Explorer 6.0 · Optimised for 1024×768 resolution</p>
        <p>
          <img src="https://img.shields.io/badge/IE-6.0-blue?style=flat" alt="IE6" style="height:14px;vertical-align:middle;opacity:0.7;" />
          &nbsp;
          <img src="https://img.shields.io/badge/resolution-1024x768-lightgrey?style=flat" alt="1024x768" style="height:14px;vertical-align:middle;opacity:0.7;" />
        </p>
      </footer>

    </div><!-- end webpage -->

    <!-- IE Status Bar -->
    <div class="ie-statusbar flex-shrink-0 flex items-center justify-between px-2">
      <span>Done</span>
      <span>🔒 Internet</span>
    </div>

  </div>
</template>

<style scoped>
/* ─── IE CHROME ─────────────────────────────────────────────────── */
.ie-menubar {
  background: var(--xp-silver);
  border-bottom: 1px solid var(--xp-silver-dark);
  padding: 1px 4px;
  display: flex;
  gap: 0;
}
.ie-menu-item {
  font-family: 'Tahoma', sans-serif;
  font-size: 11px;
  padding: 2px 6px;
  cursor: default;
  color: #000;
}
.ie-menu-item:hover { background: #316ac5; color: #fff; }

.ie-toolbar {
  background: linear-gradient(180deg, #f5f4f0 0%, #e0ddd6 100%);
  border-bottom: 1px solid var(--xp-silver-dark);
}
.ie-btn {
  font-family: 'Tahoma', sans-serif;
  font-size: 11px;
  padding: 2px 8px;
  background: linear-gradient(180deg, #fff 0%, #e8e4dc 100%);
  border: 1px outset #ccc;
  cursor: pointer;
  color: #000;
}
.ie-btn:hover { background: linear-gradient(180deg, #ddeeff 0%, #aaccee 100%); }
.ie-btn:active { border-style: inset; }
.ie-label { font-family: 'Tahoma', sans-serif; font-size: 11px; color: #000; padding: 0 4px; }
.ie-addressbar {
  font-family: 'Tahoma', sans-serif;
  font-size: 11px;
  background: white;
  border: 2px inset #999;
  padding: 1px 4px;
  color: #000080;
}
.ie-go-btn {
  font-family: 'Tahoma', sans-serif;
  font-size: 11px;
  padding: 1px 8px;
  background: linear-gradient(180deg, #fff 0%, #e0ddd6 100%);
  border: 1px outset #aaa;
  cursor: pointer;
}
.ie-linksbar {
  background: linear-gradient(180deg, #f5f4f0 0%, #e8e4dc 100%);
  border-bottom: 1px solid var(--xp-silver-dark);
  font-family: 'Tahoma', sans-serif;
  font-size: 11px;
}
.ie-link-label { color: #444; font-weight: bold; }
.ie-link { color: #0000cc; text-decoration: underline; cursor: pointer; }
.ie-link:hover { color: #cc0000; }
.ie-statusbar {
  background: linear-gradient(180deg, #e8e4dc 0%, #d4d0c8 100%);
  border-top: 1px solid #a0a0a0;
  font-family: 'Tahoma', sans-serif;
  font-size: 10px;
  color: #333;
  padding: 1px 4px;
  height: 18px;
}

/* ─── WEBPAGE BACKGROUND ────────────────────────────────────────── */
.webpage-bg {
  background: #e8f0f8;
  font-family: Arial, Verdana, sans-serif;
}

/* ─── SITE HEADER (Frutiger Aero glossy banner) ─────────────────── */
.site-header {
  position: relative;
  background: linear-gradient(180deg, #5bc4f5 0%, #1a8ad4 35%, #0d5fa8 65%, #0a4a88 100%);
  overflow: hidden;
  padding: 16px 20px;
}
.site-header-gloss {
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 50%;
  background: linear-gradient(180deg, rgba(255,255,255,0.45) 0%, rgba(255,255,255,0.05) 100%);
  pointer-events: none;
}
.site-header-content {
  position: relative;
  display: flex;
  align-items: center;
  gap: 16px;
}
.site-avatar {
  width: 56px; height: 56px;
  background: linear-gradient(135deg, #7dd4f8 0%, #1a6bb5 100%);
  border: 3px solid rgba(255,255,255,0.6);
  border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  font-family: Arial, sans-serif;
  font-size: 16px; font-weight: bold; color: white;
  flex-shrink: 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.3), inset 0 1px 0 rgba(255,255,255,0.4);
}
.site-title {
  font-family: Arial, sans-serif;
  font-size: 22px; font-weight: bold;
  color: white;
  text-shadow: 0 1px 3px rgba(0,0,0,0.5);
  margin: 0;
}
.site-subtitle {
  font-family: Arial, sans-serif;
  font-size: 13px; color: #d0eeff;
  margin: 2px 0 0;
  text-shadow: 0 1px 2px rgba(0,0,0,0.4);
}
.site-subtitle2 {
  font-family: Arial, sans-serif;
  font-size: 11px; color: #a8d8f8;
  margin: 1px 0 0;
}

/* ─── SITE NAVIGATION ───────────────────────────────────────────── */
.site-nav {
  display: flex;
  background: linear-gradient(180deg, #2a7cc7 0%, #1055a0 100%);
  border-bottom: 2px solid #0a3a78;
  padding: 0 4px;
}
.site-nav-btn {
  font-family: Arial, sans-serif;
  font-size: 12px; font-weight: bold;
  color: #d8eeff;
  background: transparent;
  border: none;
  padding: 6px 16px;
  cursor: pointer;
  border-bottom: 3px solid transparent;
  transition: all 0.1s;
}
.site-nav-btn:hover {
  color: white;
  background: rgba(255,255,255,0.15);
  text-shadow: 0 0 8px rgba(150,210,255,0.8);
}
.site-nav-btn--active {
  color: white;
  background: linear-gradient(180deg, rgba(255,255,255,0.25) 0%, rgba(255,255,255,0.05) 100%);
  border-bottom-color: #7dd4f8;
}

/* ─── SITE BODY (two-column) ────────────────────────────────────── */
.site-body {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  padding: 12px;
}

/* ─── SIDEBAR ───────────────────────────────────────────────────── */
.site-sidebar {
  width: 160px;
  flex-shrink: 0;
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.sidebar-section {
  background: linear-gradient(180deg, #daeeff 0%, #b8d8f5 100%);
  border: 1px solid #7ab8e8;
  border-radius: 0 0 6px 6px;
  overflow: hidden;
  padding: 8px;
}
.sidebar-avatar {
  width: 44px; height: 44px;
  background: linear-gradient(135deg, #5bc4f5 0%, #1055a0 100%);
  border: 2px solid rgba(255,255,255,0.7);
  border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  font-family: Arial, sans-serif;
  font-size: 13px; font-weight: bold; color: white;
  margin: 0 auto 6px;
  box-shadow: 0 2px 6px rgba(0,80,180,0.3);
}
.sidebar-name {
  font-family: Arial, sans-serif; font-size: 11px; font-weight: bold;
  color: #003366; text-align: center; margin: 0;
}
.sidebar-role {
  font-family: Arial, sans-serif; font-size: 10px;
  color: #336699; text-align: center; margin: 2px 0 6px;
}
.sidebar-status {
  display: flex; align-items: center; justify-content: center; gap: 4px;
  font-family: Arial, sans-serif; font-size: 10px; color: #336699;
}
.status-dot {
  width: 7px; height: 7px; border-radius: 50%;
  background: #44cc44;
  box-shadow: 0 0 4px #44cc44;
}
.sidebar-heading {
  font-family: Arial, sans-serif; font-size: 11px; font-weight: bold;
  color: #003366; border-bottom: 1px solid #7ab8e8; margin-bottom: 4px; padding-bottom: 2px;
}
.sidebar-table { width: 100%; border-collapse: collapse; }
.sidebar-key { font-family: Arial, sans-serif; font-size: 10px; color: #336699; font-weight: bold; padding-right: 4px; white-space: nowrap; }
.sidebar-val { font-family: Arial, sans-serif; font-size: 10px; color: #003366; }
.sidebar-links { display: flex; flex-direction: column; gap: 3px; }
.sidebar-link {
  font-family: Arial, sans-serif; font-size: 11px;
  color: #0055cc; text-decoration: none;
  display: block; padding: 1px 0;
}
.sidebar-link:hover { text-decoration: underline; color: #cc0000; }
.sidebar-dl-btn {
  width: 100%;
  font-family: Arial, sans-serif; font-size: 11px;
  background: linear-gradient(180deg, #7dd4f8 0%, #1a8ad4 50%, #0d6cb3 100%);
  border: 1px solid #0a4a88;
  border-radius: 10px;
  color: white; font-weight: bold;
  padding: 4px 8px;
  cursor: pointer;
  text-shadow: 0 1px 2px rgba(0,0,0,0.4);
  box-shadow: 0 1px 0 rgba(255,255,255,0.3) inset, 0 2px 4px rgba(0,0,0,0.2);
}
.sidebar-dl-btn:hover { background: linear-gradient(180deg, #a0e0ff 0%, #2a9ae4 50%, #1a7ac3 100%); }
.sidebar-counter {
  background: #001a40;
  border: 2px inset #003366;
  border-radius: 4px;
  padding: 6px;
  text-align: center;
}
.counter-label { font-family: 'Courier New', monospace; font-size: 9px; color: #44aa44; }
.counter-number {
  font-family: 'Courier New', monospace; font-size: 18px;
  color: #00ff44; letter-spacing: 2px;
  text-shadow: 0 0 6px #00ff44;
}

/* ─── MAIN CONTENT ──────────────────────────────────────────────── */
.site-main { flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 10px; }

.page-card {
  background: white;
  border: 1px solid #b0cce8;
  border-radius: 6px;
  box-shadow: 0 2px 6px rgba(0,80,160,0.1);
  overflow: hidden;
}
.page-card-header {
  background: linear-gradient(180deg, #4aa8e8 0%, #1a78c8 100%);
  color: white;
  font-family: Arial, sans-serif; font-size: 13px; font-weight: bold;
  padding: 5px 10px;
  text-shadow: 0 1px 2px rgba(0,0,0,0.3);
}
.page-card-body { padding: 10px 12px; }

.page-text {
  font-family: Arial, sans-serif; font-size: 12px;
  color: #333; line-height: 1.6; margin: 0 0 8px;
}
.page-title-large {
  font-family: Arial, sans-serif; font-size: 13px; font-weight: bold;
  color: #003366; line-height: 1.5; margin: 0 0 10px;
}
.page-link { color: #0055cc; text-decoration: underline; }
.page-link:hover { color: #cc0000; }

.highlight-box { display: flex; gap: 10px; align-items: flex-start; margin-bottom: 8px; }
.highlight-icon { font-size: 24px; flex-shrink: 0; }
.highlight-title {
  font-family: Arial, sans-serif; font-size: 13px; font-weight: bold;
  color: #003366; margin: 0 0 4px;
}

.tag-row { display: flex; flex-wrap: wrap; gap: 4px; margin-top: 4px; }
.frutiger-tag {
  display: inline-block;
  background: linear-gradient(180deg, #b8dcf8 0%, #78b8f0 100%);
  border: 1px solid #5898d8;
  border-radius: 10px;
  font-family: Arial, sans-serif; font-size: 10px;
  color: #003366;
  padding: 2px 8px;
}

.info-table { width: 100%; border-collapse: collapse; font-family: Arial, sans-serif; font-size: 12px; margin-bottom: 8px; }
.info-table tr:nth-child(odd) td { background: #f0f7ff; }
.info-table td { padding: 4px 8px; color: #333; vertical-align: top; }
.info-key { font-weight: bold; color: #003366; width: 120px; white-space: nowrap; }
.badge-green {
  background: linear-gradient(180deg, #90e860 0%, #44aa20 100%);
  border: 1px solid #33880f;
  border-radius: 10px;
  color: white; font-size: 11px; font-weight: bold;
  padding: 1px 8px;
  text-shadow: 0 1px 1px rgba(0,0,0,0.3);
}

.gpa-bar-wrap { display: flex; align-items: center; gap: 8px; margin-top: 6px; }
.gpa-bar-track {
  flex: 1; height: 14px;
  background: #d0e8ff;
  border: 1px inset #88b8e8;
  border-radius: 7px;
  overflow: hidden;
}
.gpa-bar-fill {
  height: 100%;
  background: linear-gradient(180deg, #7dd4f8 0%, #1a8ad4 50%, #0d6cb3 100%);
  border-radius: 7px;
  box-shadow: inset 0 1px 0 rgba(255,255,255,0.4);
}
.gpa-bar-label { font-family: Arial, sans-serif; font-size: 12px; font-weight: bold; color: #003366; white-space: nowrap; }

.news-item { display: flex; gap: 10px; font-family: Arial, sans-serif; font-size: 12px; padding: 4px 0; border-bottom: 1px dotted #b0cce8; }
.news-date { color: #336699; font-weight: bold; white-space: nowrap; min-width: 60px; }
.news-text { color: #333; }

.achievement-item { display: flex; align-items: flex-start; gap: 8px; font-family: Arial, sans-serif; font-size: 12px; color: #333; padding: 4px 0; }
.achievement-star { color: #d4a800; font-size: 14px; flex-shrink: 0; }

.project-item {
  background: #f5faff;
  border: 1px solid #c0d8ef;
  border-radius: 4px;
  padding: 8px 10px;
}
.project-item--featured {
  background: linear-gradient(180deg, #e8f4ff 0%, #d0e8ff 100%);
  border-color: #7ab8e8;
  border-left: 4px solid #1a78c8;
}
.project-header { display: flex; align-items: center; gap: 6px; margin-bottom: 4px; }
.project-icon { font-size: 16px; }
.project-title { font-family: Arial, sans-serif; font-size: 12px; font-weight: bold; color: #003366; }
.project-desc { font-family: Arial, sans-serif; font-size: 11px; color: #444; margin: 0 0 4px; line-height: 1.5; }
.project-stack { font-family: Arial, sans-serif; font-size: 10px; color: #336699; margin: 0; }

.contact-btn-row { display: flex; gap: 8px; margin-top: 12px; flex-wrap: wrap; }
.frutiger-btn {
  display: inline-block;
  background: linear-gradient(180deg, #7dd4f8 0%, #1a8ad4 50%, #0d6cb3 100%);
  border: 1px solid #0a4a88;
  border-radius: 12px;
  color: white; font-family: Arial, sans-serif; font-size: 12px; font-weight: bold;
  padding: 5px 16px;
  cursor: pointer; text-decoration: none;
  text-shadow: 0 1px 2px rgba(0,0,0,0.4);
  box-shadow: 0 1px 0 rgba(255,255,255,0.3) inset, 0 2px 4px rgba(0,0,0,0.2);
}
.frutiger-btn:hover { background: linear-gradient(180deg, #a0e0ff 0%, #2a9ae4 50%, #1a7ac3 100%); }

/* ─── FOOTER ────────────────────────────────────────────────────── */
.site-footer {
  background: linear-gradient(180deg, #d0e4f8 0%, #b0cce8 100%);
  border-top: 2px solid #7ab8e8;
  text-align: center;
  padding: 10px;
  font-family: Arial, sans-serif; font-size: 10px; color: #336699;
  line-height: 1.8;
}
</style>
