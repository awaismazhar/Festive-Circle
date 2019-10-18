# Generated by Django 2.1.8 on 2019-10-18 15:40

import ads.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('phoneNo', models.CharField(max_length=20)),
                ('postDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('featured', models.BooleanField(default=False)),
                ('description', models.TextField()),
                ('rating', models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default=3)),
                ('views', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Detail',
                'verbose_name_plural': 'Details',
            },
        ),
        migrations.CreateModel(
            name='Dish_Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Dish Menu',
                'verbose_name_plural': 'Dish Menus',
            },
        ),
        migrations.CreateModel(
            name='images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, default='model/def.jfif', height_field='height_field', null=True, upload_to=ads.models.upload_location, width_field='width_field')),
                ('height_field', models.IntegerField(default=800)),
                ('width_field', models.IntegerField(default=700)),
                ('detail_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.Detail', verbose_name='Detail')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('latitude', models.CharField(max_length=100)),
                ('longitude', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Location',
                'verbose_name_plural': 'Locations',
            },
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sitting_capacity', models.IntegerField()),
                ('category', models.IntegerField(choices=[(1, 'Banquet Hall'), (2, 'Marquee'), (3, 'Hotel Hall'), (4, 'Farmhouse'), (5, 'Lawn')], default=1)),
                ('parking_capacity', models.IntegerField()),
                ('air_conditioner', models.BooleanField(default=False)),
                ('heater', models.BooleanField(default=False)),
                ('dj_system', models.BooleanField(default=False)),
                ('wifi', models.BooleanField(default=False)),
                ('bridal_room', models.BooleanField(default=False)),
                ('valet_parking', models.BooleanField(default=False)),
                ('decoration', models.BooleanField(default=False)),
                ('generator', models.BooleanField(default=False)),
                ('outside_catering', models.BooleanField(default=False)),
                ('outside_dj', models.BooleanField(default=False)),
                ('outside_decoration', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('detail_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.Detail', verbose_name='Detail')),
            ],
            options={
                'verbose_name': 'Venue',
                'verbose_name_plural': 'Venues',
            },
        ),
        migrations.CreateModel(
            name='VenuePrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('per_guest', models.IntegerField()),
                ('air_conditioner', models.IntegerField()),
                ('heater', models.IntegerField()),
                ('dj_system', models.IntegerField()),
                ('decoration', models.IntegerField()),
                ('venue_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.Venue', verbose_name='Venue')),
            ],
            options={
                'verbose_name': 'Venue Price',
                'verbose_name_plural': 'Venue Prices',
            },
        ),
        migrations.AddField(
            model_name='dish_menu',
            name='venue_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.Venue', verbose_name='Venue'),
        ),
        migrations.AddField(
            model_name='detail',
            name='loction_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.Location', verbose_name='Location'),
        ),
    ]
