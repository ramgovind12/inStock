from django.urls import path
from . import views
from django.shortcuts import render

app_name = 'cart'

urlpatterns = [
    path('',views.fun,name='fun')
]
