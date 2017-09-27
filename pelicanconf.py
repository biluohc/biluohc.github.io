#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Wspsxing'
SITENAME = '江山雪'
SITEURL = ''
# 本地不能设置SITEURL, 否则资源404. 

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = 8
SHOW_DATE_MODIFIED = True
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
# SOCIAL = (('github', 'biluohc'), ('email', "biluohc@qq.com"),)
# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Blogroll
LINKS = (
    ('Rust', 'https://www.rust-lang.org'),
    ('Python', 'http://python.org/'),
)

THEME = "pelican-bootstrap3"
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['i18n_subsites', 'tipue_search', "better_codeblock_line_numbering",
            "render_math", 'neighbors', "neighbors", "series", "tag_cloud", "sitemap"]
SITEMAP = {
    'format': 'xml',
}

MENUITEMS = (("分类", "/categories.html"),)

STATIC_PATHS = ['static']
FAVICON = 'static/images/favicon.ico'
AVATAR = "static/images/logo.png"
ABOUT_ME = """<h3 style="text-align:center">
至虚极, 守静笃。
</h3>
"""
DIRECT_TEMPLATES = ('search', 'index', 'categories', 'authors', 'archives',
                    'tags')
GITHUB_USER = "biluohc"

# 打开标签云
DISPLAY_TAGS_ON_SIDEBAR = True
USE_PAGER = True

CC_LICENSE = "CC-BY-NC-SA"

# 文章的链接和生成文件路径设置
ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
# 分页
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = PAGE_URL
ABOUT_PAGE = "about.html"
# 分类
CATEGORY_URL = '{slug}/index.html'
CATEGORY_SAVE_AS = CATEGORY_URL
# 标签
TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = TAG_URL
TAGS_SAVE_AS = 'tag/index.html'

# 代码不自动换行, 并且标上行号
MD_EXTENSIONS = [
    'codehilite(css_class=highlight,linenums=False)',
    'extra'
    ]
CUSTOM_CSS = 'static/codeline.css'

# 关于评论, Gitment的那一块代码被我插到article.html和page.html模板的文章内容后面了.
# <div id="container"></div>
# <link rel="stylesheet" href="https://imsun.github.io/gitment/style/default.css">
# <script src="https://imsun.github.io/gitment/dist/gitment.browser.js"></script>
# <script>
#     var gitment = new Gitment({
#         // id: '', // 可选。默认为 location.href
#         owner: 'biluohc',
#         repo: 'biluohc.github.io',
#         oauth: {
#             client_id: 'c8ce4b3e0a529dc6f156',
#             client_secret: '01ea647c97776f1cb19cb069670887777c57b358',
#         },
#     })
#     gitment.render('container')
# </script>