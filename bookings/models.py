from django.db import models
from django.contrib.auth.models import User
from vehicles.models import Vehicle


class Booking(models.Model):

    STATUS_CHOICES = (
        ("PENDING", "Pending"),
        ("CONFIRMED", "Confirmed"),
        ("CANCELLED", "Cancelled"),
        ("COMPLETED", "Completed"),
    )


    PAYMENT_STATUS_CHOICES = (
        ("PENDING", "Pending"),
        ("SUCCESS", "Success"),
        ("FAILED", "Failed"),
    )


    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )


    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE
    )


    pickup_date = models.DateField()


    return_date = models.DateField()


    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PENDING"
    )


    total_price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )


    # Payment Information

    razorpay_order_id = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )


    razorpay_payment_id = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )


    razorpay_signature = models.CharField(
        max_length=500,
        blank=True,
        null=True
    )


    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS_CHOICES,
        default="PENDING"
    )


    def __str__(self):

        return f"{self.user} - {self.vehicle}"