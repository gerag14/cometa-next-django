from django.db import models
from onlybeer.core.const import STATUS_CHOICES

from .base_model import BaseModel
from .customer import Customer


class Order(BaseModel):
    STATUS_CHOICES = STATUS_CHOICES

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)

    def __str__(self):
        return f"Order {self.uuid} - {self.customer.email}"
