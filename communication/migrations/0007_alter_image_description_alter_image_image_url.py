# Generated by Django 4.2.16 on 2024-12-13 20:53

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communication', '0006_alter_image_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_url',
            field=cloudinary.models.CloudinaryField(default='placeholder_irkbnr', max_length=255, verbose_name='image'),
        ),
    ]
