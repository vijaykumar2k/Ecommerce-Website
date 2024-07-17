from django import forms
from apps.category.models import Category



class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name','type']