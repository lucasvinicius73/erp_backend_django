from django.contrib import admin

from stock.models import Batch, Category, Product


class Products(admin.ModelAdmin):
    list_display = ('id','name','price','cost')
    list_display_links = ('id','name')
    search_fields = ('name',)
    list_per_page = 20

admin.site.register(Product,Products)

# Register your models here.
