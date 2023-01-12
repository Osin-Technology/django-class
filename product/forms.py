from django import forms
from .models import (
    Product,
)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

   


class ProductCustomForm(forms.Form):
    name = forms.CharField()
    price = forms.IntegerField()
    quantity = forms.IntegerField()