# Generated by Django 3.2.9 on 2021-11-29 03:19

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('recharge', '0018_auto_20211128_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='couponcode',
            name='is_active',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='couponcode',
            name='max_number_of_times',
            field=models.PositiveIntegerField(default=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='couponcode',
            name='used_number_of_times',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='couponcode',
            name='valid_till',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='distributor',
            name='dis_price',
            field=models.FloatField(default=99),
        ),
        migrations.AddField(
            model_name='primarydistributor',
            name='primary_dis_price',
            field=models.FloatField(default=199),
        ),
        migrations.AddField(
            model_name='retailer',
            name='ret_price',
            field=models.FloatField(default=49),
        ),
        migrations.AlterField(
            model_name='couponcode',
            name='coupon_code',
            field=models.CharField(default='460369eecb', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='couponcode',
            name='dis_price',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99)]),
        ),
        migrations.AlterField(
            model_name='couponcode',
            name='primary_dis_price',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(199)]),
        ),
        migrations.AlterField(
            model_name='couponcode',
            name='ret_price',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(49)]),
        ),
        migrations.AlterField(
            model_name='distributor',
            name='retailer_referral_code',
            field=models.CharField(default='c0065692', max_length=8, unique=True),
        ),
        migrations.AlterField(
            model_name='primarydistributor',
            name='distributor_referral_code',
            field=models.CharField(default='48b6e95', max_length=7, unique=True),
        ),
        migrations.AlterField(
            model_name='primarydistributor',
            name='retailer_referral_code',
            field=models.CharField(default='431d4554', max_length=8, unique=True),
        ),
    ]
