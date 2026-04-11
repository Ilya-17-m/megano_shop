from rest_framework import serializers

from products.models import Product
from products.serializers import ImageSerializer, TagsSerializer


class ProductShortSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    tags = TagsSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            'id', 'category', 'price', 'count', 'date', 'title', 'description', 'freeDelivery',
            'images', 'tags', 'rating'
        ]