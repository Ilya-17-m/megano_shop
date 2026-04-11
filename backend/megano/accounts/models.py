from django.contrib.auth.models import User
from django.db import models


class ImageModel(models.Model):
    src = models.ImageField(upload_to='avatar')
    alt = models.CharField(max_length=255)


class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    fullName = models.CharField(max_length=50)
    email = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=50, null=True)
    avatar = models.OneToOneField(ImageModel, on_delete=models.CASCADE, null=True)
