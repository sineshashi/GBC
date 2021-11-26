from rest_framework import serializers
from rest_framework.exceptions import NotAcceptable
from .models import PrimaryDistributor, Distributor, Retailer, Wallet
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']


class CreatePrimaryDistributorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = PrimaryDistributor
        fields = ['user', 'date_of_birth', 'mobile_number',
                  'image', 'created_at', 'updated_at']

    def create(self, validated_data):
        user = validated_data.pop('user')
        userinstance = User.objects.create(**user)
        Wallet.objects.create(user=userinstance)
        return PrimaryDistributor.objects.create(user=userinstance, **validated_data)
    
    def update(self, instance, validated_data):
        if validated_data.get('user') is None:
            return super().update(instance, validated_data)
        else:
            user = validated_data.pop('user')
            User.objects.filter(id = instance.user_id).update(**user)
            return super().update(instance, validated_data)


class RetrievePrimaryDistributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrimaryDistributor
        fields = ['user', 'date_of_birth', 'mobile_number', 'percentage', 'airtel_small_percentage',
                  'image', 'retailer_referral_code', 'distributor_referral_code', 'created_at', 'updated_at']




class CreateDistributorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Distributor
        fields = ['user', 'date_of_birth', 'mobile_number', 'referred_by',
                  'image', 'created_at', 'updated_at']

    def create(self, validated_data):
        user = validated_data.pop('user')
        userinstance = User.objects.create(**user)
        Wallet.objects.create(user=userinstance)
        referring_pd = validated_data.get('referred_by')
        if referring_pd is None:
            return Distributor.objects.create(user=userinstance, **validated_data, percentage=5, airtel_small_percentage=2.5)
        else:
            referring_primary_distributor = PrimaryDistributor.objects.get(id= referring_pd.id)
            return Distributor.objects.create(user=userinstance, **validated_data, percentage = referring_primary_distributor.percentage-0.75, airtel_small_percentage=referring_primary_distributor.airtel_small_percentage)
    def update(self, instance, validated_data):
        if validated_data.get('user') is None:
            return super().update(instance, validated_data)
        else:
            user = validated_data.pop('user')
            User.objects.filter(id = instance.user_id).update(**user)
            return super().update(instance, validated_data)

class RetrieveDistributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distributor
        fields = ['user', 'date_of_birth', 'mobile_number', 'percentage', 'airtel_small_percentage', 'referred_by',
                  'image', 'retailer_referral_code', 'created_at', 'updated_at']


class CreateRetailerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Retailer
        fields = ['user', 'date_of_birth', 'mobile_number', 'referred_by_distributor', 'referred_by_primary_distributor',
                  'image', 'created_at', 'updated_at']

    def create(self, validated_data):
        user = validated_data.pop('user')
        userinstance = User.objects.create(**user)
        Wallet.objects.create(user=userinstance)
        referring_primary_distributor = validated_data.get('referred_by_primary_distributor')
        referring_distributor = validated_data.get('referred_by_distributor')
        if (referring_primary_distributor is None) and (referring_distributor is None):
            return Retailer.objects.create(user=userinstance, **validated_data, percentage=5, airtel_small_percentage=2.5)
        else:
            if (referring_primary_distributor is not None) and (referring_distributor is None):
                return Retailer.objects.create(user=userinstance, **validated_data, percentage=referring_primary_distributor.percentage - 1, airtel_small_percentage = referring_primary_distributor.airtel_small_percentage - 0.75)
            elif (referring_primary_distributor is None) and (referring_distributor is not None):
                return Retailer.objects.create(user=userinstance, **validated_data, percentage=referring_distributor.percentage - 1, airtel_small_percentage = referring_distributor.airtel_small_percentage - 0.75)
            else:
                raise NotAcceptable(detail="You have provided two referral codes.")
    def update(self, instance, validated_data):
        if validated_data.get('user') is None:
            return super().update(instance, validated_data)
        else:
            user = validated_data.pop('user')
            User.objects.filter(id = instance.user_id).update(**user)
            return super().update(instance, validated_data)


class RetrieveRetailerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retailer
        fields = ['user', 'date_of_birth', 'mobile_number', 'percentage', 'airtel_small_percentage', 'referred_by_primary_distributor',
                  'referred_by_distributor', 'image', 'created_at', 'updated_at']


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['user', 'value', 'updated_at']


class ListDistributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distributor
        fields = ['user', 'image', 'percentage', 'airtel_small_percentage', 'created_at']
        read_only_fields = ['user', 'image']

    def update(self, instance, validated_data):
        if instance.referred_by is not None:
            if validated_data.get('percentage') is not None:
                if float(validated_data['percentage']) > instance.referred_by.percentage:
                    raise NotAcceptable(detail="You can not assign percentage more than yours.")
            if validated_data.get('airtel_small_percentage') is not None:
                if float(validated_data['airtel_small_percentage']) > instance.referred_by.airtel_small_percentage:
                    raise NotAcceptable(detail="You can not assign percentage more than yours.")
        return super().update(instance, validated_data)

class ListRetailerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retailer
        fields = ['user', 'image', 'percentage', 'airtel_small_percentage', 'created_at']
    def update(self, instance, validated_data):
        if instance.referred_by_primary_distributor is not None:
            if validated_data.get('percentage')  is not None:
                if float(validated_data['percentage']) > instance.referred_by_primary_distributor.percentage:
                    raise NotAcceptable(detail="You can not assign more percentage than yours")
            if validated_data.get('airtel_small_percentage')  is not None:
                if float(validated_data['airtel_small_percentage']) > instance.referred_by_primary_distributor.airtel_small_percentage:
                    raise NotAcceptable(detail="You can not assign more percentage than yours")
        if instance.referred_by_distributor is not None:
            if validated_data.get('percentage')  is not None:
                if float(validated_data['percentage']) > instance.referred_by_distributor.percentage:
                    raise NotAcceptable(detail="You can not assign more percentage than yours")
            if validated_data.get('airtel_small_percentage')  is not None:
                if float(validated_data['airtel_small_percentage']) > instance.referred_by_distributor.airtel_small_percentage:
                    raise NotAcceptable(detail="You can not assign more percentage than yours")
        return super().update(instance, validated_data)