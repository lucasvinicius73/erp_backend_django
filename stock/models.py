import uuid

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name
    
class Batch(models.Model):
    name = models.DateField(auto_now_add=True)
    def __str__(self):
        return str(self.name)
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
    cost = models.DecimalField(
        null=False,
        blank=False,
        max_digits=7,
        decimal_places=2
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
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE
    )
    batch = models.ForeignKey(
        Batch,
        on_delete=models.CASCADE
    )