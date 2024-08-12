from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('HOme Page')

def room(request):
    return HttpResponse('Room')

# Create your views here.
