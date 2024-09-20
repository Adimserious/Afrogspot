from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _
from django.db.models import Q
from .models import Product, Category, ProductVariant
from django.forms import modelformset_factory
from .forms import ProductForm

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


@login_required
def manage_products(request):
    products = Product.objects.all()
    return render(request, 'product_catalog/manage_products.html', {'products': products})


# Add a product
@login_required
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        variant_formset = ProductVariantFormSet(request.POST, instance=Product())
        if form.is_valid() and variant_formset.is_valid():
            product = form.save()
            variant_formset.instance = product
            variant_formset.save()
            return redirect('product_list')  # Redirect after saving
    else:
        form = ProductForm()
        variant_formset = ProductVariantFormSet()

    return render(request, 'product_catalog/add_product.html', {'form': form, 'variant_formset': variant_formset})



# ProductVariantFormSet factory
ProductVariantFormSet = modelformset_factory(ProductVariant, fields=('size', 'price', 'stock'), extra=1, can_delete=True)

@login_required
def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product_form = ProductForm(request.POST, request.FILES, instance=product)
        formset = ProductVariantFormSet(request.POST, queryset=ProductVariant.objects.filter(product=product))

        if product_form.is_valid() and formset.is_valid():
            product_form.save()
            formset.save()  # Save variants
            return redirect('product_list')
    else:
        product_form = ProductForm(instance=product)
        formset = ProductVariantFormSet(queryset=ProductVariant.objects.filter(product=product))

    return render(request, 'product_catalog/update_product.html', {'form': product_form, 'formset': formset})


# Delete a product
@login_required
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == "POST":
        product.delete()
        messages.success(request, 'Product successfully deleted.')
        return redirect('manage_products')  # Redirect to product management page after deletion

    return render(request, 'product_catalog/delete_confirmation.html', {'product': product})