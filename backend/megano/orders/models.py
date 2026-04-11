from django.contrib.auth.models import User
from django.db import models

from products.models import Product
from accounts.models import Profile


class OrderModel(models.Model):
    """
        Модель заказов пользователя
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile')
    createdAt = models.CharField(max_length=25)
    products = models.ManyToManyField(Product)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=150)
    totalCost = models.SmallIntegerField(default=0)
    status = models.CharField(max_length=25)
    deliveryType = models.CharField(max_length=25)
    paymentType = models.CharField(max_length=25)



