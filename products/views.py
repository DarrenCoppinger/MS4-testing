from django.shortcuts import render
from .models import Product

# Create your views here.
def all_products(request):
    products = Product.objects.all()
    print('all_products')
    return render(request, 'products.html', {"products": products})


def filter_products(request, category):
    # products = Product.objects.all()
    print('filter_products')
    products = Product.objects.filter(category=category).order_by('-price')
    return render(request, 'products.html', {"products": products})