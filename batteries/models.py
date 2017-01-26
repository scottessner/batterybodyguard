from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
import uuid


class Battery(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    capacity = models.PositiveIntegerField()
    nickname = models.CharField(max_length=200)
    barcode = models.CharField(max_length=100, blank=True)
    max_charge_rate = models.IntegerField(default=1)
    brand = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('battery-detail', kwargs={'pk': str(self.pk)})


class Cell(models.Model):
    battery = models.ForeignKey(Battery, on_delete=models.CASCADE)
    voltage = models.DecimalField(max_digits=3, decimal_places=2)


class Charger(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    max_cells = models.IntegerField()
    max_current = models.IntegerField()
    parallel_supported = models.BooleanField()
    serial_data_supported = models.BooleanField()
    max_batteries = models.IntegerField()
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)