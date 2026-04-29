import pytest
from rest_framework.test import APIClient

from products.models import (
    ProductModel,
    SpecificationsModel,
    TagsModel,
    ReviewModel,
    SubcategoriesModel,
    CategoriesModel,
    ImagesModel
)


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def image(db):
    return ImagesModel.objects.create(
        id=1,
        alt='image',
    )


@pytest.fixture
def specification(db):
    return SpecificationsModel.objects.create(
        id=1,
        name='size',
        value='16x9',
    )


@pytest.fixture
def tag(db):
    return TagsModel.objects.create(
        id=1,
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
    )

@pytest.fixture
def subcategories(db):
    return SubcategoriesModel.objects.create(
        id=1,
        title='laptop',
    )


@pytest.fixture
def categories(db):
    return CategoriesModel.objects.create(
        id=1,
        title='tech',
    )


@pytest.fixture
def product(db):
    return ProductModel.objects.create(
        title='MacBook',
        price=2000,
        count=1,
        category=0,
        date='24.04.2026',
        description='great',
        fullDescription='I like this product',
        freeDelivery=True,
        available=True,
        rating=3,
        popular_version=True,
        limited_version=True,
        salePrice=0,
        dateForm='24.04.2026',
        dateTo='24.04.2026',
    )


@pytest.fixture
def product_rel_with_tables(product, tag, specification, image):
    product.tags.set([tag])
    product.specifications.set([specification])
    product.images.set([image])


@pytest.fixture
def categories_rel_with_tables(categories, subcategories):
    categories.subcategories.set([subcategories])


@pytest.fixture
def review_rel_with_taels(review, product):
    review.product.set([product])