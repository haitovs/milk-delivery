from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Courier
from orders.models import Order
from .serializers import AssignCourierSerializer, CourierSerializer


# Create your views here.
class CourierListView(generics.ListAPIView):
    """
    Retrieve the list of couriers.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = CourierSerializer

    def get_queryset(self):
        return Courier.objects.all()


class AssignCourierView(generics.UpdateAPIView):
    """
    Assign a courier to an order and update their workload.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = AssignCourierSerializer

    def get_queryset(self):
        return Order.objects.filter(status='pending')

    def update(self, request, *args, **kwargs):
        order = self.get_object()
        courier_id = request.data.get('courier_id')

        try:
            courier = Courier.objects.get(id=courier_id)

            # Assign the courier to the order
            order.courier = courier
            order.save()

            # Update courier workload
            courier.assigned_orders += 1
            courier.save()

            return Response(
                {
                    "message": "Courier assigned successfully",
                    "order_id": order.id,
                    "courier_id": courier.id
                },
                status=status.HTTP_200_OK,
            )
        except Courier.DoesNotExist:
            return Response(
                {"error": "Courier not found"},
                status=status.HTTTP_404_NOT_FOUND,
            )
