from api.serializers import ProductSerializer, CategorySerializer, BatchSerializer
from rest_framework import viewsets, permissions
from api.models import Product

# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

class BatchViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = BatchSerializer
    permission_classes = [permissions.IsAuthenticated]