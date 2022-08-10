# Generated by Django 4.0.6 on 2022-08-09 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0004_alter_tracks_track_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='tour',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
