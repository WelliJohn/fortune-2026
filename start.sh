#!/bin/bash

echo "🚀 启动 2026 开年运势签项目..."

# 启动后端服务
echo "🔧 启动后端服务..."
cd fortune-app/backend
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000 &

# 等待后端启动
sleep 3

# 启动前端服务
echo "🎨 启动前端服务..."
cd ../frontend
npm install
npm run dev &

echo "✅ 项目启动完成！"
echo "🌐 后端API: http://localhost:8000"
echo "🌐 前端页面: http://localhost:3000"
echo "📄 API文档: http://localhost:8000/docs"

# 保持脚本运行
wait