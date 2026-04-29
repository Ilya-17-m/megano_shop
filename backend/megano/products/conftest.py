import pytest
from rest_framework.test import APIClient

from products.models import (
    ProductModel,
    SpecificationsModel,
    TagsModel,
    ReviewModel
)


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def product(db):
    specifications = SpecificationsModel.objects.create(
        id=1,
        name='size',
        value='16x9',
    )
    tags = TagsModel.objects.create(
        name='tech',
    )

    return ProductModel.objects.create(
        title='laptop',
        price=56000,
        count=1,
        date='21.04.2026',
        description='great laptop',
        fullDescription='I like this laptop',
        freeDelivery=False,
        available=True,
        rating=4,
        specifications=specifications,
        tags=tags,
    )


@pytest.fixture
def tag(db):
    return TagsModel.objects.create(
        name='tech',
    )


@pytest.fixture
def review(db):
    return ReviewModel.objects.create(
        id=1,
        author='Ilya',
        email='user@gmail.ru',
        text='I like this product',
        rate=4,
        product=1,
    )