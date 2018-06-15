from django import forms
from food.models import Cart


class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields= ['user','item']