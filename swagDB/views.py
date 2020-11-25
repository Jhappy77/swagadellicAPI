from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Pong! You hit the swagDB index.")
# Create your views here.
