from django.urls import reverse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')