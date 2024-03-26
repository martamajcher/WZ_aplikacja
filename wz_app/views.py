from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .forms import NewWzForm, NewWzForm2
from .models import Moje_wz, UserWzOwnership
# Create your views here.
def hello_view(request: HttpRequest):
    return render(request,"wz_app/hello.html")

@login_required(login_url="login")
def wz_list(request):
    if request.method == "POST":
        slug = request.POST.get("slug")
        wz_to_delete: Moje_wz = Moje_wz.objects.filter(slug=slug)
        wz_to_delete.delete()
    user_ownerships = UserWzOwnership.objects.filter(user__username=request.user.username)
    wz: list[Moje_wz] = [ownership.w for ownership in user_ownerships]
    return render(request, "wz_app/wz-list.html", context={"wz": wz})





@login_required(login_url="login")
def add_wz(request):
    if request.method == "POST":
        filled_form = NewWzForm(request.POST)
        if filled_form.is_valid():
            new_wz= Moje_wz(**filled_form.cleaned_data)
            new_wz.save()
            user = auth.get_user(request)
            new_relationship = UserWzOwnership(user=user, w=new_wz)
            new_relationship.save()
            return redirect("wz-collection")
    return render(request, "wz_app/add-wz.html", context={"form": NewWzForm()})


def learn(request):
    w = Moje_wz.objects.all().first()
    return redirect(reverse("learn", args=[w.slug]))

def learn_wz(request, slug):
    w = get_object_or_404(Moje_wz, slug=slug)
    next_wz = Moje_wz.objects.filter(pk__gt=w.pk)
    if next_wz.exists():
        next_wz = next_wz.first()
    else:
        next_wz = Moje_wz.objects.all().first()
    context = {"w": w, "next_wz_url": next_wz.learn_url}
    return render(request, "wz_app/learn-wz.html", context=context)

@login_required(login_url="login")
def new_form(request):
    return render(request, "wz_app/new-form.html", context={"form": NewWzForm2()})
