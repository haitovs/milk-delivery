from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # Define the fields to display in the list view
    list_display = ('id', 'email', 'name', 'is_staff', 'is_active', 'created_at')
    list_display_links = ('email', 'name')  # Clickable fields for editing
    list_filter = ('is_staff', 'is_active', 'created_at')  # Add filters
    search_fields = ('email', 'name')  # Enable search by email or name
    ordering = ('-created_at',)  # Order by newest users first

    # Define fields for the edit form
    fieldsets = (
        (None, {
            'fields': ('email', 'password')
        }),
        ('Personal Info', {
            'fields': ('name', 'phone_number', 'address')
        }),
        ('Permissions', {
            'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')
        }),
        ('Important Dates', {
            'fields': ('last_login',)
        }),  # Removed 'created_at'
    )

    # Define fields for the add form
    add_fieldsets = ((None, {'classes': ('wide',), 'fields': ('email', 'password1', 'password2', 'name', 'is_staff', 'is_active')}),)
