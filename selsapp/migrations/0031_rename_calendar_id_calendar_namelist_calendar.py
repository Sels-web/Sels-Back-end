# Generated by Django 4.2.1 on 2023-08-24 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('selsapp', '0030_alter_calendar_namelist_calendar_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='calendar_namelist',
            old_name='calendar_id',
            new_name='calendar',
        ),
    ]
