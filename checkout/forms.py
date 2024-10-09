from django import forms
from django.utils.html import format_html
from django_countries.fields import CountryField
from .models import Order


class CheckoutForm(forms.ModelForm):
    save_info = forms.BooleanField(
        required=False,
        label="Save this delivery information to my profile"
    )

    # Meta class for model fields
    class Meta:
        model = Order
        fields = [
            'full_name',
            'email',
            'phone_number',
            'address_line_1',
            'address_line_2',
            'city',
            'postal_code',
            'country'
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={
                'placeholder': 'Full Name',
                'autofocus': 'autofocus'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email Address'
            }),
            'phone_number': forms.TextInput(attrs={
                'placeholder': 'Phone Number',
                'type': 'tel'
            }),
            'address_line_1': forms.TextInput(attrs={
                'placeholder': 'Address Line 1'
            }),
            'address_line_2': forms.TextInput(attrs={
                'placeholder': 'Address Line 2 (Optional)',
                'required': False
            }),
            'city': forms.TextInput(attrs={
                'placeholder': 'City'
            }),
            'postal_code': forms.TextInput(attrs={
                'placeholder': 'Postal Code'
            }),
        }

    # Override the __init__ method
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add CountryField from django-countries and set the label
        self.fields['country'] = CountryField(
            blank_label='Select a country'
        ).formfield(
            widget=forms.Select(attrs={'class': 'form-control'}),
            label="Country"
        )

        # Add asterisks for required fields and apply form-control class
        for field_name, field in self.fields.items():
            if field.required:
                field.label = format_html(
                    '{} <span class="required">*</span>',
                    field.label
                )
            field.widget.attrs.update({'class': 'form-control'})
