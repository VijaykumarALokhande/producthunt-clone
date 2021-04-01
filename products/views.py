from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ProductMC
from django.utils import timezone
def home(request):
    return render(request, 'products/home.html')

@login_required
def createfn(request):
    if request.method=="POST":
        if request.POST['title'] and request.POST['body'] and request.POST['product_url'] and request.FILES['icon'] and request.FILES['product_image']:
            obj = ProductMC()
            obj.title = request.POST['title']
            obj.body = request.POST['body']
            if request.POST['product_url'].startswith("https://") or request.POST['product_url'].startswith("http://"):
                obj.url = request.POST['product_url']
            else:
                obj.url = "https://" +request.POST['product_url']
            obj.icon = request.FILES['icon']
            obj.image = request.FILES['product_image']
            obj.pub_date = timezone.datetime.now()
            obj.hunter = request.user
            obj.save()
            return redirect('firsthomepage')
        else:
            return render(request, 'products/create.html', {'error':'enter all product details'})
    else:
        return render(request, 'products/create.html')
