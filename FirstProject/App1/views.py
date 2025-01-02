from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def f11(request):
    return HttpResponse("<h1>Hello User this is App1 django Webpage</h1>")
def f12(request):
        return HttpResponse("<h1>Hello User </h1>")
