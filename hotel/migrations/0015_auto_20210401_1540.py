# Generated by Django 3.1.7 on 2021-04-01 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0014_booking_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='user',
            new_name='username',
        ),
    ]
