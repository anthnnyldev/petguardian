# Generated by Django 5.0.6 on 2024-06-30 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0004_report_latitude_report_location_report_longitude'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='location',
        ),
    ]
