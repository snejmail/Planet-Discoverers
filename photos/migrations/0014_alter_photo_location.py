# Generated by Django 4.2.2 on 2024-04-12 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0013_alter_photo_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='location',
            field=models.CharField(blank=True, help_text='Observatory location, only if finding method is Direct Imaging', max_length=30, null=True),
        ),
    ]
