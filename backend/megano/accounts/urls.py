from django.urls import path

from .views import (
    ProfileView,
    UserLoginView,
    UserLogoutAPIView,
    UserRegisterView,
    ChangePasswordView,
    ChangeAvatarView
    )


app_name = 'accounts'


urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('sign-in', UserLoginView.as_view(), name='login'),
    path('sign-out', UserLogoutAPIView.as_view(), name='logout'),
    path('sign-up', UserRegisterView.as_view(), name='registration'),
    path('profile/password', ChangePasswordView.as_view(), name='change_password'),
    path('profile/avatar', ChangeAvatarView.as_view(), name='change_avatar'),
]