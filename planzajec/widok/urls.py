from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index, name='glowna'),
    path('login', views.logowanie, name='formularz'),
]