# Generated by Django 5.1.3 on 2024-12-01 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='end_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('canceled', 'Canceled'), ('completed', 'Completed')], db_index=True, default='active', max_length=20),
        ),
    ]
