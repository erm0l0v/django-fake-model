from __future__ import unicode_literals

from django.db import models
from django.test import TransactionTestCase
from django_fake_model import models as f


class RelatedModel(f.FakeModel):
    text = models.CharField(max_length=400)


class MyModel(f.FakeModel):
    text = models.CharField(max_length=400)
    related_model = models.ForeignKey(RelatedModel)


@MyModel.fake_me
@RelatedModel.fake_me
class TestRelatedModelsClassDecorator(TransactionTestCase):

    def test_create_models(self):
        related_model = RelatedModel()
        related_model.text = 'qwerty'
        related_model.save()
        my_model = MyModel()
        my_model.test = 'qwerty'
        my_model.related_model = related_model
        my_model.save()
        try:
            self.assertIsNotNone(my_model)
            self.assertIsNotNone(related_model)
        except Exception as ex:
            self.fail(ex.message)


