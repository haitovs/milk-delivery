from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Subscription
from .serializers import SubscriptionSerializer


# Create your views here.
class SubscriptionListCreateView(generics.ListCreateAPIView):
    """
    GET: Retrieve all subscriptions for the logged-in user.
    POST: Create a new subscription
    """
    permission_classes = [IsAuthenticated]
    serializer_class = SubscriptionSerializer

    def get_queryset(self):
        return Subscription.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SubscriptionDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retrieve a specific subsciption.
    POST: Modify an existing subscription.
    DELETE: Cancel a subscription.
    """

    permission_classes = [IsAuthenticated]
    serializer_class = SubscriptionSerializer

    def get_queryset(self):
        return Subscription.objects.filter(user=self.request.user)


class UpdateSubscriptionStatusView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            subscription = Subscription.objects.get(pk=pk, user=request.user)
            action = request.data.get("action")

            if action == "cancel":
                refund = subscription.cancel_subscription()
                return Response({"message": "Subscription canceled", "refund": refund})
            elif action == "update_status":
                subscription.update_status()
                return Response({"message": f"Subscription updated to {subscription.status}"})
            else:
                return Response({"error": "Invalid action"}, status=400)
        except Subscription.DoesNotExist:
            return Response({"error": "Subscription not found"}, status=404)
