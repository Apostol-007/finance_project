# Generated by Django 5.0.6 on 2024-07-12 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0003_rename_timestamp_cost_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cost',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='revenue',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
