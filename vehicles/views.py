from django.shortcuts import render,get_object_or_404
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
def bike_detail(request, vehicle_id):

    vehicle = get_object_or_404(
        Vehicle,
        id=vehicle_id
    )

    context = {
        "vehicle": vehicle
    }

    return render(
        request,
        "vehicles/bike_detail.html",
        context
    )