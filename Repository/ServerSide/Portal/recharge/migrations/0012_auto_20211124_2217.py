# Generated by Django 3.2.9 on 2021-11-24 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recharge', '0011_auto_20211124_2125'),
    ]

    operations = [
        migrations.RenameField(
            model_name='retailer',
            old_name='referred_by',
            new_name='referred_by_primary_distributor',
        ),
        migrations.AddField(
            model_name='retailer',
            name='referred_by_distributor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recharge.distributor'),
        ),
        migrations.AlterField(
            model_name='distributor',
            name='retailer_referral_code',
            field=models.CharField(default='009475b6', max_length=8, unique=True),
        ),
        migrations.AlterField(
            model_name='primarydistributor',
            name='distributor_referral_code',
            field=models.CharField(default='48e29de', max_length=7, unique=True),
        ),
        migrations.AlterField(
            model_name='primarydistributor',
            name='retailer_referral_code',
            field=models.CharField(default='2f4a741e', max_length=8, unique=True),
        ),
    ]
