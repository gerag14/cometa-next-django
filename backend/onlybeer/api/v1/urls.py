from django.urls import path

from .customers.customers_view import CustomerListCreateView
from .orders.orders_view import OrderListCreateView, OrderRetrieveUpdateView
from .products.products_view import ProductListCreateView

v1_urls = [
    path("customers/", CustomerListCreateView.as_view(), name="customer-list-create"),
    path("products/", ProductListCreateView.as_view(), name="product-list-create"),
    path("orders/", OrderListCreateView.as_view(), name="order-list-create"),
    path(
        "orders/<str:pk>/",
        OrderRetrieveUpdateView.as_view(),
        name="order-retrieve-update",
    ),
]
