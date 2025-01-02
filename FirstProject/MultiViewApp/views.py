from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def f1(request):
      return HttpResponse("<h1>Hello User Good Morning.....</h1>")
def f2(request):
      return HttpResponse("<h1>Hello User Good Afternoon....</h1>")
def f3(request):
      return HttpResponse("<h1>Hello User Good Evening....</h1>")
