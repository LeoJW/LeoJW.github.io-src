#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#Name, Basic Build and Path Info 
AUTHOR = u'Leo Wood'
SITENAME = u'LeoJW'
SITEURL = 'https://LeoJW.github.io'
#SITEURL = 'http://localhost:8000'
THEME = 'pelicanthemes/Flex'
PATH = 'content'

#Theme Controls
SITETITLE = 'Leo Wood'
SITESUBTITLE = 'PhD Student'
SITELOGO = SITEURL + '/images/profile.jpg'

#Basic Defaults
TIMEZONE = 'America/Chicago'
DEFAULT_LANG = u'en'


FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

STATIC_PATHS = ['images','downloads','pages']

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)


DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True