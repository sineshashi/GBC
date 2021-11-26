from django.core.exceptions import ValidationError
from rest_framework.exceptions import NotAuthenticated
from rest_framework.permissions import BasePermission
from .models import PrimaryDistributor, Distributor, Retailer

class IsPrimaryDistributor(BasePermission):
    def has_permission(self, request, view):
        if PrimaryDistributor.objects.filter(user_id = request.user.id).first() is None:
            raise NotAuthenticated("You are not a primary distributor.")
        return bool(request.user and request.user.is_authenticated)

class IsDistributor(BasePermission):
    def has_permission(self, request, view):
        if Distributor.objects.filter(user_id = request.user.id).first() is None:
            raise NotAuthenticated("You are not a distributor.")
        return bool(request.user and request.user.is_authenticated)

class IsRetailer(BasePermission):
    def has_permission(self, request, view):
        if Retailer.objects.filter(user_id = request.user.id).first() is None:
            raise NotAuthenticated("You are not a retailer.")
        return bool(request.user and request.user.is_authenticated)
class IsPrimaryDistributorOrDistirbutor(BasePermission):
    def has_permission(self, request, view):
        PD = PrimaryDistributor.objects.filter(user_id = request.user.id).first()
        D = Distributor.objects.filter(user_id = request.user.id).first()
        if (PD is None) and (D is None):
            raise NotAuthenticated("You are not a registered distributor or primary distributor.")
        return bool(request.user and request.user.is_authenticated)
class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        PD = PrimaryDistributor.objects.filter(user_id = request.user.id).first()
        D = Distributor.objects.filter(user_id = request.user.id).first()
        R = Retailer.objects.filter(user_id = request.user.id).first()
        if (PD is None) and (D is None) and (R is None):
            raise NotAuthenticated("You are not a registered distributor or primary distributor.")
        return bool(request.user and request.user.is_authenticated)