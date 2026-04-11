from django.urls import path

from .views import PaymentAPIView, OrdersAPIView, OrderAPIView


app_name = 'orders'


urlpatterns = [
    path('order/<int:pk>', OrderAPIView.as_view(), name='order'),
    path('orders', OrdersAPIView.as_view(), name='orders'),
    path('payment', PaymentAPIView.as_view(), name='payment'),
]