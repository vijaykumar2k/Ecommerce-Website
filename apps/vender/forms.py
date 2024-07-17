from django import forms

from apps.vender.models import Vender


class CreateVenderForm(forms.ModelForm):
    class Meta:
        model = Vender
        fields = ['user','name','address','open_at','close_at','image','lat','long']