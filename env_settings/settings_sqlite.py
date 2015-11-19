from __future__ import unicode_literals

DEBUG = True
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        'NAME': ':memory:',
    }
}
INSTALLED_APPS = [
    "django_fake_model",
]
SECRET_KEY = '0i+ic(!+siwn^a_swjrqr16x^@_2tfnah-e)*-kp1&m(*qx4si'
