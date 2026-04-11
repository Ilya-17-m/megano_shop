import logging
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import OrderModel
from .serializer import OrderSerializer, OrderDetailSerializer
from basket.models import Basket


logger = logging.getLogger(__name__)


class OrdersAPIView(APIView):
    """
        View история заказов пользователя
    """
    permission_classes = [IsAuthenticated]

    def get(self, request) -> Response:
        if request.user.is_authenticated:
            order = OrderModel.objects.defer('user').filter(user=request.user)
            serializer = OrderSerializer(order, many=True)
            return Response(serializer.data ,status=200)

        logger.warning('User is not authenticated!')
        return Response({'error' : 'User is not authenticated!'}, 400)


    def post(self, request):
        products = request.data

        if not isinstance(products, list):
            return Response(
                {'error': 'Expected list of products'},
                status=400
            )

        product_ids = [product['id'] for product in products if 'id' in product]

        if not product_ids:
            return Response(
                {'error': 'No product IDs provided'},
                status=400
            )

        order = OrderModel.objects.create(
            user=request.user,
            profile=request.user.profile,
            status='В пути',
            totalCost=0,
        )

        order.products.set(product_ids)

        return Response({'orderId': order.id}, status=201)


class OrderAPIView(APIView):
    """
        View для отоюражения деталей определённого заказа пользователя
        ------------------------------------
    """
    permission_classes = [IsAuthenticated]


    def post(self, request, pk) -> Response:

        order = get_object_or_404(OrderModel, pk=pk)
        serializer = OrderDetailSerializer(
            order,
            data=request.data,
            partial=True,
        )

        if serializer.is_valid():
            serializer.save()
            basket = get_object_or_404(Basket, user=request.user)
            basket.delete()
            logger.info('The user has placed an order.')
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request, pk) -> Response:
        order =  get_object_or_404(OrderModel, pk=pk, user=request.user)
        serializer = OrderSerializer(order)
        return Response(serializer.data)


class PaymentAPIView(APIView):
    """
        View для оплаты заказа
    """
    permission_classes = [IsAuthenticated]


    def post(self, request) -> Response:
        return Response({
            'number' : request.data.get('number'),
            'name' : request.data.get('name'),
            'month' : request.data.get('month'),
            'year' : request.data.get('year'),
            'code' : request.data.det('code')
        }, status=200)