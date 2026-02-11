<template>
  <div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50" @click.self="$emit('close')">
    <div class="bg-white rounded-lg p-6 max-w-md w-full max-h-[90vh] overflow-y-auto">
      <div class="flex justify-between items-center mb-4">
        <h3 class="text-xl font-bold text-gray-800">分享海报</h3>
        <button @click="$emit('close')" class="text-gray-500 hover:text-gray-700 text-2xl">&times;</button>
      </div>

      <!-- Canvas 画布 -->
      <canvas ref="canvasRef" width="600" height="900" class="w-full border border-gray-200 rounded-lg mb-4"></canvas>

      <!-- 操作按钮 -->
      <div class="flex gap-3">
        <button @click="downloadPoster" class="btn-primary flex-1">
          💾 保存图片
        </button>
        <button @click="$emit('close')" class="flex-1 bg-gray-200 text-gray-800 px-6 py-3 rounded-full font-semibold hover:bg-gray-300 transition">
          关闭
        </button>
      </div>

      <p class="text-xs text-gray-400 text-center mt-4">
        长按图片可保存到相册
      </p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, defineProps, defineEmits } from 'vue'

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

const props = defineProps<{
  result: FortuneResult | null
  nickname: string
}>()

defineEmits(['close'])

const canvasRef = ref<HTMLCanvasElement | null>(null)

onMounted(() => {
  drawPoster()
})

const drawPoster = () => {
  const canvas = canvasRef.value
  if (!canvas || !props.result) return

  const ctx = canvas.getContext('2d')
  if (!ctx) return

  // 设置画布尺寸
  const width = 600
  const height = 900

  // 绘制背景渐变
  const gradient = ctx.createLinearGradient(0, 0, width, height)
  gradient.addColorStop(0, '#DC143C')
  gradient.addColorStop(1, '#FFD700')
  ctx.fillStyle = gradient
  ctx.fillRect(0, 0, width, height)

  // 绘制白色圆角矩形背景
  ctx.fillStyle = 'white'
  roundRect(ctx, 40, 60, width - 80, height - 120, 20)
  ctx.fill()

  // 绘制标题
  ctx.fillStyle = '#DC143C'
  ctx.font = 'bold 48px Arial, sans-serif'
  ctx.textAlign = 'center'
  ctx.fillText('2026 开年运势签', width / 2, 150)

  // 绘制昵称
  ctx.fillStyle = '#666'
  ctx.font = '24px Arial, sans-serif'
  ctx.fillText(`${props.nickname} 的专属运势`, width / 2, 200)

  // 绘制分割线
  ctx.strokeStyle = '#FFD700'
  ctx.lineWidth = 2
  ctx.beginPath()
  ctx.moveTo(80, 230)
  ctx.lineTo(width - 80, 230)
  ctx.stroke()

  // 绘制关键词
  ctx.fillStyle = '#DC143C'
  ctx.font = 'bold 72px Arial, sans-serif'
  ctx.fillText(props.result.keyword, width / 2, 330)

  // 绘制运势指数
  ctx.fillStyle = '#333'
  ctx.font = 'bold 28px Arial, sans-serif'
  ctx.textAlign = 'left'
  ctx.fillText('运势指数', 80, 400)

  // 绘制综合运势
  ctx.font = '20px Arial, sans-serif'
  ctx.fillStyle = '#666'
  ctx.fillText('综合运势', 80, 450)

  ctx.fillStyle = '#DC143C'
  ctx.font = 'bold 32px Arial, sans-serif'
  ctx.textAlign = 'right'
  ctx.fillText(`${props.result.scores.overall}`, width - 80, 450)

  // 绘制进度条
  ctx.fillStyle = '#F0F0F0'
  roundRect(ctx, 80, 470, width - 160, 20, 10)
  ctx.fill()

  const barWidth = ((width - 160) * props.result.scores.overall) / 100
  const barGradient = ctx.createLinearGradient(80, 470, 80 + barWidth, 470)
  barGradient.addColorStop(0, '#DC143C')
  barGradient.addColorStop(1, '#FFD700')
  ctx.fillStyle = barGradient
  roundRect(ctx, 80, 470, barWidth, 20, 10)
  ctx.fill()

  // 绘制金句
  ctx.fillStyle = '#333'
  ctx.font = '22px Arial, sans-serif'
  ctx.textAlign = 'center'
  const quote = props.result.analysis.substring(0, 50) + '...'
  wrapText(ctx, quote, width / 2, 540, width - 160, 30)

  // 绘制幸运信息
  ctx.fillStyle = '#666'
  ctx.font = '20px Arial, sans-serif'
  ctx.textAlign = 'left'
  ctx.fillText(`🍀 幸运月份：${props.result.lucky.month}`, 80, 650)
  ctx.fillText(`🎨 幸运颜色：${props.result.lucky.color}`, 80, 690)
  ctx.fillText(`🔢 幸运数字：${props.result.lucky.number}`, 80, 730)

  // 绘制二维码占位图形
  ctx.fillStyle = '#F5F5F5'
  ctx.fillRect(width / 2 - 60, 760, 120, 120)
  ctx.strokeStyle = '#DDD'
  ctx.lineWidth = 2
  ctx.strokeRect(width / 2 - 60, 760, 120, 120)

  // 绘制二维码文字
  ctx.fillStyle = '#999'
  ctx.font = '14px Arial, sans-serif'
  ctx.textAlign = 'center'
  ctx.fillText('扫码体验', width / 2, 830)

  // 底部文字
  ctx.fillStyle = '#999'
  ctx.font = '14px Arial, sans-serif'
  ctx.fillText('本内容仅供娱乐参考，不构成实际决策建议', width / 2, height - 40)
}

// 绘制圆角矩形
const roundRect = (
  ctx: CanvasRenderingContext2D,
  x: number,
  y: number,
  width: number,
  height: number,
  radius: number
) => {
  ctx.beginPath()
  ctx.moveTo(x + radius, y)
  ctx.lineTo(x + width - radius, y)
  ctx.quadraticCurveTo(x + width, y, x + width, y + radius)
  ctx.lineTo(x + width, y + height - radius)
  ctx.quadraticCurveTo(x + width, y + height, x + width - radius, y + height)
  ctx.lineTo(x + radius, y + height)
  ctx.quadraticCurveTo(x, y + height, x, y + height - radius)
  ctx.lineTo(x, y + radius)
  ctx.quadraticCurveTo(x, y, x + radius, y)
  ctx.closePath()
}

// 文字换行
const wrapText = (
  ctx: CanvasRenderingContext2D,
  text: string,
  x: number,
  y: number,
  maxWidth: number,
  lineHeight: number
) => {
  const words = text.split('')
  let line = ''
  let currentY = y

  for (let n = 0; n < words.length; n++) {
    const testLine = line + words[n]
    const metrics = ctx.measureText(testLine)
    const testWidth = metrics.width

    if (testWidth > maxWidth && n > 0) {
      ctx.fillText(line, x, currentY)
      line = words[n]
      currentY += lineHeight
    } else {
      line = testLine
    }
  }
  ctx.fillText(line, x, currentY)
}

// 下载海报
const downloadPoster = () => {
  const canvas = canvasRef.value
  if (!canvas) return

  // 创建下载链接
  const link = document.createElement('a')
  link.download = `${props.nickname}_2026运势签.png`
  link.href = canvas.toDataURL('image/png')
  link.click()
}
</script>

<style scoped>
canvas {
  display: block;
  background: white;
}
</style>
