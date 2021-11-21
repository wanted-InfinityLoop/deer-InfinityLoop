import uuid

from django.contrib.gis.db import models


class ServiceArea(models.Model):
    id                    = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name                  = models.CharField(max_length=32, null=True)
    boundary              = models.PolygonField()
    center                = models.PointField()
    border_coords         = models.MultiPointField()
    charge                = models.ForeignKey("charges.Charge", null=True, on_delete=models.SET_NULL)
    discount_or_penalties = models.ManyToManyField("charges.DiscountOrPenalties", related_name="service_areas")

    class Meta:
        db_table = "service_areas"


class ForbiddenArea(models.Model):
    id            = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    boundary      = models.PolygonField()
    border_coords = models.MultiPointField()
    service_area  = models.ForeignKey(ServiceArea, on_delete=models.CASCADE)

    class Meta:
        db_table = "forbidden_areas"


class ParkingArea(models.Model):
    id            = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    center_lat    = models.DecimalField(max_digits=8, decimal_places=6)
    center_lng    = models.DecimalField(max_digits=9, decimal_places=6)
    radius        = models.FloatField()
    service_area  = models.ForeignKey(ServiceArea, on_delete=models.CASCADE)

    class Meta:
        db_table = "parking_areas"
