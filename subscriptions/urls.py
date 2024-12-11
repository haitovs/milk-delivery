from django.urls import path
from .views import SubscriptionListCreateView, SubscriptionDetailView, UpdateSubscriptionStatusView

urlpatterns = [
    path('', SubscriptionListCreateView.as_view(), name='subscription-list-create'),
    path('<int:pk>', SubscriptionDetailView.as_view(), name='subscription-detail'),
    path('<int:pk>/update/', UpdateSubscriptionStatusView.as_view(), name='update-subscription'),
]
