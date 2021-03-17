from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def allCryptids(request):
    return HttpResponse("all goes here")

def oneCryptids(request):
    return HttpResponse("one goes here")

def locCryptids(request):
    return HttpResponse("all locations goes here")

def locListCryptids(request):
    return HttpResponse("lists of locations go here")

def dateCryptids(request):
    return HttpResponse("date discovered/created goes here")

def cage(request):
    return HttpResponse("In the URL type either /all /one /location /listLocation /date after cage/")