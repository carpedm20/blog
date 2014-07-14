#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'carpedm20'
SITENAME = u'carpedm20'
SITEURL = ''

TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = u'ko'

# Metadata
USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = 'Blog'
DEFAULT_DATE_FORMAT = '%B %d, %Y'
FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)'

# Markup
MARKUP = ('rst',)

# Feed generation is usually not desired when developing
FEED_RSS = 'feeds/rss.xml'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Build process
STATIC_PATHS = ['images', 'files']
TYPOGRIFY = False  # TODO blocked by pelican issue #980
SUMMARY_MAX_LENGTH = 15
DEFAULT_PAGINATION = 10
DEFAULT_ORPHANS = 2

# URL configuration
RELATIVE_URLS = True  # dev only
ARTICLE_URL = '{date:%Y}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'
TAG_URL = 'tags/{slug}/'
TAG_SAVE_AS = TAG_URL + 'index.html'
TAGS_URL = 'tags/'
TAGS_SAVE_AS = 'tags/index.html'
ARCHIVES_SAVE_AS = 'archive/index.html'
ARCHIVES_URL = 'archive/'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
#MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%-m}/index.html'
#DAY_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%-m}/{date:%-d}/index.html'
PAGE_LANG_SAVE_AS = False
ARTICLE_LANG_SAVE_AS = False
AUTHOR_SAVE_AS = False
AUTHORS_SAVE_AS = False
CATEGORY_SAVE_AS = False

# Blogroll
LINKS =  (('Name', 'http://url.com/'),)

# Social widget
SOCIAL = (('Twitter', 'http://twitter.com/username'),
                  ('LinkedIn', 'http://twitter.com/username'),
                            ('Github', 'http://twitter.com/username'),)

DEFAULT_PAGINATION = 10

# Template
THEME = "themes/dbrgn"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
