# Generated by Django 4.2.2 on 2024-05-21 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='planet',
            name='is_duplicate',
            field=models.BooleanField(default=False),
        ),
    ]