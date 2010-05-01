# -*- coding: utf-8 -*-
#
# Copyright © 2010 Jonatan Littke
#
# This file is part of SimpleEditions.
#
# SimpleEditions is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# SimpleEditions is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with
# SimpleEditions. If not, see http://www.gnu.org/licenses/.
#

import os

# Whether debug help should be enabled. The following code sets it to True if
# the application is running on a development server, False if not.
DEBUG = os.environ['SERVER_SOFTWARE'].startswith('Development')

DOMAIN = 'www.simpleeditions.com'
STATIC_PATH = '/static'
TEMPLATE_DIR = 'templates'
NOT_FOUND_TEMPLATE = '404.html'

# The time that a session should be stored in a user's browser, in days.
SESSION_TTL = 7
