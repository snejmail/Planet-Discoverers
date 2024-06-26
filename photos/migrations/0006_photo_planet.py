# Generated by Django 4.2.2 on 2024-04-12 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planets', '0007_remove_planet_photos'),
        ('photos', '0005_remove_photo_tagged_planets'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='planet',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='planets.planet'),
        ),
    ]
