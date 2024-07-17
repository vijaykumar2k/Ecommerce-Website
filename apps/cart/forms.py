from django import forms

from apps.cart.models import Cart


class CreateCartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['user','vender']