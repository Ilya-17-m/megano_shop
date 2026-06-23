from django.contrib.auth.models import User
from django.db import models


class ImageModel(models.Model):
    """
        Model for create avatar in profile
    """
    src = models.ImageField(upload_to='avatar')
    alt = models.CharField(max_length=255)

    class Meta:
        db_table = 'accounts_avatar'
        ordering = ['-id',]

    def __str__(self):
        return self.alt

    def __repr__(self):
        return f'<Image: alt={self.alt}>'


class ProfileModel(models.Model):
    """
        Model for user profile
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    fullName = models.CharField(max_length=50)
    email = models.EmailField(unique=True, null=False)
    phone = models.CharField(max_length=50, null=True)
    avatar = models.OneToOneField(ImageModel, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'accounts_profile'
        ordering = ['-id',]

    def __str__(self):
        return self.fullName

    def __repr__(self):
        return f'Profile: name={self.fullName}, email={self.email}, phone={self.phone}'