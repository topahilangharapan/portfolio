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

      <!-- Site Header (Frutiger Aero sky banner) -->
      <div class="site-header">
        <div class="aero-clouds" aria-hidden="true"></div>
        <div class="aero-rays" aria-hidden="true"></div>
        <div class="aero-bubbles" aria-hidden="true">
          <span class="bubble bubble-1"></span>
          <span class="bubble bubble-2"></span>
          <span class="bubble bubble-3"></span>
          <span class="bubble bubble-4"></span>
          <span class="bubble bubble-5"></span>
          <span class="bubble bubble-6"></span>
        </div>
        <div class="site-header-gloss" aria-hidden="true"></div>
        <div class="site-header-content">
          <div class="site-avatar">MJA</div>
          <div>
            <h1 class="site-title">Musthofa Joko Anggoro</h1>
            <p class="site-subtitle">Computer Architecture Researcher &amp; PhD Aspirant</p>
            <p class="site-subtitle2">Universitas Indonesia · Fasilkom · Class of 2026</p>
          </div>
        </div>
        <div class="aero-grass" aria-hidden="true"></div>
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
              <tbody>
                <tr><td class="sidebar-key">GPA:</td><td class="sidebar-val">3.85 / 4.00</td></tr>
                <tr><td class="sidebar-key">Grad:</td><td class="sidebar-val">June 2026</td></tr>
                <tr><td class="sidebar-key">Focus:</td><td class="sidebar-val">FPGA &amp; CA</td></tr>
              </tbody>
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
                  <tbody>
                    <tr><td class="info-key">Supervisor</td><td>Prof. Dr. Ir. Petrus Mursanto, M.Sc.</td></tr>
                    <tr><td class="info-key">Institution</td><td>Universitas Indonesia, Fasilkom</td></tr>
                    <tr><td class="info-key">Status</td><td><span class="badge-green">✓ Completed — June 2026</span></td></tr>
                    <tr><td class="info-key">Platform</td><td>Xilinx Spartan-3AN (XC3S700AN)</td></tr>
                    <tr><td class="info-key">Max Frequency</td><td><strong>58.648 MHz</strong> (17.051 ns min period)</td></tr>
                    <tr><td class="info-key">Resource Usage</td><td>1,675 LUTs (14%) · 638 flip-flops (5%)</td></tr>
                  </tbody>
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
                  <tbody>
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
                  </tbody>
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

      <!-- Site Footer (grass) -->
      <footer class="site-footer">
        <p class="footer-tagline">🌿 Clean · Fresh · Connected 💧</p>
        <p>© 2007 Musthofa Joko Anggoro · All Rights Reserved</p>
        <p>Best viewed in Internet Explorer 6.0 · Optimised for 1024×768 resolution</p>
        <p>
          <img src="https://img.shields.io/badge/IE-6.0-blue?style=flat" alt="IE6" style="height:14px;vertical-align:middle;opacity:0.8;" />
          &nbsp;
          <img src="https://img.shields.io/badge/resolution-1024x768-lightgrey?style=flat" alt="1024x768" style="height:14px;vertical-align:middle;opacity:0.8;" />
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

/* ══════════════════════════════════════════════════════════════════
   FRUTIGER AERO WEBPAGE
   Signatures: hard-stop specular gloss (50%/51%), sky→grass nature
   gradients, translucent glass panels, bubbles, aurora glows.
   ══════════════════════════════════════════════════════════════════ */

/* ─── PAGE BACKGROUND (sky aurora + faint bubble rings) ─────────── */
.webpage-bg {
  --aero-font: 'Segoe UI', 'Trebuchet MS', 'Lucida Grande', Verdana, sans-serif;
  --aero-navy: #063a66;
  --aero-blue: #0b74c4;
  --aero-link: #0868b8;
  font-family: var(--aero-font);
  background:
    radial-gradient(circle 46px at 88% 220px, rgba(255,255,255,0.28) 44px, rgba(255,255,255,0) 46px),
    radial-gradient(circle 30px at 6% 420px, rgba(255,255,255,0.22) 28px, rgba(255,255,255,0) 30px),
    radial-gradient(ellipse 80% 50% at 15% -5%, rgba(255,255,255,0.75) 0%, rgba(255,255,255,0) 60%),
    radial-gradient(ellipse 70% 45% at 92% 8%, rgba(170,255,215,0.5) 0%, rgba(170,255,215,0) 60%),
    radial-gradient(ellipse 90% 40% at 50% 104%, rgba(130,230,110,0.55) 0%, rgba(130,230,110,0) 60%),
    linear-gradient(168deg, #c9f0ff 0%, #93dcf8 30%, #56c1f0 62%, #7fd9c0 88%, #9ce89a 100%);
}

/* ─── SITE HEADER (sky, clouds, light rays, bubbles, grass) ─────── */
.site-header {
  position: relative;
  background: linear-gradient(180deg, #9de2fb 0%, #4fbdf0 42%, #1690d8 78%, #0b74c4 100%);
  overflow: hidden;
  padding: 18px 20px 28px;
}
.aero-clouds {
  position: absolute;
  inset: 0;
  background:
    radial-gradient(ellipse 120px 32px at 18% 26%, rgba(255,255,255,0.9) 0%, rgba(255,255,255,0) 70%),
    radial-gradient(ellipse 85px 24px at 29% 20%, rgba(255,255,255,0.75) 0%, rgba(255,255,255,0) 70%),
    radial-gradient(ellipse 150px 38px at 76% 18%, rgba(255,255,255,0.8) 0%, rgba(255,255,255,0) 70%),
    radial-gradient(ellipse 95px 28px at 89% 32%, rgba(255,255,255,0.65) 0%, rgba(255,255,255,0) 70%),
    radial-gradient(ellipse 130px 34px at 54% 62%, rgba(255,255,255,0.3) 0%, rgba(255,255,255,0) 70%);
  animation: clouds-drift 45s ease-in-out infinite alternate;
  pointer-events: none;
}
@keyframes clouds-drift {
  from { transform: translateX(-14px); }
  to   { transform: translateX(14px); }
}
.aero-rays {
  position: absolute;
  inset: -30% -10%;
  background: linear-gradient(112deg,
    transparent 18%, rgba(255,255,255,0.2) 25%, transparent 32%,
    transparent 44%, rgba(255,255,255,0.13) 51%, transparent 58%,
    transparent 68%, rgba(255,255,255,0.18) 75%, transparent 82%);
  mix-blend-mode: screen;
  pointer-events: none;
}
.aero-bubbles { position: absolute; inset: 0; pointer-events: none; }
.bubble {
  position: absolute;
  border-radius: 50%;
  background: radial-gradient(circle at 30% 28%,
    rgba(255,255,255,0.95) 0%, rgba(255,255,255,0.3) 18%,
    rgba(255,255,255,0.06) 45%, rgba(190,240,255,0.14) 100%);
  border: 1px solid rgba(255,255,255,0.55);
  box-shadow: inset -3px -4px 8px rgba(255,255,255,0.35), 0 2px 6px rgba(8,80,140,0.18);
  animation: bubble-bob 8s ease-in-out infinite alternate;
}
.bubble-1 { width: 34px; height: 34px; left: 42%; top: 16%; animation-delay: 0s; }
.bubble-2 { width: 18px; height: 18px; left: 52%; top: 55%; animation-delay: -2.2s; }
.bubble-3 { width: 52px; height: 52px; left: 66%; top: 34%; animation-delay: -4.1s; }
.bubble-4 { width: 14px; height: 14px; left: 78%; top: 62%; animation-delay: -1.3s; }
.bubble-5 { width: 26px; height: 26px; left: 88%; top: 48%; animation-delay: -5.6s; }
.bubble-6 { width: 12px; height: 12px; left: 36%; top: 66%; animation-delay: -3s; }
@keyframes bubble-bob {
  from { transform: translateY(4px); }
  to   { transform: translateY(-8px); }
}
.site-header-gloss {
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 52%;
  background: linear-gradient(180deg, rgba(255,255,255,0.5) 0%, rgba(255,255,255,0.16) 80%, rgba(255,255,255,0) 100%);
  border-radius: 0 0 50% 50% / 0 0 26px 26px;
  pointer-events: none;
}
.aero-grass {
  position: absolute;
  left: 0; right: 0; bottom: 0;
  height: 12px;
  background:
    linear-gradient(180deg, rgba(255,255,255,0.55) 0%, rgba(255,255,255,0.08) 50%, rgba(255,255,255,0) 51%),
    linear-gradient(180deg, #b9ef7d 0%, #6ecd2f 45%, #3f9e13 100%);
  box-shadow: 0 -2px 10px rgba(130,225,95,0.55);
}
.site-header-content {
  position: relative;
  display: flex;
  align-items: center;
  gap: 16px;
}
.site-avatar {
  position: relative;
  width: 60px; height: 60px;
  background: radial-gradient(circle at 32% 28%, #b6ecff 0%, #4fb6ee 48%, #0b6ab8 100%);
  border: 2px solid rgba(255,255,255,0.8);
  border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  font-family: var(--aero-font);
  font-size: 16px; font-weight: bold; color: white;
  flex-shrink: 0;
  text-shadow: 0 1px 2px rgba(0,50,100,0.5);
  box-shadow:
    0 4px 12px rgba(4,60,110,0.4),
    inset 0 -8px 12px rgba(0,60,130,0.35),
    inset 0 2px 4px rgba(255,255,255,0.7);
  overflow: hidden;
}
.site-avatar::before {
  content: '';
  position: absolute;
  top: 3px; left: 15%; right: 15%;
  height: 42%;
  background: linear-gradient(180deg, rgba(255,255,255,0.85) 0%, rgba(255,255,255,0.05) 100%);
  border-radius: 50% 50% 45% 45%;
  pointer-events: none;
}
.site-title {
  font-family: var(--aero-font);
  font-size: 22px; font-weight: bold;
  color: white;
  text-shadow: 0 1px 3px rgba(0,50,100,0.6), 0 0 18px rgba(255,255,255,0.45);
  margin: 0;
}
.site-subtitle {
  font-family: var(--aero-font);
  font-size: 13px; color: #eafaff;
  margin: 2px 0 0;
  text-shadow: 0 1px 2px rgba(0,50,100,0.5);
}
.site-subtitle2 {
  font-family: var(--aero-font);
  font-size: 11px; color: #c5efff;
  margin: 1px 0 0;
  text-shadow: 0 1px 2px rgba(0,50,100,0.4);
}

/* ─── SITE NAVIGATION (glossy aqua bar, glass pill tabs) ────────── */
.site-nav {
  display: flex;
  gap: 4px;
  background: linear-gradient(180deg, #38a8e6 0%, #1183ce 50%, #0a63ad 51%, #0e78c4 100%);
  border-bottom: 1px solid rgba(255,255,255,0.55);
  box-shadow: inset 0 1px 0 rgba(255,255,255,0.5), 0 2px 8px rgba(10,70,130,0.3);
  padding: 5px 8px;
}
.site-nav-btn {
  font-family: var(--aero-font);
  font-size: 12px; font-weight: bold;
  color: #e6f7ff;
  background: transparent;
  border: 1px solid transparent;
  border-radius: 999px;
  padding: 4px 15px;
  cursor: pointer;
  text-shadow: 0 1px 2px rgba(0,45,90,0.5);
  transition: all 0.15s;
}
.site-nav-btn:hover {
  color: white;
  background: linear-gradient(180deg, rgba(255,255,255,0.4) 0%, rgba(255,255,255,0.12) 50%, rgba(255,255,255,0.03) 51%, rgba(255,255,255,0.18) 100%);
  border-color: rgba(255,255,255,0.45);
  box-shadow: 0 0 10px rgba(160,225,255,0.55);
}
.site-nav-btn--active {
  color: var(--aero-navy);
  background: linear-gradient(180deg, #ffffff 0%, #d9f2ff 49%, #abddf8 51%, #d2f0ff 100%);
  border-color: rgba(255,255,255,0.95);
  text-shadow: 0 1px 0 rgba(255,255,255,0.8);
  box-shadow: 0 1px 4px rgba(6,60,110,0.4), inset 0 1px 0 #fff, 0 0 12px rgba(150,255,190,0.5);
}

/* ─── SITE BODY (two-column) ────────────────────────────────────── */
.site-body {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  padding: 12px;
}

/* ─── SIDEBAR (translucent glass panels) ────────────────────────── */
.site-sidebar {
  width: 160px;
  flex-shrink: 0;
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.sidebar-section {
  background: linear-gradient(180deg, rgba(255,255,255,0.88) 0%, rgba(224,246,255,0.66) 100%);
  border: 1px solid rgba(255,255,255,0.95);
  outline: 1px solid rgba(88,170,220,0.4);
  border-radius: 10px;
  box-shadow: 0 3px 10px rgba(15,95,165,0.16), inset 0 1px 0 rgba(255,255,255,1);
  backdrop-filter: blur(3px);
  padding: 9px;
}
.sidebar-avatar {
  position: relative;
  width: 46px; height: 46px;
  background: radial-gradient(circle at 32% 28%, #a5e6ff 0%, #3fadea 50%, #0a5ea6 100%);
  border: 2px solid rgba(255,255,255,0.85);
  border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  font-family: var(--aero-font);
  font-size: 13px; font-weight: bold; color: white;
  margin: 0 auto 6px;
  text-shadow: 0 1px 2px rgba(0,50,100,0.5);
  box-shadow: 0 2px 8px rgba(0,80,180,0.35), inset 0 -5px 8px rgba(0,60,130,0.3), inset 0 1px 3px rgba(255,255,255,0.7);
  overflow: hidden;
}
.sidebar-avatar::before {
  content: '';
  position: absolute;
  top: 2px; left: 16%; right: 16%;
  height: 42%;
  background: linear-gradient(180deg, rgba(255,255,255,0.85) 0%, rgba(255,255,255,0.05) 100%);
  border-radius: 50% 50% 45% 45%;
  pointer-events: none;
}
.sidebar-name {
  font-family: var(--aero-font); font-size: 11px; font-weight: bold;
  color: var(--aero-navy); text-align: center; margin: 0;
}
.sidebar-role {
  font-family: var(--aero-font); font-size: 10px;
  color: #14669e; text-align: center; margin: 2px 0 6px;
}
.sidebar-status {
  display: flex; align-items: center; justify-content: center; gap: 4px;
  font-family: var(--aero-font); font-size: 10px; color: #14669e;
}
.status-dot {
  width: 8px; height: 8px; border-radius: 50%;
  background: radial-gradient(circle at 32% 28%, #d9ffb3 0%, #55d420 55%, #2f9a08 100%);
  box-shadow: 0 0 6px rgba(90,225,45,0.95), inset 0 1px 1px rgba(255,255,255,0.8);
  animation: status-pulse 2.2s ease-in-out infinite;
}
@keyframes status-pulse {
  0%, 100% { box-shadow: 0 0 4px rgba(90,225,45,0.7), inset 0 1px 1px rgba(255,255,255,0.8); }
  50%      { box-shadow: 0 0 10px rgba(110,240,60,1), inset 0 1px 1px rgba(255,255,255,0.8); }
}
.sidebar-heading {
  font-family: var(--aero-font); font-size: 11px; font-weight: bold;
  color: var(--aero-navy);
  border-bottom: 1px solid rgba(88,170,220,0.55);
  margin-bottom: 4px; padding-bottom: 2px;
}
.sidebar-table { width: 100%; border-collapse: collapse; }
.sidebar-key { font-family: var(--aero-font); font-size: 10px; color: #14669e; font-weight: bold; padding-right: 4px; white-space: nowrap; }
.sidebar-val { font-family: var(--aero-font); font-size: 10px; color: var(--aero-navy); }
.sidebar-links { display: flex; flex-direction: column; gap: 3px; }
.sidebar-link {
  font-family: var(--aero-font); font-size: 11px;
  color: var(--aero-link); text-decoration: none;
  display: block; padding: 1px 0;
  transition: text-shadow 0.15s;
}
.sidebar-link:hover {
  text-decoration: underline;
  color: #045094;
  text-shadow: 0 0 8px rgba(120,215,255,0.9);
}

/* Grass-green glossy download button (nature accent) */
.sidebar-dl-btn {
  position: relative;
  overflow: hidden;
  width: 100%;
  font-family: var(--aero-font); font-size: 11px;
  background: linear-gradient(180deg, #cdf78a 0%, #82d93c 49%, #4aad15 51%, #67c72a 100%);
  border: 1px solid rgba(255,255,255,0.8);
  outline: 1px solid #3c8f10;
  border-radius: 999px;
  color: white; font-weight: bold;
  padding: 5px 8px;
  cursor: pointer;
  text-shadow: 0 1px 2px rgba(20,80,0,0.55);
  box-shadow: inset 0 1px 0 rgba(255,255,255,0.75), inset 0 -4px 8px rgba(30,110,0,0.3), 0 2px 6px rgba(30,110,10,0.35);
}
.sidebar-dl-btn:hover {
  background: linear-gradient(180deg, #e0ffa8 0%, #97e651 49%, #58bd1f 51%, #78d439 100%);
  box-shadow: inset 0 1px 0 rgba(255,255,255,0.75), inset 0 -4px 8px rgba(30,110,0,0.3), 0 2px 10px rgba(90,200,50,0.6);
}
.sidebar-dl-btn::after {
  content: '';
  position: absolute;
  top: -20%; bottom: -20%; left: -60%;
  width: 40%;
  background: linear-gradient(105deg, transparent 0%, rgba(255,255,255,0.75) 50%, transparent 100%);
  transform: skewX(-20deg);
  transition: left 0.5s ease;
  pointer-events: none;
}
.sidebar-dl-btn:hover::after { left: 130%; }

/* Hit counter — dark glass LED */
.sidebar-counter {
  position: relative;
  overflow: hidden;
  background: linear-gradient(180deg, #0d2c52 0%, #04162e 100%);
  border: 1px solid rgba(160,220,255,0.4);
  border-radius: 10px;
  padding: 7px 6px;
  text-align: center;
  box-shadow: inset 0 2px 6px rgba(0,0,0,0.6), 0 2px 6px rgba(10,70,130,0.25);
}
.sidebar-counter::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 45%;
  background: linear-gradient(180deg, rgba(255,255,255,0.22) 0%, rgba(255,255,255,0.02) 100%);
  pointer-events: none;
}
.counter-label { font-family: 'Courier New', monospace; font-size: 9px; color: #55cc77; }
.counter-number {
  font-family: 'Courier New', monospace; font-size: 18px;
  color: #00ff66; letter-spacing: 2px;
  text-shadow: 0 0 8px #00ff66;
}

/* ─── MAIN CONTENT (glass cards with glossy aqua headers) ───────── */
.site-main { flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 10px; }

.page-card {
  background: linear-gradient(180deg, rgba(255,255,255,0.94) 0%, rgba(236,250,255,0.85) 100%);
  border: 1px solid rgba(255,255,255,0.95);
  outline: 1px solid rgba(88,170,220,0.4);
  border-radius: 12px;
  box-shadow: 0 4px 16px rgba(12,90,160,0.18), inset 0 1px 0 rgba(255,255,255,1);
  backdrop-filter: blur(3px);
  overflow: hidden;
}
.page-card-header {
  position: relative;
  background: linear-gradient(180deg, #58bff3 0%, #1b91da 49%, #0b70bd 51%, #1387d0 100%);
  color: white;
  font-family: var(--aero-font); font-size: 13px; font-weight: bold;
  padding: 6px 12px;
  text-shadow: 0 1px 2px rgba(0,45,90,0.55);
  border-bottom: 1px solid rgba(255,255,255,0.5);
}
.page-card-header::after {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 50%;
  background: linear-gradient(180deg, rgba(255,255,255,0.55) 0%, rgba(255,255,255,0.12) 100%);
  pointer-events: none;
}
.page-card-body { padding: 10px 12px; }

.page-text {
  font-family: var(--aero-font); font-size: 12px;
  color: #234; line-height: 1.6; margin: 0 0 8px;
}
.page-title-large {
  font-family: var(--aero-font); font-size: 13px; font-weight: bold;
  color: var(--aero-navy); line-height: 1.5; margin: 0 0 10px;
}
.page-link { color: var(--aero-link); text-decoration: underline; }
.page-link:hover { color: #045094; text-shadow: 0 0 8px rgba(120,215,255,0.8); }

.highlight-box { display: flex; gap: 10px; align-items: flex-start; margin-bottom: 8px; }
.highlight-icon { font-size: 24px; flex-shrink: 0; filter: drop-shadow(0 2px 3px rgba(10,90,160,0.35)); }
.highlight-title {
  font-family: var(--aero-font); font-size: 13px; font-weight: bold;
  color: var(--aero-navy); margin: 0 0 4px;
}

/* Glossy aqua pill tags */
.tag-row { display: flex; flex-wrap: wrap; gap: 4px; margin-top: 4px; }
.frutiger-tag {
  display: inline-block;
  background: linear-gradient(180deg, #eafaff 0%, #b6e5fb 49%, #8cd3f6 51%, #bdeeff 100%);
  border: 1px solid rgba(255,255,255,0.9);
  outline: 1px solid rgba(70,160,215,0.55);
  border-radius: 999px;
  font-family: var(--aero-font); font-size: 10px;
  color: #084a80;
  padding: 2px 9px;
  text-shadow: 0 1px 0 rgba(255,255,255,0.75);
  box-shadow: inset 0 1px 0 rgba(255,255,255,0.95), 0 1px 3px rgba(20,100,170,0.25);
}

.info-table { width: 100%; border-collapse: collapse; font-family: var(--aero-font); font-size: 12px; margin-bottom: 8px; }
.info-table tr:nth-child(odd) td { background: rgba(200,238,255,0.45); }
.info-table td { padding: 4px 8px; color: #234; vertical-align: top; }
.info-key { font-weight: bold; color: var(--aero-navy); width: 120px; white-space: nowrap; }

/* Glossy grass-green badge */
.badge-green {
  background: linear-gradient(180deg, #c1f284 0%, #7cd738 49%, #47a913 51%, #63c327 100%);
  border: 1px solid rgba(255,255,255,0.8);
  outline: 1px solid #3c8f10;
  border-radius: 999px;
  color: white; font-size: 11px; font-weight: bold;
  padding: 1px 9px;
  text-shadow: 0 1px 1px rgba(20,80,0,0.5);
  box-shadow: inset 0 1px 0 rgba(255,255,255,0.7);
}

/* GPA bar — glossy green liquid with shimmer stripes */
.gpa-bar-wrap { display: flex; align-items: center; gap: 8px; margin-top: 6px; }
.gpa-bar-track {
  flex: 1; height: 16px;
  background: linear-gradient(180deg, rgba(205,238,255,0.9) 0%, rgba(255,255,255,0.75) 100%);
  border: 1px solid rgba(255,255,255,0.9);
  outline: 1px solid rgba(80,160,210,0.5);
  border-radius: 999px;
  box-shadow: inset 0 2px 4px rgba(20,90,150,0.25);
  overflow: hidden;
}
.gpa-bar-fill {
  height: 100%;
  background:
    linear-gradient(180deg, rgba(255,255,255,0.6) 0%, rgba(255,255,255,0.12) 50%, rgba(255,255,255,0) 51%),
    repeating-linear-gradient(115deg, rgba(255,255,255,0.25) 0 8px, rgba(255,255,255,0) 8px 16px),
    linear-gradient(180deg, #a5e968 0%, #58c21e 60%, #3d9c12 100%);
  border-radius: 999px;
  box-shadow: inset 0 -3px 5px rgba(30,110,0,0.35);
  animation: gpa-shimmer 2.4s linear infinite;
}
@keyframes gpa-shimmer {
  from { background-position: 0 0, 0 0, 0 0; }
  to   { background-position: 0 0, 35px 0, 0 0; }
}
.gpa-bar-label { font-family: var(--aero-font); font-size: 12px; font-weight: bold; color: var(--aero-navy); white-space: nowrap; }

.news-item { display: flex; gap: 10px; font-family: var(--aero-font); font-size: 12px; padding: 4px 0; border-bottom: 1px dotted rgba(88,170,220,0.55); }
.news-date { color: #14669e; font-weight: bold; white-space: nowrap; min-width: 60px; }
.news-text { color: #234; }

.achievement-item { display: flex; align-items: flex-start; gap: 8px; font-family: var(--aero-font); font-size: 12px; color: #234; padding: 4px 0; }
.achievement-star { color: #f0a500; font-size: 14px; flex-shrink: 0; text-shadow: 0 0 6px rgba(255,200,60,0.8); }

/* Project items — mini glass tiles, featured gets a nature accent */
.project-item {
  background: linear-gradient(180deg, rgba(255,255,255,0.8) 0%, rgba(222,245,255,0.6) 100%);
  border: 1px solid rgba(255,255,255,0.9);
  outline: 1px solid rgba(110,185,230,0.45);
  border-radius: 9px;
  padding: 8px 10px;
  box-shadow: inset 0 1px 0 rgba(255,255,255,1), 0 2px 6px rgba(15,95,165,0.12);
  transition: box-shadow 0.15s, transform 0.15s;
}
.project-item:hover {
  box-shadow: inset 0 1px 0 rgba(255,255,255,1), 0 4px 12px rgba(15,95,165,0.25), 0 0 14px rgba(140,220,255,0.4);
  transform: translateY(-1px);
}
.project-item--featured {
  background: linear-gradient(180deg, rgba(238,255,225,0.9) 0%, rgba(208,246,190,0.7) 100%);
  outline-color: rgba(110,200,80,0.6);
  border-left: 4px solid #58c21e;
}
.project-header { display: flex; align-items: center; gap: 6px; margin-bottom: 4px; }
.project-icon { font-size: 16px; filter: drop-shadow(0 1px 2px rgba(10,90,160,0.3)); }
.project-title { font-family: var(--aero-font); font-size: 12px; font-weight: bold; color: var(--aero-navy); }
.project-desc { font-family: var(--aero-font); font-size: 11px; color: #345; margin: 0 0 4px; line-height: 1.5; }
.project-stack { font-family: var(--aero-font); font-size: 10px; color: #14669e; margin: 0; }

/* Glossy aqua capsule buttons with shine sweep */
.contact-btn-row { display: flex; gap: 8px; margin-top: 12px; flex-wrap: wrap; }
.frutiger-btn {
  position: relative;
  overflow: hidden;
  display: inline-block;
  background: linear-gradient(180deg, #a3e4ff 0%, #2ea6ea 49%, #0b74c4 51%, #2d98de 100%);
  border: 1px solid rgba(255,255,255,0.8);
  outline: 1px solid #0a5ea6;
  border-radius: 999px;
  color: white; font-family: var(--aero-font); font-size: 12px; font-weight: bold;
  padding: 6px 18px;
  cursor: pointer; text-decoration: none;
  text-shadow: 0 1px 2px rgba(0,50,100,0.55);
  box-shadow: inset 0 1px 0 rgba(255,255,255,0.7), inset 0 -4px 8px rgba(0,70,140,0.35), 0 2px 6px rgba(8,70,130,0.35);
}
.frutiger-btn:hover {
  background: linear-gradient(180deg, #c2eeff 0%, #45b6f0 49%, #1584d4 51%, #40a8e8 100%);
  box-shadow: inset 0 1px 0 rgba(255,255,255,0.7), inset 0 -4px 8px rgba(0,70,140,0.35), 0 2px 12px rgba(60,170,240,0.6);
}
.frutiger-btn::after {
  content: '';
  position: absolute;
  top: -20%; bottom: -20%; left: -60%;
  width: 40%;
  background: linear-gradient(105deg, transparent 0%, rgba(255,255,255,0.75) 50%, transparent 100%);
  transform: skewX(-20deg);
  transition: left 0.5s ease;
  pointer-events: none;
}
.frutiger-btn:hover::after { left: 130%; }

/* ─── FOOTER (glossy grass) ─────────────────────────────────────── */
.site-footer {
  position: relative;
  overflow: hidden;
  background: linear-gradient(180deg, #b9ef7d 0%, #6ecd2f 42%, #43a214 100%);
  border-top: 1px solid rgba(255,255,255,0.7);
  text-align: center;
  padding: 12px 10px;
  font-family: var(--aero-font); font-size: 10px; color: #f2ffe8;
  text-shadow: 0 1px 2px rgba(20,80,10,0.55);
  line-height: 1.8;
  box-shadow: inset 0 2px 8px rgba(255,255,255,0.35);
}
.site-footer::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 48%;
  background: linear-gradient(180deg, rgba(255,255,255,0.45) 0%, rgba(255,255,255,0.05) 100%);
  border-radius: 0 0 50% 50% / 0 0 18px 18px;
  pointer-events: none;
}
.site-footer p { position: relative; }
.site-footer img { display: inline-block; }
.footer-tagline {
  font-size: 11px;
  font-weight: bold;
  letter-spacing: 1px;
  color: #ffffff;
}
</style>
