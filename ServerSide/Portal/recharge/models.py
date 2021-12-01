from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.aggregates import Min
from .utils import generate_ref_code, generate_ref_code1, generate_ref_code2
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_primarydistributor(value):
    if value in Distributor.objects.values_list('user_id', flat=True):
        raise ValidationError(
            _('%(value)s is already a distributor'),
            params={'value': value},
        )
    elif value in Retailer.objects.values_list('user_id', flat=True):
        raise ValidationError(
            _('%(value)s is already a retailer'),
            params={'value': value},
        )


def validate_distributor(value):
    if value in PrimaryDistributor.objects.values_list('user_id', flat=True):
        raise ValidationError(
            _('%(value)s is already a primary distributor'),
            params={'value': value},
        )
    elif value in Retailer.objects.values_list('user_id', flat=True):
        raise ValidationError(
            _('%(value)s is already a retailer'),
            params={'value': value},
        )


def validate_retailer(value):
    if value in Distributor.objects.values_list('user_id', flat=True):
        raise ValidationError(
            _('%(value)s is already a distributor'),
            params={'value': value},
        )
    elif value in PrimaryDistributor.objects.values_list('user_id', flat=True):
        raise ValidationError(
            _('%(value)s is already a primary distributor'),
            params={'value': value},
        )


def validate_pdmobile(value):
    if value in Distributor.objects.values_list('mobile_number', flat=True):
        raise ValidationError(
            _('%(value)s is already a distributor'),
            params={'value': value},
        )
    elif value in Retailer.objects.values_list('mobile_number', flat=True):
        raise ValidationError(
            _('%(value)s is already a retailer'),
            params={'value': value},
        )


def validate_dmobile(value):
    if value in PrimaryDistributor.objects.values_list('mobile_number', flat=True):
        raise ValidationError(
            _('%(value)s is already a primary distributor'),
            params={'value': value},
        )
    elif value in Retailer.objects.values_list('mobile_number', flat=True):
        raise ValidationError(
            _('%(value)s is already a retailer'),
            params={'value': value},
        )


def validate_rmobile(value):
    if value in Distributor.objects.values_list('mobile_number', flat=True):
        raise ValidationError(
            _('%(value)s is already a distributor'),
            params={'value': value},
        )
    elif value in PrimaryDistributor.objects.values_list('mobile_number', flat=True):
        raise ValidationError(
            _('%(value)s is already a primary distributor'),
            params={'value': value},
        )


class PrimaryDistributor(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='primary_distributor', validators=[validate_primarydistributor])
    date_of_birth = models.DateField()
    mobile_number = models.IntegerField(validators=[MaxValueValidator(
        9999999999), MinValueValidator(1000000000), validate_pdmobile], unique=True)
    percentage = models.FloatField(
        validators=[MaxValueValidator(6)], default=5)
    airtel_small_percentage = models.FloatField(
        validators=[MaxValueValidator(3)], default=2.5)
    image = models.ImageField(blank=True, null=True)
    distributor_referral_code = models.CharField(
        max_length=7, default=generate_ref_code(), unique=True)
    retailer_referral_code = models.CharField(
        max_length=8, default=generate_ref_code1(), unique=True)
    primary_dis_price = models.FloatField(default=199)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class Distributor(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='distributor', validators=[validate_distributor])
    date_of_birth = models.DateField()
    mobile_number = models.IntegerField(validators=[MaxValueValidator(
        9999999999), MinValueValidator(1000000000), validate_dmobile], unique=True)
    percentage = models.FloatField(
        validators=[MaxValueValidator(6), MinValueValidator(3)])
    airtel_small_percentage = models.FloatField(
        validators=[MaxValueValidator(3), MinValueValidator(1.5)])
    image = models.ImageField(blank=True, null=True)
    retailer_referral_code = models.CharField(
        max_length=8, default=generate_ref_code1(), unique=True)
    referred_by = models.ForeignKey(
        PrimaryDistributor, on_delete=models.CASCADE, blank=True, null=True)
    dis_price = models.FloatField(default=99)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class Retailer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='retailer', validators=[validate_retailer])
    date_of_birth = models.DateField()
    mobile_number = models.IntegerField(validators=[MaxValueValidator(
        9999999999), MinValueValidator(1000000000), validate_rmobile], unique=True)
    percentage = models.FloatField(
        validators=[MaxValueValidator(6), MinValueValidator(2)])
    airtel_small_percentage = models.FloatField(
        validators=[MaxValueValidator(3), MinValueValidator(1)])
    image = models.ImageField(blank=True, null=True)
    referred_by_primary_distributor = models.ForeignKey(
        PrimaryDistributor, on_delete=models.CASCADE, blank=True, null=True)
    referred_by_distributor = models.ForeignKey(
        Distributor, on_delete=models.CASCADE, blank=True, null=True)
    ret_price = models.FloatField(default=49)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class Wallet(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="gcbuser")
    value = models.FloatField(default=0, validators=[MinValueValidator(0)])
    updated_at = models.DateTimeField(auto_now_add=True)


Netwrok_choices = [
    ('Airtel', 'Airtel'),
    ('Jio', 'Jio'),
    ('VI', 'VI'),
    ('BSNL', 'BSNL')
]

Area_Choices = [
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Delhi', 'Delhi'),
    ('Haryana', 'Haryana'),
    ('Gujrat', 'Gujrat'),
    ('Himanchal Pradesh', 'Himanchal Pradesh'),
    ('Jammu & Kashmir', 'Jammu & Kashmir'),
    ('Karnataka', 'Karnataka'),
    ('Kerala', 'Kerala'),
    ('Kolkata', 'Kolkata'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Maharashtra', 'Maharashtra'),
    ('Mumbai Metro', 'Mumbai Metro'),
    ('Northeast', 'Northeast'),
    ('Orissa', 'Orissa'),
    ('Punjab', 'Punjab'),
    ('Rajasthan', 'Rajasthan'),
    ('Tamilnadu', 'Tamilnadu'),
    ('Uttar Pradesh East', 'Uttar Pradesh East'),
    ('Uttar Pradesh West', 'Uttar Pradesh West'),
    ('West Bengal', 'West Bengal')
]


class RechargePlan(models.Model):
    network = models.CharField(max_length=255, choices=Netwrok_choices)
    plan = models.IntegerField(validators=[MinValueValidator(0)])
    telecom_area = models.CharField(max_length=255, choices=Area_Choices)
    details = models.TextField(max_length=600)

    def __str__(self):
        return str(self.plan) + "  " + self.network + " " + str(self.telecom_area)


class Recharge(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recharging_user")
    plan = models.ForeignKey(
        RechargePlan, on_delete=models.CASCADE, related_name="recharge_plan")
    created_at = models.DateTimeField(auto_now_add=True)


class CouponCode(models.Model):
    coupon_code = models.CharField(
        max_length=255, unique=True, default=generate_ref_code2())
    primary_dis_price = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(199)], default=0)
    dis_price = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(99)], default=0)
    ret_price = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(49)], default=0)
    max_number_of_times = models.PositiveIntegerField()
    used_number_of_times = models.PositiveIntegerField(default=0)
    valid_till = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
