from rest_framework import serializers
from api.models import Product,Category,Batch

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'price',
            'cost',
            'description',
            'category',
            'batch',
        ]
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name'
        ]
class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = [
            'id'
        ]