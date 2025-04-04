Title: 我的第二篇博客文章13
Category: 技术
Date: 2023-11-01 10:00
Tags: pelican, python, 博客
Slug: my-second-post12
Summary: 这是我使用Pelican创建的第二篇博客文章
# 使用 Pelican + GitHub Actions 搭建自动化静态博客全攻略

## 一、环境准备（Windows/macOS/Linux通用）

### 1.1 安装基础工具链
```bash
安装Python 3.10+
# 安装Pelican及其依赖
pip install pelican markdown ghp-import

```

### 1.2 创建项目目录结构
```bash
创建一个以小写github用户名命名的项目目录并在终端打开
pelican-quickstart  # 按默认配置快速生成项目骨架
```
在交互式提示中，您需要回答一些问题来配置您的博客。以下是一些建议的回答：

- 博客路径：直接按Enter使用当前目录
- 博客标题：输入您想要的博客标题，例如"我的技术博客"
- 博客作者：输入您的名字
- 博客语言：输入 [Chinese (Simplified)]
- 时区：输入 Asia/Shanghai
- 是否使用自定义URL：如果您有域名，输入 y ，否则输入 n
- 如果选择了自定义URL，输入您的域名
- 是否生成Makefile：输入 y
- 是否自动生成文章：输入 y
- 是否使用GitHub Pages：输入 y
- 是否使用GitHub项目页面：输入 y （这将使用 gh-pages 分支）

生成后的关键目录：
```
├── content/        # 原始文章存放地（Markdown格式）
├── output/         # 自动生成的静态文件
├── pelicanconf.py  # 主配置文件
└── Makefile        # 自动化构建脚本
```
### 1.3 生成依赖文件
```bash
# 生成依赖文件
pip freeze > requirements.txt
```
---

## 二、Pelican核心配置（可选）

### 2.1 基础配置
编辑`pelicanconf.py`文件以自定义您的博客
```python
# 基础信息
AUTHOR = 'YourName'
SITENAME = 'Tech Insights'
SITEURL = 'https://yourusername.github.io'

# 路径配置
PATH = 'content'
OUTPUT_PATH = 'output'

# 时间配置
TIMEZONE = 'Asia/Shanghai'
DATE_FORMATS = {
    'zh-CN': '%Y-%m-%d %H:%M',
}
# 主题设置
# THEME = 'notmyidea'  # 默认主题

```
编辑 `publishconf.py`文件以配置发布设置：
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# 如果您有自定义域名，请取消注释并修改下面的行
# SITEURL = 'https://yourdomain.com'
SITEURL = 'https://yourusername.github.io'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# 以下设置通常对于发布很有用
# 取消注释以启用它们
#DISQUS_SITENAME = "yourdisqusname"
#GOOGLE_ANALYTICS = "UA-XXXXXXXX-X"
```
`pelicanconf.py`和`publishconf.py`文件中的配置项可以根据您的需求进行调整。前者是开发环境配置（本地开发和预览），后者是生产环境配置（用于发布）。
### 2.2 在content文件夹创建首篇文章
```bash
content/welcome.md
```

文章头信息（Front Matter）：
```markdown
Title: 欢迎来到我的技术博客
Date: 2025-04-03 10:00
Category: 技术
Tags: pelican, github-actions
Slug: welcome
```

正文内容：
```markdown
欢迎使用Pelican搭建个人技术博客！本文将指导你完成从环境搭建到自动化部署的全流程...

## 安装指南
1. 安装Python环境
2. 创建Pelican项目
3. 编写第一篇文章
```


## 三、GitHub Actions自动化构建

### 3.1 创建GitHub Actions工作流
在项目根目录下创建 `.github/workflows/build.yml`：
```yml
name: Deploy to GitHub Pages

on:
  push:
    branches: [ "main" ]

jobs:
  deploy:
    runs-on: ubuntu-latest  # 改为Linux环境

    steps:
    - name: Checkout
      uses: actions/checkout@v4
      with:
        submodules: recursive

    - name: Set up Python 3.10
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Build site
      run: |
        pelican content -s publishconf.py

    - name: Deploy to GitHub Pages
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      run: |
        ghp-import -m "Automated deployment" -p -f output
```

---

## 四、GitHub Actions自动化部署

### 4.1 创建GitHub仓库
```bash
使用VScode推送并创建远程仓库main分支和gh-pages分支
```
然后修改远程仓库设置中修改仓库名：在原仓库名后面加上.github.io

### 4.2 配置GitHub Pages
在仓库设置中GitHub Pages中选择从分支部署：
- 选择分支：`gh-pages`
- 根目录

---

## 五、持续集成与发布

### 5.1 在本地content中添加文章

### 5.2在主分支推送项目后，检测到主分支内容变动会触发自动构建工作流build.yml
```bash
git add .
git commit -m "这里是提交的信息"
git push origin main
```
工作流会自动构建静态页面并存放到gh-pages分支。
### 5.3 gh-pages分支内容变动会触发自动部署工作流

部署完成后，GitHub Actions会自动生成构建日志，部署成功后即可通过仓库的GitHub Pages链接访问博客。
## 六：更新博客
每当您想要添加新文章或更新博客时，请按照以下步骤操作：

1. 在 content 目录中创建新的Markdown文件
3. 提交更改： git add . && git commit -m "提交信息"
4. 推送到GitHub： git push origin main
5. 等待几分钟，新文章将自动部署到GitHub Pages。
（推荐使用git桌面gui工具提交）