from django.conf import settings
from django.db import models

class Forklift(models.Model):
    name = models.CharField(max_length=120)
    serial_number = models.CharField(max_length=120, unique=True)
    location = models.CharField(max_length=120, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Battery(models.Model):
    code = models.CharField(max_length=120, unique=True)
    serial_number = models.CharField(max_length=120, blank=True)
    voltage_v = models.DecimalField(max_digits=6, decimal_places=2)
    capacity_ah = models.DecimalField(max_digits=7, decimal_places=2)
    chemistry = models.CharField(max_length=60, blank=True)
    forklift = models.ForeignKey(Forklift, null=True, blank=True, on_delete=models.SET_NULL, related_name="batteries")
    in_service = models.BooleanField(default=True)

    def __str__(self):
        return self.code

class ChargeSession(models.Model):
    battery = models.ForeignKey(Battery, on_delete=models.CASCADE, related_name="charges")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="charges")
    charger_id = models.CharField(max_length=120, blank=True)
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField(null=True, blank=True)
    kwh_in = models.DecimalField(max_digits=8, decimal_places=3, null=True, blank=True)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["-started_at"]