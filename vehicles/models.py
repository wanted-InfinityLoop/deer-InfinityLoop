import uuid

from django.db import models


class Vehicle(models.Model):
    id           = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    deer_name    = models.CharField(max_length=32)
    service_area = models.ForeignKey("areas.ServiceArea", null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = "vehicles"


class Usage(models.Model):
    id            = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vehicle       = models.ForeignKey(Vehicle, null=True, on_delete=models.SET_NULL)
    end_lat       = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    end_lng       = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    start_at      = models.DateTimeField(auto_now_add=True)    
    end_at        = models.DateTimeField(null=True)    
    charge_amount = models.PositiveIntegerField(default=0)
    user          = models.ForeignKey("users.User", null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = "usages"
