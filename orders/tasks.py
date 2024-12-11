from celery import shared_task
from datetime import date
from subscriptions.models import Subscription
from .models import Order


@shared_task
def generate_daily_orders():
    today = date.today()
    active_subscriptions = Subscription.objects.filter(
        status='active',
        start_date__lte=today,
        end_date__gte=today,
    )
    for subscription in active_subscriptions:
        Order.objects.get_or_create(
            subscription=subscription,
            delivery_date=today,
            defaults={'status': 'pending'},
        )


@shared_task
def mark_overdue_orders_as_failed():
    overdue_orders = Order.objects.filter(delivery_date__lt=date.today(), status='pending')
    for order in overdue_orders:
        order.update_status('failed')
