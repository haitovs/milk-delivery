from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer


# Create your views here.
class OrderListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

    def get_queryset(self):
        user = self.request.user

        # If the user is a courier, fetch orders assigned to the courier
        if hasattr(user, "courier_profile"):
            # Optimize query with select_related for related 'courier' data
            return Order.objects.select_related("courier", "subscription").filter(courier=user.courier_profile)

        # Otherwise, fetch orders based on the user's subscriptions
        return Order.objects.select_related("subscription").filter(subscription__user=user)


class UpdateOrderStatusView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

    def post(self, request, pk):
        try:
            # Ensure the user has a courier profile
            if not hasattr(request.user, "courier_profile"):
                return Response({"error": "User is not authorized to update this order."}, status=403)

            # Fetch the order with courier check
            order = Order.objects.select_related("courier").get(pk=pk, courier=request.user.courier_profile)

            # Validate the new status
            new_status = request.data.get("status")
            valid_statuses = dict(Order.STATUS_CHOICES)  # Convert choices to dictionary
            if new_status not in valid_statuses:
                return Response({"error": f"Invalid status. Valid statuses are: {', '.join(valid_statuses.values())}"}, status=400)

            # Update the order's status
            order.status = new_status
            order.save()

            return Response({"message": f"Order status updated to {order.status}"}, status=200)

        except Order.DoesNotExist:
            return Response({"error": "Order not found or unauthorized."}, status=404)

    # No need for get_queryset in this case.
