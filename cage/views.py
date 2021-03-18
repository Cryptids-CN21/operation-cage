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

def dateCryptids(request):
    return HttpResponse("date discovered/created goes here")

