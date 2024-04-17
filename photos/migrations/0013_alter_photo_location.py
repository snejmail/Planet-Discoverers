# Generated by Django 4.2.2 on 2024-04-12 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0012_photo_image_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='location',
            field=models.CharField(blank=True, help_text='Observatory location', max_length=30, null=True),
        ),
    ]
