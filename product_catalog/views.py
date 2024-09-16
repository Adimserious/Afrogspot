from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.utils.translation import gettext as _
from django.db.models import Q
from .models import Product, Category, ProductVariant

# Create your views here.
def product_list(request):
    query = request.GET.get('q')
    category_name = request.GET.get('category')

    products = Product.objects.all()

    if category_name:
        products = products.filter(category__name__iexact=category_name)

    if query:
        products = products.filter(
            Q(name__icontains=query) | 
            Q(description__icontains=query)
        )

    # Handle empty query search scenario
    if not query and not category_name:
        messages.warning(request, "You didn't enter a search term. Please enter something to search for products.")

    context = {
        'products': products,
        'query': query,
        'category_name': category_name,
        'categories': Category.objects.all(),  # For the category dropdown
    }

    return render(request, 'product_catalog/product_list.html', context)


def product_detail(request, product_id):
    """ A view to show individual products"""

    product = get_object_or_404(Product, id=product_id)
    variants = product.variants.all()  # Get all available size variants if they exist


    
    context = {
        'product': product,
        'description': _(product.description),
        'variants': variants,  
    }

    return render(request, 'product_catalog/product_detail.html', context)
