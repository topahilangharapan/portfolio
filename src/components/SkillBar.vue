<template>
  <div class="mb-4">
    <div class="flex justify-between items-center mb-2">
      <span class="text-sm font-medium text-gray-700">{{ name }}</span>
      <span class="text-sm text-gray-500">{{ level }}%</span>
    </div>
    <div class="w-full bg-gray-200 rounded-full h-2">
      <div
          :class="color"
          class="h-2 rounded-full transition-all duration-1000 ease-out"
          :style="{ width: animatedLevel + '%' }"
      ></div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'

interface Props {
  name: string
  level: number
  color: string
}

const props = defineProps<Props>()
const animatedLevel = ref(0)

onMounted(() => {
  // Animate the skill bar on mount
  setTimeout(() => {
    animatedLevel.value = props.level
  }, 300)
})
</script>