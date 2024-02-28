import random
from django.http import HttpRequest
import requests
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .serializers import GymUserSerializer


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

        phonenum = request.data
        print(phonenum['phonenumber'])
        phonenum=phonenum['phonenumber']
        otp = generate_otp()
        OTP.objects.create(phone=phonenum, otp=otp)
        send_otp(phonenum, otp)
        return Response({'message': 'OTP sent successfully'}, status=status.HTTP_200_OK)

class VerifyOTP(APIView):
    def post(self, request):
        if 'phoneNumber' in request.data and 'otp' in request.data:
            phonenum = request.data['phoneNumber']
            user_otp = request.data['otp']
            try:
                otp_obj = OTP.objects.get(phone=phonenum, otp=user_otp)
            except OTP.DoesNotExist:
                return Response({'error': 'Invalid OTP or phone number'}, status=status.HTTP_400_BAD_REQUEST)
            otp_obj.delete()
            return Response({'message': 'OTP verified successfully'}, status=status.HTTP_200_OK)
        return Response({'error': 'Phone number and OTP are required'}, status=status.HTTP_400_BAD_REQUEST)


class UserAddView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if not username or not password or not email:
            return Response({'error': 'Username, password, and email are required.'}, status=400)

        user = User.objects.create(
            username=username,
            email=email,
            password=make_password(password)
        )

        return Response({'message': 'User created successfully.'}, status=201)

class UserDeleteView(APIView):
    def delete(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
            user.delete()
            return Response({'message': 'User deleted successfully.'})
        except User.DoesNotExist:
            return Response({'error': 'User does not exist.'}, status=404)


class UserBlockView(APIView):
    def post(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
            user.is_active = False
            user.save()
            return Response({'message': 'User blocked successfully.'})
        except User.DoesNotExist:
            return Response({'error': 'User does not exist.'}, status=404)


class ResetPasswordView(APIView):
    def post(self, request):
        print("Reached")
        try:
            contact_number = request.data.get('phonenumber')
            new_password = request.data.get('newPassword')
            print(contact_number,new_password)
            gym_user = GymUser.objects.get(contact_number=contact_number)
            user = gym_user.user
            print (user)
            user.set_password(new_password)
            user.save()
            
            return Response({'message': 'Password reset successfully.'})
        except GymUser.DoesNotExist:
            return Response({'error': 'User does not exist.'}, status=404)


class GymUserCreateAPIView(APIView):
    def post(self, request):
        serializer = GymUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
