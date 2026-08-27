from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def register(request):

    if request.method == "POST":

        form = UserCreationForm(
            request.POST
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Account created successfully. Please login."
            )

            return redirect(
                "login"
            )

    else:

        form = UserCreationForm()


    context = {

        "form": form

    }


    return render(
        request,
        "accounts/register.html",
        context
    )

def login_view(request):

    if request.method == "POST":

        username = request.POST.get(
            "username"
        )

        password = request.POST.get(
            "password"
        )


        user = authenticate(

            request,

            username=username,

            password=password

        )


        if user is not None:

            login(
                request,
                user
            )

            return redirect(
                "home"
            )

        else:

            messages.error(
                request,
                "Invalid username or password."
            )


    return render(
        request,
        "accounts/login.html"
    )


def logout_view(request):

    logout(request)

    return redirect(
        "home"
    )