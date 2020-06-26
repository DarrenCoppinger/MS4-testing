from django.shortcuts import render, reverse, redirect
from .models import Product

# Create your views here.


def all_products(request):
    """ Display all products in Products dataset """
    products = Product.objects.all()
    return render(request, 'products.html', {"products": products})

def filtered_products(request, category_name):
    print('category_name= '+str(category_name))
    products = Product.objects.filter(category=category_name)

    return render(request, 'products.html', {"products": products})

def sort_products(request):
    sort = request.POST.get('sort-select')
    print('sort= '+str(sort))
    products = Product.objects.filter(category='Cocktails').order_by('price')

    return render(request, 'products.html', {"products": products})


# def filter_products(request, category_name):
#     print('category_name= '+str(category_name))
#     products = Product.objects.filter(category=category_name)

#     return render(request, 'products.html', {"products": products})


# def cocktails_view(request, *args, **kwargs):
#     category_name = 'Cocktails'
    
#     return redirect(url('products',category_name= 'Cocktails'))

    # if request.method == "POST":
    # products = Product.objects.all().filter(category=category_name)
    # sort = request.POST.get('sort-select')
    # print('Sort= '+str(sort))
    # if sort == 'high':
    # products = Product.objects.filter(category=category_name)
    # elif sort == 'low':
    #     products = Product.objects.all().filter(category='Cocktails').order_by('price')
    # else:
    #     print('Else')
    #     products = Product.objects.all()


