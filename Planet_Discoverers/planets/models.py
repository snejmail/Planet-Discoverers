from django.core.exceptions import ValidationError

from Planet_Discoverers.users.models import User
from django.conf import settings
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.text import slugify


def default_planet_picture():
    return 'staticfiles/images/unknown_planet.jpg'


class Planet(models.Model):
    FINDING_METHODS = (
        ('Transit Method', 'Transit Method'),
        ('Radial Velocity Method', 'Radial Velocity Method (Doppler Method)'),
        ('Direct Imaging', 'Direct Imaging'),
        ('Microlensing', 'Microlensing'),
        ('Astrometry', 'Astrometry'),
        ('Pulsar Timing', 'Pulsar Timing'),
    )
    PLANET_TYPES = (
        ('Gas Giant', 'Gas Giant'),
        ('Super-Earth', 'Super-Earth'),
        ('Neptune-like', 'Neptune-like'),
        ('Terrestrial', 'Terrestrial'),
    )

    name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(3)],
        null=False,
        blank=False,
        unique=True,
    )
    type = models.CharField(
        choices=PLANET_TYPES,
        default='',
    )
    in_habitable_zone = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )
    mass = models.FloatField(
        default=1,
        help_text='(Mass of the planet compared to planet Earth (how many Earths is it?))'
    )
    description = models.TextField(
        null=False,
        blank=False,
        help_text="(Planet's characteristics, such as temperature, diameter, age, revolution, rotation, "
                  "interesting facts, etc)"
    )
    discoverer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    finding_method = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        choices=FINDING_METHODS,
    )
    primary_photo = models.ImageField(
        blank=True,
        null=True,
        upload_to='planet_images'
    )
    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
        editable=False,
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Photo(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    planet = models.ForeignKey(
        Planet,
        related_name='photos',
        on_delete=models.CASCADE,
        null=True,
    )
    image_upload = models.ImageField(
        upload_to='planet_images',
        default='',
    )
    description = models.TextField(
        max_length=300,
        validators=[MinLengthValidator(10),],
        blank=True,
        null=True,
    )
    location = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        help_text='Observatory location, only if finding method is Direct Imaging',
    )
    date_of_publication = models.DateField(
        auto_now=True,
    )


