import uuid

from django.db import models


class Charge(models.Model):
    id                = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    rental_charge     = models.SmallIntegerField()
    additional_charge = models.SmallIntegerField()

    class Meta:
            db_table = "charges"
