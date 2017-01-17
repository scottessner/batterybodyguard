from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User


class Battery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cells = models.IntegerField()
    capacity = models.IntegerField()
    nickname = models.CharField(max_length=200)
    barcode = models.CharField(max_length=100)
    cell_voltage = models.DecimalField(max_digits=3, decimal_places=2)

    def get_absolute_url(self):
        return reverse('battery-update', kwargs={'pk': self.pk})
