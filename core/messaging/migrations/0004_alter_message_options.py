# Generated by Django 5.0.6 on 2024-06-29 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0003_message_read'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-timestamp']},
        ),
    ]
