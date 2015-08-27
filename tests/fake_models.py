from __future__ import unicode_literals
from django_fake_model import models as f
from django.db import models


class MyFakeModel(f.FakeModel):

    name = models.CharField(max_length=100)