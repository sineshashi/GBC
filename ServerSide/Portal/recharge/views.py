from django.shortcuts import render
from rest_framework import generics, serializers, status
from rest_framework.exceptions import NotAcceptable
from .models import CouponCode, PrimaryDistributor, Distributor, Recharge, Retailer, Wallet
from .serializers import (
    CreateDistributorSerializer, CreatePrimaryDistributorSerializer, CreateRetailerSerializer, RechargeSerializer,
    RetrieveDistributorSerializer, RetrieveRetailerSerializer, RetrievePrimaryDistributorSerializer,
    WalletSerializer, ListDistributorSerializer, ListRetailerSerializer, WalletWithdrawSerializer
)
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from .MyPermissionClasses import (IsPrimaryDistributor, IsDistributor, IsRetailer,
                                  IsPrimaryDistributorOrDistirbutor, IsAuthenticated, IsRetailerOrDistirbutor)


class CreatePrimaryDistrubutorView(generics.CreateAPIView):
    def create(self, request, *args, **kwargs):
        if len(request.data) == 0:
            raise NotAcceptable(detail="No data provided")
        if request.data.get('user') is None:
            raise NotAcceptable(detail="No user data provided")
        userdata = request.data.get('user')
        if userdata.get('first_name') is None:
            raise NotAcceptable(detail="First Name not Provided")
        if userdata.get('email') is None:
            raise NotAcceptable(detail="email not Provided")
        if userdata.get('username') is None:
            raise NotAcceptable(detail="username not Provided")
        if userdata.get('password') is None:
            raise NotAcceptable(detail="password not Provided")
        if len(str(request.data['user']['password'])) < 8:
            raise NotAcceptable(
                detail="Password must contain at least 8 character.")
        password = request.data['user']['password']
        if password.isdigit():
            raise NotAcceptable(detail="password must cantain alphabets.")
        for char in list(str(password)):
            try:
                int(char)
                bool = True
            except:
                bool = False
        if bool == True:
            raise NotAcceptable(
                detail="At least one numeric digit must be provided.")
        if userdata.get('confirm_password') is None:
            raise NotAcceptable(detail="confirm password not Provided")
        if request.data['user']['password'] != request.data['user']['confirm_password']:
            raise NotAcceptable(detail="Passwords did not match")
        else:
            if request.data.get('mobile_number') is None:
                raise NotAcceptable(detail="mobile number not Provided")
            if request.data.get('date_of_birth') is None:
                raise NotAcceptable(detail="date of birth not Provided")
            password = make_password(password)
            request.data['user']['password'] = password
            del request.data['user']['confirm_password']
            if request.data.get('coupon_code') is not None:
                if request.data.get('coupon_code') not in CouponCode.objects.values_list('coupon_code', flat=True):
                    raise NotAcceptable(
                        detail="Please enter a valid coupon code.")
                else:
                    coupon = CouponCode.objects.filter(
                        coupon_code=request.data.get('coupon_code')).first()
                    if coupon.is_active == False:
                        raise NotAcceptable(
                            detail="This coupon code has expired.")
                    else:
                        coupon_price = coupon.primary_dis_price
                        request.data['primary_dis_price'] = coupon_price
            else:
                request.data['primary_dis_price'] = 199
        return super().create(request, *args, **kwargs)
    queryset = PrimaryDistributor.objects.all()
    serializer_class = CreatePrimaryDistributorSerializer


class UpdatePrimaryDistributor(generics.UpdateAPIView):
    def update(self, request, *args, **kwargs):
        if kwargs.get('pk') is None:
            raise NotAcceptable(detail="No data provided for update.")
        kwargs['partial'] = True
        id = kwargs.get('pk')
        primary_distributor = PrimaryDistributor.objects.filter(id=id).first()
        if primary_distributor is None:
            raise NotAcceptable(detail="No such primary distributor exists")
        if self.request.user.id != primary_distributor.user_id:
            raise NotAcceptable(
                detail="You are not authorized for this action")
        return super().update(request, *args, **kwargs)
    queryset = PrimaryDistributor.objects.all()
    serializer_class = CreatePrimaryDistributorSerializer
    permission_classes = [IsPrimaryDistributor]


class RetrievePrimaryDistributorView(generics.RetrieveAPIView):
    def retrieve(self, request, *args, **kwargs):
        if kwargs.get('pk') is None:
            raise NotAcceptable(detail="No data provided for update.")
        kwargs['partial'] = True
        id = kwargs.get('pk')
        primary_distributor = PrimaryDistributor.objects.filter(id=id).first()
        if primary_distributor is None:
            raise NotAcceptable(detail="No such primary distributor exists")
        if self.request.user.id != primary_distributor.user_id:
            raise NotAcceptable(
                detail="You are not authorized for this action")
        return super().retrieve(request, *args, **kwargs)
    queryset = PrimaryDistributor.objects.all()
    serializer_class = RetrievePrimaryDistributorSerializer
    permission_classes = [IsPrimaryDistributor]


class CreateDistrubutorView(generics.CreateAPIView):
    def create(self, request, *args, **kwargs):
        if len(request.data) == 0:
            raise NotAcceptable(detail="No data provided")
        if request.data.get('user') is None:
            raise NotAcceptable(detail="No user data provided")
        userdata = request.data.get('user')
        if userdata.get('first_name') is None:
            raise NotAcceptable(detail="First Name not Provided")
        if userdata.get('email') is None:
            raise NotAcceptable(detail="email not Provided")
        if userdata.get('username') is None:
            raise NotAcceptable(detail="username not Provided")
        if userdata.get('password') is None:
            raise NotAcceptable(detail="password not Provided")
        if len(str(request.data['user']['password'])) < 8:
            raise NotAcceptable(
                detail="Password must contain at least 8 character.")
        password = request.data['user']['password']
        if password.isdigit():
            raise NotAcceptable(detail="password must cantain alphabets.")
        for char in list(str(password)):
            try:
                int(char)
                bool = True
            except:
                bool = False
        if bool == False:
            raise NotAcceptable(
                detail="At least one numeric digit must be provided.")
        if userdata.get('confirm_password') is None:
            raise NotAcceptable(detail="confirm password not Provided")
        if request.data['user']['password'] != request.data['user']['confirm_password']:
            raise NotAcceptable(detail="Passwords did not match")
        else:
            if request.data.get('mobile_number') is None:
                raise NotAcceptable(detail="mobile number not Provided")
            if request.data.get('date_of_birth') is None:
                raise NotAcceptable(detail="date of birth not Provided")
            password = make_password(password)
            request.data['user']['password'] = password
            del request.data['user']['confirm_password']
            if kwargs.get('ref_code') is not None:
                request.data['referral_code'] = kwargs.get('ref_code')
            if request.data.get('referral_code') is not None:
                referring_prime_dis = PrimaryDistributor.objects.filter(
                    distributor_referral_code=request.data['referral_code']).first()
                if referring_prime_dis is None:
                    raise NotAcceptable(
                        detail="Please provide right referral code")
                else:
                    request.data['referred_by'] = referring_prime_dis.id
            if request.data.get('coupon_code') is not None:
                if request.data.get('coupon_code') not in CouponCode.objects.values_list('coupon_code', flat=True):
                    raise NotAcceptable(
                        detail="Please enter a valid coupon code.")
                else:
                    coupon = CouponCode.objects.filter(
                        coupon_code=request.data.get('coupon_code')).first()
                    if coupon.is_active == False:
                        raise NotAcceptable(
                            detail="This coupon code has expired.")
                    else:
                        coupon_price = coupon.dis_price
                        request.data['dis_price'] = coupon_price
            else:
                request.data['dis_price'] = 99
        return super().create(request, *args, **kwargs)
    queryset = Distributor.objects.all()
    serializer_class = CreateDistributorSerializer


class UpdateDistributor(generics.UpdateAPIView):
    def update(self, request, *args, **kwargs):
        if kwargs.get('pk') is None:
            raise NotAcceptable(detail="No data provided for update.")
        kwargs['partial'] = True
        id = kwargs.get('pk')
        distributor = Distributor.objects.filter(id=id).first()
        if distributor is None:
            raise NotAcceptable(detail="No such ]distributor exists")
        if self.request.user.id != distributor.user_id:
            raise NotAcceptable(
                detail="You are not authorized for this action")
        return super().update(request, *args, **kwargs)
    queryset = Distributor.objects.all()
    serializer_class = CreateDistributorSerializer
    permission_classes = [IsDistributor]


class RetrieveDistributorView(generics.RetrieveAPIView):
    def retrieve(self, request, *args, **kwargs):
        if kwargs.get('pk') is None:
            raise NotAcceptable(detail="No data provided for update.")
        kwargs['partial'] = True
        id = kwargs.get('pk')
        distributor = Distributor.objects.filter(id=id).first()
        if distributor is None:
            raise NotAcceptable(detail="No such distributor exists")
        if self.request.user.id != distributor.user_id:
            raise NotAcceptable(
                detail="You are not authorized for this action")
        return super().retrieve(request, *args, **kwargs)
    queryset = Distributor.objects.all()
    serializer_class = RetrieveDistributorSerializer
    permission_classes = [IsDistributor]


class CreateRetailerView(generics.CreateAPIView):
    def create(self, request, *args, **kwargs):
        if len(request.data) == 0:
            raise NotAcceptable(detail="No data provided")
        if request.data.get('user') is None:
            raise NotAcceptable(detail="No user data provided")
        userdata = request.data.get('user')
        if userdata.get('first_name') is None:
            raise NotAcceptable(detail="First Name not Provided")
        if userdata.get('email') is None:
            raise NotAcceptable(detail="email not Provided")
        if userdata.get('username') is None:
            raise NotAcceptable(detail="username not Provided")
        if userdata.get('password') is None:
            raise NotAcceptable(detail="password not Provided")
        if len(str(request.data['user']['password'])) < 8:
            raise NotAcceptable(
                detail="Password must contain at least 8 character.")
        password = request.data['user']['password']
        if password.isdigit():
            raise NotAcceptable(detail="password must cantain alphabets.")
        for char in list(str(password)):
            try:
                int(char)
                bool = True
            except:
                bool = False
        if bool == False:
            raise NotAcceptable(
                detail="At least one numeric digit must be provided.")
        if userdata.get('confirm_password') is None:
            raise NotAcceptable(detail="confirm password not Provided")
        if request.data['user']['password'] != request.data['user']['confirm_password']:
            raise NotAcceptable(detail="Passwords did not match")
        else:
            if request.data.get('mobile_number') is None:
                raise NotAcceptable(detail="mobile number not Provided")
            if request.data.get('date_of_birth') is None:
                raise NotAcceptable(detail="date of birth not Provided")
            password = make_password(password)
            request.data['user']['password'] = password
            del request.data['user']['confirm_password']
            if kwargs.get('ref_code') is not None:
                request.data['referral_code'] = kwargs.get('ref_code')
            if request.data.get('referral_code') is not None:
                referring_prime_dis = PrimaryDistributor.objects.filter(
                    retailer_referral_code=request.data['referral_code']).first()
                if referring_prime_dis is None:
                    referring_dis = Distributor.objects.filter(
                        retailer_referral_code=request.data['referral_code']).first()
                    if referring_dis is None:
                        raise NotAcceptable(
                            detail="Please provide right referral code")
                    else:
                        request.data['referred_by_distributor'] = referring_dis.id
                else:
                    request.data['referred_by_primary_distributor'] = referring_prime_dis.id
            if request.data.get('coupon_code') is not None:
                if request.data.get('coupon_code') not in CouponCode.objects.values_list('coupon_code', flat=True):
                    raise NotAcceptable(
                        detail="Please enter a valid coupon code.")
                else:
                    coupon = CouponCode.objects.filter(
                        coupon_code=request.data.get('coupon_code')).first()
                    if coupon.is_active == False:
                        raise NotAcceptable(
                            detail="This coupon code has expired.")
                    else:
                        coupon_price = coupon.ret_price
                        request.data['ret_price'] = coupon_price
            else:
                request.data['ret_price'] = 49
        return super().create(request, *args, **kwargs)
    queryset = Retailer.objects.all()
    serializer_class = CreateRetailerSerializer


class UpdateRetailer(generics.UpdateAPIView):
    def update(self, request, *args, **kwargs):
        if kwargs.get('pk') is None:
            raise NotAcceptable(detail="No data provided for update.")
        kwargs['partial'] = True
        id = kwargs.get('pk')
        retailer = Retailer.objects.filter(id=id).first()
        if retailer is None:
            raise NotAcceptable(detail="No such retailer exists")
        if self.request.user.id != retailer.user_id:
            raise NotAcceptable(
                detail="You are not authorized for this action")
        return super().update(request, *args, **kwargs)
    queryset = Retailer.objects.all()
    serializer_class = CreateDistributorSerializer
    permission_classes = [IsRetailer]


class RetrieveRetailerView(generics.RetrieveAPIView):
    def retrieve(self, request, *args, **kwargs):
        if kwargs.get('pk') is None:
            raise NotAcceptable(detail="No data provided for update.")
        kwargs['partial'] = True
        id = kwargs.get('pk')
        retailer = Retailer.objects.filter(id=id).first()
        if retailer is None:
            raise NotAcceptable(detail="No such retailer exists")
        if self.request.user.id != retailer.user_id:
            raise NotAcceptable(
                detail="You are not authorized for this action")
        return super().retrieve(request, *args, **kwargs)
    queryset = Retailer.objects.all()
    serializer_class = RetrieveRetailerSerializer
    permission_classes = [IsRetailer]


class ListDistributorView(generics.ListAPIView):
    def get_queryset(self):
        userid = self.request.user.id
        referring_prime_dis = PrimaryDistributor.objects.get(user_id=userid)
        return Distributor.objects.filter(referred_by=referring_prime_dis.id)
    serializer_class = ListDistributorSerializer
    permission_classes = [IsPrimaryDistributor]


class UpdateReferredDistributorView(generics.RetrieveUpdateAPIView):
    def retrieve(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        distributor = Distributor.objects.filter(id=id).first()
        if distributor is None:
            raise NotAcceptable(detail="No such distributor exists.")
        if distributor.referred_by is not None:
            if self.request.user.id != distributor.referred_by.user_id:
                raise NotAcceptable(
                    detail="You are not authorized for this action")
        if distributor.referred_by is None:
            raise NotAcceptable(
                detail="You are not authorized for this action")
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        kwargs['partial'] = True
        distributor = Distributor.objects.get(id=id)
        if distributor is None:
            raise NotAcceptable(detail="No such distributor exists.")
        if distributor.referred_by is not None:
            if self.request.user.id != distributor.referred_by.user_id:
                raise NotAcceptable(
                    detail="You are not authorized for this action")
        if distributor.referred_by is None:
            raise NotAcceptable(
                detail="You are not authorized for this action")
        return super().update(request, *args, **kwargs)

    def get_queryset(self):
        userid = self.request.user.id
        referring_prime_dis = PrimaryDistributor.objects.get(user_id=userid)
        return Distributor.objects.filter(referred_by=referring_prime_dis.id)
    serializer_class = ListDistributorSerializer
    permission_classes = [IsPrimaryDistributor]


class ListRetailerView(generics.ListAPIView):
    def get_queryset(self):
        userid = self.request.user.id
        referring_PD = PrimaryDistributor.objects.filter(
            user_id=userid).first()
        referring_D = Distributor.objects.filter(user_id=userid).first()
        if referring_PD is not None:
            return Retailer.objects.filter(referred_by_primary_distributor=referring_PD.id)
        elif referring_D is not None:
            return Retailer.objects.filter(referred_by_distributor=referring_D.id)
        else:
            return Response("You have no referred retailers.")
    serializer_class = ListRetailerSerializer
    permission_classes = [IsPrimaryDistributorOrDistirbutor]


class UpdateReferredRetailersView(generics.RetrieveUpdateAPIView):
    def retrieve(self, request, *args, **kwargs):
        pk = int(kwargs.get('pk'))
        userid = self.request.user.id
        referring_PD = PrimaryDistributor.objects.filter(
            user_id=userid).first()
        referring_D = Distributor.objects.filter(user_id=userid).first()
        retailer = Retailer.objects.filter(id=pk).first()
        if retailer is None:
            raise NotAcceptable(detail="No such retailer exists.")
        if referring_PD is not None:
            if retailer.referred_by_primary_distributor is not None:
                if retailer.referred_by_primary_distributor.id != referring_PD.id:
                    raise NotAcceptable(
                        detail="You are not authorized for this action")
            if retailer.referred_by_primary_distributor is None:
                raise NotAcceptable(
                    detail="You are not authorized for this action")
        if referring_D is not None:
            if retailer.referred_by_distributor is not None:
                if retailer.referred_by_distributor.id != referring_D.id:
                    raise NotAcceptable(
                        detail="You are not authorized for this action")
            if retailer.referred_by_distributor is None:
                raise NotAcceptable(
                    detail="You are not authorized for this action")
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        pk = int(kwargs.get('pk'))
        userid = self.request.user.id
        referring_PD = PrimaryDistributor.objects.filter(
            user_id=userid).first()
        referring_D = Distributor.objects.filter(user_id=userid).first()
        retailer = Retailer.objects.filter(id=pk).first()
        kwargs['partial'] = True
        if retailer is None:
            raise NotAcceptable(detail="No such retailer exists.")
        if referring_PD is not None:
            if retailer.referred_by_primary_distributor is not None:
                if retailer.referred_by_primary_distributor.id != referring_PD.id:
                    raise NotAcceptable(
                        detail="You are not authorized for this action")
            if retailer.referred_by_primary_distributor is None:
                raise NotAcceptable(
                    detail="You are not authorized for this action")
        if referring_D is not None:
            if retailer.referred_by_distributor is not None:
                if retailer.referred_by_distributor.id != referring_D.id:
                    raise NotAcceptable(
                        detail="You are not authorized for this action")
            if retailer.referred_by_distributor is None:
                raise NotAcceptable(
                    detail="You are not authorized for this action")
        return super().update(request, *args, **kwargs)

    def get_queryset(self):
        userid = self.request.user.id
        referring_PD = PrimaryDistributor.objects.filter(
            user_id=userid).first()
        referring_D = Distributor.objects.filter(user_id=userid).first()
        if referring_PD is not None:
            return Retailer.objects.filter(referred_by_primary_distributor=referring_PD.id)
        elif referring_D is not None:
            return Retailer.objects.filter(referred_by_distributor=referring_D.id)
        else:
            return Response("You have no referred retailers.")
    serializer_class = ListRetailerSerializer
    permission_classes = [IsPrimaryDistributorOrDistirbutor]


class WalletView(generics.RetrieveUpdateAPIView):
    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        wallet = Wallet.objects.filter(id=pk).first()
        if wallet is None:
            raise NotAcceptable(detail="Please go with the right wallet id")
        if self.request.user.id != wallet.user_id:
            raise NotAcceptable(
                detail="You are not authorized for this action.")
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        # payment has to be managed here.
        pk = kwargs.get('pk')
        wallet = Wallet.objects.filter(id=pk).first()
        if wallet is None:
            raise NotAcceptable(detail="Please go with the right wallet id")
        if self.request.user.id != wallet.user_id:
            raise NotAcceptable(
                detail="You are not authorized for this action.")
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    permissoion_classes = [IsAuthenticated]


class WithdrawView(generics.UpdateAPIView):
    def update(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        wallet = Wallet.objects.filter(id=pk).first()
        if wallet is None:
            raise NotAcceptable(detail="Please go with the right wallet id")
        if self.request.user.id != wallet.user_id:
            raise NotAcceptable(
                detail="You are not authorized for this action.")
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)
    queryset = Wallet.objects.all()
    serializer_class = WalletWithdrawSerializer
    permissoion_classes = [IsAuthenticated]


class RechargeView(generics.ListCreateAPIView):
    def create(self, request, *args, **kwargs):
        request.data['user'] = self.request.user.id
        return super().create(request, *args, **kwargs)

    def get_queryset(self):
        return Recharge.objects.filter(user_id=self.request.user.id)
    serializer_class = RechargeSerializer
    permission_classes = [IsAuthenticated]
