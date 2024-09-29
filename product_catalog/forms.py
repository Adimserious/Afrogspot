# forms.py
from django import forms
from .models import Product, Category, ProductVariant, ProductRating
from django.forms import inlineformset_factory


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

# Formset to manage ProductVariants in the same form as the Product
ProductVariantFormSet = inlineformset_factory(
    Product, ProductVariant,
    fields=['product', 'size', 'price', 'stock'],
    extra=1, can_delete=True
)


class ProductRatingForm(forms.ModelForm):
    class Meta:
        model = ProductRating
        fields = ['rating', 'review']

    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]
    rating = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect, label="Rate this product")