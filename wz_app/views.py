from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify

from .models import Moje_wz
# Create your views here.
def hello_view(request):
    return render(request,"hello.html")

def wz_list(request):
    wz=Moje_wz.objects.all()
    return render(request,"wz-list.html",context={"wz":wz})

def wz_learn(request, slug):
    wz = get_object_or_404(Moje_wz, slug=slug)
    next_wzs = Moje_wz.objects.filter(pk__gt=wz.pk)
    if next_wzs.exists():
        next_wz = next_wzs.first()
    else:
        next_wz = Moje_wz.objects.all().first()
    context = {"wz": wz, "next_wz_url": next_wz.learn_url}
    return render(request, "wz_app/wz-learn.html", context=context)



def form1(request):
    context={}
    if request.method=="POST":
        first_name=request.POST.get("first-name")
        last_name = request.POST.get("last-name")
        context={
            "first_name":first_name,
            "last_name":last_name
        }
    return render(request,"form1.html", context=context)

def form2(request):
    context={}
    if request.method=="POST":
        product_name=request.POST.get("product-name")
        product_number = request.POST.get("product-number")
        transport = request.POST.get("transport")
        context={
            "product-name":product_name,
            "product-number":product_number,
            "transport":transport
        }
    return render(request,"form2.html",context=context)