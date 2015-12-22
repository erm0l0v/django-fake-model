from __future__ import unicode_literals
import os


DEBUG = True
DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': os.environ.get('MYSQL_HOST', None),
        'NAME': 'django_fake_model',
    }
}
INSTALLED_APPS = [
    "django_fake_model",
]
SECRET_KEY = '0i+ic(!+siwn^a_swjrqr16x^@_2tfnah-e)*-kp1&m(*qx4si'
