from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.allCryptids, name="cryptids"),
    path("<int:cryptid_id>/", views.oneCryptids, name="cryptid"),
    path("locations/", views.locations, name="locations"),
    path("locations/<int:location_id>/", views.location, name="location"),
    path("date/", views.dateCryptids, name="dateLocated"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)