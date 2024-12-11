from django.contrib import admin
from .models import Subscription


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'duration', 'start_date', 'end_date', 'status', 'price')
    list_display_links = ('id', 'user')  # Makes 'id' and 'user' clickable for editing
    list_filter = ('status', 'start_date', 'end_date')
    search_fields = ('user__email',)
