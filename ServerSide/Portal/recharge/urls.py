from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')


urlpatterns = [
    url(r'^$', schema_view),
    path('primarydistributor', views.CreatePrimaryDistrubutorView.as_view(),
         name="create_primary_distributor"),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('primarydistributor/updateprofile/<int:pk>',
         views.UpdatePrimaryDistributor.as_view(), name="update_primary_distributor"),
    path('primarydistributor/myprofile',
         views.RetrievePrimaryDistributorView.as_view(), name="retrieve_primary_distributor"),
    path('distributor/<str:ref_code>', views.CreateDistrubutorView.as_view(),
         name="create_distributor_with_referral"),
    path('distributor', views.CreateDistrubutorView.as_view(),
         name="create_distributor"),
    path('distributor/updateprofile/<int:pk>', views.UpdateDistributor.as_view(),
         name="update_distributor_with_referral"),
    path('distributor/myprofile', views.RetrieveDistributorView.as_view(),
         name="retrieve_distributor_with_referral"),
    path('retailer/<str:ref_code>', views.CreateRetailerView.as_view(),
         name="create_retailer_with_referral"),
    path('retailer', views.CreateRetailerView.as_view(),
         name="create_retailer"),
    path('retailer/updateprofile/<int:pk>', views.UpdateRetailer.as_view(),
         name="update_retailer_with_referral"),
    path('retailer/myprofile', views.RetrieveRetailerView.as_view(),
         name="retrieve_retailer_with_referral"),
    path('referred-distributors',
         views.ListDistributorView.as_view(), name='referred_distributors'),
    path('referred-distributors/<int:pk>',
         views.UpdateReferredDistributorView.as_view(), name='update_referred_distributor'),
    path('referredretailers', views.ListRetailerView.as_view(),
         name="referred_by_retailers"),
    path('referredretailers/<int:pk>', views.UpdateReferredRetailersView.as_view(),
         name="update_referred_by_retailers"),
    path('mywallet/<int:pk>', views.WalletView.as_view(), name="wallet"),
    path('mywallet/withdraw/<int:pk>', views.WithdrawView.as_view(), name="withdraw_value"),
    path('myprofile/recharge', views.RechargeView.as_view(), name='recharge')
]
