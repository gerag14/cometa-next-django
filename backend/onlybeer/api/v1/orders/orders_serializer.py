from onlybeer.core.models import Order, OrderDetail
from rest_framework import serializers


class OrderDetailSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source="product.name")
    total = serializers.ReadOnlyField()

    class Meta:
        model = OrderDetail
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    customer_email = serializers.ReadOnlyField(source="customer.email")
    total = serializers.ReadOnlyField()
    items = OrderDetailSerializer(many=True, required=True)

    class Meta:
        model = Order
        fields = "__all__"
