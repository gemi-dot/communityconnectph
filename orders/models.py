from django.db import models

# Create your models here.
class WaterStation(models.Model):
    name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.name

class WaterRefillRequest(models.Model):
    CONTAINER_CHOICES = [
        ('5 Gallon', '5 Gallon'),
        ('3 Gallon', '3 Gallon'),
        ('Others', 'Others'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Assigned', 'Assigned'),
        ('Completed', 'Completed'),
    ]

    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    container_type = models.CharField(max_length=20, choices=CONTAINER_CHOICES)
    quantity = models.PositiveIntegerField()
    preferred_delivery_time = models.CharField(max_length=100)
    notes = models.TextField(blank=True)
    assigned_station = models.ForeignKey(WaterStation, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.name} - {self.container_type} x{self.quantity}"
