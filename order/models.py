from django.db import models

# Create your models here.

from product.models import Product

class Order(models.Model):
    address = models.CharField(max_length=99)
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

