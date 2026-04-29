from django.contrib.auth.models import User
from django.db import models

from products.models import ProductModel


class BasketModel(models.Model):
    """
        Model user basket
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)

    class Meta:
        name = 'basket'
        ordering = ['-id',]