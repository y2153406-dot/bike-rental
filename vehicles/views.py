from django.shortcuts import render


def bike_list(request):
    return render(request, "vehicles/bike_list.html")