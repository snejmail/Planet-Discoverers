# Generated by Django 4.2.2 on 2024-04-12 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0007_alter_photo_photo_alter_photo_planet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='photo',
        ),
    ]