from __future__ import unicode_literals

import os

from .settings_common import *  #noqa


DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_fake_model',
    }
}
if 'MYSQL_HOST' in os.environ:
    DATABASES['default']['HOST'] = os.environ['MYSQL_HOST']
