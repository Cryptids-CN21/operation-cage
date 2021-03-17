from django.urls import path
from . import views

urlpatterns = [
    path("all/", views.allCryptids, name="allCryptids"),
    path("one/<int:cryptid_id>/", views.oneCryptids, name="oneCryptids"),
    path("location/", views.locCryptids, name="locCryptids"),
    path("listLocation/", views.locListCryptids, name="listLocCryptids"),
    path("date/", views.dateCryptids, name="dateLocated"),
    path("", views.cage, name="homePage"),
]