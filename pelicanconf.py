#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#Name, Basic Build and Path Info 
AUTHOR = u'Leo Wood'
SITENAME = u'LeoJW'
SITEURL = 'https://LeoJW.github.io'
THEME = 'pelicanthemes/Flex'
PATH = 'content'

#Theme Controls
SITETITLE = 'Leo Wood'
SITESUBTITLE = 'MSc Student, UBC Department of Zoology'
SITELOGO = SITEURL + '/images/profile.png'

#Basic Defaults
TIMEZONE = 'America/Chicago'
DEFAULT_LANG = u'en'


FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

STATIC_PATHS = ['images','download','pages']

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True