from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from vehicles.models import Vehicle
from .models import Booking
from datetime import datetime
from django.views.decorators.http import require_POST
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

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


        # Validate dates

        if return_date_object <= pickup_date_object:

            messages.error(
                request,
                "Return date must be after pickup date."
            )

            return redirect(
                "create_booking",
                vehicle_id=vehicle.id
            )


        # Check vehicle availability

        existing_booking = Booking.objects.filter(

            vehicle=vehicle,

            pickup_date__lt=return_date_object,

            return_date__gt=pickup_date_object

        ).exclude(

            status="CANCELLED"

        ).exists()


        # If vehicle is already booked

        if existing_booking:

            messages.error(
                request,
                "This bike is already booked for the selected dates."
            )

            return redirect(
                "create_booking",
                vehicle_id=vehicle.id
            )


        # Calculate number of days

        total_days = (
            return_date_object - pickup_date_object
        ).days


        # Calculate total price

        total_price = (
            total_days * vehicle.price_per_day
        )


        # Create booking

        booking = Booking.objects.create(

            user=request.user,

            vehicle=vehicle,

            pickup_date=pickup_date_object,

            return_date=return_date_object,

            total_price=total_price

        )


        # Create Razorpay client

        client = razorpay.Client(

            auth=(

                settings.RAZORPAY_KEY_ID,

                settings.RAZORPAY_KEY_SECRET

            )

        )


        # Create Razorpay order

        razorpay_order = client.order.create({

            "amount": int(total_price * 100),

            "currency": "INR",

        })


        # Save Razorpay order ID

        booking.razorpay_order_id = razorpay_order["id"]

        booking.save()


        # Redirect to payment page

        return redirect(

            "payment_page",

            booking_id=booking.id

        )


    context = {

        "vehicle": vehicle

    }


    return render(

        request,

        "bookings/create_booking.html",

        context

    )

@login_required
def payment_page(request, booking_id):

    booking = get_object_or_404(

        Booking,

        id=booking_id,

        user=request.user

    )


    context = {

        "booking": booking,

        "razorpay_key_id": settings.RAZORPAY_KEY_ID

    }


    return render(

        request,

        "bookings/payment.html",

        context

    )

@login_required
def verify_payment(request):

    if request.method != "POST":

        return JsonResponse(
            {
                "success": False,
                "message": "Invalid request method."
            },
            status=405
        )


    razorpay_payment_id = request.POST.get(
        "razorpay_payment_id"
    )

    razorpay_order_id = request.POST.get(
        "razorpay_order_id"
    )

    razorpay_signature = request.POST.get(
        "razorpay_signature"
    )


    try:

        booking = Booking.objects.get(

            razorpay_order_id=razorpay_order_id,

            user=request.user

        )


        client = razorpay.Client(

            auth=(

                settings.RAZORPAY_KEY_ID,

                settings.RAZORPAY_KEY_SECRET

            )

        )


        client.utility.verify_payment_signature({

            "razorpay_order_id": razorpay_order_id,

            "razorpay_payment_id": razorpay_payment_id,

            "razorpay_signature": razorpay_signature

        })


        # Save successful payment details

        booking.razorpay_payment_id = razorpay_payment_id

        booking.razorpay_signature = razorpay_signature

        booking.payment_status = "SUCCESS"

        booking.status = "CONFIRMED"

        booking.save()


        return JsonResponse(
            {
                "success": True,

                "booking_id": booking.id
            }
        )


    except Booking.DoesNotExist:

        return JsonResponse(
            {
                "success": False,

                "message": "Booking not found."
            },
            status=404
        )


    except razorpay.errors.SignatureVerificationError:

        return JsonResponse(
            {
                "success": False,

                "message": "Payment verification failed."
            },
            status=400
        )


@login_required
def booking_success(request, booking_id):

    booking = get_object_or_404(
        Booking,
        id=booking_id,
        user=request.user
    )

    context = {

        "booking": booking

    }

    return render(
        request,
        "bookings/booking_success.html",
        context
    )

@login_required
def my_bookings(request):

    bookings = Booking.objects.filter(
        user=request.user
    )

    context = {
        "bookings": bookings
    }

    return render(
        request,
        "bookings/my_bookings.html",
        context
    )

@login_required
@require_POST
def cancel_booking(request, booking_id):

    booking = get_object_or_404(
        Booking,
        id=booking_id,
        user=request.user
    )


    if booking.status == "CANCELLED":

        messages.error(
            request,
            "This booking is already cancelled."
        )

        return redirect(
            "my_bookings"
        )


    booking.status = "CANCELLED"

    booking.save()


    messages.success(
        request,
        "Booking cancelled successfully."
    )


    return redirect(
        "my_bookings"
    )