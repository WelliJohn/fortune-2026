<template>
  <div class="min-h-screen flex items-center justify-center p-4">
    <div class="card max-w-md w-full p-8 text-center">
      <!-- 装饰元素 -->
      <div class="text-6xl mb-6 animate-bounce">🧧</div>

      <!-- 标题 -->
      <h1 class="text-4xl font-bold mb-4 bg-gradient-to-r from-red-600 to-yellow-500 bg-clip-text text-transparent">
        2026 开年运势签
      </h1>

      <!-- 副标题 -->
      <p class="text-gray-600 text-lg mb-8">
        抽一签，看看你的2026剧情走向
      </p>

      <!-- 按钮 -->
      <button
        class="btn-primary w-full"
        @click="goToDraw"
      >
        🎯 抽我的2026
      </button>

      <!-- 装饰图案 -->
      <div class="mt-8 flex justify-center gap-2 text-2xl">
        <span class="animate-pulse">✨</span>
        <span class="animate-pulse" style="animation-delay: 0.2s">💫</span>
        <span class="animate-pulse" style="animation-delay: 0.4s">⭐</span>
      </div>

      <!-- 底部说明 -->
      <p class="text-xs text-gray-400 mt-8">
        本内容仅供娱乐参考，不构成实际决策建议。
      </p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'

const router = useRouter()

const goToDraw = () => {
  router.push('/draw')
}
</script>

<style scoped>
@keyframes bounce {
  0%, 100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-10px);
  }
}

.animate-bounce {
  animation: bounce 2s infinite;
}

@keyframes pulse {
  0%, 100% {
    opacity: 1;
  }
  50% {
    opacity: 0.5;
  }
}

.animate-pulse {
  animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}
</style>
