# forms.py
from django import forms
from .models import Product

class AddToCartForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all())
    quantity = forms.IntegerField(min_value=1)
