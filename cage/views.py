from django.shortcuts import render
from django.http import HttpResponse
from .models import Cryptid

# Create your views here.

def allCryptids(request):
    content = {"cryptids": Cryptid.objects.all()}
    return render(request, "cage/index.html", content)

def oneCryptids(request, cryptid_id):
    try:
        c = Cryptid.objects.get(pk=cryptid_id)
        return render(request, "cage/cryptid.html", c)
    
    except Cryptid.DoesNotExist as ex:
        return HttpResponse("No such Cryptid")

def locCryptids(request):
    return HttpResponse("all locations goes here")

def locListCryptids(request):
    return HttpResponse("lists of locations go here")

def dateCryptids(request):
    return HttpResponse("date discovered/created goes here")

def cage(request):
    return HttpResponse("In the URL type either /all /one /location /listLocation /date after cage/")