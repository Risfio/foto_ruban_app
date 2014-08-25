# -*- coding:utf-8 -*-

import os
from django.contrib.staticfiles import storage

# This pathes will be used in templates.
# We will not use {% load static from staticfiles %}
# Just use {{ styles }} and the same.
# This variables will used in views code in response context.
# I do it - cause in gulp projects i can use just {{ [variable name] }}
# constructions.
static = storage.ConfiguredStorage()
styles = os.path.join(static.location, 'css')
scripts = os.path.join(static.location, 'js')
fonts = os.path.join(static.location, 'fonts')
