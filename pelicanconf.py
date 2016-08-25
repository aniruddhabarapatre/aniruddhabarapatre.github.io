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
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),)

LINKS =  (
    ('Archives', 'archives.html'),
         )

# Social widget
SOCIAL = (('Github', 'https://github.com/aniruddhabarapatre'),
          ('Twitter', 'https://twitter.com/aniruddhabara'),
          ('Linkedin', 'https://linkedin.com/in/aniruddhabarapatre'),)

DEFAULT_PAGINATION = 6

# Specify theme
# THEME = "../pelican-themes/bootstrap"
THEME = "/Users/aniruddhabarapatre1/Blogs/GitBlog/pelican-themes/pelican-blue"

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

TWITTER_USERNAME = "aniruddhabara"
DISQUS_SITENAME = "pelican-blog"
GOOGLE_ANALYTICS = "UA-83099004-1"

