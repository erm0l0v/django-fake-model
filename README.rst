=============================
django-fake-model
=============================

.. image:: https://badge.fury.io/py/django-fake-model.png
    :target: https://badge.fury.io/py/django-fake-model

.. image:: https://travis-ci.org/erm0l0v/django-fake-model.png?branch=master
    :target: https://travis-ci.org/erm0l0v/django-fake-model

Simple library for creating fake models in the unit tests.


Quickstart
----------

Install django-fake-model::

    pip install django-fake-model

Then use it in a project::

    from django_fake_model import models as f
    from django.db import models
    from django.test import TestCase
    
    
    class MyFakeModel(f.FakeModel):

        name = models.CharField(max_length=100)
    
    
    @MyFakeModel.fake_me
    class MyFakeModelTests(TestCase):

        def test_create_model(self):
            MyFakeModel.objects.create(name='123')
            model = MyFakeModel.objects.get(name='123')
            self.assertEqual(model.name, '123')
    
    
    class MyFakeModelFunctionTest(TestCase):

        @MyFakeModel.fake_me
        def test_create_model(self):
            MyFakeModel.objects.create(name='123')
            model = MyFakeModel.objects.get(name='123')
            self.assertEqual(model.name, '123')

Features
--------

* TODO

Cookiecutter Tools Used in Making This Package
----------------------------------------------

*  cookiecutter
*  cookiecutter-djangopackage
