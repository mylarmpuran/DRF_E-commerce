from rest_framework import serializers
from .models import (User, Vendor, Category, Product, Order, OrderItem, Cart, CartItem, Shipping, Payment, Coupon, Review, Wishlist,Notification,Blog,
                     Contact,FAQ,Analytics,Configuration,Tax,Subscription,Refund)



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field = '__all__'



class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        field = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        field = '__all__'

class ProductSerializer(serializers.ModelSerializer):

    category = CategorySerializer(read_only = True)
    vendor = VendorSerializer(read_only = True)
    review = serializers.StringRelatedField(many=True, read_only = True)

    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):

    customer = UserSerializer(read_only = True)
    products = ProductSerializer(read_only = True)
        
    class Meta:
        model = Order
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):

     
    class Meta:
        model = OrderItem
        field = '__all__'



