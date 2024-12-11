from datetime import datetime
from django.db import models
from subscriptions.models import Subscription
from couriers.models import Courier


class Order(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("delivered", "Delivered"),
        ("failed", "Failed"),
    ]

    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE, related_name="orders")
    delivery_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending", db_index=True)
    courier = models.ForeignKey(Courier, on_delete=models.SET_NULL, null=True, blank=True, related_name="orders", db_index=True)
    delivery_time = models.DateTimeField(null=True, blank=True, db_index=True)

    def update_status(self, new_status):
        if new_status in dict(self.STATUS_CHOICES):
            self.status = new_status
            self.delivery_time = datetime.now() if new_status == 'delivered' else None
            self.save()
        else:
            raise ValueError("Invalid status")

    def __str__(self):
        return f"Order {self.id} - {self.delivery_date} - {self.status}"
