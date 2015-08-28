from __future__ import unicode_literals

DEBUG = True
USE_TZ = True
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
    }
},
ROOT_URLCONF = "django_fake_model.urls",
INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "django_fake_model",
],
SITE_ID = 1,
MIDDLEWARE_CLASSES = (),