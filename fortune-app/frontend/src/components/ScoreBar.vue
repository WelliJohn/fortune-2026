<template>
  <div class="score-bar">
    <div class="flex justify-between items-center mb-2">
      <span class="text-sm font-medium text-gray-700">{{ label }}</span>
      <span class="text-sm font-bold" :style="{ color: color }">{{ score }}</span>
    </div>
    <div class="w-full bg-gray-200 rounded-full h-3 overflow-hidden">
      <div
        class="h-full rounded-full transition-all duration-1000 ease-out"
        :style="{
          width: `${score}%`,
          background: `linear-gradient(90deg, ${color} 0%, ${lightenColor(color)} 100%)`
        }"
      ></div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { defineProps } from 'vue'

defineProps<{
  label: string
  score: number
  color: string
}>()

// 辅助函数：让颜色变亮
const lightenColor = (color: string): string => {
  // 简单的颜色变亮处理
  const colorMap: { [key: string]: string } = {
    '#DC143C': '#FF6B8A',
    '#FF6347': '#FF8C69',
    '#FFD700': '#FFE55C',
    '#FF69B4': '#FFB3D9',
    '#32CD32': '#7FE57F'
  }
  return colorMap[color] || color
}
</script>

<style scoped>
.score-bar {
  animation: fadeIn 0.5s ease-in;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateX(-10px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}
</style>
