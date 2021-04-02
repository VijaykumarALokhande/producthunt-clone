from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ProductMC
from django.utils import timezone
def home(request):
    all_products = ProductMC.objects
    return render(request, 'products/home.html', {'all_products':all_products})

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
            return redirect('/products/'+str(obj.id) )
        else:
            return render(request, 'products/create.html', {'error':'enter all product details'})
    else:
        return render(request, 'products/create.html')

def detailfn(request, product_id):
    specific_product = get_object_or_404(ProductMC, pk=product_id)
    return render(request, 'products/detail.html', {'pr_dt':specific_product})

@login_required
def upvotefn(request, product_id):
    if request.method=='POST':
        specific_product = get_object_or_404(ProductMC, pk=product_id)
        specific_product.votes_total+=1
        specific_product.save()
        return redirect('/products/'+str(specific_product.id) )
