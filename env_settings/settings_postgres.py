from __future__ import unicode_literals
import os


DEBUG = True
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

INSTALLED_APPS = [
    "django_fake_model",
]
SECRET_KEY = '0i+ic(!+siwn^a_swjrqr16x^@_2tfnah-e)*-kp1&m(*qx4si'
