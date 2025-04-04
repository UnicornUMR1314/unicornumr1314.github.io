AUTHOR = 'Uni星人'
SITENAME = 'Uni星人的博客'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Asia/Shanghai'

# DEFAULT_LANG = 'Chinese (Simplified)'
DEFAULT_LANG = 'zh_CN'  # 修正为标准的语言代码

# 添加本地化配置（必须放在THEME设置之前）
LOCALE = 'zh_CN.UTF-8'
# 添加完整的国际化插件配置
PLUGINS = ['i18n_subsites']
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
    'lstrip_blocks': True,
    'trim_blocks': True
}
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = 'pelican-bootstrap3' # 主题设置
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
# 添加以下配置项允许覆盖输出文件
DELETE_OUTPUT_DIRECTORY = True  # 构建前清空输出目录
OUTPUT_RETENTION = []  # 不保留任何旧文件

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
