from __future__ import unicode_literals

import os

from .settings_common import *  #noqa


DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_fake_model',
    }
}
if 'PGHOST' in os.environ:
    DATABASES['default']['HOST'] = os.environ['PGHOST']
if 'PGUSER' in os.environ:
    DATABASES['default']['USER'] = os.environ['PGUSER']
