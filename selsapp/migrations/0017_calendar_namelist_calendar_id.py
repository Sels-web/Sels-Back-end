# Generated by Django 4.2.1 on 2023-07-01 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selsapp', '0016_remove_calendar_enternames_calendar_name_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendar_namelist',
            name='calendar_id',
            field=models.CharField(default='', max_length=100),
        ),
    ]
