from rest_framework.response import Response
from rest_framework.views import APIView
from decimal import Decimal
from django.db.models import Q

from products.models import Product
from .serializers import ProductShortSerializer


class CatalogView(APIView):
    """
        View для фильтрации товаров в каталоге
    """

    def get(self, request, *args, **kwargs)  -> Response:
        data = request.query_params
        queryset_filters = Q()

        name:str = data.get('filter[name]', '').strip()
        min_price:int = data.get('filter[minPrice]')
        max_price:int = data.get('filter[maxPrice]')
        free_delivery:bool = data.get('filter[freeDelivery]')
        available:bool = data.get('filter[available]')
        tags:str = data.getlist('tags[]')

        if name:
            queryset_filters &= Q(title__icontains=name)

        if min_price is not None:
            queryset_filters &= Q(price__gte=Decimal(min_price))

        if max_price is not None:
            queryset_filters &= Q(price__lte=Decimal(max_price))

        if free_delivery in ('true', 'false'):
            queryset_filters &= Q(freeDelivery=free_delivery == 'true')

        if available == 'true':
            queryset_filters &= Q(count__gt=0)

        if tags:
            queryset_filters &= Q(tags__id__in=tags)

        queryset = Product.objects.filter(queryset_filters)

        sort = data.get('sort')
        sort_type = data.get('sortType')
        if sort:
            if sort_type == 'dec':
                sort = f'-{sort}'
            queryset = queryset.order_by(sort)

        page:int = int(data.get('currentPage', 1))
        limit:int = int(data.get('limit', 20))
        offset:int = (page - 1) * limit
        queryset = queryset[offset:offset + limit]

        serializer = ProductShortSerializer(queryset, many=True)
        return Response({
            'items':serializer.data,
            'currentPage': page,
            'lastPage': 1,
        })