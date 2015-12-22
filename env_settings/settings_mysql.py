from __future__ import unicode_literals
import os


DEBUG = True
DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_fake_model',
    }
}
if 'MYSQL_HOST' in os.environ:
    DATABASES['default']['HOST'] = os.environ['MYSQL_HOST']

INSTALLED_APPS = [
    "django_fake_model",
]
SECRET_KEY = '0i+ic(!+siwn^a_swjrqr16x^@_2tfnah-e)*-kp1&m(*qx4si'
