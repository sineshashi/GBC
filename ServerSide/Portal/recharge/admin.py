from django.contrib import admin
from .models import PrimaryDistributor, Distributor, Retailer, Wallet, Recharge, RechargePlan, CouponCode
from django.utils import timezone
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
    list_display = ['id', 'user', 'plan', 'created_at']


@admin.register(CouponCode)
class CouponCodeAdmin(admin.ModelAdmin):
    list_display = ['id', 'coupon_code', 'primary_dis_price', 'dis_price', 'ret_price',
                    'max_number_of_times', 'used_number_of_times', 'is_active_now', 'valid_till', 'created_at', 'updated_at']
    def is_active_now(self, instance):
        if instance.max_number_of_times == 0:
            instance.is_active = False
            instance.save()
            return False
        if instance.used_number_of_times == instance.max_number_of_times:
            instance.is_active = False
            instance.save()
            return False
        if instance.valid_till < timezone.now():
            instance.is_active = False
            instance.save()
            return False
        else:
            instance.is_active = True
            instance.save()
            return True
  