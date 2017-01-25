from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
import uuid


class Battery(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cells = models.PositiveSmallIntegerField()
    capacity = models.PositiveIntegerField()
    nickname = models.CharField(max_length=200)
    barcode = models.CharField(max_length=100, blank=True)
    cell_voltage = models.DecimalField(max_digits=3, decimal_places=2)


    def get_absolute_url(self):
        return reverse('battery-detail', kwargs={'pk': str(self.pk)})
