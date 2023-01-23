from django.shortcuts import render

from home.models import Talcherdb

# Create your views here.

from django.db.models import Q

from datetime import date, timedelta

import pandas as pd

from django.contrib.auth import authenticate,logout,login
 
from django.contrib.auth.models import User


def index(request):
    return render(request,'index.html')

def welcome(request):

    if request.method =="POST":
        username= request.POST.get('username')
        password= request.POST.get('password')
        user= authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            request.session['username']= username
            return render(request,'welcome.html', {'username': username})



    return render(request,'index.html')

def welcome2(request):

    if request.session.has_key('username'):

      return render(request,'welcome.html')  
      
    else:
      return render(request, 'login.html', {})


def schedule(request):

    if request.session.has_key('username'):

        talcherdb= Talcherdb.objects.all()
        return render(request, 'index.html', {'talcherdb':talcherdb})
    else:
      return render(request, 'login.html', {})

def milestone(request):

    if request.session.has_key('username'):
   
        talcherdb= Talcherdb.objects.filter(activity_type='MIL')
        
        return render(request, 'milestone.html', {'talcherdb':talcherdb})
    else:
        return render(request, 'login.html', {})

def civil(request):

    if request.session.has_key('username'):
   
        talcherdb= Talcherdb.objects.filter(activity_type='CIV')
        
        return render(request, 'civil.html', {'talcherdb':talcherdb})
    else:
        return render(request, 'login.html', {})

def erection(request):
   

    talcherdb= Talcherdb.objects.filter(Q(activity_type='ERC') | Q(activity_type='COM'))
    
    return render(request, 'erection.html', {'talcherdb':talcherdb})


def ordering(request):
   

    talcherdb= Talcherdb.objects.filter(Q(activity_type='ORD') | Q(activity_type ='ENQ'))
    
    return render(request, 'ordering.html', {'talcherdb':talcherdb})


def sixmonth(request):
   

    startdate= date.today()
    enddate= startdate+ timedelta(days=240)

    

    talcherdb= Talcherdb.objects.filter(planned_finish__range= [startdate,enddate])

    
    
    return render(request, 'sixmonth.html', {'talcherdb':talcherdb})




def handlelogout(request):
    
    logout(request)
    
    
    return render(request,'index.html')


def engineering(request):

    if request.session.has_key('username'):

      return render(request,'welcome.html')  
      
    else:
      return render(request, 'engineering.html', {})