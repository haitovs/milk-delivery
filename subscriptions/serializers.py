from rest_framework import serializers
from .models import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = ['id', 'user', 'duration', 'start_date', 'end_date', 'price', 'status']
        read_only_fields = ['start_date', 'end_date', 'user', 'status']

    def validate_duration(self, value):
        if value not in [3, 7, 30]:
            raise serializers.ValidationError("Invalid duration. Must be 3, 7, 30 days")
        return value

    def create(self, validate_data):
        validate_data['user'] = self.context['request'].user
        return super().create(validate_data)
