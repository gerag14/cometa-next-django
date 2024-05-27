from django.db import models
from onlybeer.core.const import STATUS_CHOICES

from .base_model import BaseModel
from .order import Order


class Invoice(BaseModel):
    STATUS_CHOICES = STATUS_CHOICES

    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    invoice_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)

    def __str__(self):
        return f"Invoice {self.uuid} - {self.order.customer.name}"
