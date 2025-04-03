AUTHOR = 'Uni星人'
SITENAME = 'Uni星人的博客'
SITEURL = "" # 本地开发环境配置（空字符串自动使用 http://localhost:8000 作为根路径）

PATH = "content"

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'Chinese (Simplified)'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
# 主题设置
#THEME = 'notmyidea'  # 默认主题

# 静态路径
# STATIC_PATHS = ['images', 'extra/CNAME','downloads']
# EXTRA_PATH_METADATA = {
#     'extra/CNAME': {'path': 'CNAME'},
# }

# 文章URL结构
# ARTICLE_URL = 'posts/{slug}/'
# ARTICLE_SAVE_AS = 'posts/{slug}/index.html'
# PAGE_URL = 'pages/{slug}/'
# PAGE_SAVE_AS = 'pages/{slug}/index.html'

# 启用Markdown扩展
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}