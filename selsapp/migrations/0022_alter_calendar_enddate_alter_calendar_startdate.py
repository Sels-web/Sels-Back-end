# Generated by Django 4.2.1 on 2023-08-21 19:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('selsapp', '0021_reference_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar',
            name='endDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='startDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
