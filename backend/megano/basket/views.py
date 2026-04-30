import logging
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import BasketSerializer
from .models import BasketModel
from products.models import ProductModel


logger = logging.getLogger(__name__)


class BasketAPIView(APIView):
    """
        View для работы с корзиной
    """
    def get(self, request) -> Response:
        if request.user.is_authenticated:
            basket = BasketModel.objects.defer('user').filter(user=request.user)
            serializer = BasketSerializer(basket, many=True)

            if serializer.is_valid():
                logger.info('The user opened the shopping cart.')

                return Response(serializer.data, status=200)

            else:
                return Response({'message': 'Something went wrong...'})

        basket = request.session.get('basket', {})
        products = ProductModel.objects.filter(id__in=basket.keys())

        data = []
        for product in products:
            data.append({
                'id' : product.id,
                'title' : product.title,
                'price' : product.price,
                'count' : product.count,
            })
        return Response(data)


    def post(self, request) -> Response:
        product_id = request.data.get('id')
        product = get_object_or_404(ProductModel, id=product_id)
        if request.user.is_authenticated:
            basket = BasketModel.objects.create(
                user=request.user,
                product=product
            )
            serializer = BasketSerializer(basket)

            if serializer.is_valid():
                logger.info('The user added the product to the cart.')
                return Response(serializer.data, status=201)

            else:
                return Response({'message': 'Something went wrong...'})

        basket = request.session.get('basket', {})
        basket[product_id] = basket.get(product_id, 0) + 1
        request.session['basket'] = basket
        request.session.modified = True
        return Response(status=201)


    def delete(self, request) -> Response:
        product = request.data.get('id')
        if request.user.is_authenticated:
            basket = BasketModel.objects.get(
                user=request.user,
                product=product
            )

            if basket:
                basket.delete()
                logger.info('The user deleted the product from the shopping cart.')

                return Response(status=status.HTTP_204_NO_CONTENT)

            else:
                return Response({'message': 'Something went wrong...'})

        basket = request.session.get('basket', {})
        if product in basket:
            del basket[product]
            request.session['basket'] = basket
            request.session.modified = True
        return Response(status=204)