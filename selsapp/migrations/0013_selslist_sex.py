# Generated by Django 4.2.1 on 2023-06-27 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selsapp', '0012_selslist_accumulated_cost_selslist_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='selslist',
            name='sex',
            field=models.CharField(default='', max_length=50),
        ),
    ]
