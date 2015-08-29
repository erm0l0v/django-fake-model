from __future__ import unicode_literals
from functools import wraps
from django.core.management.color import no_style
from django.db import connection, models
from django.test import TestCase
from django_fake_model.case_extension import CaseExtension


class FakeModel(models.Model):

    class Meta:
        abstract = True

    @classmethod
    def create_table(cls):
        raw_sql, refs = connection.creation.sql_create_model(
            cls,
            no_style(),
            [])
        cls.delete_table()
        cursor = connection.cursor()
        try:
            cursor.execute(*raw_sql)
        finally:
            cursor.close()

    @classmethod
    def delete_table(cls):
        cursor = connection.cursor()
        try:
            cursor.execute('DROP TABLE IF EXISTS {0}'.format(cls._meta.db_table))
        finally:
            cursor.close()

    @classmethod
    def fake_me(cls, source):
        if source and type(source) == type and issubclass(source, TestCase):
            return cls._class_extension(source)
        elif hasattr(source, '__call__'):
            return cls._decorator(source)
        else:
            raise AttributeError('source - must be a TestCase subclass of function')

    @classmethod
    def _class_extension(cls, source):
        if not issubclass(source, CaseExtension):
            class __wrap_class__ (source, CaseExtension):
                pass
            source = __wrap_class__
        source.append_model(cls)
        return source

    @classmethod
    def _decorator(cls, source):
        @wraps(source)
        def __wrapper__(*args, **kwargs):
            try:
                cls.create_table()
                return source(*args, **kwargs)
            finally:
                cls.delete_table()
        return __wrapper__