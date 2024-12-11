from django.db import models
from users.models import User
from django.core.exceptions import ValidationError


# Create your models here.
class Courier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='courier_profile', db_index=True)
    name = models.CharField(max_length=255, db_index=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    assigned_orders = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if Courier.objects.filter(user=self.user).exists() and not self.pk:
            raise ValidationError(f"User {self.user.email} already has a courier profile.")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
