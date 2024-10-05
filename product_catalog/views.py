from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _
from django.db.models import Q
from .models import Product, Category, ProductVariant, Country, ProductRating
from django.forms import modelformset_factory
from .forms import ProductForm, ProductRatingForm
from django.conf import settings
from django.db.models import Avg 
import logging
from django.utils.http import url_has_allowed_host_and_scheme


# ProductVariantFormSet factory
ProductVariantFormSet = modelformset_factory(ProductVariant, fields=('id', 'size', 'price', 'stock'), extra=1, can_delete=True)


def product_list(request):
    query = request.GET.get('q', '').strip()
    category_name = request.GET.get('category')

    products = Product.objects.filter(is_active=True)

    # Filter parameters from request
    vegan = request.GET.get('vegan', '')
    gluten_free = request.GET.get('gluten_free', '')
    country = request.GET.get('country', '')

    # Applying filters
    if vegan:
        products = products.filter(is_vegan=True)
    
    if gluten_free:
        products = products.filter(is_gluten_free=True)

    if country:
        products = products.filter(country__name=country)
    
    # List of countries for the filter options
    countries = Country.objects.all()

    # If a category is selected, clear the search query
    if category_name:
        products = products.filter(category__name__iexact=category_name)
        query = ''  # Reset query when a category is selected

    # If no category is selected and there's a search query, filter by the query
    if query:
        products = products.filter(
            Q(name__icontains=query) | 
            Q(description__icontains=query)
        )
        category_name = '' # Clear the category query
    
    # Check if no products are found after all filters
    if products.count() == 0:
        messages.info(request, "No products found matching your criteria. Please try again with different filters or a search term.")


    # Only display the warning if the user explicitly submitted the form without entering a query or selecting a category
    if request.GET and not query and not category_name and not vegan and not gluten_free and not country:
        messages.warning(request, "You didn't enter a search term or select a category. Please try again.")

    # Identify products the user has purchased
    purchased_products = []
    if request.user.is_authenticated:
        purchased_products = [product.id for product in products if user_has_purchased_product(request.user, product)]

    context = {
        'products': products,
        'query': query,
        'category_name': category_name,
        'categories': Category.objects.all(),  # For the category dropdown
        'countries': countries,
        'vegan': vegan,
        'gluten_free': gluten_free,
        'selected_country': country,
        'purchased_products': purchased_products,
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
    """ Add products to the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        variant_formset = ProductVariantFormSet(request.POST) 

        if form.is_valid() and variant_formset.is_valid():
            product = form.save()  # Save the product first

            # Save variants if they exist
            variants = variant_formset.save(commit=False)
            for variant in variants:
                variant.product = product  # Associate each variant with the product
                variant.save()

            # Handle deleted variants
            for variant in variant_formset.deleted_objects:
                variant.delete()

            messages.success(request, 'Product has been successfully added!')
            return redirect('product_list')
        else:
            messages.error(request, 'There was an error adding the product. Please check the form and try again.')
    else:
        form = ProductForm()
        variant_formset = ProductVariantFormSet(queryset=ProductVariant.objects.none())  # Empty formset for new variants

    return render(request, 'product_catalog/add_product.html', {
        'form': form,
        'variant_formset': variant_formset
    })


@login_required
def update_product(request, pk):

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product_form = ProductForm(request.POST, request.FILES, instance=product)
        formset = ProductVariantFormSet(request.POST, queryset=ProductVariant.objects.filter(product=product))

        if product_form.is_valid() and formset.is_valid():
            product = product_form.save()  # Save the product first

            # Save variants
            variants = formset.save(commit=False)
            for variant in variants:
                variant.product = product  # Ensures that each variant is linked to the product
                variant.save()

            # Handle deleted variants
            for variant in formset.deleted_objects:
                variant.delete()

            messages.success(request, 'Product has been successfully updated!')
            return redirect('product_list')
        else:
            messages.error(request, 'There was an error updating the product. Please check the form and try again.')
    else:
        product_form = ProductForm(instance=product)
        formset = ProductVariantFormSet(queryset=ProductVariant.objects.filter(product=product))

    return render(request, 'product_catalog/update_product.html', {
        'form': product_form,
        'formset': formset,
        })

# Delete a product
@login_required
def delete_product(request, pk):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
        
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == "POST":
        product.delete()
        messages.success(request, 'Product successfully deleted.')
        return redirect('manage_products')  # Redirect to product management page after deletion

    return render(request, 'product_catalog/delete_confirmation.html', {'product': product})



@login_required
def rate_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Checks if the user has purchased the product
    if not user_has_purchased_product(request.user, product):
        messages.error(request, "You can only rate products you've purchased.")
        return redirect('product_detail', product_id=product_id)

    # Capture the 'next' parameter from the GET request, or fallback to the product detail page
    next_url = request.GET.get('next', None)
    if not next_url or not url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
        next_url = reverse('product_detail', kwargs={'product_id': product_id})

    if request.method == 'POST':
        form = ProductRatingForm(request.POST)
        if form.is_valid():
            # Check if the user has already rated this product
            existing_rating = ProductRating.objects.filter(product=product, user=request.user).first()
            if existing_rating:
                existing_rating.rating = form.cleaned_data['rating']
                existing_rating.review = form.cleaned_data.get('review')
                existing_rating.save()
                messages.success(request, 'Your rating has been updated.')
            else:
                rating = form.save(commit=False)
                rating.user = request.user
                rating.product = product
                rating.save()
                messages.success(request, 'Your rating has been submitted.')
            
            # Update product's average rating
            update_product_rating(product)

            return redirect('product_detail', product_id=product_id)
    else:
        form = ProductRatingForm()

    return render(request, 'product_catalog/rate_product.html', {
        'form': form,
        'product': product,
        'next_url': next_url
    })

def update_product_rating(product):
    """
    Recalculate the product's average rating after a new rating is added.
    """
    ratings = product.ratings.all()
    if ratings.exists():
        product.rating = ratings.aggregate(Avg('rating'))['rating__avg']
        product.save()


def user_has_purchased_product(user, product):
    """
    Checks if the user has purchased the product.
    """
    return user.orders.filter(items__product=product).exists()

logger = logging.getLogger('product_catalog')
def new_arrivals(request):
    new_arrival_products = Product.get_new_arrivals().order_by('-created_at')[:30]

    logger.info(f'New arrival products count: {new_arrival_products.count()}')  # Log the count
    
    context = {
        'new_arrival_products': new_arrival_products
    }
    
    return render(request, 'product_catalog/new_arrivals.html', context)