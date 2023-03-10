from django.urls import include, path
from rest_framework.routers import DefaultRouter

from stock.views import (BatchViewSet, BrandViewSet, CategoryViewSet,
                         ProductViewSet)

router = DefaultRouter()
router.register(r'products', ProductViewSet,basename='Products')
router.register(r'categorys', CategoryViewSet,basename='Categorys')
router.register(r'brands', BrandViewSet,basename='Brand')
router.register(r'batchs', BatchViewSet,basename='Batchs')

app_name = 'stock'

urlpatterns =[
    path('',include(router.urls)),
]
