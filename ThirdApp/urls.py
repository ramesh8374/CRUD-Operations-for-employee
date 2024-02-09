from django.contrib import admin
from django.urls import path
from ThirdApp import views

urlpatterns = [
    path("view", views.User),
    path("user_details/", views.user_details),
]