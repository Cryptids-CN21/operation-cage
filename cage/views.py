from django.shortcuts import render
from django.http import HttpResponse
from .models import Cryptid, Location
# Create your views here.

def allCryptids(request):
    content = {"cryptids": Cryptid.objects.all()}
    return render(request, "cage/index.html", content)

def oneCryptids(request, cryptid_id):
    try:
        c = {"cryptid": Cryptid.objects.get(pk=cryptid_id)}
        return render(request, "cage/cryptid.html", c)
    
    except Cryptid.DoesNotExist as ex:
        return HttpResponse("No such Cryptid")

def locations(request):
    content = {"locations": Location.objects.all()}
    return render(request, "cage/locations.html", content)

def location(request, location_id):
    l = {"location": Location.objects.get(pk=location_id)}
    return render(request, "cage/location.html", l)

def dateYearCryptids(request, year):
    y = {"year": Cryptid.objects.get(pk=year)}
    return render(request, "cage/year.html", y)

def dateMonthCryptids(request):
    return HttpResponse("month")

def dateDayCryptids(request):
    return HttpResponse("day")