from django.db import models

from .base_model import BaseModel
from .order import Order
from .product import Product


class OrderDetail(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def total(self):
        return self.quantity * self.price

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    class Meta:
        unique_together = ("order", "product")
