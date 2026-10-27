from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from FarmersMarket import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('FarmersMarket.common.urls')),
    path('markets/', include('FarmersMarket.markets.urls')),
    path('producers/', include('FarmersMarket.producers.urls')),
    path('products/', include('FarmersMarket.products.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)