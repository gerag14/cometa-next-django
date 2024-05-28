from django.core.exceptions import ValidationError
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
        if self.quantity and self.price:
            return self.quantity * self.price
        else:
            return 0

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    class Meta:
        unique_together = ("order", "product")

    def save(self, *args, **kwargs):
        self.price = self.product.price
        self.product.stock -= self.quantity
        if self.product.stock < 0:
            raise ValidationError("No hay suficiente stock disponible.")
        self.product.save()
        super().save(*args, **kwargs)
