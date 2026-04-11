from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import CategoriesModel, TagsModel, ProductModel, ReviewModel
from .serializers import (
        TagsSerializer,
        CategoriesSerializer,
        ProductFullSerializer,
        BannersSerializer,
        ReviewSerializer,
        SaleSerializer,
    )


@method_decorator(cache_page(60 * 3), name='dispatch')
class BannersListView(ListAPIView):
    """
        View для показа баннеров продукта на главную страницу
    """
    queryset = (ProductModel.objects
                .only('category', 'price', 'count', 'date', 'title', 'description', 'freeDelivery', 'rating')
                .prefetch_related('images', 'tags', 'reviews')
                )
    serializer_class = BannersSerializer


@method_decorator(cache_page(60 * 3), name='dispatch')
class ProductPopularListView(ListAPIView):
    """
        View для показа популярных продуктов на главной странице
    """
    queryset =  (ProductModel.objects
                 .only('category', 'price', 'count', 'date', 'title', 'description', 'freeDelivery', 'rating')
                 .prefetch_related('images', 'tags', 'reviews')
                 .filter(popular_version=True)
                 )
    serializer_class = ProductFullSerializer


@method_decorator(cache_page(60 * 3), name='dispatch')
class ProductLimitedListView(ListAPIView):
    """
        View для показа лимитированных продуктов на главной странице
    """
    queryset =  (ProductModel.objects
                 .only('category', 'price', 'count', 'date', 'title', 'description', 'freeDelivery', 'rating')
                 .prefetch_related('images', 'tags', 'reviews')
                 .filter(limited_version=True)
                 )
    serializer_class = ProductFullSerializer


@method_decorator(cache_page(60 * 3), name='dispatch')
class TagsListView(ListAPIView):
    """
        View для фильтрации по тегам в каталоге
    """
    queryset = TagsModel.objects.only('name')
    serializer_class = TagsSerializer


@method_decorator(cache_page(60 * 3), name='dispatch')
class CategoriesListView(ListAPIView):
    """
        View для фильтрации по категориям товаров
    """
    queryset = CategoriesModel.objects.only('title').prefetch_related('image', 'subcategories')
    serializer_class = CategoriesSerializer


class ProductDetailView(RetrieveAPIView):
    """
        View для показа деталей продукта
    """
    queryset = (ProductModel.objects
                .only('category', 'price', 'date', 'description',
                      'fullDescription', 'title', 'count','freeDelivery', 'rating')
                .prefetch_related('images', 'tags', 'reviews', 'specifications')
                )
    serializer_class = ProductFullSerializer


class ReviewCreateAPIView(APIView):
    """
        View для создания отзыва на продукт
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, pk) -> Response:
        product = get_object_or_404(ProductModel, id=pk)

        review = ReviewModel.objects.create(
            author=request.data.get('author'),
            email=request.data.get('email'),
            rate=request.data.get('rate'),
            text=request.data.get('text'),
            product=product,
        )

        serializer = ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SalesListView(APIView):
    """
        View для отображения товаров со скидкой
    """
    def get(self, request) -> Response:

        data = request.query_params
        page:int = int(data.get('currentPage', 1))
        queryset = ProductModel.objects.only('images', 'price', 'title', 'dateForm', 'dateTo', 'salePrice').filter(salePrice__gt=0)
        serializer = SaleSerializer(queryset, many=True)
        return Response({
            'items': serializer.data,
            'currentPage': page,
            'lastPage': 1,
        })