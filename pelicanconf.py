#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from pyembed.rst import PyEmbedRst


AUTHOR = u'Roger Andrés González'
SITENAME = u'Roger Andrés González - rogerandresgonzalez.com.ve'
SITETITLE = 'Roger Andrés González'
SITEURL = 'http://localhost:8000'
#SITEURL = 'http://rogerandresgonzalez.com.ve'

PATH = 'content'

TIMEZONE = 'America/Caracas'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['i18n_subsites', 'sitemap', 'pelican_youtube',]

# Language configs
I18N_SUBSITES = {
    'es': {
        'MENUITEMS': (('Acerca de', '/es/pages/about/'),
			                ('Curriculum', '/es/pages/curriculum/'),
			                ('Archivos', '/es/archives/'),
                      ('Categorías', '/es/category/'),
                      ('Tags', '/es/tag/'),
                      ('English', '/')),
       	'THEME': 'svbhack-theme',
       	'TAGLINE': 'Pythonista. De buen comer. Crítico. Amante de la música. Siempre con ganas de aprender.',
        'SOCIAL': (('linkedin', 'https://ve.linkedin.com/in/rogergonzalez21'),
                   ('github', 'https://github.com/Rogergonzalez21'),
                   ('envelope-o', 'mailto:me@rogerandresgonzalez.com.ve')),
        'HREFLANG' : (('en', 'rogerandresgonzalez.com.ve'),),
        'NEW_POSTS' : "Nuevas Publicaciones",
        'OLD_POSTS' : "Publicaciones Anteriores",
        }
    }

# Sitemap
SITEMAP = {
    'format': 'xml',
    'exclude': ['tag/', 'category/', 'drafts/'],
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# PyEmbed
PyEmbedRst().register()

# Pagination configs
NEW_POSTS = 'Newer Posts'
OLD_POSTS = 'Older Posts'

# Other configs 
HREFLANG = (('es', 'rogerandresgonzalez.com.ve/es/'),)
DISPLAY_PAGES_ON_MENU = False
DEFAULT_DATE_FORMAT = '%d/%m/%Y'
SUMMARY_MAX_LENGTH = 50
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
SLUGIFY_SOURCE = 'title'
STATIC_PATHS = ['images']
THEME = 'svbhack-theme'
USER_LOGO_URL = SITEURL + '/images/yo.png'
META_IMAGE = USER_LOGO_URL
META_IMAGE_TYPE = 'image/png'
FAVICON = SITEURL + '/images/favicon.ico'
GOOGLE_ANALYTICS = 'UA-69257856-1'
DISQUS_SITENAME = 'rogergonzalez21'
TAGLINE = 'Pythonista. Love to eat. Critic. Music lover. Always wanting to learn more.'
DELETE_OUTPUT_DIRECTORY = False
DEFAULT_METADATA = {
    'status': 'draft',
}
MAIN_MENU = True
MENUITEMS = (('About', '/pages/about/'),
			 ('Curriculum Vitae', '/pages/curriculum/'),
			 ('Archive', '/archives/'),
             ('Category', '/category/'),
             ('Tags', '/tag/'),
             ('Español', '/es/'))

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
SOCIAL = (('linkedin', 'https://ve.linkedin.com/in/rogergonzalez21/en'),
          ('github', 'https://github.com/Rogergonzalez21'),
          ('envelope-o', 'mailto:me@rogerandresgonzalez.com.ve'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
    