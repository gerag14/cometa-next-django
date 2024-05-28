from onlybeer.core.models import Product
from rest_framework import generics

from .products_serializer import ProductsSerializer


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer
