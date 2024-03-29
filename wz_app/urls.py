"""
URL configuration for project_wz project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from . import views

urlpatterns = [
    path('',views.hello_view,name="index"),
    path('wz',views.wz_list,name="wz-collection"),
    path('wz/learn/', views.learn, name="learn"),
    path('wz/learn/<slug:slug>', views.learn_wz, name="learn-wz"),
    path('wz/add',views.add_wz, name="add-wz"),
    path('wz/add/form',views.new_form, name="new-form")
]

from django.urls import path
from . import views

