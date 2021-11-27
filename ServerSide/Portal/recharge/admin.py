from django.contrib import admin
from .models import PrimaryDistributor, Distributor, Retailer, Wallet, Recharge, RechargePlan
# Register your models here.


@admin.register(PrimaryDistributor)
class PrimaryDistributorAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'user_id', 'date_of_birth', 'mobile_number', 'percentage', 'airtel_small_percentage',
                     'image', 'retailer_referral_code', 'distributor_referral_code', 'created_at', 'updated_at']

@admin.register(Distributor)
class DistributorAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'user_id', 'date_of_birth', 'mobile_number', 'percentage', 'airtel_small_percentage',
                    'referred_by', 'image', 'retailer_referral_code', 'created_at', 'updated_at']

@admin.register(Retailer)
class RetailerAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'user_id', 'date_of_birth', 'mobile_number', 'percentage', 'airtel_small_percentage',
                    'referred_by', 'image', 'created_at', 'updated_at']
    def referred_by(self, instance):
        if instance.referred_by_primary_distributor is not None:
            return instance.referred_by_primary_distributor
        elif instance.referred_by_distributor is not None:
            return instance.referred_by_distributor
        else:
            return None
@admin.register(Wallet)
class WalletSerializer(admin.ModelAdmin):
    list_display = ['id', 'user', 'value', 'updated_at']

@admin.register(RechargePlan)
class RechargePlanAdmin(admin.ModelAdmin):
    list_display = ['id', 'network', 'plan', 'telecom_area', 'details']

@admin.register(Recharge)
class RechargeAdmin(admin.ModelAdmin):
    list_display= ['id', 'user', 'plan', 'created_at']