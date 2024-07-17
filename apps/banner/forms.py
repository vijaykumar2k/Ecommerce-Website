from django import forms

from apps.banner.models import HomeBanner


class CreateBannerForm(forms.ModelForm):
    class Meta:
        model = HomeBanner
        fields = ['vender','category','name','is_active','image']


class CSVUploadForm(forms.Form):
    csv_file = forms.FileField()