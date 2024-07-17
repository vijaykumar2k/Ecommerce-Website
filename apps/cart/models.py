from django.db import models
from application.custom_models import DateTimeModel
from apps.product.models import Product, ProductAddOn, ProductAddOnOption
from apps.user.models import User
from apps.vender.models import Vender


# Create your models here.
class Cart(DateTimeModel):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    vender = models.ForeignKey(Vender,on_delete=models.CASCADE,null=True)


class CartItem(DateTimeModel):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    addon_data = models.CharField(blank=True,null=True, max_length=255)
    quantity = models.PositiveIntegerField(blank=True,null=True)

    def __str__(self):
        return self.addon_data


class CartItemAddOn(DateTimeModel):
    cartitem = models.ForeignKey(CartItem,on_delete=models.CASCADE,null=True)
    product_addon = models.ForeignKey(ProductAddOn,on_delete=models.CASCADE,null=True)

class CartItemAddOnOption(DateTimeModel):
    cartitemaddon = models.ForeignKey(CartItemAddOn,on_delete=models.CASCADE,null=True)
    product_addon_option = models.ForeignKey(ProductAddOnOption,on_delete=models.CASCADE,null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True)