from django.urls import path
from . import views

urlpatterns = [
    path("", views.bike_list, name="bike_list"),
     path("<int:vehicle_id>/", views.bike_detail, name="bike_detail"),
]