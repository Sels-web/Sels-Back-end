# Generated by Django 4.2.1 on 2023-08-11 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selsapp', '0020_alter_reference_options_alter_reference_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='reference',
            name='content',
            field=models.TextField(default='', max_length=5000),
        ),
    ]