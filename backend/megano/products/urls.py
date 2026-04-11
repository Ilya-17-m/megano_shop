from django.urls import path

from .views import (
        TagsListView,
        CategoriesListView,
        ProductPopularListView,
        ProductLimitedListView,
        BannersListView,
        ProductDetailView,
        ReviewCreateAPIView,
        SalesListView,
  )

app_name = 'products'


urlpatterns = [
    path('tags/', TagsListView.as_view(), name='tags'),
    path('categories/', CategoriesListView.as_view(), name='categories'),
    path('products/popular/', ProductPopularListView.as_view(), name='popular_product'),
    path('products/limited/', ProductLimitedListView.as_view(), name='limited_product'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('banners/', BannersListView.as_view(), name='banners'),
    path('sales/', SalesListView.as_view(), name='sales'),
    path('product/<int:pk>/reviews', ReviewCreateAPIView.as_view(), name='review'),
]