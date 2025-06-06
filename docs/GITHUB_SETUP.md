# GitHub 仓库设置指南

## 1. 创建 GitHub 仓库
1. 访问 https://github.com/new
2. 输入仓库名称：`odoo-scraper`
3. 添加描述：`基于 Odoo 的可配置网页爬虫系统`
4. 选择仓库可见性（公开/私有）
5. 不要初始化仓库（不要添加 README、.gitignore 或 License）

## 2. 连接本地仓库到 GitHub
```bash
# 添加远程仓库
git remote add origin https://github.com/[你的用户名]/odoo-scraper.git

# 推送代码到 GitHub
git push -u origin main
```

## 3. 验证设置
1. 刷新 GitHub 仓库页面
2. 确认所有文件都已上传
3. 检查目录结构是否完整

## 4. 协作设置（可选）
1. 在 GitHub 仓库设置中添加协作者
2. 设置分支保护规则
3. 配置 GitHub Actions（如果需要 CI/CD）

## 5. 安全考虑
1. 确保 `.gitignore` 正确配置
2. 检查是否有敏感信息（如密码、密钥）
3. 必要时使用环境变量或配置文件

## 6. 日常使用流程
```bash
# 获取最新更新
git pull origin main

# 提交本地更改
git add .
git commit -m "更新说明"
git push origin main
``` 