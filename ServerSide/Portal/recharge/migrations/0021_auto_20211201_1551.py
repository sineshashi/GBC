# Generated by Django 3.2.9 on 2021-12-01 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recharge', '0020_auto_20211129_0907'),
    ]

    operations = [
        migrations.AddField(
            model_name='couponcode',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='couponcode',
            name='coupon_code',
            field=models.CharField(default='cd3caf29a1', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='distributor',
            name='retailer_referral_code',
            field=models.CharField(default='c0eefce6', max_length=8, unique=True),
        ),
        migrations.AlterField(
            model_name='primarydistributor',
            name='distributor_referral_code',
            field=models.CharField(default='e8997ee', max_length=7, unique=True),
        ),
        migrations.AlterField(
            model_name='primarydistributor',
            name='retailer_referral_code',
            field=models.CharField(default='8cab796f', max_length=8, unique=True),
        ),
    ]
