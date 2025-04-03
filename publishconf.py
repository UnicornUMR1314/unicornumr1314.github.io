# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = "https://unicornumr1314.github.io"
RELATIVE_URLS = False

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
AUTHOR_FEED_RSS = 'feeds/{slug}.rss.xml' 

DELETE_OUTPUT_DIRECTORY = True
# 设置英文日期格式
DATE_FORMATS = {
    'en': '%a, %d %b %Y',
}

# 设置中文日期格式
LOCALE = ['zh_CN.utf8', 'zh_CN.UTF-8']
DEFAULT_DATE_FORMAT = '%Y年%m月%d日'

# Following items are often useful when publishing

# DISQUS_SITENAME = ""
# GOOGLE_ANALYTICS = ""
