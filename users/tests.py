from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User


class UserTests(APITestCase):

    def test_user_registration(self):
        url = "/api/auth/register/"
        data = {"email": "testuser@example.com", "password": "password123", "name": "Test User", "phone_number": "1234567890", "address": "Test Address"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)

    def test_user_login(self):
        # Create a user
        user = User.objects.create_user(email="testuser@example.com", password="password123", name="Test User")

        # Attempt login
        url = "/api/auth/login/"
        data = {"email": "testuser@example.com", "password": "password123"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
