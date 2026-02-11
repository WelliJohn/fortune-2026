#!/bin/bash

# GitHub部署脚本
# 作者: AI助手
# 用途: 自动化部署fortune-2026项目到GitHub

echo "🚀 开始部署 2026 开年运势签项目到GitHub..."

# 检查Git状态
echo "🔍 检查Git状态..."
if [[ -z $(git status --porcelain) ]]; then
    echo "✅ 工作目录干净"
else
    echo "⚠️  工作目录有未提交的更改，正在提交..."
    git add .
    git commit -m "Auto commit before deployment"
fi

# 获取GitHub用户名
read -p "请输入你的GitHub用户名: " github_username

if [[ -z "$github_username" ]]; then
    echo "❌ 错误: GitHub用户名不能为空"
    exit 1
fi

# 设置远程仓库
echo "🔗 设置远程仓库..."
repo_url="git@github.com:$github_username/fortune-2026.git"
git remote add origin $repo_url 2>/dev/null || git remote set-url origin $repo_url

# 推送代码
echo "📤 推送代码到GitHub..."
git push -u origin main

if [ $? -eq 0 ]; then
    echo "✅ 代码推送成功！"
    echo ""
    echo "🎉 部署完成！"
    echo "🌐 前端访问地址: https://$github_username.github.io/fortune-2026"
    echo "📝 GitHub仓库地址: https://github.com/$github_username/fortune-2026"
    echo ""
    echo "⚙️  下一步配置:"
    echo "1. 访问 https://github.com/$github_username/fortune-2026/settings/pages"
    echo "2. 在'Source'部分选择'GitHub Actions'"
    echo "3. 等待几分钟，GitHub Actions会自动部署"
    echo ""
    echo "📱 部署完成后，你就可以通过上述网址公网访问了！"
else
    echo "❌ 代码推送失败，请检查网络连接和GitHub权限"
    exit 1
fi