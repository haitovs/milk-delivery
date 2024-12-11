from django.urls import path
from .views import OrderListView, UpdateOrderStatusView

urlpatterns = [
    path('', OrderListView.as_view(), name='orders-list'),
    path('<int:pk>/', UpdateOrderStatusView.as_view(), name='orders-update'),
    path('<int:pk>/status/', UpdateOrderStatusView.as_view(), name='update-order-status'),
]
