from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models


class User(AbstractUser):
    username = models.CharField(
        max_length=150,
        validators=[MinLengthValidator(3)],
        blank=False,
        null=False,
        unique=True,
    )
    email = models.EmailField(
        unique=True
    )
    country = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )
    # password = models.CharField(
    #     max_length=150,
    #     validators=[MinLengthValidator(8)],
    #     blank=False,
    #     null=False,
    # )
    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


User._meta.get_field('groups').remote_field.related_name = 'user_groups'
User._meta.get_field('user_permissions').remote_field.related_name = 'user_permissions_set'
