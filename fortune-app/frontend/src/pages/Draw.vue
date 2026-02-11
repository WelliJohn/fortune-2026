<template>
  <div class="min-h-screen flex items-center justify-center p-4">
    <div class="card max-w-md w-full p-8">
      <!-- 标题 -->
      <h2 class="text-3xl font-bold text-center mb-6 bg-gradient-to-r from-red-600 to-yellow-500 bg-clip-text text-transparent">
        填写信息
      </h2>

      <!-- 表单 -->
      <form @submit.prevent="handleSubmit" class="space-y-6">
        <!-- 昵称 -->
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-2">
            昵称 <span class="text-red-500">*</span>
          </label>
          <input
            v-model="formData.nickname"
            type="text"
            required
            maxlength="20"
            placeholder="请输入您的昵称"
            class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-500 focus:border-transparent outline-none transition"
          />
        </div>

        <!-- 出生年份 -->
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-2">
            出生年份（选填）
          </label>
          <input
            v-model.number="formData.birth_year"
            type="number"
            min="1950"
            max="2020"
            placeholder="例如：1995"
            class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-500 focus:border-transparent outline-none transition"
          />
        </div>

        <!-- 关注方向 -->
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-3">
            关注方向（多选）
          </label>
          <div class="grid grid-cols-2 gap-3">
            <label
              v-for="option in focusOptions"
              :key="option"
              class="flex items-center space-x-2 p-3 border rounded-lg cursor-pointer transition hover:bg-gray-50"
              :class="{ 'bg-red-50 border-red-500': formData.focus.includes(option) }"
            >
              <input
                type="checkbox"
                :value="option"
                v-model="formData.focus"
                class="w-4 h-4 text-red-600 rounded"
              />
              <span class="text-sm">{{ option }}</span>
            </label>
          </div>
        </div>

        <!-- 提交按钮 -->
        <button
          type="submit"
          :disabled="loading || !formData.nickname"
          class="btn-primary w-full disabled:opacity-50 disabled:cursor-not-allowed"
        >
          {{ loading ? '抽签中...' : '🎲 立即抽签' }}
        </button>
      </form>

      <!-- 返回按钮 -->
      <button
        @click="goBack"
        class="mt-4 w-full text-gray-600 py-2 text-sm hover:text-gray-800 transition"
      >
        ← 返回首页
      </button>

      <!-- 底部说明 -->
      <p class="text-xs text-gray-400 text-center mt-6">
        本内容仅供娱乐参考，不构成实际决策建议。
      </p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()

const formData = ref({
  nickname: '',
  birth_year: null as number | null,
  focus: [] as string[]
})

const focusOptions = ['财运', '事业', '感情', '健康', '综合']
const loading = ref(false)

const handleSubmit = async () => {
  if (!formData.value.nickname) {
    alert('请输入昵称')
    return
  }

  loading.value = true

  try {
    const response = await axios.post('/api/fortune', {
      nickname: formData.value.nickname,
      birth_year: formData.value.birth_year,
      focus: formData.value.focus
    })

    // 将结果存储到 sessionStorage
    sessionStorage.setItem('fortuneResult', JSON.stringify(response.data))
    sessionStorage.setItem('userInfo', JSON.stringify({
      nickname: formData.value.nickname,
      birth_year: formData.value.birth_year
    }))

    // 跳转到结果页
    router.push('/result')
  } catch (error) {
    console.error('抽签失败:', error)
    alert('抽签失败，请稍后重试')
  } finally {
    loading.value = false
  }
}

const goBack = () => {
  router.push('/')
}
</script>
