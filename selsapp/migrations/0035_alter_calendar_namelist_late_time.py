# Generated by Django 4.2.1 on 2023-08-24 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selsapp', '0034_remove_calendar_namelist_state_point_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar_namelist',
            name='late_time',
            field=models.DateTimeField(default=''),
        ),
    ]