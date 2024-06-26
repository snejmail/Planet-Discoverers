# Generated by Django 4.2.2 on 2024-04-10 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planets', '0002_remove_planet_size_planet_mass_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='planet',
            name='in_habitable_zone',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='planet',
            name='type',
            field=models.CharField(choices=[('Gas Giant', 'Gas Giant'), ('Super-Earth', 'Super-Earth'), ('Neptune-like', 'Neptune-like'), ('Terrestrial', 'Terrestrial')], default=''),
        ),
        migrations.AlterField(
            model_name='planet',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
    ]
