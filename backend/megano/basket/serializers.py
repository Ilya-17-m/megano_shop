from .models import BasketModel
from rest_framework import serializers

from catalog.serializers import ProductShortSerializer


class BasketSerializer(serializers.ModelSerializer):
    product = ProductShortSerializer(read_only=True)

    class Meta:
        model = BasketModel
        fields = [
            'id','product'
        ]

    def to_representation(self, instance):
        return ProductShortSerializer(instance.product).data