# forms.py
from django import forms
from .models import Product, ProductVariant
from django.forms import inlineformset_factory

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image', 'category', 'stock']

# Formset to manage ProductVariants in the same form as the Product
ProductVariantFormSet = inlineformset_factory(
    Product, ProductVariant,
    fields=['product', 'size', 'price', 'stock'],
    extra=1, can_delete=True
)
