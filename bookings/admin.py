from django.contrib import admin

from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = (

        "id",

        "user",

        "vehicle",

        "pickup_date",

        "return_date",

        "status",

        "total_price",

    )


    list_filter = (

        "status",

        "pickup_date",

        "return_date",

    )


    search_fields = (

        "user__username",

        "vehicle__brand",

        "vehicle__name",

    )


    ordering = (

        "-id",

    )