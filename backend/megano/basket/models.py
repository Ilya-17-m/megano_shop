from django.contrib.auth.models import User
from django.db import models

from products.models import ProductModel


class BasketModel(models.Model):
    """
        Модель корзины пользователя
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)