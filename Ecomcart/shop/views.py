from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'shop/index.html')

def about(request):
    return HttpResponse('About Us')

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