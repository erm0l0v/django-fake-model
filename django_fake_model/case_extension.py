from __future__ import unicode_literals
from django.test import TestCase


class CaseExtension(TestCase):

    _models = tuple()

    @classmethod
    def append_model(cls, model):
        cls._models += (model, )

    def _pre_setup(self):
        super(CaseExtension, self)._pre_setup()
        self._map_over_temporary_models('create_table')

    def _post_teardown(self):
        self._map_over_temporary_models('delete_table')
        super(CaseExtension, self)._post_teardown()

    def _map_over_temporary_models(self, method_name):
        for model in self._models:
            try:
                getattr(model, method_name)()
            except AttributeError:
                raise TypeError("{0} doesn't support table mgmt.".format(model))