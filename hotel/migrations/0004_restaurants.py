# Generated by Django 3.1.7 on 2021-03-30 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_auto_20210330_1214'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(default='defo', upload_to='images/')),
            ],
        ),
    ]
