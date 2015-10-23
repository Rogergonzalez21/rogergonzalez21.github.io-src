#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Roger González blog'
SITENAME = u'Roger González - rogergonzalez.com.ve'
SITETITLE = 'Roger González Blog'
SITEURL = 'http://localhost:8000'
#SITEURL = 'http://rogergonzalez21.github.io'

PATH = 'content'

TIMEZONE = 'America/Caracas'

DEFAULT_LANG = u'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Other configs 
DISPLAY_PAGES_ON_MENU = False
DEFAULT_DATE_FORMAT = '%d/%m/%Y'
SUMMARY_MAX_LENGTH = 50
SLUGIFY_SOURCE = 'title'
STATIC_PATHS = ['images']
THEME = 'svbhack-theme'
USER_LOGO_URL = SITEURL + '/images/yo.png'
FAVICON = SITEURL + '/images/favicon.ico'
GOOGLE_ANALYTICS = ''
DISQUS_SITENAME = ''
TAGLINE = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit' # some text rendered right below the logo
DELETE_OUTPUT_DIRECTORY = False
MAIN_MENU = True
MENUITEMS = (('CV', '/pages/about/'),
			 ('Archives', '/archives/'),
             ('Categories', '/category/'),
             ('Tags', '/tag/'))

# URL's
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'
DRAFT_URL = 'drafts/{slug}/'
DRAFT_SAVE_AS = 'drafts/{slug}.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
TAGS_URL = 'tag/'
TAGS_SAVE_AS = 'tag/index.html'
CATEGORIES_URL = 'category/'
CATEGORIES_SAVE_AS = 'category/index.html'
ARCHIVES_URL = 'archives/'
ARCHIVES_SAVE_AS = 'archives/index.html'

# Social widget
SOCIAL = (('linkedin', 'https://ve.linkedin.com/in/rogergonzalez21'),
          ('github', 'https://github.com/Rogergonzalez21'),
          ('envelope-o', 'mailto:rogergonzalez21@gmail.com'),
          ('stack-overflow', 'http://stackoverflow.com/users/4824187/roger-gonzalez'))

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
