from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path(
        "admin/",
        admin.site.urls
    ),


    path(
        "",
        include("core.urls")
    ),


    path(
        "bikes/",
        include("vehicles.urls")
    ),


    path(
        "bookings/",
        include("bookings.urls")
    ),


    # Custom Authentication

    path(
        "accounts/",
        include("accounts.urls")
    ),


    # Django Allauth / Google OAuth

    path(
        "social/",
        include("allauth.urls")
    ),

]


if settings.DEBUG:

    urlpatterns += static(

        settings.MEDIA_URL,

        document_root=settings.MEDIA_ROOT

    )