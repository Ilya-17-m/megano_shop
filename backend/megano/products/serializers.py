from rest_framework import serializers
from .models import (
    ProductModel,
    CategoriesModel,
    TagsModel,
    ReviewModel,
    ImagesModel,
    SpecificationsModel,
    SubcategoriesModel,
    )


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagesModel
        fields = [
            'src', 'alt'
        ]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewModel
        fields = [
            'author', 'email', 'rate', 'date', 'text',
        ]


class SpecificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecificationsModel
        fields = ['id', 'name', 'value']


class BannersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = [
            'id', 'category', 'price', 'count', 'date', 'title', 'description', 'freeDelivery', 'images', 'tags',
            'rating', 'reviews'
        ]


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagsModel
        fields = ['id', 'name']


class SubcategoriesSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = SubcategoriesModel
        fields = [
            'id','title', 'image'
        ]

    def get_image(self, obj):
        image = obj.image
        if image:
            return ImageSerializer(image).data
        return None


class CategoriesSerializer(serializers.ModelSerializer):
    subcategories = SubcategoriesSerializer(many=True, read_only=True)
    image = serializers.SerializerMethodField()

    class Meta:
        model = CategoriesModel
        fields = [
            'id', 'title', 'image', 'subcategories',
        ]

    def get_image(self, obj):
        image = obj.image
        if image:
            return ImageSerializer(image).data
        return None


class ProductFullSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    tags = TagsSerializer(many=True, read_only=True)
    specifications = SpecificationsSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = ProductModel
        fields = ['id', 'category', 'price', 'count', 'date', 'title', 'description', 'fullDescription',
                  'freeDelivery', 'images', 'tags', 'rating', 'specifications', 'reviews'
                  ]


class SaleSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = ProductModel
        fields = [
            'id','title', 'salePrice', 'price', 'dateTo', 'dateForm', 'images'
        ]