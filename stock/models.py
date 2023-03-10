import uuid

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name
class Brand(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name
    
# Create your models here.
class Product(models.Model):
    name = models.CharField(
        max_length=60,
        null=False,
        blank=False
    )
    price = models.DecimalField(
        null=False,
        blank=False,
        max_digits=7,
        decimal_places=2
    )
    brand = models.ForeignKey(Brand)
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE
    )
    quantity = models.IntegerField(
        null=False,
        blank=False,
    )
    
    description = models.CharField(
        max_length=120,
        null=False,
        blank=False
    )
class Batch(models.Model):
    date = models.DateField(auto_now_add=True)
    idProduct = models.ForeignKey(Product,)
    costUnit = models.DecimalField(
        null=False,
        blank=False,
        max_digits=7,
        decimal_places=2
    )
    quantity = models.IntegerField(
        null=False,
        blank=False,
    )

    def __str__(self):
        return str(self.name)