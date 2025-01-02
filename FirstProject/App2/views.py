from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def f22(request):
    return HttpResponse("<h1>This is App2 Django Page</h1>")