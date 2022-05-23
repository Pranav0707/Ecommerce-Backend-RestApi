from pyexpat import model
from rest_framework import serializers

from .models import Order,OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderItem
        fields=[
            'quantity',
            'product',
            'price',
        ]

class OrderSerializer(serializers.ModelSerializer):
    items=OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "address",
            "zipcode",
            "place",
            "phone",
            "stripe_token",
            "items",
        )

    def create(self, validated_data):
        item_data=validated_data.pop('items')
        order=Order.objects.create(**validated_data)
        for item in item_data:
            Order.objects.create(order=order,**item)
        return order