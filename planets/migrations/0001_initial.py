# Generated by Django 4.2.2 on 2024-04-05 14:37

import Planet_Discoverers.planets.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, validators=[django.core.validators.MinLengthValidator(3)])),
                ('size', models.PositiveIntegerField(help_text='Size of the planet compared to planet Earth (how many Earths is it?)')),
                ('description', models.TextField(help_text="Planet's characteristics, such as temperature, mass, diameter, age, revolution, rotation, interesting facts, etc")),
                ('finding_method', models.CharField(choices=[('Transit Method', 'Transit Method'), ('Radial Velocity Method', 'Radial Velocity Method (Doppler Method)'), ('Direct Imaging', 'Direct Imaging'), ('Microlensing', 'Microlensing'), ('Astrometry', 'Astrometry'), ('Pulsar Timing', 'Pulsar Timing')], max_length=100)),
                ('planet_picture', models.ImageField(blank=True, default=Planet_Discoverers.planets.models.default_planet_picture, null=True, upload_to='planet_images/')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('discoverer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
