from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, "portal/index.html")

def charts(request):
    return render(request, "portal/charts.html")

def predict(request):
    return render(request, "portal/predictor.html")

def contact(request):
    return render(request, "portal/contact.html")