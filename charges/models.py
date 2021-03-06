import uuid

from django.db import models

from core.managers import CustomModelManager


class Charge(models.Model):
    id                = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    rental_charge     = models.PositiveSmallIntegerField()
    additional_charge = models.PositiveSmallIntegerField()

    class Meta:
            db_table = "charges"

class Unit(models.Model):
    id   = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=16)

    class Meta:
            db_table = "units"

class Type(models.Model):
    class Type(models.IntegerChoices):
        DISCOUNT = 1
        PENALTY  = 2

    name = models.CharField(max_length=16)

    class Meta:
            db_table = "types"

class DiscountOrPenalties(models.Model):
    id          = models.CharField(primary_key=True, unique=True, max_length=16)
    number      = models.PositiveIntegerField()
    description = models.CharField(max_length=32)
    unit        = models.ForeignKey(Unit, on_delete=models.PROTECT)
    type        = models.ForeignKey(Type, on_delete=models.PROTECT)
    objects     = CustomModelManager()
    
    class Meta:
            db_table = "discount_or_penalties"
