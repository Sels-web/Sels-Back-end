# Generated by Django 4.2.1 on 2023-08-24 15:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('selsapp', '0028_alter_reference_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reference',
            name='upload_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
