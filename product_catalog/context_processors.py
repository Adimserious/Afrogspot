from django.conf import settings

def categories_processor(request):
    """
    Adds categories and language-related context to all templates.
    This version is SAFE to use when the database is still empty
    (e.g. right after deploying to Heroku and before running migrations).
    """
    try:
        from .models import Category
        categories = Category.objects.all()
    except Exception:
        # Table doesn't exist yet (fresh DB) or DB isn't ready
        categories = []

    return {
        'categories': categories,
        'LANGUAGES': getattr(settings, 'LANGUAGES', []),
        'current_language': getattr(request, 'LANGUAGE_CODE', 'en'),
    }
