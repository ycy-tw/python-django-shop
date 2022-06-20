from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['email', 'name', 'address']
        widgets = {
            'email': forms.EmailInput(
                attrs={'class': 'form-control'}
            ),
            'name': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'address': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
        }
