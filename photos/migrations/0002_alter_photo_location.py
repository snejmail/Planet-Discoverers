# Generated by Django 4.2.2 on 2024-04-10 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='location',
            field=models.CharField(blank=True, help_text='Observatory location / telescope name', max_length=30, null=True),
        ),
    ]
