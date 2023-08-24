# Generated by Django 4.2.1 on 2023-08-24 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selsapp', '0033_alter_calendar_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calendar_namelist',
            name='state_point',
        ),
        migrations.AddField(
            model_name='calendar_namelist',
            name='late_time',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='calendar_namelist',
            name='state',
            field=models.IntegerField(default=0),
        ),
    ]