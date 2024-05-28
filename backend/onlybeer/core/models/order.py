from django.db import models
from onlybeer.core.const import STATUS_CHOICES

from .base_model import BaseModel
from .customer import Customer


class Order(BaseModel):
    STATUS_CHOICES = STATUS_CHOICES
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)

    @property
    def total(self):
        total = 0
        for item in self.items.all():
            total += item.total
        return total

    def __str__(self):
        return f"Order {self.uuid} - {self.customer.email}"
