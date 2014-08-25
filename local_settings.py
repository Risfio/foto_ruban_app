# -*- coding:utf-8 -*-

import os
from django.contrib.staticfiles import storage

static = storage.ConfiguredStorage()
styles = os.path.join(static.location, 'css')
scripts = os.path.join(static.location, 'js')
fonts = os.path.join(static.location, 'fonts')
