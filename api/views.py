import random
from django.http import HttpRequest
import requests
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import OTP

def send_otp(phone_num, otp):
    print("Reached Otp sent helper")
    url = "https://www.fast2sms.com/dev/bulkV2"
    payload = f'variables_values={otp}&route=otp&language=english&numbers={phone_num}'
    headers = {
        'authorization': "mEgP0Z5wnldKSerOu1GW8qUbVctH3jkYaM7QCI4Jzp69XNT2ALFmiofRb467D0rSOWVB3qp8J5HYeIvt",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }
    response = requests.request("POST", url, data=payload, headers=headers)
 
    print(response.text)

def generate_otp():
    return str(random.randint(1000, 9999))

class SendOTP(APIView):
    def post(self, request):
        if 'phone' in request.data:
            phonenum = request.data['phone']
            otp = generate_otp()  # Generate OTP
            # Save OTP to database
            OTP.objects.create(phone=phonenum, otp=otp)
            send_otp(phonenum, otp)  # Send OTP (assuming this function is defined)
            return Response({'message': 'OTP sent successfully'}, status=status.HTTP_200_OK)
        return Response({'error': 'Phone number is required'}, status=status.HTTP_400_BAD_REQUEST)

class VerifyOTP(APIView):
    def post(self, request):
        if 'phone' in request.data and 'otp' in request.data:
            phonenum = request.data['phone']
            user_otp = request.data['otp']
            try:
                otp_obj = OTP.objects.get(phone=phonenum, otp=user_otp)
            except OTP.DoesNotExist:
                return Response({'error': 'Invalid OTP or phone number'}, status=status.HTTP_400_BAD_REQUEST)
            otp_obj.delete()
            return Response({'message': 'OTP verified successfully'}, status=status.HTTP_200_OK)
        return Response({'error': 'Phone number and OTP are required'}, status=status.HTTP_400_BAD_REQUEST)

