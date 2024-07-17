from django import forms
from apps.product.models import Product, ProductAddOn, ProductAddOnOption


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category','name','price','description','available','stock','is_feature','is_popular']


class CSVUploadForm(forms.Form):
    csv_file = forms.FileField()



#product-add-0n form

class CreateProductAddOnForm(forms.ModelForm):
    class Meta:
        model = ProductAddOn
        fields = ['title','type','is_required']

#product-add-0n-option form

class CreateProductAddOnOptionForm(forms.ModelForm):
    class Meta:
        model = ProductAddOnOption
        fields = ['addon','title','price']