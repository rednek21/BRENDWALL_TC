from rest_framework.routers import DefaultRouter
from products.api.api import ProductListViewSet, ProductCreateViewSet

router = DefaultRouter()
router.register(r'products', ProductListViewSet, basename='product-list')
router.register(r'products/create', ProductCreateViewSet, basename='product-create')

urlpatterns = router.urls
