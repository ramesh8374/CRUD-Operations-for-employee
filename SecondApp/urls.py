"""
URL configuration for PythonProject1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from SecondApp import views

urlpatterns = [
    path("worldcup/", views.worldcup, name="worldcup"),
    path("product/", views.product, name="product"),
    path("product_total/",views.product_total,name="product_total"),
    path("emp_details/",views.emp_details,name="emp_details"),
    path("register/", views.register, name="register"),
    path("registerdetails/", views.registerdetails, name="registerdetails"),
]
