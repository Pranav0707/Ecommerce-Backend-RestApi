from dataclasses import fields
import imp
from rest_framework.serializers import ModelSerializer

from .models import Cart, CartItems
from rest_framework import serializers
class CartGETSerializer(ModelSerializer):
    class Meta:
        model=Cart
        fields=["items_in_cart","total_price"]
        
    # def create(self, validated_data):
    #     validated_data["user"]=self.context["request"].user
    #     return super().create(validated_data)
class CartSerializer(ModelSerializer):
    class Meta:
        model=Cart
        fields=["items_in_cart","total_price"]

class CartItemSerializer(ModelSerializer):
    class Meta:
        model=CartItems
        fields=[]