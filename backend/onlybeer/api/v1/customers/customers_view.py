from onlybeer.core.models import Customer
from rest_framework import generics

from .customers_serializer import CustomersSerializer


class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomersSerializer
