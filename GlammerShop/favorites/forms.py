from django import forms

from products.models import Product


class AddToFavoritesForm(forms.Form):
    product_id = forms.IntegerField()

    def clean_product_id(self):
        product_id = self.cleaned_data['product_id']
        if not Product.objects.filter(id=product_id).exists():
            raise forms.ValidationError("Продукт не существует")
        return product_id