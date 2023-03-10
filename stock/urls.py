from rest_framework.routers import DefaultRouter
from views import ProductViewSet,CategoryViewSet,BatchViewSet


app_name = 'stock'

router = DefaultRouter(trailing_slash=False)
router.register(r'products', ProductViewSet)
router.register(r'categorys', CategoryViewSet)
router.register(r'batchs', BatchViewSet)

urlpatterns = router.urls