from datetime import datetime
from django.urls import path ,include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from . import  views

urlpatterns = [
    path('',views.signin_page),
    path('<str:user_id>/',views.home_page),
    path('<str:user_id>/informations/',views.staff_informations_page),
    path('<str:user_id>/<str:pack_name>/',views.pack_page),
]
