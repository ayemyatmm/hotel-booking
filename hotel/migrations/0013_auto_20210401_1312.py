# Generated by Django 3.1.7 on 2021-04-01 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0012_auto_20210331_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='number_rooms',
            field=models.IntegerField(max_length=2),
        ),
        migrations.AlterField(
            model_name='room',
            name='price',
            field=models.IntegerField(max_length=100),
        ),
    ]
