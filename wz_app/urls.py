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
from .views import hello_view,wz_list,wz_learn,form1,form2

urlpatterns = [
    path('',hello_view),
    path('wz',wz_list,name="wz-collection"),
    path('wz/learn/<slug:slug>',wz_learn, name="wz-learn"),
    path('wz/form1',form1, name="form1"),
    path('wz/form2',form2,name="form2")
]

from django.urls import path
from . import views

