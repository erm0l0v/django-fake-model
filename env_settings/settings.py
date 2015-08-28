from __future__ import unicode_literals


DEBUG = True
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
    }
}
INSTALLED_APPS = [
    "django_fake_model",
]
SECRET_KEY = '_'