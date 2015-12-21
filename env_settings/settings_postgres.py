from __future__ import unicode_literals
import os


DEBUG = True
DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': os.environ.get('PGHOST', None),
        'USER': os.environ.get('PGUSER', None),
        'NAME': 'django_fake_model',
    }
}
INSTALLED_APPS = [
    "django_fake_model",
]
SECRET_KEY = '0i+ic(!+siwn^a_swjrqr16x^@_2tfnah-e)*-kp1&m(*qx4si'
