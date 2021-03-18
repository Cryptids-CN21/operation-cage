from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("all/", views.allCryptids, name="allCryptids"),
    path("one/<int:cryptid_id>/", views.oneCryptids, name="oneCryptids"),
    path("location/", views.locCryptids, name="locCryptids"),
    path("listLocation/", views.locListCryptids, name="listLocCryptids"),
    path("date/", views.dateCryptids, name="dateLocated"),
    path("", views.cage, name="homePage"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


