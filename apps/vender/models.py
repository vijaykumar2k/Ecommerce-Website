from django.conf import settings
from django.db import models
from application.custom_models import DateTimeModel

# Create your models here.

class Vender(DateTimeModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=255,null=True)
    open_at = models.TimeField(null=True)
    close_at = models.TimeField(null=True)
    image = models.ImageField(upload_to='vendor_images/',null=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6,null=True)
    long = models.DecimalField(max_digits=9, decimal_places=6,null=True)




    def __str__(self):
        return self.name
