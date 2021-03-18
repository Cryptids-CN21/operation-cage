from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("cryptids/", views.allCryptids, name="cryptids"),
    path("cryptids/<int:cryptid_id>/", views.oneCryptids, name="cryptid"),
    path("locations/", views.locations, name="locations"),
    path("locations/<int:location_id>/", views.location, name="location"),
    path("date/", views.dateCryptids, name="dateLocated"),
    path("", views.cage, name="homePage"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


