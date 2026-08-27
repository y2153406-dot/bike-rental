from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from vehicles.models import Vehicle
from .models import Booking
from datetime import datetime


@login_required
def create_booking(request, vehicle_id):

    vehicle = get_object_or_404(
        Vehicle,
        id=vehicle_id
    )


    if request.method == "POST":

        pickup_date = request.POST.get("pickup_date")

        return_date = request.POST.get("return_date")


        # Convert string dates into date objects

        pickup_date_object = datetime.strptime(
            pickup_date,
            "%Y-%m-%d"
        ).date()


        return_date_object = datetime.strptime(
            return_date,
            "%Y-%m-%d"
        ).date()


        # Calculate number of days

        total_days = (
            return_date_object - pickup_date_object
        ).days


        # Calculate total price

        total_price = (
            total_days * vehicle.price_per_day
        )


        # Create booking

        Booking.objects.create(

            user=request.user,

            vehicle=vehicle,

            pickup_date=pickup_date_object,

            return_date=return_date_object,

            total_price=total_price

        )
        return redirect("booking_success")


    context = {

        "vehicle": vehicle

    }


    return render(
        request,
        "bookings/create_booking.html",
        context
    )

def booking_success(request):

    return render(
        request,
        "bookings/booking_success.html"
    )