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
    """ this view returns all cryptids in given year """
    try:
        context = {"cryptids": Cryptid.objects.filter(discovery_date__year=year)}
        return render(request, "cage/year.html", context)
    except Cryptid.DoesNotExist as ex:
        return HttpResponse(f"{year}")


def dateMonthCryptids(request, year, month):
    """ this view returns all cryptids in given year and month """
    try:
        context = {"cryptids": Cryptid.objects.filter(discovery_date__year=year).filter(discovery_date__month=month)}
        return render(request, "cage/month.html", context)
    except Cryptid.DoesNotExist as ex:
        return HttpResponse(f"cryptid not discovered on {year}/{month}")
    

def dateDayCryptids(request, year, month, day):
    """ this view returns all cryptids in given year, month and day"""
    return HttpResponse(f"{year}/{month}/{day}")