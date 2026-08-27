from django.contrib import admin

from .models import Vehicle


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):

    list_display = (

        "id",

        "brand",

        "name",

        "price_per_day",

    )


    search_fields = (

        "brand",

        "name",

    )


    ordering = (

        "brand",

        "name",

    )