from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _
from django.db.models import Q, Avg
from django.forms import modelformset_factory
from django.conf import settings
from django.utils.http import url_has_allowed_host_and_scheme
import logging

logger = logging.getLogger("product_catalog")

# make model imports SAFE so Django can start on an empty DB
try:
    from .models import (
        Product,
        Category,
        ProductVariant,
        Country,
        ProductRating,
    )
except Exception:
    Product = None
    Category = None
    ProductVariant = None
    Country = None
    ProductRating = None


def get_variant_formset():
    """
    Create the formset only when we actually need it.
    (Doing this at import time crashes on a fresh DB.)
    """
    if ProductVariant is None:
        return None

    return modelformset_factory(
        ProductVariant,
        fields=("id", "size", "price", "stock"),
        extra=1,
        can_delete=True,
    )


def product_list(request):
    query = request.GET.get("q", "").strip()
    category_name = request.GET.get("category")

    # If DB/tables not ready, just show empty page
    if Product is None:
        return render(
            request,
            "product_catalog/product_list.html",
            {
                "products": [],
                "categories": [],
                "countries": [],
                "query": query,
            },
        )

    # Prioritized categories
    prioritized_categories = [
        "Nuts and Seeds",
        "Veggies",
        "Peppers",
        "Seasonings",
        "Others",
        "Lean Meat or Seafood",
    ]

    # Base product query
    products = Product.objects.filter(is_active=True).prefetch_related("images")

    # Apply priority ordering to products
    products = products.annotate(
        is_prioritized=Q(category__name__in=prioritized_categories)
    ).order_by("-is_prioritized", "category__name")

    # Filter parameters from request
    vegan = request.GET.get("vegan", "")
    gluten_free = request.GET.get("gluten_free", "")
    country = request.GET.get("country", "")

    # Applying filters
    if vegan:
        products = products.filter(is_vegan=True)
    if gluten_free:
        products = products.filter(is_gluten_free=True)
    if country:
        products = products.filter(country__name=country)

    # If a category is selected, clear the search query
    if category_name:
        products = products.filter(category__name__iexact=category_name)
        query = ""  # Reset query when a category is selected

    # If no category is selected and there's a search query, filter by query
    if query:
        products = products.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
        category_name = ""  # Clear the category query

    # Check if no products are found after all filters
    no_products_found = False
    if products.count() == 0:
        no_products_found = True
        messages.info(
            request,
            "No products found matching your criteria. Please try again with different filters or a search term.",
        )

    # Only display the warning if the user explicitly submitted
    if (
        request.GET
        and not query
        and not category_name
        and not vegan
        and not gluten_free
        and not country
    ):
        messages.warning(
            request,
            "You didn't enter a search term or select a category. Please try again.",
        )

    # Identify products the user has purchased
    purchased_products = []
    if request.user.is_authenticated:
        purchased_products = [
            product.id
            for product in products
            if user_has_purchased_product(request.user, product)
        ]

    # categories / countries might also fail on empty DB → protect them
    try:
        categories = Category.objects.all()
    except Exception:
        categories = []

    try:
        countries = Country.objects.all()
    except Exception:
        countries = []

    context = {
        "products": products,
        "query": query,
        "category_name": category_name,
        "categories": categories,
        "countries": countries,
        "vegan": vegan,
        "gluten_free": gluten_free,
        "selected_country": country,
        "purchased_products": purchased_products,
        "no_products_found": no_products_found,
    }

    return render(request, "product_catalog/product_list.html", context)


def product_detail(request, product_id):
    """A view to show individual products with multiple images"""

    if Product is None:
        messages.error(request, "Products are not available yet.")
        return redirect("home")

    product = get_object_or_404(Product, id=product_id)
    variants = product.variants.all()
    reviews = ProductRating.objects.filter(product=product).order_by("-created_at")
    additional_images = product.images.all()

    context = {
        "product": product,
        "description": _(product.description),
        "variants": variants,
        "reviews": reviews,
        "additional_images": additional_images,
    }

    return render(request, "product_catalog/product_detail.html", context)


@login_required
def manage_products(request):
    if Product is None:
        products = []
    else:
        products = Product.objects.all()
    return render(request, "product_catalog/manage_products.html", {"products": products})


@login_required
def add_product(request):
    """Add products to the store"""

    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    ProductVariantFormSet = get_variant_formset()

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        variant_formset = (
            ProductVariantFormSet(request.POST) if ProductVariantFormSet else None
        )

        if form.is_valid() and (not ProductVariantFormSet or variant_formset.is_valid()):
            product = form.save()

            # Save variants if they exist
            if ProductVariantFormSet and variant_formset:
                variants = variant_formset.save(commit=False)
                for variant in variants:
                    variant.product = product
                    variant.save()

                for variant in variant_formset.deleted_objects:
                    variant.delete()

            messages.success(request, "Product has been successfully added!")
            return redirect("product_list")
        else:
            messages.error(
                request,
                "There was an error adding the product. Please check the form and try again.",
            )
    else:
        form = ProductForm()
        if ProductVariantFormSet:
            variant_formset = ProductVariantFormSet(
                queryset=ProductVariant.objects.none()
            )
        else:
            variant_formset = None

    return render(
        request,
        "product_catalog/add_product.html",
        {
            "form": form,
            "variant_formset": variant_formset,
        },
    )


@login_required
def update_product(request, pk):
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=pk)
    ProductVariantFormSet = get_variant_formset()

    if request.method == "POST":
        product_form = ProductForm(request.POST, request.FILES, instance=product)
        formset = (
            ProductVariantFormSet(
                request.POST, queryset=ProductVariant.objects.filter(product=product)
            )
            if ProductVariantFormSet
            else None
        )

        if product_form.is_valid() and (not formset or formset.is_valid()):
            product = product_form.save()

            if formset:
                variants = formset.save(commit=False)
                for variant in variants:
                    variant.product = product
                    variant.save()

                for variant in formset.deleted_objects:
                    variant.delete()

            messages.success(request, "Product has been successfully updated!")
            return redirect("product_list")
        else:
            messages.error(
                request,
                "There was an error updating the product. Please check the form and try again.",
            )
    else:
        product_form = ProductForm(instance=product)
        if ProductVariantFormSet:
            formset = ProductVariantFormSet(
                queryset=ProductVariant.objects.filter(product=product)
            )
        else:
            formset = None

    return render(
        request,
        "product_catalog/update_product.html",
        {
            "form": product_form,
            "formset": formset,
        },
    )


@login_required
def delete_product(request, pk):
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        product.delete()
        messages.success(request, "Product successfully deleted.")
        return redirect("manage_products")

    return render(
        request, "product_catalog/delete_confirmation.html", {"product": product}
    )


@login_required
def rate_product(request, product_id):
    if Product is None:
        messages.error(request, "Products are not available yet.")
        return redirect("home")

    product = get_object_or_404(Product, id=product_id)

    if not user_has_purchased_product(request.user, product):
        messages.error(request, "You can only rate products you've purchased.")
        return redirect("product_detail", product_id=product_id)

    next_url = request.GET.get("next", None)
    if not next_url or not url_has_allowed_host_and_scheme(
        next_url, allowed_hosts={request.get_host()}
    ):
        next_url = reverse("product_detail", kwargs={"product_id": product_id})

    if request.method == "POST":
        form = ProductRatingForm(request.POST)
        if form.is_valid():
            existing_rating = ProductRating.objects.filter(
                product=product, user=request.user
            ).first()
            if existing_rating:
                existing_rating.rating = form.cleaned_data["rating"]
                existing_rating.review = form.cleaned_data.get("review")
                existing_rating.save()
                messages.success(request, "Your rating has been updated.")
            else:
                rating = form.save(commit=False)
                rating.user = request.user
                rating.product = product
                rating.save()
                messages.success(request, "Your rating has been submitted.")

            update_product_rating(product)

            return redirect("product_detail", product_id=product_id)
    else:
        form = ProductRatingForm()

    return render(
        request,
        "product_catalog/rate_product.html",
        {"form": form, "product": product, "next_url": next_url},
    )


def update_product_rating(product):
    ratings = product.ratings.all()
    if ratings.exists():
        product.rating = ratings.aggregate(Avg("rating"))["rating__avg"]
        product.save()


def user_has_purchased_product(user, product):
    return user.orders.filter(items__product=product).exists()


def new_arrivals(request):
    if Product is None:
        return render(
            request,
            "product_catalog/new_arrivals.html",
            {"new_arrival_products": []},
        )

    new_arrival_products = Product.get_new_arrivals().order_by("-created_at")[:30]
    logger.info(f"New arrival products count: {new_arrival_products.count()}")

    return render(
        request,
        "product_catalog/new_arrivals.html",
        {"new_arrival_products": new_arrival_products},
    )


def recipes(request):
    if Product is None:
        return render(request, "product_catalog/recipes.html", {"ingredients": {}})

    ingredients = {
        "crayfish": Product.objects.filter(name__icontains="crayfish").first(),
        "ogbono": Product.objects.filter(name__icontains="ogbono").first(),
        "stuck_fish": Product.objects.filter(name__icontains="stuck fish").first(),
        "mangala_fish": Product.objects.filter(name__icontains="mangala fish").first(),
        "red_peppers": Product.objects.filter(name__icontains="red peppers").first(),
        "knorr_cube": Product.objects.filter(name__icontains="knorr cube").first(),
    }

    return render(request, "product_catalog/recipes.html", {"ingredients": ingredients})
