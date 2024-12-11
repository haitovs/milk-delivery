from rest_framework.test import APITestCase
from rest_framework import status
from subscriptions.models import Subscription
from users.models import User
from datetime import date


class SubscriptionTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(email="testuser@example.com", password="password123")
        self.client.login(username="testuser@example.com", password="password123")

    def test_create_subscription(self):
        url = "/api/subscriptions/"
        data = {"duration": 30, "start_date": "2024-11-30", "price": 100.00}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Subscription.objects.count(), 1)

    def test_cancel_subscription(self):
        subscription = Subscription.objects.create(user=self.user, duration=30, start_date=date.today(), end_date=date.today(), price=100.00, status="active")
        url = f"/api/subscriptions/{subscription.id}/update/"
        data = {"status": "canceled"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        subscription.refresh_from_db()
        self.assertEqual(subscription.status, "canceled")
