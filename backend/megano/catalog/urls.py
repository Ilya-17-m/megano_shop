from django.urls import path

from .views import CatalogView


app_name = 'catalog'


urlpatterns = [
    path('catalog/', CatalogView.as_view(), name='catalog'),
]