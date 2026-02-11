# 2026 开年运势签

一个移动端互动 H5 应用，让用户通过抽签的方式查看 2026 年的运势预测。

## 📋 项目简介

这是一个前后端分离的全栈项目：
- **前端**：Vue 3 + Vite + TypeScript + TailwindCSS
- **后端**：Python FastAPI
- **特点**：移动端适配、Canvas 生成分享海报、同昵称返回稳定结果

## 🎯 功能特性

### 1️⃣ 首页
- 精美的欢迎界面
- 动画效果
- 一键进入抽签

### 2️⃣ 抽签页面
- 昵称输入（必填）
- 出生年份（选填）
- 关注方向多选（财运、事业、感情、健康、综合）

### 3️⃣ 结果页面
- **年度关键词**：从 50+ 关键词池中随机生成
- **运势指数**：综合、事业、财运、感情、健康（60-95 分）
- **运势解析**：200 字左右的正向鼓励文案
- **行动建议**：3 条实用建议
- **幸运彩蛋**：幸运月份、颜色、数字
- **分享海报**：Canvas 生成精美海报图片

## 🛠️ 技术栈

### 后端
- Python 3.10+
- FastAPI（Web 框架）
- Uvicorn（ASGI 服务器）
- Pydantic（数据验证）

### 前端
- Vue 3（渐进式框架）
- Vite（构建工具）
- TypeScript（类型安全）
- TailwindCSS（样式框架）
- Axios（HTTP 客户端）
- Vue Router（路由管理）

## 🚀 快速开始

### 前置要求

- Python 3.10 或更高版本
- Node.js 16 或更高版本
- npm 或 yarn

### 安装步骤

#### 1. 克隆项目

```bash
git clone [你的Gitee仓库地址]
cd my_future_predict
```

#### 2. 启动后端

```bash
# 进入后端目录
cd fortune-app/backend

# 安装依赖
pip install -r requirements.txt

# 启动服务（默认端口 8000）
uvicorn main:app --reload
```

后端服务将运行在 `http://localhost:8000`

#### 3. 启动前端

打开新的终端窗口：

```bash
# 进入前端目录
cd fortune-app/frontend

# 安装依赖
npm install

# 启动开发服务器（默认端口 3000）
npm run dev
```

前端应用将运行在 `http://localhost:3000`

#### 4. 访问应用

在浏览器中打开 `http://localhost:3000`

**建议使用移动端模式查看**：
- Chrome 浏览器：按 F12 打开开发者工具，点击设备模拟图标
- 或直接在手机浏览器中访问（需确保手机和电脑在同一网络）

## 📊 API 文档

### POST /api/fortune

获取运势结果

**请求体：**

```json
{
  "nickname": "张三",
  "birth_year": 1995,
  "focus": ["事业", "财运"]
}
```

**响应示例：**

```json
{
  "keyword": "破圈",
  "scores": {
    "overall": 82,
    "career": 85,
    "wealth": 78,
    "love": 70,
    "health": 88
  },
  "analysis": "2026年对你来说是一个充满机遇的年份...",
  "suggestions": [
    "上半年多布局，下半年主动争取机会",
    "提升一个核心技能，建立竞争优势",
    "扩大有效社交圈，链接优质资源"
  ],
  "lucky": {
    "month": "8月",
    "color": "暗红",
    "number": 6
  }
}
```

## 🎯 设计亮点

### UI/UX
- 红金渐变主题，符合新年氛围
- 卡片式设计，层次分明
- 流畅的动画过渡
- 移动端手势友好

### 技术特点
- 前后端完全分离
- TypeScript 类型安全
- 组件化开发
- 响应式布局

### 合规设计
- 页面底部明确标注"本内容仅供娱乐参考"
- 不使用"必然""一定"等绝对词
- 正向鼓励，不涉及迷信
- 不提供医疗/投资建议

## 🔧 开发命令

### 后端

```bash
# 启动开发服务器（热重载）
uvicorn main:app --reload

# 启动生产服务器
uvicorn main:app --host 0.0.0.0 --port 8000

# 查看 API 文档
# 访问 http://localhost:8000/docs
```

### 前端

```bash
# 开发模式
npm run dev

# 构建生产版本
npm run build

# 预览生产构建
npm run preview
```

## 📱 移动端调试

### Chrome DevTools
1. 打开开发者工具（F12）
2. 点击设备切换图标（Ctrl+Shift+M）
3. 选择移动设备型号

### 真机测试
1. 确保手机和电脑在同一局域网
2. 获取电脑 IP 地址
3. 在手机浏览器访问 `http://[电脑IP]:3000`

## 🐛 常见问题

### 1. 后端启动失败

**问题**：`ModuleNotFoundError: No module named 'fastapi'`

**解决**：
```bash
pip install -r requirements.txt
```

### 2. 前端启动失败

**问题**：`Cannot find module 'vue'`

**解决**：
```bash
npm install
```

### 3. API 请求失败

**问题**：前端无法访问后端 API

**解决**：
- 确保后端服务已启动（http://localhost:8000）
- 检查 Vite 代理配置（vite.config.ts）
- 查看浏览器控制台错误信息

## 🎉 功能扩展建议

如需扩展功能，可以考虑：

1. **数据持久化**
   - 接入 SQLite/PostgreSQL 数据库
   - 记录用户历史抽签

2. **社交分享**
   - 接入微信/微博分享 SDK
   - 生成真实二维码

3. **更多互动**
   - 添加抽签动画效果
   - 音效反馈
   - 多种海报模板

4. **数据分析**
   - 统计热门关键词
   - 用户行为分析
   - 访问量统计

## 📄 开源协议

MIT License

## 👥 贡献

欢迎提交 Issue 和 Pull Request！

---
**免责声明：本内容仅供娱乐参考，不构成实际决策建议。**