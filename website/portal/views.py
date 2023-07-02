from django.shortcuts import render
from .models import College

# Create your views here.
from django.http import HttpResponse
#from bs4 import BeautifulSoup
#import requests as rt
#import pandas as pd



def index(request):
    objects = College.objects.all()
    context = {
        'objects': objects
    }
    return render(request, "portal/index.html", context)

def charts(request):
    return render(request, "portal/charts.html")

def predict(request):
    return render(request, "portal/predictor.html")

def contact(request):
    return render(request, "portal/contact.html")

url = 'https://josaa.admissions.nic.in/applicant/seatmatrix/OpeningClosingRankArchieve.aspx'
params = {
    #"ctl00$ContentPlaceHolder1$ddlroundno": 
    "ctl00$ContentPlaceHolder1$ddlInstype": "ALL",
    "ctl00$ContentPlaceHolder1$ddlInstitute": "ALL",
    "ctl00$ContentPlaceHolder1$ddlBranch": "ALL",
    "ctl00$ContentPlaceHolder1$ddlSeatType": "ALL",
    "ctl00$ContentPlaceHolder1$btnSubmit": "Submit"
}


