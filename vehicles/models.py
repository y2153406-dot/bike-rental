from django.db import models

# Create your models here.
class Vehicle(models.Model):
     VEHICLE_TYPE_CHOICES = [
        ("scooter", "Scooter"),
        ("motorcycle", "Motorcycle"),
    ]

     TRANSMISSION_CHOICES = [
        ("automatic", "Automatic"),
        ("manual", "Manual"),
    ]
     name=models.CharField(max_length=100)
     brand=models.CharField(max_length=100)
     vehicle_type=models.CharField(max_length=20, choices=VEHICLE_TYPE_CHOICES)
     transmission=models.CharField(max_length=20, choices=TRANSMISSION_CHOICES)
     price_per_day = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )
     seates=models.PositiveIntegerField(default=2)
     is_available=models.BooleanField(default=True)
     created_at=models.DateTimeField(auto_now_add=True)
     image = models.ImageField(upload_to="vehicles/", blank=True, null=True)
     def __str__(self):
        return f"{self.brand} {self.name}"
