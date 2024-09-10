from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from products.api.endpoints import urlpatterns as product_urls

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('products.urls')),
    path('api/v1/', include(product_urls)),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/docs/', SpectacularSwaggerView.as_view(url_name='schema')),
]
