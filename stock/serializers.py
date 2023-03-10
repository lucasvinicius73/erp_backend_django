from rest_framework import serializers
from .models import Batch, Brand, Category, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'price',
            'brand',
            'category',
            'description',
        ]
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name'
        ]
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = [
            'name'
        ]
class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = [
            'id',
            'date',
            'Product',
            'costUnit',
            'quantity'
        ]