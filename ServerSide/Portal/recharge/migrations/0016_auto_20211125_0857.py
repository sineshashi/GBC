# Generated by Django 3.2.9 on 2021-11-25 03:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recharge', '0015_auto_20211124_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distributor',
            name='airtel_small_percentage',
            field=models.FloatField(validators=[django.core.validators.MaxValueValidator(3), django.core.validators.MinValueValidator(1.5)]),
        ),
        migrations.AlterField(
            model_name='distributor',
            name='percentage',
            field=models.FloatField(validators=[django.core.validators.MaxValueValidator(6), django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='distributor',
            name='retailer_referral_code',
            field=models.CharField(default='9874a83e', max_length=8, unique=True),
        ),
        migrations.AlterField(
            model_name='primarydistributor',
            name='distributor_referral_code',
            field=models.CharField(default='6378ba2', max_length=7, unique=True),
        ),
        migrations.AlterField(
            model_name='primarydistributor',
            name='retailer_referral_code',
            field=models.CharField(default='68958484', max_length=8, unique=True),
        ),
        migrations.AlterField(
            model_name='retailer',
            name='airtel_small_percentage',
            field=models.FloatField(validators=[django.core.validators.MaxValueValidator(3), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='retailer',
            name='percentage',
            field=models.FloatField(validators=[django.core.validators.MaxValueValidator(6), django.core.validators.MinValueValidator(2)]),
        ),
    ]
