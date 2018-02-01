#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Stu  Hilton'
SITEURL = 'http://localhost:8000'
SITENAME = 'Stu Hilton the Software Engineer'
SITETITLE = AUTHOR
SITESUBTITLE = 'Software Engineer'
SITEDESCRIPTION = '%s\'s thoughts' % AUTHOR
SITELOGO = SITEURL + '/images/profile.png'
FAVICON = SITEURL + '/images/favicon.ico'

THEME = "/home/stu/pelican-themes/Flex"
PATH = 'content'
TIMEZONE = 'Europe/London'
DEFAULT_LANG = 'en'

SOCIAL = (('linkedin', 'https://www.linkedin.com/in/stuhilton'),
          ('github', 'https://github.com/nullMethod'),
          ('twitter', 'https://twitter.com/stuhil'),)


DEFAULT_PAGINATION = 10
