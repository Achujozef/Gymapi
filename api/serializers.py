from rest_framework import serializers
from .models import *

class GymUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = GymUser
        fields = '__all__'

class GymEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GymEquipment
        fields = '__all__'

class BasicGymEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GymEquipment
        fields = ['id', 'name', 'image', 'additional_notes']

class EnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Enquiry
        fields = '__all__'
class EnquiryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enquiry
        exclude = ['branch', 'added_by', 'gym']

class GymUserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = GymUser
        fields = '__all__'




class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['id', 'user', 'gym', 'branch', 'date', 'time']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'slot', 'user', 'date']


class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slot
        fields = ['id', 'gym', 'branch', 'day', 'start_time', 'end_time', 'available']

class ListBookingSerializer(serializers.ModelSerializer):
    slot_start_time = serializers.TimeField(source='slot.start_time')
    slot_end_time = serializers.TimeField(source='slot.end_time')
    slot_day = serializers.CharField(source='slot.get_day_display')

    class Meta:
        model = Booking
        fields = ['id', 'slot_start_time', 'slot_end_time', 'slot_day', 'date']


class GymPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = GymPlan
        fields = ['id', 'gym', 'branch', 'name', 'description', 'price', 'duration', 'duration_type','image','terms_and_conditions']


class GymPlanPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GymPlanPayment
        fields = ['id', 'gym', 'branch', 'gym_plan', 'user', 'transaction_id', 'screenshot', 'status']