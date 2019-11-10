from django.db import models


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating `created` and
    `modified` fields.
    """

    dt_created = models.DateTimeField(auto_now_add=True)
    dt_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
