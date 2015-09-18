from __future__ import unicode_literals


DEBUG = True
DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_fake_model',
    }
}
INSTALLED_APPS = [
    "django_fake_model",
]
SECRET_KEY = '_'