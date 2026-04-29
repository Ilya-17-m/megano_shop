from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView


# def sentry_debug(request):
#     return 1 / 0


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('frontend.urls')),
    path('metrics/', include('django_prometheus.urls'), name='prometheus'),
    path('api/', include('products.urls'), name='product'),
    path('api/', include('accounts.urls'), name='account'),
    path('api/', include('basket.urls'), name='basket'),
    path('api/', include('orders.urls'), name='order'),
    path('api/', include('catalog.urls'), name='catalog'),

    path('schema/', SpectacularAPIView.as_view(), name='schema'),

    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # path('sentry-debug/', sentry_debug),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)