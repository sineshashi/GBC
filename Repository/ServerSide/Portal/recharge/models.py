from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.aggregates import Min
from .utils import generate_ref_code, generate_ref_code1
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
    distributor_referral_code = models.CharField(max_length=7, default = generate_ref_code(), unique = True)
    retailer_referral_code = models.CharField(max_length=8, default = generate_ref_code1(), unique=True)
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
    percentage = models.FloatField(validators=[MaxValueValidator(6), MinValueValidator(3)])
    airtel_small_percentage = models.FloatField(
        validators=[MaxValueValidator(3), MinValueValidator(1.5)])
    image = models.ImageField(blank=True, null=True)
    retailer_referral_code = models.CharField(max_length=8, default = generate_ref_code1(), unique = True)
    referred_by = models.ForeignKey(
        PrimaryDistributor, on_delete=models.CASCADE, blank=True, null=True)
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
    percentage = models.FloatField(validators=[MaxValueValidator(6), MinValueValidator(2)])
    airtel_small_percentage = models.FloatField(
        validators=[MaxValueValidator(3), MinValueValidator(1)])
    image = models.ImageField(blank=True, null=True)
    referred_by_primary_distributor = models.ForeignKey(
        PrimaryDistributor, on_delete=models.CASCADE, blank=True, null=True)
    referred_by_distributor = models.ForeignKey(
        Distributor, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="gcbuser")
    value = models.FloatField(default=0, validators=[MinValueValidator(0)])
    updated_at = models.DateTimeField(auto_now_add=True)

    
