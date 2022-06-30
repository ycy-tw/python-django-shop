from django import forms
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _
from .models import Product, Category, Shop
from decimal import Decimal


class SearchForm(forms.Form):
    query = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'id': 'search',
                'class': 'form-control',
                'placeholder': _('Search'),
            }
        )
    )


class ProductForm(forms.ModelForm):

    name = forms.CharField(
        label=_('Product Name'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }),
    )

    price = forms.DecimalField(
        label=_('Price'),
        decimal_places=2,
        max_digits=10,
        validators=[MinValueValidator(Decimal('0.01'))],
        widget=forms.NumberInput(
            attrs={'class': 'form-control'}
        )
    )

    description = forms.CharField(
        label=_('Description'),
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'style': 'resize:none; height:100px;'}),
    )

    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'description', 'shop']
        widgets = {
            'category': forms.Select(
                attrs={
                    'class': 'form-select',
                },
            ),
            'shop': forms.Select(
                attrs={
                    'class': 'form-select',
                },
            ),
        }

    def __init__(self, user, *args, **kwargs):

        # take user as one of arguments
        # for filter shops belonged to the user
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['shop'].queryset = Shop.objects.filter(user=user)


class ShopForm(forms.ModelForm):

    name = forms.CharField(
        label=_('Shop Name'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }),
    )

    description = forms.CharField(
        label=_('Description'),
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'style': 'resize:none; height:100px;'}),
    )

    shop_img = forms.ImageField(
        label=_('Shop Image'),
        widget=forms.FileInput(
            attrs={'class': 'form-control', }),
    )

    class Meta:
        model = Shop
        fields = ['name', 'description', 'shop_img']

    def __init__(self, *args, **kwargs):

        super(ShopForm, self).__init__(*args, **kwargs)
        self.fields['shop_img'].required = False
