from django.shortcuts import render, redirect, get_object_or_404
from .models import Product #Rating

# Create your views here.
def product_list(request):
    """ A view to show list of products that are available"""

    products = Product.objects.filter(is_active=True).order_by('name')

    context = {
        'products': products,
    }

    return render(request, 'product_catalog/product_list.html', {'products': products})


def product_detail(request, product_id):
    """ A view to show individual products"""

    product = get_object_or_404(Product, id=product_id)
    #reviews = Rating.objects.filter(product=product).order_by('-created_at')

    context = {
        'product': product,
        #'reviews': reviews,
    }

    return render(request, 'product_catalog/product_detail.html', {'product': product}) # 'reviews': reviews})