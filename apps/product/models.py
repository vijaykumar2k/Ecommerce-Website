from django.db import models
from application.custom_models import DateTimeModel
from apps import product
from apps.category.models import Category
from apps.product.constants import PRODUCT_ADD_ON_TYPE
from apps.user.models import User
from apps.vender.models import Vender


# Create your models here.





class Product(DateTimeModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=200,null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    description = models.TextField(null=True)
    available = models.BooleanField(default=True,null=True)  # Changed to BooleanField
    stock = models.IntegerField(null=True)
    is_feature = models.BooleanField(default=False,null=True)
    is_popular = models.BooleanField(default=False,null=True)

    def __str__(self):
        return self.name


class ProductAddOn(DateTimeModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=100,null=True)
    type = models.CharField(choices=PRODUCT_ADD_ON_TYPE,max_length=50,blank=True,null=True)
    is_required = models.BooleanField(default=False,null=True)

    def __str__(self):
        return self.title


class ProductAddOnOption(DateTimeModel):
    addon = models.ForeignKey(ProductAddOn, on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=100,null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True)

    def __str__(self):
        return self.title


class FavoriteProduct(DateTimeModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    vender = models.ForeignKey(Vender, on_delete=models.CASCADE,null=True)

