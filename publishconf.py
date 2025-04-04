# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = "https://unicornumr1314.github.io/"
RELATIVE_URLS = False

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

DELETE_OUTPUT_DIRECTORY = True
# DEFAULT_LANG = 'Chinese (Simplified)'
DEFAULT_LANG = 'zh_CN'  # 修正为标准的语言代码

# 添加完整的国际化插件配置
PLUGINS = ['i18n_subsites']
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
    'lstrip_blocks': True,
    'trim_blocks': True
}
THEME = 'pelican-themes/mg'


DEFAULT_PAGINATION = 4
# Following items are often useful when publishing

# DISQUS_SITENAME = ""
# GOOGLE_ANALYTICS = ""
