from django.db import models

# Create your models here.
from django.urls import reverse

from staff.models import CustomUser
from client.models import Client


class Vehicles(models.Model):
    VehicleType = models.TextChoices('VehicleType', 'TRUCK SUV SEDAN JEEP')
    number = models.CharField(blank=True,max_length=255)
    assigned = models.BooleanField(default=False)
    vehicle_type = models.CharField(blank=True, choices=VehicleType.choices, max_length=255)

    def __str__(self):
        return '{}, {}'.format(self.number, self.vehicle_type)


class AllocatedVehicles(models.Model):
    vehicle_assigned = models.ForeignKey(Vehicles, on_delete=models.CASCADE, related_name='allocated_vehicle')
    client_assigned = models.ForeignKey(Client, on_delete=models.PROTECT)
    allocated_by = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    towing_in_date = models.DateTimeField()
    towing_out_date = models.DateTimeField()
    towing_out = models.BooleanField(default=False)
    payment_id = models.CharField(blank=False, null=False, max_length=200)

    def get_absolute_url(self):
        return reverse('vehicle_list')

    def save(self, *args, **kwargs):
        self.vehicle_assigned.assigned = not self.towing_out
        self.vehicle_assigned.save()
        return super().save(*args, **kwargs)
