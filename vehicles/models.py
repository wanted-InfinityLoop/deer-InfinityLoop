import uuid

from django.db import models


class Vehicle(models.Model):
    id           = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    deer_name    = models.CharField(max_length=32)
    service_area = models.ForeignKey("areas.ServiceArea", on_delete=models.PROTECT)

    class Meta:
        db_table = "vehicles"


class Usage(models.Model):
    id            = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vehicle       = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    end_lat       = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    end_lng       = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    start_at      = models.DateTimeField(auto_now_add=True)    
    end_at        = models.DateTimeField(null=True)    
    charge_amount = models.IntegerField(null=True)
    user          = models.ForeignKey("users.User", on_delete=models.CASCADE)

    class Meta:
        db_table = "usages"
