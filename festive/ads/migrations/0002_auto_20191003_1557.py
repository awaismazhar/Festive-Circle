# Generated by Django 2.2.5 on 2019-10-03 15:57

import ads.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='images',
            options={'verbose_name': 'Image', 'verbose_name_plural': 'Images'},
        ),
        migrations.AlterField(
            model_name='detail',
            name='phoneNo',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(blank=True, default='model/def.jfif', height_field='height_field', null=True, upload_to=ads.models.upload_location, width_field='width_field'),
        ),
    ]