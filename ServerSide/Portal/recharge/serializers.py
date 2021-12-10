from rest_framework import serializers
from rest_framework.exceptions import NotAcceptable
from .models import PrimaryDistributor, Distributor, Retailer, Wallet, Recharge
from django.contrib.auth.models import User

'''
    All payments has to be managed yet.
'''


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'password']


class CreatePrimaryDistributorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = PrimaryDistributor
        fields = ['user', 'date_of_birth', 'mobile_number', 'primary_dis_price',
                  'image', 'created_at', 'updated_at']

    def create(self, validated_data):
        # payments are to be managed here.
        user = validated_data.pop('user')
        userinstance = User.objects.create(**user)
        Wallet.objects.create(user=userinstance)
        return PrimaryDistributor.objects.create(user=userinstance, **validated_data)

    def update(self, instance, validated_data):
        if validated_data.get('user') is None:
            return super().update(instance, validated_data)
        else:
            user = validated_data.pop('user')
            User.objects.filter(id=instance.user_id).update(**user)
            return super().update(instance, validated_data)


class RetrievePrimaryDistributorSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = PrimaryDistributor
        fields = ['id', 'user', 'date_of_birth', 'mobile_number', 'percentage', 'airtel_small_percentage', 'primary_dis_price',
                  'image', 'retailer_referral_code', 'distributor_referral_code', 'created_at', 'updated_at']

class CreateDistributorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Distributor
        fields = ['user', 'date_of_birth', 'mobile_number', 'referred_by',
                  'image', 'created_at', 'updated_at']

    def create(self, validated_data):
        # payments are to be managed here.
        user = validated_data.pop('user')
        userinstance = User.objects.create(**user)
        Wallet.objects.create(user=userinstance)
        referring_pd = validated_data.get('referred_by')
        if referring_pd is None:
            return Distributor.objects.create(user=userinstance, **validated_data, percentage=5, airtel_small_percentage=2.5)
        else:
            referring_primary_distributor = PrimaryDistributor.objects.get(
                id=referring_pd.id)
            return Distributor.objects.create(user=userinstance, **validated_data, percentage=referring_primary_distributor.percentage-0.75, airtel_small_percentage=referring_primary_distributor.airtel_small_percentage)

    def update(self, instance, validated_data):
        if validated_data.get('user') is None:
            return super().update(instance, validated_data)
        else:
            user = validated_data.pop('user')
            User.objects.filter(id=instance.user_id).update(**user)
            return super().update(instance, validated_data)


class RetrieveDistributorSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Distributor
        fields = ['user', 'date_of_birth', 'mobile_number', 'percentage', 'airtel_small_percentage', 'referred_by',
                  'image', 'retailer_referral_code', 'created_at', 'updated_at']


class CreateRetailerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Retailer
        fields = ['user', 'date_of_birth', 'mobile_number', 'referred_by_distributor', 'referred_by_primary_distributor',
                  'image', 'ret_price', 'created_at', 'updated_at']

    def create(self, validated_data):
        # payments has to be managed here.
        user = validated_data.pop('user')
        userinstance = User.objects.create(**user)
        Wallet.objects.create(user=userinstance)
        referring_primary_distributor = validated_data.get(
            'referred_by_primary_distributor')
        referring_distributor = validated_data.get('referred_by_distributor')
        if (referring_primary_distributor is None) and (referring_distributor is None):
            return Retailer.objects.create(user=userinstance, **validated_data, percentage=5, airtel_small_percentage=2.5)
        else:
            if (referring_primary_distributor is not None) and (referring_distributor is None):
                return Retailer.objects.create(user=userinstance, **validated_data, percentage=referring_primary_distributor.percentage - 1, airtel_small_percentage=referring_primary_distributor.airtel_small_percentage - 0.75)
            elif (referring_primary_distributor is None) and (referring_distributor is not None):
                return Retailer.objects.create(user=userinstance, **validated_data, percentage=referring_distributor.percentage - 1, airtel_small_percentage=referring_distributor.airtel_small_percentage - 0.75)
            else:
                raise NotAcceptable(
                    detail="You have provided two referral codes.")

    def update(self, instance, validated_data):
        if validated_data.get('user') is None:
            return super().update(instance, validated_data)
        else:
            user = validated_data.pop('user')
            User.objects.filter(id=instance.user_id).update(**user)
            return super().update(instance, validated_data)


class RetrieveRetailerSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    class Meta:
        model = Retailer
        fields = ['user', 'date_of_birth', 'mobile_number', 'percentage', 'airtel_small_percentage', 'referred_by_primary_distributor',
                  'referred_by_distributor', 'image', 'created_at', 'updated_at']


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['user', 'value', 'updated_at']

    def update(self, instance, validated_data):
        # payments has to be managed here.
        requested_added_money = float(validated_data['value'])
        instance.value = instance.value+requested_added_money
        instance.save()
        return instance


class WalletWithdrawSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['value', 'updated_at']

    def update(self, instance, validated_data):
        # payments has to be managed here.
        requested_added_money = float(validated_data['value'])
        if requested_added_money > instance.value:
            raise NotAcceptable(detail="You don't have enough value")
        instance.value = instance.value-requested_added_money
        instance.save()
        return instance


class ListDistributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distributor
        fields = ['user', 'image', 'percentage',
                  'airtel_small_percentage', 'created_at']
        read_only_fields = ['user', 'image']

    def update(self, instance, validated_data):
        if instance.referred_by is not None:
            if validated_data.get('percentage') is not None:
                if float(validated_data['percentage']) > instance.referred_by.percentage:
                    raise NotAcceptable(
                        detail="You can not assign percentage more than yours.")
            if validated_data.get('airtel_small_percentage') is not None:
                if float(validated_data['airtel_small_percentage']) > instance.referred_by.airtel_small_percentage:
                    raise NotAcceptable(
                        detail="You can not assign percentage more than yours.")
        return super().update(instance, validated_data)


class ListRetailerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retailer
        fields = ['user', 'image', 'percentage',
                  'airtel_small_percentage', 'created_at']

    def update(self, instance, validated_data):
        if instance.referred_by_primary_distributor is not None:
            if validated_data.get('percentage') is not None:
                if float(validated_data['percentage']) > instance.referred_by_primary_distributor.percentage:
                    raise NotAcceptable(
                        detail="You can not assign more percentage than yours")
            if validated_data.get('airtel_small_percentage') is not None:
                if float(validated_data['airtel_small_percentage']) > instance.referred_by_primary_distributor.airtel_small_percentage:
                    raise NotAcceptable(
                        detail="You can not assign more percentage than yours")
        if instance.referred_by_distributor is not None:
            if validated_data.get('percentage') is not None:
                if float(validated_data['percentage']) > instance.referred_by_distributor.percentage:
                    raise NotAcceptable(
                        detail="You can not assign more percentage than yours")
            if validated_data.get('airtel_small_percentage') is not None:
                if float(validated_data['airtel_small_percentage']) > instance.referred_by_distributor.airtel_small_percentage:
                    raise NotAcceptable(
                        detail="You can not assign more percentage than yours")
        return super().update(instance, validated_data)


class RechargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recharge
        fields = ['id', 'user', 'plan', 'created_at']

    def create(self, validated_data):
        user = validated_data['user']
        primary_distributor = PrimaryDistributor.objects.filter(
            user_id=user.id).first()
        distributor = Distributor.objects.filter(user_id=user.id).first()
        retailer = Retailer.objects.filter(user_id=user.id).first()
        wallet = Wallet.objects.filter(user_id=user.id).first()
        requestplan = validated_data['plan']
        if requestplan.plan > wallet.value:
            raise NotAcceptable(
                detail=f"Please add {wallet.value - requestplan.plan} to your wallet on http://127.0.0.1:8000/mywallet/{wallet.id}")
        if primary_distributor is not None:
            if (requestplan.network == "Airtel") and (requestplan.plan < 300):
                airtel_small_percentage = primary_distributor.airtel_small_percentage
                wallet_value = wallet.value - requestplan.plan + \
                    (requestplan.plan*airtel_small_percentage/100)
                Wallet.objects.filter(user_id=user.id).update(
                    value=wallet_value)
            else:
                percentage = primary_distributor.percentage
                wallet_value = wallet.value-requestplan.plan + \
                    (requestplan.plan*percentage/100)
                Wallet.objects.filter(user_id=user.id).update(
                    value=wallet_value)
        if distributor is not None:

            if (requestplan.network == "Airtel") and (requestplan.plan < 300):
                airtel_small_percentage = distributor.airtel_small_percentage
                wallet_value = wallet.value - requestplan.plan + \
                    (requestplan.plan*airtel_small_percentage/100)
                Wallet.objects.filter(user_id=user.id).update(
                    value=wallet_value)
                if distributor.referred_by is not None:
                    referring_airtel_small_percentage = distributor.referred_by.airtel_small_percentage
                    ref_wallet = Wallet.objects.get(
                        user_id=distributor.referred_by.user.id)
                    Wallet.objects.filter(user_id=distributor.referred_by.user.id).update(
                        value=ref_wallet.value + requestplan.plan*(referring_airtel_small_percentage-airtel_small_percentage)/100)
            else:
                percentage = distributor.percentage
                wallet_value = wallet.value - requestplan.plan + \
                    (requestplan.plan*percentage/100)
                Wallet.objects.filter(user_id=user.id).update(
                    value=wallet_value)
                if distributor.referred_by is not None:
                    referring_percentage = distributor.referred_by.percentage
                    ref_wallet = Wallet.objects.get(
                        user_id=distributor.referred_by.user.id)
                    Wallet.objects.filter(user_id=distributor.referred_by.user.id).update(
                        value=ref_wallet.value + requestplan.plan*(referring_percentage-percentage)/100)
        if retailer is not None:
            if (requestplan.network == "Airtel") and (requestplan.plan < 300):
                airtel_small_percentage = retailer.airtel_small_percentage
                wallet_value = wallet.value - requestplan.plan + \
                    (requestplan.plan*airtel_small_percentage/100)
                Wallet.objects.filter(user_id=user.id).update(
                    value=wallet_value)
                if retailer.referred_by_primary_distributor is not None:
                    referring_airtel_small_percentage = retailer.referred_by_primary_distributor.airtel_small_percentage
                    ref_wallet = Wallet.objects.get(
                        user_id=retailer.referred_by_primary_distributor.user.id)
                    Wallet.objects.filter(user_id=retailer.referred_by_primary_distributor.user.id).update(
                        value=ref_wallet.value + requestplan.plan*(referring_airtel_small_percentage-airtel_small_percentage)/100)
                if retailer.referred_by_distributor is not None:
                    referring_airtel_small_percentage = retailer.referred_by_distributor.airtel_small_percentage
                    dis_ref_wallet = Wallet.objects.get(
                        user_id=retailer.referred_by_distributor.user.id)
                    Wallet.objects.filter(user_id=retailer.referred_by_distributor.user.id).update(
                        value=dis_ref_wallet.value + requestplan.plan*(referring_airtel_small_percentage-airtel_small_percentage)/100)
                    if retailer.referred_by_distributor.referred_by is not None:
                        sup_referring_airtel_percentage = retailer.referred_by_distributor.referred_by.airtel_small_percentage
                        ref_wallet = Wallet.objects.get(
                            user_id=retailer.referred_by_distributor.referred_by.user.id)
                        Wallet.objects.filter(user_id=retailer.referred_by_distributor.referred_by.user.id).update(
                            value=ref_wallet.value + requestplan.plan*(sup_referring_airtel_percentage-referring_airtel_small_percentage)/100)
            else:
                percentage = retailer.percentage
                wallet_value = wallet.value - requestplan.plan + \
                    (requestplan.plan*percentage/100)
                Wallet.objects.filter(user_id=user.id).update(
                    value=wallet_value)
                if retailer.referred_by_primary_distributor is not None:
                    referring_percentage = retailer.referred_by_primary_distributor.percentage
                    ref_wallet = Wallet.objects.get(
                        user_id=retailer.referred_by_primary_distributor.user.id)
                    Wallet.objects.filter(user_id=retailer.referred_by_primary_distributor.user.id).update(
                        value=ref_wallet.value + requestplan.plan*(referring_percentage-percentage)/100)
                if retailer.referred_by_distributor is not None:
                    referring_percentage = retailer.referred_by_distributor.percentage
                    dis_ref_wallet = Wallet.objects.get(
                        user_id=retailer.referred_by_distributor.user.id)
                    Wallet.objects.filter(user_id=retailer.referred_by_distributor.user.id).update(
                        value=dis_ref_wallet.value + requestplan.plan*(referring_percentage-percentage)/100)
                    if retailer.referred_by_distributor.referred_by is not None:
                        sup_referring_percentage = retailer.referred_by_distributor.referred_by.percentage
                        ref_wallet = Wallet.objects.get(
                            user_id=retailer.referred_by_distributor.referred_by.user.id)
                        Wallet.objects.filter(user_id=retailer.referred_by_distributor.referred_by.user.id).update(
                            value=ref_wallet.value + requestplan.plan*(sup_referring_percentage-referring_percentage)/100)
        return Recharge.objects.create(user=user, plan=requestplan)
