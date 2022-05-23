from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView

from cart.models import Cart
from cart.serializers import CartSerializer,CartGETSerializer
# Create your views here.

class CartView(APIView):
    def get(self,request):
        try:
            cart=Cart.objects.get(user=request.user)
            serializer=CartGETSerializer(cart)
            return Response(serializer.data)
        except:
            return Response(serializer.errors)
    def post(self,request):
        serializer=CartSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data)
        return Response(serializer.errors)
        
    def put(self,request):
        try:
            cart=Cart.objects.get(user=request.user)
            serializer=CartSerializer(cart,data=request.data,context={'request':request})
            if serializer.is_valid():
                serializer.save(user=self.request.user)
                return Response(serializer.data)
            return Response(serializer.errors)
        except:
            return Response(serializer.errors)
    def delete(self,request):
        cart=Cart.objects.get(user=request.user)
        cart.delete()
        return Response({"Success":"Deleted Successfully"})
