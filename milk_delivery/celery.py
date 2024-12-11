from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
import crontab as crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'milk_delivery.settings')

app = Celery('milk_delivery')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Look for task modules in Django apps.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'mark-overdue-orders': {
        'task': 'orders.tasks.mark_overdue_orders_as_failed',
        'schedule': crontab(hour=0, minute=0),  # Runs daily at midnight
    },
}
