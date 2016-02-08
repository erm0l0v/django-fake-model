=============================
django-fake-model
=============================

.. image:: https://badge.fury.io/py/django-fake-model.png
    :target: https://badge.fury.io/py/django-fake-model

.. image:: https://travis-ci.org/erm0l0v/django-fake-model.png?branch=master
    :target: https://travis-ci.org/erm0l0v/django-fake-model

.. image:: https://landscape.io/github/erm0l0v/django-fake-model/master/landscape.svg?style=flat
   :target: https://landscape.io/github/erm0l0v/django-fake-model/master
   :alt: Code Health

.. image:: https://api.codacy.com/project/badge/235f71efbf3144178975bb3eb86964c8
    :target: https://www.codacy.com/app/erm0l0v/django-fake-model

.. image:: https://requires.io/github/erm0l0v/django-fake-model/requirements.svg?branch=master
     :target: https://requires.io/github/erm0l0v/django-fake-model/requirements/?branch=master
     :alt: Requirements Status

.. image:: https://codecov.io/github/erm0l0v/django-fake-model/coverage.svg?branch=master
    :target: https://codecov.io/github/erm0l0v/django-fake-model?branch=master

Simple library for creating fake models in the unit tests.

This simple library allows to create fake models in your test without migrations, test apps and test tables in your base. All tables that you need will created/removed during the test.

Install
-------

Install django-fake-model::

    pip install django-fake-model

Quickstart
----------

Just create a model in any file (Ex: in your test) and add decorator **@YourModel.fake_me** to test method or test class.

.. code:: python

    from django_fake_model import models as f
    from django.db import models
    from django.test import TestCase, TransactionTestCase


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


    class RelatedModel(f.FakeModel):
        text = models.CharField(max_length=400)


    class NyModel(f.FakeModel):
        text = models.CharField(max_length=400)
        related_model = models.ForeignKey(RelatedModel)


    @NyModel.fake_me
    @RelatedModel.fake_me
    class TestRelatedModelsClassDecorator(TransactionTestCase):

        def test_create_models(self):
            related_model = RelatedModel()
            related_model.text = 'qwerty'
            related_model.save()
            my_model = NyModel()
            my_model.test = 'qwerty'
            my_model.related_model = related_model
            my_model.save()
            self.assertIsNotNone(my_model)
            self.assertIsNotNone(related_model)


Development:
------------

To develop on this locally with `Docker`_, install the Docker Engine and
`Docker Compose`_. Then you can build the Docker image and run the tests
on all tox activities(this also uses a shared pip cache to reduce download
times)::

    docker-compose up -d pg mysql
    docker-compose run --rm test

If you wanna run just one Tox activity you can specify that as well::

    docker-compose run --rm test tox -e py35-dj19-mysql-unittest

If you add any dependencies or change the tox configuration, you have
to rebuild the image::

    docker-compose build

It will share this folder with the Docker containers, so that


.. _Docker: https://www.docker.com/
.. _Docker Compose: https://docs.docker.com/compose/


Cookiecutter Tools Used in Making This Package
----------------------------------------------

*  cookiecutter
*  cookiecutter-djangopackage
