from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'subscription', 'delivery_date', 'status', 'courier')
    list_display_links = ('id', 'subscription')  # Makes 'id' and 'subscription' clickable
    list_filter = ('status', 'delivery_date')
    search_fields = ('subscription__user__email',)
