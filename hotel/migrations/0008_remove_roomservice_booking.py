# Generated by Django 3.1.7 on 2021-03-31 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0007_auto_20210331_1203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roomservice',
            name='booking',
        ),
    ]
