from rest_framework import serializers
from django.contrib.auth.models import User

from .models import ProfileModel, ImageModel


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = [
            'src', 'alt'
        ]


class ProfileSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()

    class Meta:
        model = ProfileModel
        fields = [
            'id', 'avatar', 'email', 'phone', 'fullName'
        ]

    def get_avatar(self, obj):
        image = obj.avatar
        if image:
            return ImageSerializer(image).data
        return None