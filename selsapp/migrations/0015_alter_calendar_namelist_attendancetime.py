# Generated by Django 4.2.1 on 2023-06-28 09:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('selsapp', '0014_alter_calendar_namelist_attendancetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar_namelist',
            name='attendanceTime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
