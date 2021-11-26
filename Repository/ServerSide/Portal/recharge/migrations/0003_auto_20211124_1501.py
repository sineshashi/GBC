# Generated by Django 3.2.9 on 2021-11-24 09:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import recharge.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recharge', '0002_auto_20211124_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distributor',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='distributor', to=settings.AUTH_USER_MODEL, validators=[recharge.models.validate_distributor]),
        ),
        migrations.AlterField(
            model_name='primarydistributor',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='primary_distributor', to=settings.AUTH_USER_MODEL, validators=[recharge.models.validate_primarydistributor]),
        ),
    ]
