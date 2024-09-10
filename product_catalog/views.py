from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.utils.translation import gettext as _
from django.db.models import Q
from .models import Product, Category

# Create your views here.
def product_list(request):
    """ A view to show list of products that are available, search and category"""

    products = Product.objects.filter(is_active=True).order_by('name')
    category_name = request.GET.get('category')
    query = request.GET.get('q')
    
    if category_name and category_name.strip() != '':
        # Check if the category exists (case-insensitive search)
        category = get_object_or_404(Category, name__iexact=category_name)
        products = products.filter(category=category)

    
    # search query
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                
        
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
        


    context = {
        'products': products,
        'query': query,
        'category_name': category_name,  # selected category name
        'categories': Category.objects.all(),  # To populate the category dropdown in the template
    }

    return render(request, 'product_catalog/product_list.html', context)


def product_detail(request, product_id):
    """ A view to show individual products"""

    product = get_object_or_404(Product, id=product_id)

    
    context = {
        'product': product,
        'description': _(product.description),  
    }

    return render(request, 'product_catalog/product_detail.html', context)
