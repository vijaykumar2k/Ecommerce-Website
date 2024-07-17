from django.db import models

from application.custom_models import DateTimeModel


# Create your models here.
class Category(DateTimeModel):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100,null=True,blank=True)


    def __str__(self):
        return self.name