import uuid

from django.db import models


class User(models.Model):
    id           = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name         = models.CharField(max_length=32)
    phone_number = models.CharField(max_length=32, unique=True)

    class Meta:
        db_table = "users"
