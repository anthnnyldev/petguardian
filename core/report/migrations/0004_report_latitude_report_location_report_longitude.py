# Generated by Django 5.0.6 on 2024-06-30 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0003_report_likes_alter_report_media_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
    ]
