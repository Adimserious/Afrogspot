"""afrogspot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from afrogspot.views import four_o_four_view, handler505
from django.conf.urls.i18n import i18n_patterns, set_language

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Allauth doesn't require i18n
    path('trigger-505/', handler505, name='trigger_505'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# i18n patterns for language-prefixed URLs
urlpatterns += i18n_patterns(
    path('set_language/', set_language, name='set_language'),
    path('', include('home.urls')),  # Homepage
    path('product_catalog/', include('product_catalog.urls')),  # Product catalog
    path('cart/', include('cart.urls')),  # Shopping cart
    path('checkout/', include('checkout.urls')),  # Checkout
    path('profiles/', include('profiles.urls')),  # User profiles
    path('contact/', include('contact.urls')),  # Contact page
)

handler404 = four_o_four_view




