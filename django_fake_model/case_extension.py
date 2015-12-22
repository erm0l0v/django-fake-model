from __future__ import unicode_literals
from django.test import SimpleTestCase


class CaseExtension(SimpleTestCase):

    _models = tuple()

    @classmethod
    def append_model(cls, model):
        cls._models += (model, )

    def _pre_setup(self):
        super(CaseExtension, self)._pre_setup()
        self._map_models('create_table')

    def _post_teardown(self):
        # If we don't remove them in reverse order, then if we created table A
        # after table B and it has a foreignkey to table B, then trying to
        # remove B first will fail on some configurations, as documented
        # in issue #1
        self._map_models('delete_table', reverse=True)
        super(CaseExtension, self)._post_teardown()

    def _map_models(self, method_name, reverse=False):
        for model in (reversed(self._models) if reverse else self._models):
            try:
                getattr(model, method_name)()
            except AttributeError:
                raise TypeError("{0} doesn't support table method {1}".format(model, method_name))
