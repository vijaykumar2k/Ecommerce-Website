from django.db import models
from application.custom_models import DateTimeModel
from apps.category.models import Category
from apps.vender.models import Vender


class HomeBanner(DateTimeModel):
    vender = models.ForeignKey(Vender, on_delete=models.CASCADE,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=255,null=True)
    is_active = models.BooleanField(default=True,null=True)
    image = models.ImageField(upload_to='home_banners/',null=True)



    def __str__(self):
        return self.name