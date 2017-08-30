from __future__ import unicode_literals

from .settings_common import *  #noqa


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        'NAME': ':memory:',
    }
}
