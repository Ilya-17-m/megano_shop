from django.db import models

from products.models import ProductModel
from accounts.models import ProfileModel


class OrderModel(models.Model):
    """
        Model user orders
    """
    profile = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name='profile')
    products = models.ManyToManyField(ProductModel)
    createdAt = models.CharField(max_length=25)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=150)
    totalCost = models.SmallIntegerField(default=0)
    status = models.CharField(max_length=25)
    deliveryType = models.CharField(max_length=25)
    paymentType = models.CharField(max_length=25)

    class Meta:
        db_table = 'orders'
        ordering = ['-id',]