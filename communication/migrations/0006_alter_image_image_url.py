# Generated by Django 4.2.16 on 2024-11-25 17:13

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('communication', '0005_alter_image_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_url',
            field=cloudinary.models.CloudinaryField(default='', max_length=255, verbose_name='image'),
        ),
    ]
