from django.urls import path
from .views import DailyDeliveryReportView, StatisticsReportView

urlpatterns = [
    path('daily/', DailyDeliveryReportView.as_view(), name='daily-report'),
    path('statistics/', StatisticsReportView.as_view(), name='statistics-report'),
]
