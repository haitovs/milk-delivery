from django.contrib import admin
from .models import Courier


@admin.register(Courier)
class CourierAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_number', 'assigned_orders')
    list_display_links = ('id', 'name')  # Makes 'id' and 'name' clickable
    search_fields = ('name', 'phone_number')
