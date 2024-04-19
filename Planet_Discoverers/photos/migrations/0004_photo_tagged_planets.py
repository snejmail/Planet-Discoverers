# Generated by Django 4.2.2 on 2024-04-11 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planets', '0005_remove_planet_planet_picture_planet_photos'),
        ('photos', '0003_remove_photo_tagged_planets_alter_photo_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='tagged_planets',
            field=models.ManyToManyField(blank=True, to='planets.planet'),
        ),
    ]
