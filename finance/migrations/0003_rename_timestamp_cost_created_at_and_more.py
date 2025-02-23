# Generated by Django 5.0.6 on 2024-07-12 09:05

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0002_cost_timestamp_revenue_timestamp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cost',
            old_name='timestamp',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='revenue',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='revenue',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='cost',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='revenue',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
