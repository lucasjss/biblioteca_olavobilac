from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def cadastrar(request):
    return HttpResponse('olá')


def home(request):
    return render(request, "home.html")
