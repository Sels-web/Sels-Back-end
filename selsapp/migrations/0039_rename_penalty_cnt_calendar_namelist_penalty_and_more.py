# Generated by Django 4.2.1 on 2023-08-25 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('selsapp', '0038_rename_penalty_point_calendar_namelist_penalty_cnt'),
    ]

    operations = [
        migrations.RenameField(
            model_name='calendar_namelist',
            old_name='penalty_cnt',
            new_name='penalty',
        ),
        migrations.RenameField(
            model_name='selslist',
            old_name='penalty_point_cnt',
            new_name='penalty_cnt',
        ),
    ]
