import imp
from attr import fields
from rest_framework import serializers
from .models import Product,Category
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=["id","name","description","price","get_image","get_thumbnail"]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=["id","name","slug","products"]

class CreateCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"

class CreateProductSerializer(serializers.ModelSerializer):
    # products = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model=Product
        fields=["name","description","price","category","items_in_stock","slug"]
    def to_representation(self, instance):
        response=super().to_representation(instance)
        response['category']=CategorySerializer(instance.category).data
        return response