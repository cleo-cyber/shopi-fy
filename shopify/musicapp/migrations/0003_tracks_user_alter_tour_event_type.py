# Generated by Django 4.0.6 on 2022-08-23 19:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0002_account_first_name_account_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='tracks',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tour',
            name='event_type',
            field=models.CharField(default='Performance', max_length=200),
        ),
    ]
