## 快速说明 (给 AI 代理)

这是一个使用 Pelican 构建的静态博客（内容在 `content/`，主题在 `pelican-themes/`）。下面的要点帮你快速在此仓库内生成、预览、编辑和发布站点。

### 核心概念（大局观）
- 静态站点：由 Pelican（`pelican==4.11.0`，见 `requirements.txt`）把 `content/` 下的 Markdown 转为 `output/` 下的静态页面。
- 配置分环境：`pelicanconf.py` 用于开发，`publishconf.py` 用于发布（生产）。发布配置会把 `SITEURL` 指向 GitHub Pages 地址。
- 主题：存放在 `pelican-themes/`，默认主题由 `THEME` 指向（当前配置使用 `pelican-themes/mg`）。
- 插件：项目使用 `pelican-i18n-subsites` 和站点地图插件（在 `pelicanconf.py` / `publishconf.py` 的 `PLUGINS` 中）。

### 关键文件参考（检索示例）
- 站点配置：`pelicanconf.py`, `publishconf.py`
- 构建脚本：`Makefile`（常见命令）和 `tasks.py`（Invoke 任务，跨平台更可靠）
- 依赖：`requirements.txt`
- 内容样例：`content/个人介绍.md`（展示文章 front-matter 字段：Title, Date, Category, Tags, Slug, Author, Summary）

### 常用命令（在仓库根目录）
- 安装依赖（推荐先激活虚拟环境）：

    pip install -r requirements.txt

- 用 Make（Unix / 有 Make 的 Windows）:

    make html           # 生成开发版本到 output/
    make publish        # 用 publishconf.py 生成发布版本
    make devserver      # 本地带监视的开发服务器

- 在 Windows / 跨平台建议用 Invoke（仓库内有 tasks.py）:

    pip install invoke
    invoke build       # 构建（等同 make html）
    invoke regenerate  # 监听文件修改并重建
    invoke serve       # 使用 tasks.py 中配置的 host/port 启动（会打开浏览器）
    invoke livereload  # livereload 方案（会监视 theme 模板和 content）

- 发布到 GitHub Pages（Makefile 已配置 ghp-import）：

    make github        # 使用 ghp-import 工具并 push 到 `main` 分支（见 Makefile）

或使用 Invoke 的 gh_pages 任务：

    invoke gh_pages

注意：`tasks.py` 的 `publish` 任务使用 `rsync`/SSH（需要在 `CONFIG` 中配置 `ssh_*` 字段），如果没有远程 rsync，应改用 `gh_pages` 或 Makefile 的 `github`。

### 项目约定与模式（对 AI 很重要）
- 内容路径：`PATH = "content"`，`ARTICLE_PATHS = ['']` 表明文章直接放在 `content/` 根目录。
- 静态文件：`STATIC_PATHS = ['attach']` — 附件放 `content/attach/`。
- 国际化/语言：`DEFAULT_LANG = 'zh_CN'`，并使用 `i18n_subsites` 插件。日期格式在 `DATE_FORMATS` 中定义。
- 分页：`DEFAULT_PAGINATION = 4`。

### 编辑内容的示例（可直接参考）
- `content/个人介绍.md` 的 front-matter 用法：

    Title: 个人介绍
    Date: 2025-06-11 10:00
    Category: 个人介绍
    Tags: meta
    Slug: my-intro

  当生成页面时，保持这些字段的存在和合理格式（尤其是 Date 与 Slug）。

### 开发与调试提示（已验证的实践）
- Windows 用户可能没有 Make：优先使用 `invoke`（`tasks.py`）来运行相同任务。
- 如果需要传递 pelican 参数，Makefile 支持通过环境变量覆盖：`PELICAN=pelican make html`，或直接在 `invoke` 后接参数。
- livereload 配置会监视主题模板（`{THEME}/templates/**/*.html`）和 `content/**/*.md`，修改主题或模板后可使用 `invoke livereload` 观察效果。

### 发布/CI 注意事项
- `publishconf.py` 将 `SITEURL` 指向 GitHub Pages（不要在开发时提交未准备好的 SITEURL 变更）。
- Makefile 的 `github` 目标使用 `ghp-import` 并 push 到 `main` 分支（仓库当前 `GITHUB_PAGES_BRANCH=main`）。
- `tasks.py:gh_pages` 也会调用 `ghp-import`，可作为跨平台替代。

### 交互与集成点
- GitHub Pages: `ghp-import` / `git push`（Makefile and tasks.py）
- 本地编辑: theme 模板在 `pelican-themes/` 下，页面在 `content/` 下。修改模板时同时观察 `invoke livereload` 输出。

### 变更和限制（提醒 AI）
- 不要随意移除或更改 `publishconf.py` 中的生产 `SITEURL`，除非你在做发布相关修改。
- `tasks.py` 中的 `publish` 使用 `rsync` 并读取 `CONFIG`（包含 `ssh_*` 字段），不要在没有验证 SSH 配置的情况下运行。

如果你想让我把这些规则精简、拓展为 CI 步骤（例如 GitHub Actions workflow），或把 `Makefile` 的常用命令转为 Windows-friendly PowerShell 脚本，我可以继续实现。请告诉我哪部分需要更详细的例子或补充。 
