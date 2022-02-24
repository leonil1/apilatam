from django.db import models

from apps.utils.models import BaseModel


class Product(BaseModel):
    name = models.CharField('name Category', max_length=100)
    description = models.TextField('description', max_length=250, blank=True)
    brand = models.CharField(max_length=50, blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='images/category', blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    stock = models.PositiveIntegerField(default=1, blank=True)
    rating = models.DecimalField(max_digits=5, decimal_places=2, default=0.05)
    number_view = models.PositiveIntegerField(default=1, blank=True)

    def __str__(self):
        return self.name
