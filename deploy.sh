#!/bin/bash

# 生产环境部署脚本

echo "🚀 开始部署 2026 开年运势签..."

# 更新系统
sudo apt update && sudo apt upgrade -y

# 安装 Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER

# 安装 Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/download/v2.20.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# 克隆代码（你需要替换为你的Gitee仓库地址）
git clone [你的Gitee仓库地址] /opt/fortune-app
cd /opt/fortune-app

# 构建并启动服务
docker-compose up -d --build

echo "✅ 部署完成！"
echo "应用查看地址: http://你的服务器IP:3000"
echo "API文档地址: http://你的服务器IP:8000/docs"