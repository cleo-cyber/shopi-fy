# Generated by Django 4.0.6 on 2022-08-09 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0005_alter_product_price_alter_tour_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='event_type',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
