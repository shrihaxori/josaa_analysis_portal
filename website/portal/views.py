from django.shortcuts import render
from .models import College

# Create your views here.
from django.http import HttpResponse
#from bs4 import BeautifulSoup
#import requests as rt
import pandas as pd
import os



def index(request):
    objects = College.objects.all()
    context = {
        'objects': objects
    }
    return render(request, "portal/index.html", context)

def charts(request):
    df26 = pd.read_csv('portal/data/combinedv2.csv', low_memory = False)
 
    category_values = df26['Seat Type'].unique()
    gender_values = df26['Gender'].unique()
    institute_values = df26['Institute'].unique()
    year_values = df26['Year'].unique()
    round_values = df26['Round'].unique()
    program_values = df26['Academic Program Name'].unique()
 
    sf1 = request.GET.get('category')
    sf2 = request.GET.get('gender')
    sf3 = request.GET.get('institute')
    sf4 = request.GET.get('year')
    sf5 = request.GET.get('program')
 
    if sf1:
        df26 = df26[df26['Seat Type']==sf1]
    if sf2:
        df26 = df26[df26['Gender']==sf2]
    if sf3:
        df26 = df26[df26['Institute']==sf3]
    #df26 = df26[df26['Quota']=='AI']
    df26 = df26[df26['Round']==6]
    if sf4:
        sf4 = int(sf4)
        df26 = df26[df26['Year']==sf4]
    if sf5:
        df26 = df26[df26['Academic Program Name']==sf5]
    
    print(sf1, sf2, sf3, sf4, sf5)
    context = {
        'category_values' : category_values,
        'gender_values': gender_values,
        'institute_values': institute_values,
        'year_values': year_values,
        'program_values' : program_values,
        'df26': df26.to_html()
    }
    df26.to_csv(os.getcwd()+'/portal/static/portal/data/df26.csv')
 
    return render(request, "portal/charts.html", context)

def predict(request):
    df = pd.read_csv('portal/data/combinedv2.csv', low_memory=False)
    category_values = df['Seat Type'].unique()
    gender_values = df['Gender'].unique()
    institute_values = df['Institute'].unique()
    year_values = df['Year'].unique()
    quota_values = df['Quota'].unique()
    program_values = df['Academic Program Name'].unique()

    sf1 = request.GET.get('category')
    sf2 = request.GET.get('gender')
    sf3 = request.GET.get('institute')
    sf4 = request.GET.get('year')
    sf5 = request.GET.get('quota')
    sf6 = request.GET.get('program')
     
    if sf1:
        df = df[df['Seat Type']==sf1]
    if sf2:
        df = df[df['Gender']==sf2]
    if sf3:
        df = df[df['Institute']==sf3]
    if sf4:
        sf4 = int(sf4)
        df = df[df['Year']==sf4]
    if sf5:
        df = df[df['Quota']==sf5]
    if sf6:
        df = df[df['Academic Program Name']==sf6]

    print(sf1, sf2, sf3, sf4, sf5, sf6)
    context = {
        'category_values' : category_values,
        'gender_values' : gender_values,
        'institute_values': institute_values,
        'year_values': year_values,
        'quota_values': quota_values,
        'program_values': program_values,
    }
    df.to_csv(os.getcwd()+'/portal/static/portal/data/df.csv')
    return render(request, "portal/table.html", context)

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


