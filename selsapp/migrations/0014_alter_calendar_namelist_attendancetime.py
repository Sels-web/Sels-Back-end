# Generated by Django 4.2.1 on 2023-06-28 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selsapp', '0013_selslist_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar_namelist',
            name='attendanceTime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]