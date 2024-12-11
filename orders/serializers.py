from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['id', 'subscription', 'delivery_date', 'status', 'courier']
        read_only_fields = ['id', 'subscription', 'delivery_date']
