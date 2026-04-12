import json
import logging
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ProfileModel, ImageModel
from .serializers import ProfileSerializer


logger = logging.getLogger(__name__)


class UserLogoutAPIView(APIView):
    """
        View для выхода пользователя из системы
    """
    permission_classes = [IsAuthenticated]

    def post(self, request) -> Response:

        logout(request)
        logger.info('The user is logged out.')

        return Response({'message':'Вы вышли из системы!'})


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    """
        View для перехода в профиль пользователя
    """

    def post(self, request) -> Response:

        profile = get_object_or_404(ProfileModel, user=request.user)
        serializer = ProfileSerializer(
            profile,
            data=request.data,
            partial=True,
        )

        if serializer.is_valid():
            serializer.save()
            logger.info('The user changed the profile information.')
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request) -> Response:
        profile = get_object_or_404(ProfileModel, user=request.user)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)


class UserLoginView(APIView):
    """
        View для входа пользователя в систему
    """

    def post(self, request) -> Response:
        data = json.loads(request.body)

        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)

        if user is None:
            logger.info('User not found')
            return Response({
                'message': 'Invalid credentials'
            }, status=status.HTTP_400_BAD_REQUEST)

        logger.info('The user is logged in')
        login(request, user)

        return Response({
            'message': 'Ok'
        }, status=status.HTTP_200_OK)


class UserRegisterView(APIView):

    def post(self, request):
        data = json.loads(request.body)

        name = data.get("name")
        username = data.get("username")
        password = data.get("password")

        if not all([name, username, password]):
            return Response(
                {"error": "name, username and password are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if User.objects.filter(username=username).exists():
            return Response(
                {"error": "User already exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=name
        )

        ProfileModel.objects.create(
            user=user,
            fullName=name,
            email='',
            avatar=2,
            phone=''
        )

        login(request, user)

        return Response(status=status.HTTP_201_CREATED)


class ChangePasswordView(APIView):
    """
        View для изменения пароля пользователя
    """

    def post(self, request) -> Response:
        if not request.user.is_authenticated:
            return Response(
                {'error': 'Authentication required'},
                status=status.HTTP_401_UNAUTHORIZED
            )

        data = request.data

        old_password = None
        new_password = None

        if len(data) == 1:
            try:
                raw_key = list(data.keys())[0]
                parsed = json.loads(raw_key)

                old_password = parsed.get('currentPassword')
                new_password = parsed.get('newPassword')
            except (json.JSONDecodeError, IndexError):
                pass
        else:
            old_password = data.get('currentPassword')
            new_password = data.get('newPassword')

        if not old_password or not new_password:
            return Response(
                {'error': 'Not password'},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = request.user

        if not user.check_password(old_password):
            return Response(
                {'error': 'Old password is incorrect'},
                status=status.HTTP_400_BAD_REQUEST
            )

        user.set_password(new_password)
        user.save()

        update_session_auth_hash(request, user)

        return Response(status=status.HTTP_200_OK)


class ChangeAvatarView(APIView):
    """
        View для изменения аватара пользователя
    """
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request) -> Response:
        if not request.user.is_authenticated:
            return Response(
                {'error': 'Authentication required'},
                status=status.HTTP_401_UNAUTHORIZED
            )

        avatar_file = request.FILES.get('avatar')

        if not avatar_file:
            return Response(
                {'error': 'Avatar file is required'},
                status=status.HTTP_400_BAD_REQUEST
            )

        profile = get_object_or_404(ProfileModel, user=request.user)


        if profile.avatar:
            profile.avatar.delete()

        image = ImageModel.objects.create(
            src=avatar_file,
            alt=f"{profile.user.username} avatar"
        )

        profile.avatar = image
        profile.save()

        return Response(status=status.HTTP_200_OK)