import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient


@pytest.fixture
def client(db):
    return APIClient()


@pytest.fixture
def user(db):
    return User.objects.create(
        id=1,
        username='people',
        first_name='Ilya',
        last_name='M',
    )


@pytest.fixture
def auth_client(client, user):
    client.force_authenticate(user=user)
    return client