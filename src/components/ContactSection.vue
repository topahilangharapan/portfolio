<template>
  <div class="max-w-5xl mx-auto">
    <!-- XP Window Container -->
    <div class="xp-window">
      <!-- XP Title Bar -->
      <div class="xp-title-bar">
        <div class="flex items-center">
          <span class="w-4 h-4 bg-white rounded-sm mr-2 flex items-center justify-center text-xs"
            >📧</span
          >
          <span class="font-xp-title">Contact Information - User Properties</span>
        </div>
        <div class="xp-window-controls">
          <div class="xp-control-btn">_</div>
          <div class="xp-control-btn">□</div>
          <div class="xp-control-btn xp-close-btn" @click="toggleOpen">×</div>
        </div>
      </div>

      <!-- Menu Bar -->
      <div class="xp-menubar mb-4">
        <span class="xp-menu-item inline-block">File</span>
        <span class="xp-menu-item inline-block">Edit</span>
        <span class="xp-menu-item inline-block">View</span>
        <span class="xp-menu-item inline-block">Navigate</span>
        <span class="xp-menu-item inline-block">Help</span>
      </div>

      <!-- XP Window Content -->
      <div class="p-4 pt-0 pb-2 bg-xp-window">
        <div class="grid md:grid-cols-2 gap-6">
          <!-- Left Column - Contact Info -->
          <div class="space-y-4">
            <!-- Contact Information Group -->
            <div class="xp-group">
              <div class="xp-group-title">Contact Details</div>
              <div class="space-y-4">
                <p class="font-xp text-black leading-relaxed">
                  I'm always open to discussing new opportunities, collaborations, or just having a
                  chat about technology and development. Feel free to reach out!
                </p>

                <!-- Email Info -->
                <div class="xp-panel-raised p-3">
                  <div class="flex items-center">
                    <div
                      class="w-8 h-8 xp-button flex items-center justify-center mr-3 text-sm font-bold"
                    >
                      @
                    </div>
                    <div>
                      <p class="font-xp text-xs text-gray-600 mb-1">Email Address</p>
                      <a
                        href="mailto:musthofaja.topa@gmail.com"
                        class="font-xp text-blue-600 hover:text-blue-800 font-bold underline"
                      >
                        musthofaja.topa@gmail.com
                      </a>
                    </div>
                  </div>
                </div>

                <!-- Response Time Info -->
                <div class="xp-panel-raised p-3 bg-green-50">
                  <div class="flex items-center">
                    <div class="w-8 h-8 xp-button flex items-center justify-content mr-3 text-sm">
                      ⏱
                    </div>
                    <div>
                      <p class="font-xp text-xs text-gray-600 mb-1">Response Time</p>
                      <p class="font-xp text-green-700 font-bold">Usually within 24 hours</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Right Column - Social Links -->
          <div class="space-y-4">
            <!-- Social Links Group -->
            <div class="xp-group">
              <div class="xp-group-title">Social Networks</div>
              <div class="space-y-3">
                <!-- Profile Links Section -->
                <div class="space-y-4">

                  <!-- LinkedIn -->
                  <div class="xp-panel-raised p-3">
                    <div class="flex items-center">
                      <a
                          href="https://www.linkedin.com/in/musthofa-joko-anggoro/"
                          target="_blank"
                          class="w-10 h-10 bg-blue-600 text-white rounded-sm mr-3 flex items-center justify-center text-xs font-bold"
                      >
                        in
                      </a>
                      <div>
                        <p class="font-xp text-xs text-gray-600 mb-1">LinkedIn Profile</p>
                        <a
                            href="https://www.linkedin.com/in/musthofa-joko-anggoro/"
                            target="_blank"
                            class="font-xp text-blue-600 hover:text-blue-800 font-bold underline break-all"
                        >
                          https://www.linkedin.com/in/musthofa-joko-anggoro/
                        </a>
                      </div>
                    </div>
                  </div>

                  <!-- GitHub -->
                  <div class="xp-panel-raised p-3">
                    <div class="flex items-center">
                      <a
                          href="https://github.com/topahilangharapan"
                          target="_blank"
                          class="w-10 h-10 bg-gray-800 text-white rounded-sm mr-3 flex items-center justify-center text-xs font-bold"
                      >
                        { }
                      </a>
                      <div>
                        <p class="font-xp text-xs text-gray-600 mb-1">GitHub</p>
                        <a
                            href="https://github.com/topahilangharapan"
                            target="_blank"
                            class="font-xp text-gray-800 hover:text-gray-600 font-bold underline break-all"
                        >
                          https://github.com/topahilangharapan
                        </a>
                      </div>
                    </div>
                  </div>

                </div>


                <!-- Portfolio Button -->
                <!--                  <a-->
                <!--                      href="https://johndoe-portfolio.vercel.app"-->
                <!--                      target="_blank"-->
                <!--                      class="xp-button w-full py-3 px-4 flex items-center justify-center text-center hover:bg-green-100 transition-colors duration-200"-->
                <!--                  >-->
                <!--                    <span class="w-6 h-6 bg-green-600 text-white rounded-sm mr-3 flex items-center justify-center text-xs">-->
                <!--                      🌐-->
                <!--                    </span>-->
                <!--                    <span class="font-xp font-bold">Live Portfolio</span>-->
                <!--                  </a>-->
              </div>
            </div>

            <!-- Status Group -->
            <div class="xp-group">
              <div class="xp-group-title">Current Status</div>
              <div class="xp-panel p-3">
                <div class="flex items-center">
                  <div class="w-3 h-3 bg-green-500 rounded-full mr-3 animate-pulse"></div>
                  <div>
                    <p class="font-xp text-xs text-gray-600 mb-1">Availability</p>
                    <p class="font-xp text-green-800 font-bold">Available for opportunities</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Bottom Section -->
        <!--          <div class="mt-6 pt-4 border-t border-gray-400">-->
        <!--            <div class="text-center">-->
        <!--              <p class="font-xp text-black mb-4">-->
        <!--                Ready to build something amazing together?-->
        <!--              </p>-->
        <!--              <button-->
        <!--                  @click="scrollToTop"-->
        <!--                  class="xp-button py-2 px-8 font-xp font-bold"-->
        <!--              >-->
        <!--                Back to Top-->
        <!--              </button>-->
        <!--            </div>-->
        <!--          </div>-->
      </div>
      <!-- XP Status Bar -->
      <div class="xp-status flex justify-between items-center">
        <span class="font-xp">Contact form ready</span>
        <div class="flex items-center space-x-4">
          <span class="font-xp text-xs">📧 Email enabled</span>
          <span class="font-xp text-xs">🌐 Links verified</span>
          <span class="font-xp text-xs">Ready</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
interface Props {
  isOpen: boolean;
}

const props = defineProps<Props>();
const emit = defineEmits<{
  (e: 'update:isOpen', value: boolean): void;
}>();

function toggleOpen() {
  emit('update:isOpen', !props.isOpen);
}

// const scrollToTop = (): void => {
//   window.scrollTo({
//     top: 0,
//     behavior: 'smooth'
//   });
// };
</script>
