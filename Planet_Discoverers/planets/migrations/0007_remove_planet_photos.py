# Generated by Django 4.2.2 on 2024-04-12 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planets', '0006_remove_planet_photos_planet_photos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planet',
            name='photos',
        ),
    ]
