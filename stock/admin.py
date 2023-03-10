from django.contrib import admin

from stock.models import Batch, Brand, Category, Product

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Batch)
admin.site.register(Brand)