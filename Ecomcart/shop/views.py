from django.shortcuts import render
from django.http import HttpResponse
from .models import product
import  math

# Create your views here.
def index(request):
    products = product.objects.all()
    n= len(products)
    nslides = n//4 + math.ceil((n/4) + (n//4))
    params = {'no_of_slides': nslides, 'range': range(1, nslides), 'product': products}
    return render(request, 'shop/index.html',params)

# def index(request):
#     products = product.objects.all()
#     return render(request, 'shop/index.html', {'products': products})

def product_list(request):
    products = product.objects.all() # Retrieves all product objects
    context = {'products': products}
    return render(request, 'shop/product_list.html', context)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return HttpResponse('Contact Us')

def tracker(request):
    return HttpResponse('Tracker')

def Search(request):
    return HttpResponse('Search')

def ProductView(request):
    return HttpResponse('ProductView')

def checkout(request):
    return HttpResponse('Checkout')