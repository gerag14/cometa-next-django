from onlybeer.core.models import Customer
from rest_framework import serializers


class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"
