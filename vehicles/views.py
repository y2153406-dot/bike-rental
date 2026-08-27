from django.shortcuts import render
from .models import Vehicle

def bike_list(request):
    vehicles=Vehicle.objects.filter(is_available=True)
    return render(
    request,
    "vehicles/bike_list.html",
    {
        "vehicles": vehicles
    }
)