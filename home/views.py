from django.shortcuts import render
from django.conf import settings

# TEMP: make this safe when product_catalog is not installed (like on fresh Heroku)
try:
    from product_catalog.models import Category
except Exception:
    Category = None


def home(request):
    """A view to render the home page (safe even if DB is empty)."""

    categories = []

    if Category is not None:
        try:
            categories = Category.objects.all()
        except Exception:
            # table doesn't exist yet
            categories = []

    context = {
        'categories': categories,
        'LANGUAGES': getattr(settings, 'LANGUAGES', []),
    }

    return render(request, 'home/home.html', context)


def about_us(request):
    return render(request, 'home/about_us.html')
