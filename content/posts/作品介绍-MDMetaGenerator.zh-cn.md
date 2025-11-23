---
title: MDMetaGenerator：Markdown 元信息创建生成器（带 UI）
subtitle: 一键生成符合 Hugo/DoIt 的文章 Front Matter 与结构
date: 2025-11-23
lastmod: 2025-11-23
draft: false
authors: ["Uni星人"]
description: 表单化生成 Markdown 文章的元信息、摘要分隔与路径命名，内置打包脚本与数据库存储，助力高效创作与规范化发布。

tags: ["作品", "工具", "开源", "Markdown", "Hugo"]
categories: ["作品集"]
series: ["工具与自动化"]

featuredImage: "/images/mdmetagenerator-cover.svg"
featuredImagePreview: "/images/mdmetagenerator-preview.png"

toc:
  enable: true
  auto: true
math:
  enable: false
lightgallery: true
share:
  enable: true
comment:
  enable: true
license: ""
---

## 摘要
MDMetaGenerator 是一款面向内容创作者的桌面端工具，提供图形化界面，表单化生成 Markdown 文章的 Front Matter、摘要与正文分隔（`<!--more-->`）、文件命名与保存路径；内置打包脚本与本地数据库，帮助我在 Hugo + DoIt 主题的站点中快速、规范地发布文章。

<!--more-->

## 项目简介
- 仓库地址：`https://github.com/UnicornUMR1314/MDMetaGenerator`
- 设计目标：降低写作的重复劳动，统一文章元信息与结构；让“写内容”与“发文章”两步更高效、更一致
- 适配场景：本博客使用 Hugo 与 DoIt 主题，生成器输出的 Front Matter 与结构与 `archetypes/posts.md` 完全匹配

## 功能特性
- 表单化生成 Front Matter：`title`、`subtitle`、`date`、`lastmod`、`draft`、`authors`、`description`、`tags`、`categories`、`series`、`featuredImage`、`featuredImagePreview`
- 结构化正文：自动插入 `<!--more-->` 分隔，摘要与正文分离；提供“摘要/正文/附录”建议段落
- 交互开关映射：`toc.enable`/`toc.auto`、`lightgallery`、`share.enable`、`comment.enable`、`math.enable`
- 路径与命名：默认保存至 `content/posts/`，中文后缀 `.zh-cn.md`；可自定义子目录与文件名 slug
- 数据与打包：提供数据库文件与构建脚本，便于记录与分发可执行版本

## 技术栈
- 核心语言：Python
- 打包与构建：批处理/PowerShell 脚本与规范化构建配置
- 数据存储：本地数据库文件用于持久化模板与历史记录

## 架构设计（简述）
- 应用层：GUI 表单 → 字段校验 → 预览与确认 → 文件生成
- 模板层：与站点 `archetypes/posts.md` 字段一一映射，保证兼容性
- 存储层：记录常用作者、系列、分类、默认开关与生成历史，支持复用
- 构建层：提供跨平台脚本，便于发布使用

## 使用方法（与本站集成）
- 选择“中文文章”并填写标题、作者、标签等字段
- 输入摘要与正文，预览分隔与目录生成效果
- 确认保存路径（默认 `content/posts/`），生成 `*.zh-cn.md`
- 本地构建验证：运行 `hugo -D` 或开发预览 `hugo server -D`

## 适配我的博客
- 模板对齐：已与 `archetypes/posts.md` 一致，生成文章即可直接加入本站构建
- 交互一致：目录、分享、评论开关按站点习惯默认开启，可在单篇覆盖
- 版权策略：若 `license` 留空，沿用站点统一版权（参考 `hugo.toml:78`）

## 未来规划
- 多语言联动：同时生成 `.en.md` 英文版本，支持双语 Front Matter
- 模板管理：在 UI 中切换不同栏目模板（如专栏、系列、文档页）
- 资源助手：特色图与预览图的校验与复制自动化

## 仓库链接
- 开源仓库：`https://github.com/UnicornUMR1314/MDMetaGenerator`
- 欢迎 Star 与反馈 Issue，一起把创作流程打磨得更顺手！