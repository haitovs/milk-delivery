# Generated by Django 5.1.3 on 2024-11-30 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_order_delivery_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
