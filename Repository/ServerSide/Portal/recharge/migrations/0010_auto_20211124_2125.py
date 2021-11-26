# Generated by Django 3.2.9 on 2021-11-24 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recharge', '0009_auto_20211124_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distributor',
            name='retailer_referral_code',
            field=models.CharField(default='c786e150', max_length=8, unique=True),
        ),
        migrations.AlterField(
            model_name='primarydistributor',
            name='distributor_referral_code',
            field=models.CharField(default='ae438dd', max_length=7, unique=True),
        ),
        migrations.AlterField(
            model_name='primarydistributor',
            name='retailer_referral_code',
            field=models.CharField(default='cf5724d8', max_length=8, unique=True),
        ),
    ]
