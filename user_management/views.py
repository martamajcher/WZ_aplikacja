from typing import Optional

from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import CreateUserForm, LoginForm

def register(request: HttpRequest) -> HttpResponse:
    context = {"form": CreateUserForm()}
    if request.method == "POST":
        filled_form = CreateUserForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            return redirect("login")
        else:
            context["form"] = filled_form


    return render(request, "user_management/register.html", context=context)

def login(request: HttpRequest) -> HttpResponse:
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user: Optional[User] = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("wz-collection")
    context = {
        "form": form
    }
    return render(request, "user_management/login.html", context=context)


def logout(request):
    auth.logout(request)
    index_url = reverse("index")
    return redirect(f"{index_url}?logout=true")
