<script setup lang="ts">
import { onMounted, ref } from 'vue'

interface Props {
  isOpenContact: boolean
  isOpenProjects: boolean
}

const props = defineProps<Props>();

const emit = defineEmits<{
  (e: 'update:isOpenContact', value: boolean): void;
  (e: 'update:isOpenProjects', value: boolean): void;
}>();

function toggleOpenContact() {
  emit('update:isOpenContact', !props.isOpenContact);
}

function toggleOpenProjects() {
  emit('update:isOpenProjects', !props.isOpenProjects);
}

const typingText = ref('')
const fullText = 'Full Stack Developer | Student at Universitas Indonesia'
const typingComplete = ref(false)

const available = ref(true)
const collaboration = ref(true)
const internship = ref(true)

// const scrollToContact = () => {
//   const element = document.getElementById('contact')
//   if (element) {
//     element.scrollIntoView({ behavior: 'smooth' })
//   }
// }
//
// const scrollToProjects = () => {
//   const element = document.getElementById('projects')
//   if (element) {
//     element.scrollIntoView({ behavior: 'smooth' })
//   }
// }

const downloadCV = () => {
  const confirmDownload = confirm(
      'Do you want to download the CV file?\n\nThis will download Musthofa Joko Anggoro_CV.pdf to your computer.'
  )
  if (confirmDownload) {
    const link = document.createElement('a')
    link.href = '/public/Copy of CV_Musthofa Joko Anggoro.pdf'
    link.download = 'Musthofa Joko Anggoro_CV.pdf'
    link.click()
  }
}

onMounted(() => {
  // XP boot-up style typing animation
  let index = 0
  const typeInterval = setInterval(() => {
    if (index <= fullText.length) {
      typingText.value = fullText.substring(0, index)
      index++
    } else {
      typingComplete.value = true
      clearInterval(typeInterval)
    }
  }, 80)
})
</script>

<template>
  <div class="container mx-auto px-4 py-8 min-h-screen">
    <div class="flex flex-col lg:flex-row items-start justify-between gap-6">
      <!-- Main Content Window -->
      <div class="flex-1">
        <div class="xp-window">
          <!-- XP Title Bar -->
          <div class="xp-title-bar">
            <div class="flex items-center">
              <span class="w-4 h-4 bg-white rounded-sm mr-2 flex items-center justify-center text-xs">👋</span>
              <span class="font-xp-title">Welcome - Musthofa Joko Anggoro Portfolio</span>
            </div>
<!--            <div class="xp-window-controls">-->
<!--              <div class="xp-control-btn" @click="minimizeWindow">_</div>-->
<!--              <div class="xp-control-btn" @click="maximizeWindow">□</div>-->
<!--              <div class="xp-control-btn xp-close-btn">×</div>-->
<!--            </div>-->
          </div>

          <!-- XP Menu Bar -->
          <div class="xp-menubar">
            <span class="xp-menu-item inline-block">File</span>
            <span class="xp-menu-item inline-block">Edit</span>
            <span class="xp-menu-item inline-block">View</span>
            <span class="xp-menu-item inline-block">Navigate</span>
            <span class="xp-menu-item inline-block">Help</span>
          </div>

          <!-- Window Content -->
          <div class="p-6 bg-xp-window">
            <!-- Personal Information Group -->
            <div class="xp-group mb-6">
              <div class="xp-group-title">Personal Information</div>
              <div class="space-y-4">
                <div>
                  <h2 class="text-3xl lg:text-4xl font-bold text-black mb-2 font-xp">
                    Musthofa Joko Anggoro
                  </h2>
                  <div class="h-6 mb-4">
                    <p class="text-lg lg:text-xl text-blue-600 font-bold font-xp">
                      {{ typingText }}
                      <span v-if="!typingComplete" class="animate-pulse">|</span>
                    </p>
                  </div>
                  <div class="xp-panel p-4">
                    <p class="font-xp text-black">
                      I'm driven by a simple question: "How can we make this better?" My curiosity is always pushing me to learn new technologies and understand how things tick. I enjoy putting together all the pieces, from the user's experience to the powerful systems in the Back-End, to build helpful and effective systems.
                    </p>
                  </div>
                </div>
              </div>
            </div>

            <!-- Action Controls Group -->
            <div class="xp-group mb-6">
              <div class="xp-group-title">Quick Actions</div>
              <div class="grid sm:grid-cols-3 gap-3 mt-4">
                <button
                    @click="toggleOpenContact"
                    class="xp-button px-4 py-3 font-xp font-bold"
                >
                  📧 Get In Touch
                </button>
                <button
                    @click="toggleOpenProjects"
                    class="xp-button px-4 py-3 font-xp font-bold"
                >
                  💼 View Projects
                </button>
                <button
                    @click="downloadCV"
                    class="xp-button-primary px-4 py-3 font-xp font-bold"
                >
                  📄 Download CV
                </button>
              </div>
            </div>

            <!-- Statistics Group -->
            <div class="xp-group">
              <div class="xp-group-title">Portfolio Overview</div>
              <div class="grid grid-cols-3 gap-3 mt-4">
                <!-- Projects Panel -->
                <div class="xp-panel-raised p-3">
                  <div class="flex items-center space-x-2 mb-2">
                    <div class="w-6 h-6 xp-button flex items-center justify-center text-xs">💼</div>
                    <span class="font-xp text-xs font-bold text-black">Projects</span>
                  </div>
                  <div class="text-center">
                    <div class="text-2xl font-bold text-blue-600 font-xp">6</div>
                    <div class="font-xp text-xs text-gray-600">Completed</div>
                  </div>
                  <div class="mt-2 pt-2 border-t border-gray-400">
                    <div class="font-xp text-xs text-black">Web • Mobile • AI</div>
                  </div>
                </div>

                <!-- Experience Panel -->
                <div class="xp-panel-raised p-3">
                  <div class="flex items-center space-x-2 mb-2">
                    <div class="w-6 h-6 xp-button flex items-center justify-center text-xs">⏱️</div>
                    <span class="font-xp text-xs font-bold text-black">Experience</span>
                  </div>
                  <div class="text-center">
                    <div class="text-2xl font-bold text-green-600 font-xp">2+</div>
                    <div class="font-xp text-xs text-gray-600">Years</div>
                  </div>
                  <div class="mt-2 pt-2 border-t border-gray-400">
                    <div class="font-xp text-xs text-black">Learning • Building</div>
                  </div>
                </div>

                <!-- Tech Stack Panel -->
                <div class="xp-panel-raised p-3">
                  <div class="flex items-center space-x-2 mb-2">
                    <div class="w-6 h-6 xp-button flex items-center justify-center text-xs">⚙️</div>
                    <span class="font-xp text-xs font-bold text-black">Tech Stack</span>
                  </div>
                  <div class="text-center">
                    <div class="text-2xl font-bold text-purple-600 font-xp">10+</div>
                    <div class="font-xp text-xs text-gray-600">Technologies</div>
                  </div>
                  <div class="mt-2 pt-2 border-t border-gray-400">
                    <div class="font-xp text-xs text-black">Frontend • Backend • AI/ML</div>
                  </div>
                </div>
              </div>

              <!-- Detailed Stats Row -->
              <div class="mt-4 xp-panel p-3">
                <div class="grid grid-cols-2 lg:grid-cols-4 gap-4 text-center">
                  <div class="text-center">
                    <div class="font-xp text-lg font-bold text-blue-600">Vue.js</div>
                    <div class="font-xp text-xs text-gray-600">Frontend</div>
                  </div>
                  <div class="text-center">
                    <div class="font-xp text-lg font-bold text-green-600">Java</div>
                    <div class="font-xp text-xs text-gray-600">Backend</div>
                  </div>
                  <div class="text-center">
                    <div class="font-xp text-lg font-bold text-purple-600">Spring Boot</div>
                    <div class="font-xp text-xs text-gray-600">Framework</div>
                  </div>
                  <div class="text-center">
                    <div class="font-xp text-lg font-bold text-cyan-600">TypeScript</div>
                    <div class="font-xp text-xs text-gray-600">Support</div>
                  </div>
                </div>
              </div>
            </div>

            <!-- XP Status Bar -->
            <div class="xp-status mt-6 flex justify-between items-center">
              <span class="font-xp">Portfolio loaded successfully</span>
              <div class="flex items-center space-x-4">
                <span class="font-xp text-xs">👨‍💻 Developer</span>
                <span class="font-xp text-xs">🎓 Student</span>
                <span class="font-xp text-xs">Ready</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Profile Image Window -->
      <div class="flex-shrink-0 lg:w-80">
        <div class="xp-window">
          <!-- Profile Window Title Bar -->
          <div class="xp-title-bar">
            <div class="flex items-center">
              <span class="w-4 h-4 bg-white rounded-sm mr-2 flex items-center justify-center text-xs">👤</span>
              <span class="font-xp-title">Profile Picture - Properties</span>
            </div>
<!--            <div class="xp-window-controls">-->
<!--              <div class="xp-control-btn">_</div>-->
<!--              <div class="xp-control-btn">□</div>-->
<!--              <div class="xp-control-btn xp-close-btn">×</div>-->
<!--            </div>-->
          </div>

          <!-- Profile Content -->
          <div class="p-4 bg-xp-window">
            <!-- Profile Image Panel -->
            <div class="xp-panel-raised p-4 mb-4">
              <div class="w-full h-64 xp-panel overflow-hidden flex items-center justify-center">
                <img
                    src="/src/components/Casual_Photo.jpg"
                    alt="Profile"
                    class="w-full h-full object-cover"
                />
              </div>
            </div>


            <!-- Profile Details Group -->
            <div class="xp-group">
              <div class="xp-group-title">Contact Status</div>
              <div class="space-y-2 mt-2">
                <div class="flex items-center space-x-2">
                  <input v-model="available" type="checkbox" class="xp-checkbox" disabled/>
                  <span class="font-xp text-sm">Available for work</span>
                </div>
                <div class="flex items-center space-x-2">
                  <input v-model="collaboration" type="checkbox" class="xp-checkbox" disabled/>
                  <span class="font-xp text-sm">Open to collaboration</span>
                </div>
                <div class="flex items-center space-x-2">
                  <input v-model="internship" type="checkbox" class="xp-checkbox" disabled/>
                  <span class="font-xp text-sm">Seeking internships</span>
                </div>
              </div>
            </div>

            <!-- University Info -->
            <div class="xp-panel mt-4 p-3">
              <div class="text-center">
                <div class="font-xp text-sm font-bold text-black">🎓 University of Indonesia</div>
                <div class="font-xp text-xs text-gray-600">Faculty of Computer Science</div>
                <div class="font-xp text-xs text-blue-600">Expected Graduation: 2026</div>
              </div>
            </div>

            <!-- Profile Status Bar -->
            <div class="xp-status mt-4">
              <span class="font-xp">Status: Available for opportunities</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.container {
  max-width: 1200px;
}

/* XP Typing Animation */
@keyframes blink {
  0%, 50% { opacity: 1; }
  51%, 100% { opacity: 0; }
}

/* Custom checkbox styles for checked state */
.xp-checkbox:checked {
  background: white;
}

.xp-checkbox:checked::after {
  content: '✓';
  position: absolute;
  top: -2px;
  left: 1px;
  font-size: 10px;
  font-weight: bold;
  color: #000;
}

/* Responsive adjustments */
@media (max-width: 1024px) {
  .container {
    padding-left: 1rem;
    padding-right: 1rem;
  }

  .flex-col.lg\\:flex-row {
    gap: 1rem;
  }
}

@media (max-width: 640px) {
  .grid.sm\\:grid-cols-3 {
    grid-template-columns: 1fr;
    gap: 0.75rem;
  }

  .xp-window {
    border-width: 2px;
  }

  .text-3xl.lg\\:text-4xl {
    font-size: 1.5rem;
  }
}
</style>