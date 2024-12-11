from django.shortcuts import render
from product_catalog.models import Category
from django.shortcuts import redirect
from django.conf import settings


def home(request):
    """ A view to render the home page """
    categories = Category.objects.all()

    context = {
        'categories': categories,
        'LANGUAGES': settings.LANGUAGES,
    }

    return render(request, 'home/home.html', context)


def about_us(request):
    return render(request, 'home/about_us.html')
