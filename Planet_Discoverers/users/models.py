from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models


class User(AbstractUser):
    pass
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
    profile_picture = models.ImageField(
        null=True,
        blank=True,
    )
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'auth_user'


# User._meta.get_field('groups').remote_field.related_name = 'user_groups'
# User._meta.get_field('user_permissions').remote_field.related_name = 'user_permissions_set'
