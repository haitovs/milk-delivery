from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Subscription
from orders.models import Order


@receiver(post_save, sender=Subscription)
def generate_orders(sender, instance, created, **kwargs):
    if created and instance.status == "active":
        from datetime import timedelta
        for day in range(instance.duration):
            delivery_date = instance.start_date + timedelta(days=day)
            Order.objects.create(
                subscription=instance,
                delivery_date=delivery_date,
                status="pending",
            )
