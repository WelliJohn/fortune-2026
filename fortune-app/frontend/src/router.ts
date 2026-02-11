import { createRouter, createWebHistory } from 'vue-router'
import Home from './pages/Home.vue'
import Draw from './pages/Draw.vue'
import Result from './pages/Result.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/draw',
    name: 'Draw',
    component: Draw
  },
  {
    path: '/result',
    name: 'Result',
    component: Result
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
