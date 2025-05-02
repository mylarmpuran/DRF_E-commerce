from django.urls import path, include
from rest_framework import routers
from .views import (
    UserViewSet, VendorViewSet, CategoryViewSet, ProductViewSet,
    OrderViewSet, OrderItemSerializer, CartViewSet, CartItemViewSet,
    ShippingViewSet, PaymentViewSet, CouponViewSet, ReviewViewSet,
    WishlistViewSet, NotificationViewSet, BlogViewSet, ContactViewSet,
    FAQViewSet, AnalyticsViewSet, ConfigurationViewSet, TaxViewSet,
    SubscriptionViewSet, RefundViewSet
)


router = routers.DefaultRouter()
router.register(r'users', UserViewSet,)

urlpatterns = [
    path('', views.home, name='home'),  # example view
]