from onlybeer.core.models import Order
from onlybeer.core.services import OrderService
from rest_framework import generics, status
from rest_framework.response import Response

from .orders_serializer import OrderSerializer


class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = OrderService()
        service.create_order(serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class OrderRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        service = OrderService(order=instance)
        service.update_order(serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_200_OK)
