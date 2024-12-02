from .models import Category
from django.conf import settings

def categories_processor(request):
    """
    Adds categories and language-related context to all templates.
    """
    categories = Category.objects.all()
    return {
        'categories': categories,  # Existing categories context
        'LANGUAGES': settings.LANGUAGES,  # Available languages
        'current_language': request.LANGUAGE_CODE,  # Current selected language
    }
