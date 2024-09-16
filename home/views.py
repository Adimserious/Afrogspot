from django.shortcuts import render
from product_catalog.models import Category

# Create your views here.
def home(request):
    """ A view to render the home page """
    categories = Category.objects.all()  # Fetch categories for dropdown

    context = {
        'categories': categories,
    }

    return render(request, 'home/home.html', context)