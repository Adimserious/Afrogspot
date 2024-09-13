from django import forms
from .models import Order

class CheckoutForm(forms.ModelForm):
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
            'email': forms.EmailInput(attrs={'placeholder': 'Email Address'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone Number', 'type': 'tel'}),
            'address_line_1': forms.TextInput(attrs={'placeholder': 'Address Line 1'}),
            'address_line_2': forms.TextInput(attrs={'placeholder': 'Address Line 2 (Optional)', 'required': False}),
            'city': forms.TextInput(attrs={'placeholder': 'City'}),
            'postal_code': forms.TextInput(attrs={'placeholder': 'Postal Code'}),
            'country': forms.TextInput(attrs={'placeholder': 'Country'}),
        }

    # automatically append a star to required fields using Django’s form field rendering
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.required:
                field.label = f'{field.label} <span class="required">*</span>'
                field.widget.attrs.update({'class': 'form-control'})