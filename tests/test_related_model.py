from __future__ import unicode_literals
from django.db import models
from django.test import TestCase
from django_fake_model import models as f


class RelatedModel(f.FakeModel):
    text = models.CharField(max_length=400)


class NyModel(f.FakeModel):
    text = models.CharField(max_length=400)
    related_model = models.ForeignKey(RelatedModel)


@NyModel.fake_me
@RelatedModel.fake_me
class TestRelatedModelsClassDecorator(TestCase):

    def test_create_models(self):
        related_model = RelatedModel()
        related_model.text = 'qwerty'
        related_model.save()
        my_model = NyModel()
        my_model.test = 'qwerty'
        my_model.related_model = related_model
        my_model.save()
        try:
            self.assertIsNotNone(my_model)
            self.assertIsNotNone(related_model)
        except Exception as ex:
            self.fail(ex.message)


@RelatedModel.fake_me
@NyModel.fake_me
class TestRelatedModelsClassDecoratorChangeOrder(TestCase):

    def test_create_models(self):
        related_model = RelatedModel()
        related_model.text = 'qwerty'
        related_model.save()
        my_model = NyModel()
        my_model.test = 'qwerty'
        my_model.related_model = related_model
        my_model.save()
        try:
            self.assertIsNotNone(my_model)
            self.assertIsNotNone(related_model)
        except Exception as ex:
            self.fail(ex.message)


class TestRelatedModelsFunctionDecorator(TestCase):

    @NyModel.fake_me
    @RelatedModel.fake_me
    def test_create_models(self):
        related_model = RelatedModel()
        related_model.text = 'qwerty'
        related_model.save()
        my_model = NyModel()
        my_model.test = 'qwerty'
        my_model.related_model = related_model
        my_model.save()
        try:
            self.assertIsNotNone(my_model)
            self.assertIsNotNone(related_model)
        except Exception as ex:
            self.fail(ex.message)


class TestRelatedModelsFunctionDecoratorChangeOrder(TestCase):

    @RelatedModel.fake_me
    @NyModel.fake_me
    def test_create_models(self):
        related_model = RelatedModel()
        related_model.text = 'qwerty'
        related_model.save()
        my_model = NyModel()
        my_model.test = 'qwerty'
        my_model.related_model = related_model
        my_model.save()
        try:
            self.assertIsNotNone(my_model)
            self.assertIsNotNone(related_model)
        except Exception as ex:
            self.fail(ex.message)
