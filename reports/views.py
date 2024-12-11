from datetime import date
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from orders.models import Order
from subscriptions.models import Subscription
from django.db.models import Count  # Import Count here
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


# Create your views here.
@method_decorator(cache_page(60 * 60), name='dispatch')
class DailyDeliveryReportView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        today = date.today()
        deliveries = (
            Order.objects.filter(delivery_date=today, status='delivered').values('courier__name').annotate(total_deliveries=Count('id'))  # Use Count here
        )

        return Response({"date": today, "deliveries": list(deliveries)}, status=200)


class StatisticsReportView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Optimizing subscription-related queries with select_related
        total_subscriptions = Subscription.objects.count()
        active_subscriptions = Subscription.objects.filter(status='active').count()

        # Using select_related to optimize fetching related subscription data in orders
        total_orders = Order.objects.select_related('subscription').count()
        delivered_orders = Order.objects.select_related('subscription').filter(status='delivered').count()
        failed_orders = Order.objects.select_related('subscription').filter(status='failed').count()

        return Response(
            {
                "subscriptions": {
                    "total": total_subscriptions,
                    "active": active_subscriptions,
                },
                "orders": {
                    "total": total_orders,
                    "delivered": delivered_orders,
                    "failed": failed_orders,
                }
            },
            status=200)
