from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def eggs(request):
    return HttpResponse('<h1>eggs are great</h1>')
