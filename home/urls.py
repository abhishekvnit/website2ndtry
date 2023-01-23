"""talcherlatest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name="login"),
    path('home', views.welcome2, name="welcome2"),
    path('milestone', views.milestone, name="milestone"),
    path('civil', views.civil, name="civil"),
    path('erection', views.erection, name="erection"),
    path('ordering', views.ordering, name="ordering"),
    path('sixmonth', views.sixmonth, name="sixmonth"),
    path('welcome', views.welcome, name="welcome"),
    path('schedule', views.schedule, name="schedule"),
    path('engineering', views.engineering, name="schedule"),
    path('handlelogout', views.handlelogout, name="handlelogout"),
]
