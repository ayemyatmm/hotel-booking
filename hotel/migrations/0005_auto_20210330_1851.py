# Generated by Django 3.1.7 on 2021-03-30 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0004_restaurants'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='booking',
        ),
        migrations.AddField(
            model_name='booking',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hotel.room'),
        ),
    ]
