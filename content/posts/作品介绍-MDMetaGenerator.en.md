---
title: "MDMetaGenerator: Markdown Metadata Generator (UI)"
subtitle: "One-click Front Matter and structure for Hugo/DoIt articles"
date: 2025-11-23
lastmod: 2025-11-23
draft: false
authors: ["Uni星人"]
description: "Generate article Front Matter, summary separator, and file naming via a UI. Built-in scripts and local database help standardized, efficient publishing."

tags: ["Project", "Tool", "Open Source", "Markdown", "Hugo"]
categories: ["Portfolio"]
series: ["Tools & Automation"]

featuredImage: "/posts/image/mdmetagenerator-cover.png"
featuredImagePreview: "/posts/image/mdmetagenerator-preview.png"

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

## Summary
MDMetaGenerator is a desktop tool for content creators. It provides a GUI to generate Markdown Front Matter, insert the `<!--more-->` separator, and control file naming and save path. With packaging scripts and a local database, it helps me publish posts quickly and consistently on a Hugo site using the DoIt theme.

<!--more-->

## Overview
- Repository: `https://github.com/UnicornUMR1314/MDMetaGenerator`
- Goal: Reduce repetitive writing tasks and unify article metadata and structure
- Fit: Output Front Matter and structure align with `archetypes/posts.md` in this blog

## Features
- Front Matter via form: `title`, `subtitle`, `date`, `lastmod`, `draft`, `authors`, `description`, `tags`, `categories`, `series`, `featuredImage`, `featuredImagePreview`
- Structured content: auto `<!--more-->` insertion, suggested sections for Summary/Body/Appendix
- Toggles mapping: `toc.enable`/`toc.auto`, `lightgallery`, `share.enable`, `comment.enable`, `math.enable`
- Path & naming: default `content/posts/` with `.en.md` for English; custom subdir and slug supported
- Data & packaging: database file and build scripts for recording and distributing executables

## Tech Stack
- Language: Python
- Build: batch/PowerShell scripts and configuration
- Storage: local database for templates and history

## Architecture
- UI: form → validation → preview & confirm → file generation
- Template: one-to-one mapping to `archetypes/posts.md`
- Storage: common authors, series, categories, defaults, generation history
- Build: cross-platform scripts

## Usage (in this blog)
- Choose language, fill title, authors, tags
- Write Summary and Body, preview separator and ToC
- Confirm save path (default `content/posts/`), generate `*.en.md`
- Validate locally: `hugo -D` or dev preview `hugo server -D`

## Blog Integration
- Template aligned: compatible with `archetypes/posts.md`
- Toggles: ToC, share, comments enabled by default; per-post override supported
- License: leave `license` empty to use site-wide license (`hugo.toml:78`)

## Roadmap
- Bilingual generation: produce `.zh-cn.md` and `.en.md` together
- Template management: switch among column/series/docs templates in UI
- Asset helper: validate/copy featured and preview images automatically

## Links
- Repository: `https://github.com/UnicornUMR1314/MDMetaGenerator`
