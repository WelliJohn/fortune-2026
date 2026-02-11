<template>
  <div class="min-h-screen p-4 py-8">
    <div class="max-w-md mx-auto space-y-4">
      <!-- 返回按钮 -->
      <button
        @click="goHome"
        class="text-white mb-4 hover:underline"
      >
        ← 返回首页
      </button>

      <!-- 关键词卡片 -->
      <div class="card p-8 text-center">
        <p class="text-gray-500 text-sm mb-2">{{ userInfo?.nickname }} 的2026年度关键词</p>
        <h1 class="text-5xl font-bold bg-gradient-to-r from-red-600 to-yellow-500 bg-clip-text text-transparent">
          {{ result?.keyword }}
        </h1>
      </div>

      <!-- 运势指数 -->
      <div class="card p-6">
        <h3 class="text-xl font-bold mb-4 text-gray-800">📊 运势指数</h3>
        <div class="space-y-3">
          <ScoreBar label="综合运势" :score="result?.scores.overall || 0" color="#DC143C" />
          <ScoreBar label="事业" :score="result?.scores.career || 0" color="#FF6347" />
          <ScoreBar label="财运" :score="result?.scores.wealth || 0" color="#FFD700" />
          <ScoreBar label="感情" :score="result?.scores.love || 0" color="#FF69B4" />
          <ScoreBar label="健康" :score="result?.scores.health || 0" color="#32CD32" />
        </div>
      </div>

      <!-- 运势解析 -->
      <div class="card p-6">
        <h3 class="text-xl font-bold mb-3 text-gray-800">🔮 运势解析</h3>
        <p class="text-gray-600 leading-relaxed">{{ result?.analysis }}</p>
      </div>

      <!-- 行动建议 -->
      <div class="card p-6">
        <h3 class="text-xl font-bold mb-3 text-gray-800">💡 行动建议</h3>
        <ul class="space-y-2">
          <li
            v-for="(suggestion, index) in result?.suggestions"
            :key="index"
            class="flex items-start"
          >
            <span class="text-red-500 mr-2 mt-1">•</span>
            <span class="text-gray-600">{{ suggestion }}</span>
          </li>
        </ul>
      </div>

      <!-- 幸运彩蛋 -->
      <div class="card p-6">
        <h3 class="text-xl font-bold mb-4 text-gray-800">🎁 幸运彩蛋</h3>
        <div class="grid grid-cols-3 gap-4 text-center">
          <div>
            <p class="text-gray-500 text-sm mb-1">幸运月份</p>
            <p class="text-2xl font-bold text-red-600">{{ result?.lucky.month }}</p>
          </div>
          <div>
            <p class="text-gray-500 text-sm mb-1">幸运颜色</p>
            <p class="text-2xl font-bold text-yellow-600">{{ result?.lucky.color }}</p>
          </div>
          <div>
            <p class="text-gray-500 text-sm mb-1">幸运数字</p>
            <p class="text-2xl font-bold text-red-600">{{ result?.lucky.number }}</p>
          </div>
        </div>
      </div>

      <!-- 分享按钮 -->
      <div class="flex gap-3">
        <button
          @click="showPoster = true"
          class="btn-primary flex-1"
        >
          🎨 生成分享海报
        </button>
        <button
          @click="drawAgain"
          class="flex-1 bg-gray-200 text-gray-800 px-6 py-3 rounded-full font-semibold hover:bg-gray-300 transition"
        >
          🔄 再抽一次
        </button>
      </div>

      <!-- 底部说明 -->
      <p class="text-xs text-white text-center opacity-70 mt-4">
        本内容仅供娱乐参考，不构成实际决策建议。
      </p>
    </div>

    <!-- 海报弹窗 -->
    <PosterCanvas
      v-if="showPoster"
      :result="result"
      :nickname="userInfo?.nickname || ''"
      @close="showPoster = false"
    />
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import ScoreBar from '../components/ScoreBar.vue'
import PosterCanvas from '../components/PosterCanvas.vue'

interface FortuneResult {
  keyword: string
  scores: {
    overall: number
    career: number
    wealth: number
    love: number
    health: number
  }
  analysis: string
  suggestions: string[]
  lucky: {
    month: string
    color: string
    number: number
  }
}

interface UserInfo {
  nickname: string
  birth_year?: number
}

const router = useRouter()
const result = ref<FortuneResult | null>(null)
const userInfo = ref<UserInfo | null>(null)
const showPoster = ref(false)

onMounted(() => {
  // 从 sessionStorage 获取结果
  const storedResult = sessionStorage.getItem('fortuneResult')
  const storedUserInfo = sessionStorage.getItem('userInfo')

  if (storedResult) {
    result.value = JSON.parse(storedResult)
  } else {
    // 如果没有结果，返回首页
    router.push('/')
  }

  if (storedUserInfo) {
    userInfo.value = JSON.parse(storedUserInfo)
  }
})

const goHome = () => {
  router.push('/')
}

const drawAgain = () => {
  router.push('/draw')
}
</script>
