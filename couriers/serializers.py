from rest_framework import serializers
from .models import Courier
from orders.models import Order


class CourierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Courier
        fields = ['id', 'name', 'phone_number', 'assigned_orders']


class AssignCourierSerializer(serializers.ModelSerializer):
    courier_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Order
        fields = ['id', 'status', 'courier_id']

        def update(self, instance, validated_data):
            courier = Courier.objects.get(id=validated_data['courier_id'])
            instance.courier = courier
            instance.save()
            courier.assigned_orders += 1
            courier.save()
            return instance
