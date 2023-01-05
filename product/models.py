from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=99)
    quantity = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return self.name


