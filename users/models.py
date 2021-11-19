import uuid

from django.db import models


class Role(models.Model):
    class Type(models.IntegerChoices):
        ADMIN    = 1
        CUSTOMER = 2

    name = models.CharField(max_length=16)

    class Meta:
        db_table = "roles"


class User(models.Model):
    id           = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name         = models.CharField(max_length=32)
    email        = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=128)
    role         = models.ForeignKey(Role, on_delete=models.PROTECT, default=Role.Type.CUSTOMER.value)

    class Meta:
        db_table = "users"
