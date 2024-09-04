from django.shortcuts import render
from .models import Product

# Create your views here.
def product_list(request):
    """ A view to show list of products"""
    products = Product.objects.filter(is_active=True).order_by('name')

    context = {
        'products': products,
    }

    return render(request, 'product_catalog/product_list.html', {'products': products})