from django.core.validators import RegexValidator
from django.db import models

from application.custom_models import DateTimeModel


# Create your models here.

class Store(DateTimeModel):
    name = models.CharField(max_length=100,null=True)
    open_at = models.TimeField(null=True)
    close_at = models.TimeField(null=True)
    description = models.TextField(null=True)
    city = models.CharField(max_length=100,null=True)
    state = models.CharField(max_length=100,null=True)
    pin_code = models.CharField(max_length=6,validators=[RegexValidator(r'^\d{6}$', 'Enter a valid 6-digit PIN code.')],null=True)
    country = models.CharField(max_length=20,null=True)
    address = models.CharField(max_length=300,null=True)




    def __str__(self):
        return self.name