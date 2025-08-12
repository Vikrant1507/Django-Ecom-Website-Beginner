from django.shortcuts import render
from django.http import HttpResponse
from .models import product
from math import ceil


# Create your views here.
def index(request):
    products = product.objects.all()
    print(products)
    n = len(products)
    nSlides = n//4 + ceil((n/4)-(n//4))

    # allProds = []
    # catprods = product.objects.values('category', 'id')
    # cats = {item['category'] for item in catprods}
    # for cat in cats:
    #     prod = product.objects.filter(category=cat)
    #     n = len(prod)
    #     nSlides = n // 4 + ceil((n / 4) - (n // 4))
    #     allProds.append([prod, range(1, nSlides), nSlides])

    params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    allProds = [[products, range(1, nSlides), nSlides],
                [products, range(1, nSlides), nSlides]]
    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)


# def index(request):
#     products = product.objects.all()
#     return render(request, 'shop/index.html', {'products': products})

def product_list(request):
    products = product.objects.all()  # Retrieves all product objects
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
