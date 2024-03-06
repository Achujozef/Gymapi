import datetime
import random
from django.http import HttpRequest
import requests
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .serializers import *
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
import cloudinary.uploader


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
    
class AddEquipment(APIView):
    def post(self, request):
  
        image_data = request.FILES.get('image')
       
        if image_data:
            # Upload image to Cloudinary
            result = cloudinary.uploader.upload(image_data)
            image_url = result['secure_url']
            print("image_url",image_url)
            request.data['image'] = image_url

        serializer = GymEquipmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteEquipment(APIView):
    def delete(self, request, pk):
        try:
            equipment = GymEquipment.objects.get(pk=pk)
        except GymEquipment.DoesNotExist:
            raise Http404
        equipment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ListUnlistEquipment(APIView):
    def put(self, request, pk):
        try:
            equipment = GymEquipment.objects.get(pk=pk)
        except GymEquipment.DoesNotExist:
            raise Http404
        equipment.availability = not equipment.availability
        equipment.save()
        return Response(status=status.HTTP_200_OK)

class ReadEquipment(APIView):
    def get(self, request, pk):
        try:
            equipment = GymEquipment.objects.get(pk=pk)
        except GymEquipment.DoesNotExist:
            raise Http404
        serializer = GymEquipmentSerializer(equipment)
        return Response(serializer.data)
    
class ListEquipment(APIView):
    def get(self, request):
        equipment = GymEquipment.objects.all()
        serializer = GymEquipmentSerializer(equipment, many=True)
        return Response(serializer.data)

class EditEquipment(APIView):
    def get_object(self, pk):
        try:
            return GymEquipment.objects.get(pk=pk)
        except GymEquipment.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        equipment = self.get_object(pk)
        serializer = GymEquipmentSerializer(equipment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ListBasicEquipment(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        equipment = GymEquipment.objects.all()
        serializer = BasicGymEquipmentSerializer(equipment, many=True)
        return Response(serializer.data)
    
class AddAttendanceView(APIView):
    def post(self, request):

        current_user = request.user
        try:
            gym_owner = GymOwner.objects.get(user=current_user)
            gym = gym_owner.gym
            branch = None 
        except GymOwner.DoesNotExist:
            try:
                staff = Staff.objects.get(user=current_user)
                gym = staff.gym
                branch = staff.branch
            except Staff.DoesNotExist:
                return Response({'error': 'User is not associated with any gym or branch'}, status=status.HTTP_400_BAD_REQUEST)

        user_id = request.data.get('user_id')
        user_type = request.data.get('user_type')  # Possible values: 'user', 'trainer', 'staff'


        if not user_id or not user_type:
            return Response({'error': 'Missing required fields in request'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            if user_type == 'user':
                user = User.objects.get(pk=user_id)
                if not Member.objects.filter(user=user, gym=gym).exists():
                    return Response({'error': 'User is not associated with the gym'}, status=status.HTTP_400_BAD_REQUEST)
            elif user_type == 'trainer':
                trainer = GymTrainer.objects.get(user=user_id)
                if trainer.gym != gym:
                    return Response({'error': 'Trainer is not associated with the gym'}, status=status.HTTP_400_BAD_REQUEST)
            elif user_type == 'staff':
                staff = Staff.objects.get(pk=user_id)
                if staff.gym != gym:
                    return Response({'error': 'Staff member is not associated with the gym'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'Invalid user type'}, status=status.HTTP_400_BAD_REQUEST)
        except (User.DoesNotExist, GymTrainer.DoesNotExist, Staff.DoesNotExist):
            return Response({'error': 'User does not exist or is not associated with the gym'}, status=status.HTTP_400_BAD_REQUEST)

        Attendance.objects.create(
            user=user,
            gym=gym,
            branch=branch
        )

        return Response({'message': 'Attendance recorded successfully'}, status=status.HTTP_201_CREATED)
        


class AttendanceListView(APIView):
    def get(self, request):
        # Retrieve all attendance records
        attendance = Attendance.objects.all()
        # Serialize the data
        serializer = AttendanceSerializer(attendance, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DeleteAttendance(APIView):
    def delete(self, request, attendance_id):
        try:
            attendance = Attendance.objects.get(id=attendance_id)
            attendance.delete()
            return Response({"message": "Attendance record deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Attendance.DoesNotExist:
            return Response({"error": "Attendance record not found"}, status=status.HTTP_404_NOT_FOUND)
        
class EnquiryCreate(APIView):
    def post(self, request):
        serializer = EnquiryCreateSerializer(data=request.data)
        if serializer.is_valid():
            gym = None
            branch = None
            added_by = request.user
            if hasattr(request.user, 'staff'):
                gym = request.user.staff.gym
                branch = request.user.staff.branch
            elif hasattr(request.user, 'gymowner'):
                gym = request.user.gymowner.gym
            serializer.save(gym=gym, branch=branch, added_by=added_by)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class EnquiryRetrieve(APIView):
    def get_object(self, pk):
        try:
            return Enquiry.objects.get(pk=pk)
        except Enquiry.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        enquiry = self.get_object(pk)
        serializer = EnquirySerializer(enquiry)
        return Response(serializer.data)
    
class EnquiryUpdate(APIView):
    def get_object(self, pk):
        try:
            return Enquiry.objects.get(pk=pk)
        except Enquiry.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        enquiry = self.get_object(pk)
        serializer = EnquirySerializer(enquiry, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class EnquiryDelete(APIView):
    def get_object(self, pk):
        try:
            return Enquiry.objects.get(pk=pk)
        except Enquiry.DoesNotExist:
            raise Http404

    def delete(self, request, pk):
        enquiry = self.get_object(pk)
        enquiry.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class EnquiryListView(APIView):
    def get(self, request):
        enquiries = Enquiry.objects.all()
        if hasattr(request.user, 'staff'):
            gym = request.user.staff.gym
            branch = request.user.staff.branch
            enquiries = enquiries.filter(gym=gym, branch=branch)
        elif hasattr(request.user, 'gymowner'):
            gym = request.user.gymowner.gym
            enquiries = enquiries.filter(gym=gym)
        serializer = EnquirySerializer(enquiries, many=True)
        return Response(serializer.data)
    


class GymUserCreateView(APIView):
    def post(self, request):
        data = request.data
        
        current_user = request.user
        
        gym = None
        branch = None
        try:
            member = Member.objects.get(user=current_user)
            gym = member.gym
            branch = member.branch
        except Member.DoesNotExist:
            pass
        
        user = User.objects.create_user(
            username=data.get('contact_number'),
            password='12345678',  
            email=data.get('email')
        )
        membership_type_id = data.get('membership_type')
        membership_type = get_object_or_404(GymPlan, pk=membership_type_id)
        member = Member.objects.create(
            user=user,
            gym=gym,
            branch=branch,
            is_user=True
        )
        
        gym_user = GymUser.objects.create(
            user=user,
            gender=data.get('gender'),
            date_of_birth=data.get('date_of_birth'),
            contact_number=data.get('contact_number'),
            email=data.get('email'),
            address=data.get('address'),
            membership_type=membership_type,
            joining_date=data.get('joining_date'),
            membership_expiry_date=data.get('membership_expiry_date'),
            is_active=data.get('is_active'),
            health_conditions=data.get('health_conditions'),
            fitness_goals=data.get('fitness_goals'),
            workout_schedule=data.get('workout_schedule'),
            exercise_restrictions=data.get('exercise_restrictions'),
            emergency_contact_name=data.get('emergency_contact_name'),
            emergency_contact_phone_number=data.get('emergency_contact_phone_number'),
            emergency_contact_relationship=data.get('emergency_contact_relationship'),
            membership_id_number=data.get('membership_id_number'),
            access_information=data.get('access_information'),
            assigned_personal_trainer=data.get('assigned_personal_trainer'),
            trainer_contact_information=data.get('trainer_contact_information'),
            assigned_locker_number=data.get('assigned_locker_number'),
            feedback=data.get('feedback'),
            weight=data.get('weight')
        )
        
        serializer = GymUserSerializer(gym_user)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class GymOwnerRegistrationView(APIView):
    def post(self, request):
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        phone_number = request.data.get('phone_number')
        email = request.data.get('email')
        gym_name = request.data.get('gym_name')
        address = request.data.get('address')
        password = request.data.get('password')
        state = request.data.get('state')
        district = request.data.get('district')
        city = request.data.get('city')
        branch_count = request.data.get('branch_count')
        gym_contact = request.data.get('gym_contact')

        required_fields = ['first_name', 'last_name', 'phone_number', 'email', 'gym_name', 'address', 'password', 'state', 'district', 'city', 'branch_count']
        for field in required_fields:
            if field not in request.data:
                return Response({'error': f'Missing required field: {field}'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=phone_number).exists():
            return Response({'error': 'Phone number is already registered'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(
            username=phone_number, 
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )
        gym_owner = GymOwner.objects.create(
            user=user,
            phone_number=phone_number,
            gym_name=gym_name,
            address=address,
            state=state,
            branch_count=branch_count,
            city=city,
            district=district,
            gym_contact=gym_contact
        )
        return Response({'message': 'Gym owner registered successfully.'}, status=status.HTTP_201_CREATED)