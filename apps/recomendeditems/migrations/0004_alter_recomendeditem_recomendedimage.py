# Generated by Django 3.2.7 on 2022-02-23 04:32

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recomendeditems', '0003_auto_20220223_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recomendeditem',
            name='recomendedimage',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='recomendedimage'),
        ),
    ]