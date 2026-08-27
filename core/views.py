from django.shortcuts import render


from django.shortcuts import render
from vehicles.models import Vehicle


def home(request):

    vehicles = Vehicle.objects.filter(
        is_available=True
    )[:3]

    context = {
        "vehicles": vehicles
    }

    return render(
        request,
        "core/home.html",
        context
    )


def about(request):
    return render(request, "core/about.html")


def contact(request):
    return render(request, "core/contact.html")