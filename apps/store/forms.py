from django import forms
from apps.store.models import Store


class CreateStoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['name','open_at','close_at','description','city','state','pin_code','country','address']