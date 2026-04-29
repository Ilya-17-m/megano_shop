from django.contrib.auth.models import User
from django.db import models


class ImageModel(models.Model):
    """
        Model for create avatar in profile
    """
    src = models.ImageField(upload_to='avatar')
    alt = models.CharField(max_length=255)

    class Meta:
        name = 'accounts_avatar'
        ordering = ['-id',]


class ProfileModel(models.Model):
    """
        Model for user profile
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    fullName = models.CharField(max_length=50)
    email = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=50, null=True)
    avatar = models.OneToOneField(ImageModel, on_delete=models.CASCADE, null=True)

    class Meta:
        name = 'accounts_profile'
        ordering = ['-id',]