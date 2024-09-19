from django import forms
from .models import Profile

#Custom form
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'default_full_name', 'default_email', 'default_phone_number',
            'default_address_line_1', 'default_address_line_2',
            'default_city', 'default_postal_code', 'default_country'
        ]
        widgets = {
            'default_country': forms.Select(attrs={'class': 'form-control'}),
            'default_full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'default_email': forms.EmailInput(attrs={'class': 'form-control'}),  
            'default_phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'default_address_line_1': forms.TextInput(attrs={'class': 'form-control'}),
            'default_address_line_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Optional'}),  # Optional field
            'default_city': forms.TextInput(attrs={'class': 'form-control'}),
            'default_postal_code': forms.TextInput(attrs={'class': 'form-control'}),
        }
