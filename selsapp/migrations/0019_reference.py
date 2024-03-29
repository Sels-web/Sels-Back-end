# Generated by Django 4.2.1 on 2023-08-11 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selsapp', '0018_remove_calendar_name_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('file_location', models.FileField(blank=True, upload_to='Uploaded Files/%y/%m/%d/')),
                ('upload_date', models.DateField(auto_now=True)),
            ],
        ),
    ]
