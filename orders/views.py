from locale import currency
from django.shortcuts import render
from django.conf import Settings, settings
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import OrderSerializer
import stripe
# Create your views here.


@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def checkout(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        stripe_api_key = 'sk_test_51KzcSpSES1tjrnyoY9hDZeOtmipXuMHFD90QzdB1YPORau7aYXKwqSLBor9ZiyJY0ZHAVpsgbxlgoixaSCe8Etea00kUnumtJ6'
        # paid_amount=sum(item.get('quantity')*item.get('product').price for item in serializer.validated_data['items'])
        paid_amount = 1000
        try:
            charge = stripe.PaymentIntent.create(
                amount=1000, currency='pln',
                payment_method_types=['card'],
                receipt_email='test@example.com')

            serializer.save(user=request.user, paid_amount=paid_amount)

            return Response(data=charge, status=status.HTTP_201_CREATED)
        except Exception:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
