AUTHOR = 'Uni星人'
SITENAME = 'Uni星人的博客'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Asia/Shanghai'

# DEFAULT_LANG = 'Chinese (Simplified)'
DEFAULT_LANG = 'zh_CN'  # 修正为标准的语言代码

# 添加本地化配置（必须放在THEME设置之前）
# 修正Locale设置
LOCALE = ('zh_CN.UTF-8', 'zh_CN', 'zh', 'zh_Hans_CN', 'zh_Hans', 'en_US.UTF-8')
# 添加完整的国际化插件配置
PLUGINS = ['i18n_subsites','pelican.plugins.sitemap',]
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
    'lstrip_blocks': True,
    'trim_blocks': True
}
# 英文日期格式
DATE_FORMATS = {
    'en': '%a, %d %b %Y',
    'zh_CN': '%Y年%m月%d日',
}

# 默认日期格式
DEFAULT_DATE_FORMAT = '%Y年%m月%d日'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = 'pelican-themes/mg' # 主题设置
# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("twitter", "https://x.com/nicornU214610"),
    ("bilibili", "https://space.bilibili.com/84203884"),
    ("github","https://github.com/UnicornUMR1314"),
    ("youtube", "https://youtube.com/channel/UCsQNS3huk3nB-SCOc7C-y8w?si=YKW4WsgDOzl2O8-o"),
)
DEFAULT_PAGINATION = 4

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
