# Generated by Django 3.1.7 on 2021-04-01 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0024_booking_diff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='diff',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='booking',
            name='guest',
            field=models.CharField(max_length=100),
        ),
    ]
