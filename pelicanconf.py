#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Aniruddha Barapatre'
SITENAME = 'AB Log'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/aniruddhabarapatre'),
          ('Twitter', 'https://twitter.com/aniruddhabara'),
          ('Linkedin', 'https://linkedin.com/in/aniruddhabarapatre'),)

DEFAULT_PAGINATION = 6

# Specify theme
# THEME = "../pelican-themes/bootstrap"
# THEME = "pelican-elegant"

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
