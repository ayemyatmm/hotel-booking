# Generated by Django 3.1.7 on 2021-04-01 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0015_auto_20210401_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='username',
            field=models.CharField(max_length=100),
        ),
    ]
