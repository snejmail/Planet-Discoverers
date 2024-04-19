from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

from Planet_Discoverers.photos.validators import validate_file_size
from Planet_Discoverers.planets.models import Planet
from Planet_Discoverers.users.models import User


class Photo(models.Model):
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
    planet = models.ForeignKey(
        Planet,
        related_name='planet_photos',
        on_delete=models.CASCADE,
        null=True,
    )

    # def clean(self):
    #     super().clean()
    #     if self.planet.finding_method == 'Direct Imaging' and not self.location:
    #         raise ValidationError("Location must be provided for photos of planets found through direct imaging.")
    #
