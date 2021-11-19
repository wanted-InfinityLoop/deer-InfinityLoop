import uuid

from django.db import models


class Charge(models.Model):
    id                = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    rental_charge     = models.PositiveSmallIntegerField()
    additional_charge = models.PositiveSmallIntegerField()

    class Meta:
            db_table = "charges"
