from django.urls import path
from .views import AssignCourierView, CourierListView

urlpatterns = [
    path('', CourierListView.as_view(), name='courier-list'),
    path('assign/<int:pk>', AssignCourierView.as_view(), name='couriers-assign'),
]
