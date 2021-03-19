from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.allCryptids, name="cryptids"),
    path("<int:cryptid_id>/", views.oneCryptids, name="cryptid"),
    path("locations/", views.locations, name="locations"),
    path("locations/<int:location_id>/", views.location, name="location"),
    #passes the name="year to year.html"
    #<int:year>/ goes into views as pk="year"
    path("date/<int:year>/", views.dateYearCryptids, name="year"),
    path("date/<int:year>/<int:month>/", views.dateMonthCryptids, name="month"),
    path("date/<int:year>/<int:month>/<int:day>/", views.dateDayCryptids, name="day"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)