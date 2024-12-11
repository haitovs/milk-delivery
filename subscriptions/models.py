from decimal import Decimal
from django.db import models
from datetime import timedelta
from django.utils.timezone import now
from users.models import User
from datetime import date
# Create your models here.


class Subscription(models.Model):
    STATUS_CHOICES = [
        ("active", "Active"),
        ("canceled", "Canceled"),
        ("completed", "Completed"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="subscriptions", db_index=True)
    duration = models.PositiveIntegerField(choices=[(3, "3 Days"), (7, "7 Days"), (30, "30 Days")])
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(db_index=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="active", db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        if not self.start_date:
            self.start_date = now()  # Use the current time if start_date is not set
        if not self.end_date:
            self.end_date = self.start_date + timedelta(days=self.duration)
        super().save(*args, **kwargs)

    def update_status(self):
        if date.today() > self.end_date and self.status == 'active':
            self.status = 'completed'
            self.save()
        elif self.status == 'canceled':
            # No changes needed, already canceled
            pass

    def cancel_subscription(self):
        if self.status == 'active':
            days_used = Decimal((date.today() - self.start_date.date()).days)  # Convert days_used to Decimal
            days_total = Decimal((self.end_date.date() - self.start_date.date()).days)  # Convert days_total to Decimal
            refund_ratio = Decimal(1) - (days_used / days_total)  # Ensure the ratio is Decimal
            refund_amount = self.price * refund_ratio  # Multiply Decimal by Decimal

            # Process refund logic (mocked here)
            self.status = 'canceled'
            self.save()
            return refund_amount.quantize(Decimal("0.01"))  # Round to 2 decimal places
        return Decimal(0)

    def __str__(self):
        return f"Subscription {self.id} - {self.user.email}"
