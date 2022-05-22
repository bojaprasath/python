from django.db import models
from django_mysql import models as dm_models


class Bats(models.Model):
    """ Model for storing data related to pull requests

    """

    bats_name = models.CharField(max_length=100, unique=True)
    subbuild_id = models.CharField(max_length=6)
    status = models.CharField(max_length=10)
    timestamp = models.CharField(max_length=20)
    attributes = dm_models.JSONField()

    class Meta:
        unique_together = ('bats_name', 'subbuild_id')