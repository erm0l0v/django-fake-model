from __future__ import unicode_literals

from django.contrib.contenttypes.models import ContentType
from django.test import TestCase

from tests.fake_models import MyFakeModel


@MyFakeModel.fake_me
class MyFakeModelTests(TestCase):

    def test_create_model(self):
        MyFakeModel.objects.create(name='123')
        model = MyFakeModel.objects.get(name='123')
        self.assertEqual(model.name, '123')


@MyFakeModel.fake_me
class ContentTypeTests_class(TestCase):

    def test_contenttype(self):
        try:
            app_label = MyFakeModel._meta.app_label
            model_name = MyFakeModel._meta.model_name
            ContentType.objects.get(app_label=app_label, model=model_name)
        except Exception as ex:
            self.fail(ex.message)
