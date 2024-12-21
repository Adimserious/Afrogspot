from django import forms
from .models import Product, Category, ProductVariant, ProductRating
from django.forms import inlineformset_factory


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class ProductVariantForm(forms.ModelForm):
    class Meta:
        model = ProductVariant
        fields = ['product', 'size', 'price', 'stock']

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if isinstance(price, str):
            # Replace commas with dots for consistency
            price = price.replace(',', '.')
        return Decimal(price)  # Convert to Decimal after cleaning


# Formset to manage ProductVariants in the same form as the Product
ProductVariantFormSet = inlineformset_factory(
    Product, ProductVariant,
    form=ProductVariantForm,
    fields=['product', 'size', 'price', 'stock'],
    extra=1, can_delete=True

)


class ProductRatingForm(forms.ModelForm):
    class Meta:
        model = ProductRating
        fields = ['rating', 'review']

    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]
    rating = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.
                               RadioSelect, label="Rate this product")
