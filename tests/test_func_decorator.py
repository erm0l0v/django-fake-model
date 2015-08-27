from __future__ import unicode_literals
from django.test import TestCase
from tests.fake_models import MyFakeModel


class MyFakeModelTests(TestCase):

    @MyFakeModel.fake_me
    def test_create_model(self):
        MyFakeModel.objects.create(name='123')
        model = MyFakeModel.objects.get(name='123')
        self.assertEqual(model.name, '123')