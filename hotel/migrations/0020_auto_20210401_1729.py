# Generated by Django 3.1.7 on 2021-04-01 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0019_auto_20210401_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='diff',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
